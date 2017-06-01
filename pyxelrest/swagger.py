import os
import re
import requests
import logging
from collections import OrderedDict

try:
    # Python 3
    from configparser import ConfigParser
    from urllib.parse import urlsplit
except ImportError:
    # Python 2
    from ConfigParser import ConfigParser
    from urlparse import urlsplit

import vba
from pyxelresterrors import *
import authentication


def to_valid_python_vba(str_value):
    return re.sub('[^a-zA-Z_]+[^a-zA-Z_0-9]*', '', str_value)


class SwaggerService:
    def __init__(self, service_name, config):
        """
        Load service information from configuration and swagger JSON.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param config: ConfigParser instance from where service details are retrieved.
        """
        self.name = service_name
        self.udf_prefix = to_valid_python_vba(service_name)
        self.methods = [method.strip() for method in self.get_item(config, 'methods').split(',') if method.strip()]
        if not self.methods:
            raise NoMethodsProvided()
        self.tags = [tag.strip() for tag in self.get_item_default(config, 'tags', '').split(',') if tag.strip()]
        swagger_url = self.get_item(config, 'swagger_url')
        swagger_url_parsed = urlsplit(swagger_url)
        proxy_url = self.get_item_default(config, 'proxy_url', None)
        self.proxy = {swagger_url_parsed.scheme: proxy_url} if proxy_url else {}
        self.rely_on_definitions = bool(self.get_item_default(config, 'rely_on_definitions', False))
        self.connect_timeout = float(self.get_item_default(config, 'connect_timeout', 1))
        self.read_timeout = self.get_item_default(config, 'read_timeout', None)
        if self.read_timeout:
            self.read_timeout = float(self.read_timeout)
        self.swagger = self._retrieve_swagger(swagger_url)
        self.validate_swagger_version()
        self.uri = self._extract_uri(swagger_url_parsed, config)
        security_details = self.get_item_default(config, 'security_details', None)
        authentication.add_service_security(self.name, self.swagger, security_details)

    def _extract_uri(self, swagger_url_parsed, config):
        # The default scheme to be used is the one used to access the Swagger definition itself.
        scheme = self.swagger.get('schemes', [swagger_url_parsed.scheme])[0]
        # If the host is not included, the host serving the documentation is to be used (including the port).
        # service_host property is here to handle services behind a reverse proxy
        # (otherwise host will be the reverse proxy one)
        host = self.swagger.get('host', self.get_item_default(config, 'service_host', swagger_url_parsed.netloc))
        # Allow user to provide service_host starting with scheme (removing it)
        host_parsed = urlsplit(host)
        if host_parsed.netloc:
            host = host_parsed.netloc + host_parsed.path
        # If it is not included, the API is served directly under the host.
        base_path = self.swagger.get('basePath', None)

        return scheme + '://' + host + base_path if base_path else scheme + '://' + host

    def should_provide_tags(self, tags):
        if not self.tags:
            return True
        for tag in tags:
            if tag in self.tags:
                return True
        return False

    def definitions(self):
        return self.swagger.get('definitions')

    def responses(self, responses):
        if not responses:
            raise EmptyResponses(self.name)
        return responses

    def get_item(self, config, key):
        try:
            # Python 3
            section = config[self.name]
            if key not in section:
                raise MandatoryPropertyNotProvided(self.name, key)
            return section[key]
        except AttributeError:
            # Python 2
            if not config.has_option(self.name, key):
                raise MandatoryPropertyNotProvided(self.name, key)
            return config.get(self.name, key)

    def get_item_default(self, config, key, default_value):
        try:
            # Python 3
            section = config[self.name]
            return section[key] if key in section else default_value
        except AttributeError:
            # Python 2
            return config.get(self.name, key) if config.has_option(self.name, key) else default_value

    def _retrieve_swagger(self, swagger_url):
        """
        Retrieve swagger JSON from service.
        :param swagger_url: URI of the service swagger JSON.
        :return: Dictionary representation of the retrieved swagger JSON.
        """
        response = requests.get(swagger_url, proxies=self.proxy, verify=False, timeout=(self.connect_timeout, self.read_timeout))
        response.raise_for_status()
        # Always keep the order provided by server (for definitions)
        swagger = response.json(object_pairs_hook=OrderedDict)
        self._normalize_methods(swagger)
        return swagger

    # TODO Clean this method as it is too big and a smart refactoring of SwaggerService might be needed
    @classmethod
    def _normalize_methods(cls, swagger_json):
        """
        Normalize method parameters from dict representing the swagger JSON to:
        - rename parameters name that are VBA restricted keywords 
        - rename parameters name that uses '-' (to '_')
        - cascade parameters defined at path level to operation level

        Normalize method produces from dict representing the swagger JSON to:
        - cascade produces defined at root level to operation level

        :param swagger_json: Dictionary representing the swagger JSON.
        :return: None
        """

        def _normalise_names(parameters):
            for parameter in parameters:
                parameter["server_param_name"] = parameter["name"]

                # replace vba restricted keywords
                if parameter['name'].lower() in vba.vba_restricted_keywords:
                    parameter['name'] = vba.vba_restricted_keywords[parameter['name'].lower()]
                # replace '-'
                if "-" in parameter['name']:
                    parameter['name'] = parameter['name'].replace("-", "_")
                if parameter['name'].startswith("_"):
                    parameter['name'] = parameter['name'][1:]
            return parameters

        def _update_method_parameters(method, global_parameters):
            method['parameters'] = global_parameters + _normalise_names(method.get('parameters', []))

            method_parameters_names = [parameter['name'] for parameter in method['parameters']]
            if len(set(method_parameters_names)) != len(method_parameters_names):
                raise DuplicatedParameters(method)

        def _update_method_produces(method, global_produces):
            method['produces'] = global_produces + method.get('produces', [])

        global_produces = swagger_json.get('produces', [])

        for methods in swagger_json['paths'].values():
            # retrieve parameters listed at the path level
            global_parameters = _normalise_names(methods.pop("parameters", []))
            for mode, method in methods.items():
                if mode not in ['get', 'post', 'put', 'delete']:
                    logging.warning("'{0}' mode is not supported for now. Supported ones are "
                                    "['get', 'post', 'put', 'delete']".format(mode))

                _update_method_parameters(method, global_parameters)
                _update_method_produces(method, global_produces)

    def validate_swagger_version(self):
        if 'swagger' not in self.swagger:
            raise SwaggerVersionNotProvided()
        if self.swagger['swagger'] != '2.0':
            raise UnsupportedSwaggerVersion(self.swagger['swagger'])

    def __str__(self):
        return '[{0}] service. {1}'.format(self.name, self.uri)


def load_services():
    """
    Retrieve swagger JSON for each service defined in configuration file.
    :return: List of SwaggerService objects, size is the same one as the number of sections within configuration file
    (DEFAULT excluded).
    """
    config_parser = ConfigParser()
    file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'services.ini')
    if not config_parser.read(file_path):
        raise ConfigurationFileNotFound(file_path)

    logging.debug('Loading services from "{0}"...'.format(file_path))
    loaded_services = []
    for service_name in config_parser.sections():
        service = load_service(service_name, config_parser)
        if service:
            loaded_services.append(service)

    check_for_duplicates(loaded_services)
    return loaded_services


def load_service(service_name, config_parser):
    logging.debug('Loading "{0}" service...'.format(service_name))
    try:
        service = SwaggerService(service_name, config_parser)
        logging.info('"{0}" service will be available.'.format(service_name))
        logging.debug(str(service))
        return service
    except Exception as e:
        logging.error('"{0}" service will not be available: {1}'.format(service_name, e))


def check_for_duplicates(loaded_services):
    services_by_prefix = {}
    for service in loaded_services:
        duplicates = services_by_prefix.get(service.udf_prefix, [])
        duplicates.append(service.name)
        services_by_prefix[service.udf_prefix] = duplicates
    for udf_prefix in services_by_prefix:
        service_names = services_by_prefix[udf_prefix]
        if len(service_names) > 1:
            logging.warning('{0} services will use the same "{1}" prefix, in case there is the same call available, '
                            'only the last declared one will be available.'.format(service_names, udf_prefix))
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

    def definitions(self):
        return self.swagger.get('definitions')

    def method(self, swagger_method, method_path):
        return SwaggerMethod(self, swagger_method, method_path)

    def should_provide_method(self, swagger_methods, http_verb):
        if http_verb not in self.methods:
            return False
        swagger_method = swagger_methods.get(http_verb)
        if not swagger_method:
            return False
        return self._allow_tags(swagger_method.get('tags')) and \
               self.return_type_can_be_handled(swagger_method.get('produces', []))

    def _allow_tags(self, method_tags):
        if not self.tags or not method_tags:
            return True
        for method_tag in method_tags:
            if method_tag in self.tags:
                return True
        return False

    def return_type_can_be_handled(self, method_produces):
        return 'application/octet-stream' not in method_produces

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


class SwaggerMethod:
    def __init__(self, service, swagger_method, path):
        self.uri = '{0}{1}'.format(service.uri, path)
        self.service = service
        self.swagger_method = swagger_method
        self.parameters = swagger_method.get('parameters', [])
        self.path_parameters = []
        self.required_parameters = []
        self.optional_parameters = []
        for parameter in self.parameters:
            if parameter['in'] == 'path':
                self.path_parameters.append(parameter)
            # Required but not in path
            elif parameter.get('required'):
                self.required_parameters.append(parameter)
            else:
                self.optional_parameters.append(parameter)
        # Uses "or" in case swagger contains None in description (explicitly set by service)
        self.help_url = SwaggerMethod.extract_url(swagger_method.get('description') or '')
        self.udf_name = '{0}_{1}'.format(service.udf_prefix, swagger_method['operationId'])
        self.responses = swagger_method.get('responses')
        if not self.responses:
            raise EmptyResponses(self.udf_name)

    def return_a_list(self):
        return ('application/json' in self.swagger_method['produces']) or \
               ('application/msqpack' in self.swagger_method['produces'])

    def security(self):
        return self.swagger_method.get('security')

    def summary(self):
        return self.swagger_method.get('summary')

    def initial_header(self):
        """
        Initial header content
        For more details refer to https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
        """
        # TODO Only set content-type when there is a body
        # TODO Set Accept header
        if 'application/msgpackpandas' in self.swagger_method['produces'] and support_pandas:
            return {'content-type': 'application/msgpackpandas'}
        if 'application/json' in self.swagger_method['produces']:
            return {'content-type': 'application/json'}
        return {}

    def contains_parameters(self):
        # TODO This method is only temporary as a transition from ugly Jinja template to cleaner code
        return len(self.required_parameters) > 0 or len(self.optional_parameters) > 0

    @staticmethod
    def extract_url(text):
        """
        Swagger URLs are interpreted thanks to the following format:
        [description of the url](url)
        :return: URL or None if no URL can be found.
        """
        urls = re.findall('^.*\[.*\]\((.*)\).*$', text)
        if urls:
            return urls[0]


def support_pandas():
    try:
        import pandas
        return True
    except:
        return False


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

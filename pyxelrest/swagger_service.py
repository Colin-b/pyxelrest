import os
try:
    # Python 3
    from configparser import ConfigParser
    from urllib.parse import urlparse
except ImportError:
    # Python 2
    from ConfigParser import ConfigParser
    from urlparse import urlparse

import requests
import vba
import logging


def extract_host(swagger_url):
    result = urlparse(swagger_url)
    return result.scheme + '://' + result.netloc


def extract_base_path(swagger_url):
    result = urlparse(swagger_url)
    full_path = result.path
    if len(full_path) == 0:
        return None
    # Remove last section of the path as it is used to access documentation
    paths = result.path.split('/')
    return '/'.join(paths[:-1])


class SwaggerService:
    def __init__(self, udf_prefix, config):
        """
        Load service information from configuration and swagger JSON.
        :param udf_prefix: Prefix to use in front of services UDFs to avoid duplicate between services.
        :param config: ConfigParser instance from where service details are retrieved.
        """
        self.udf_prefix = udf_prefix
        self.methods = [method.strip() for method in self.get_item(config, 'methods').split(',')]
        swagger_url = self.get_item(config, 'swagger_url')
        self.swagger = self._retrieve_swagger(swagger_url)
        self.validate_swagger_version()
        self.uri = self._extract_uri(swagger_url)
        logging.info('"{0}" service ({1}) will be available.'.format(udf_prefix, self.uri))

    def _extract_uri(self, swagger_url):
        # If the host is not included, the host serving the documentation is to be used (including the port).
        host = self.swagger['host'] if 'host' in self.swagger else extract_host(swagger_url)
        # If it is not included, the API is served directly under the host.
        base_path = self.swagger['basePath'] if 'basePath' in self.swagger else extract_base_path(swagger_url)

        return host + base_path if base_path else host

    def get_item(self, config, key):
        try:
            # Python 3
            section = config[self.udf_prefix]
            if key not in section:
                raise Exception('"{0}" configuration section must provide "{1}".'.format(self.udf_prefix, key))
            return section[key]
        except AttributeError:
            # Python 2
            if not config.has_option(self.udf_prefix, key):
                raise Exception('"{0}" configuration section must provide "{1}".'.format(self.udf_prefix, key))
            return config.get(self.udf_prefix, key)

    def get_item_default(self, config, key, default_value):
        try:
            # Python 3
            section = config[self.udf_prefix]
            return section[key] if key in section else default_value
        except AttributeError:
            # Python 2
            return config.get(self.udf_prefix, key) if config.has_option(self.udf_prefix, key) else default_value

    def _retrieve_swagger(self, swagger_url):
        """
        Retrieve swagger JSON from service.
        :param swagger_url: URI of the service swagger JSON.
        :return: Dictionary representation of the retrieved swagger JSON.
        """
        response = requests.get(swagger_url)
        response.raise_for_status()
        swagger = response.json()
        self._update_vba_restricted_keywords(swagger)
        return swagger

    @classmethod
    def _update_vba_restricted_keywords(cls, swagger_json):
        """
        Update name of parameters in the swagger JSON to avoid using VBA restricted keywords as parameter names.
        :param swagger_json: Dictionary representing the swagger JSON.
        :return: None
        """
        for methods in swagger_json['paths'].values():
            for method in methods.values():
                if 'parameters' in method:
                    for parameter in method['parameters']:
                        if parameter['name'] in vba.vba_restricted_keywords:
                            parameter['name'] = vba.vba_restricted_keywords[parameter['name']]

    def validate_swagger_version(self):
        if self.swagger['swagger'] != '2.0':
            raise Exception('PyxelRest does not support any other version (in this case "{}") than Swagger 2.0'.format(self.swagger['swagger']))


def load_services():
    """
    Retrieve swagger JSON for each service defined in configuration file.
    :return: List of SwaggerService objects, size is the same one as the number of sections within configuration file
    (DEFAULT excluded).
    """
    config_parser = ConfigParser()
    file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration.ini')
    if not config_parser.read(file_path):
        raise Exception('"{0}" configuration file cannot be read.'.format(file_path))
    logging.info('Loading configuration from "{0}".'.format(file_path))
    loaded_services = []
    for service in config_parser.sections():
        try:
            loaded_services.append(SwaggerService(service, config_parser))
        except Exception:
            logging.exception('"{0}" service will not be available.'.format(service))
    return loaded_services

import os
try:
    # Python 3
    from configparser import ConfigParser
except ImportError:
    # Python 2
    from ConfigParser import ConfigParser

import requests
import vba
import logging


class SwaggerService:
    def __init__(self, udf_prefix, config):
        """
        Load service information from configuration and swagger JSON.
        :param udf_prefix: Prefix to use in front of services UDFs to avoid duplicate between services.
        :param config: ConfigParser instance from where service details are retrieved.
        """
        logging.info('Creating {0} Swagger service.'.format(udf_prefix))
        self.udf_prefix = udf_prefix
        self.uri = self.get_item(config, 'host')
        self.methods = [method.strip() for method in self.get_item(config, 'methods').split(',')]

        # Consider that swagger is provided by base url
        swagger_suffix = self.get_item_default(config, 'swaggerBasePath', '/')
        self.swagger = self._retrieve_swagger(swagger_suffix)

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

    def _retrieve_swagger(self, swagger_suffix):
        """
        Retrieve swagger JSON from service.
        :param swagger_suffix: URI of the swagger JSON on the service.
        :return: Dictionary representation of the retrieved swagger JSON.
        """
        response = requests.get(self.uri + swagger_suffix)
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


def load_services():
    """
    Retrieve swagger JSON for each service defined in configuration file.
    :return: List of SwaggerService objects, size is the same one as the number of sections within configuration file
    (DEFAULT excluded).
    """
    config_parser = ConfigParser()
    file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'pixelrest_config.ini')
    if not config_parser.read(file_path):
        raise Exception('"{0}" configuration file cannot be read.'.format(file_path))
    logging.info('Loading configuration from "{0}".'.format(file_path))
    loaded_services = []
    for service in config_parser.sections():
        try:
            loaded_services.append(SwaggerService(service, config_parser))
        except Exception:
            logging.exception('Unable to load "{0}" service.'.format(service))
    return loaded_services

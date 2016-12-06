import datetime
import os, sys
from configparser import ConfigParser
import requests
from jinja2 import Environment, FileSystemLoader

# Some parameter names might be VBA keywords, this dictionary is used to use valid VBA parameter names.
vba_restricted_keywords = {
    'currency': 'currency_visual_basic'
}


class SwaggerService:
    def __init__(self, udf_prefix, config):
        """
        Load service information from configuration and swagger JSON.
        :param udf_prefix: Prefix to use in front of services UDFs to avoid duplicate between services.
        :param config: ConfigParser instance from where service details are retrieved.
        """
        section = config[udf_prefix]
        self.udf_prefix = udf_prefix

        if 'host' not in section:
            raise Exception('"{0}" configuration section must provide "host".'.format(udf_prefix))
        self.uri = section['host']

        if 'methods' not in section:
            raise Exception('"{0}" configuration section must provide "methods".'.format(udf_prefix))
        self.methods = [method.strip() for method in section['methods'].split(',')]

        # Consider that swagger is provided by base url
        swagger_suffix = section['swaggerBasePath'] if 'swaggerBasePath' in section else '/'
        self.swagger = self._retrieve_swagger(swagger_suffix)

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
                for parameter in method['parameters']:
                    if parameter['name'] in vba_restricted_keywords:
                        parameter['name'] = vba_restricted_keywords[parameter['name']]


def load_services(config_file_path):
    """
    Retrieve swagger JSON for each service defined in configuration file.
    :param config_file_path: Absolute file path (related to this file) to configuration file.
    :return: List of SwaggerService objects, size is the same one as the number of sections within configuration file
    (DEFAULT excluded).
    """
    config_parser = ConfigParser()
    file_path = os.path.abspath(config_file_path)
    if not config_parser.read(file_path):
        raise Exception('"{0}" configuration file cannot be read.'.format(file_path))
    return [SwaggerService(service, config_parser) for service in config_parser.sections()]


def user_defined_functions():
    """
    Create xlwings User Defined Functions according to user_defined_functions template.
    :return: A string containing python code with all xlwings UDFs.
    """
    renderer = Environment(loader=FileSystemLoader(os.path.dirname(__file__)), trim_blocks=True)
    return renderer.get_template('user_defined_functions.tpl').render(
        current_utc_time=datetime.datetime.utcnow().isoformat(),
        services=load_services('resources/config/default.ini'),
        modified_parameters={value: key for key, value in vba_restricted_keywords.items()}
    )


def generate_user_defined_functions():
    """
    Create user_defined_functions.py python file containing generated xlwings User Defined Functions.
    :return: None
    """
    with open(os.path.join(os.path.dirname(__file__), 'user_defined_functions.py'), 'w') as generated_file:
        generated_file.write(user_defined_functions())


generate_user_defined_functions()

from src.main.python.pyxelrest.user_defined_functions import *

# Uncomment to debug Microsoft Excel UDF calls.
# if __name__ == '__main__':
#     xw.serve()

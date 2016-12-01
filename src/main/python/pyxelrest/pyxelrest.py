import datetime
import os
from configparser import ConfigParser
import requests
from jinja2 import Environment, FileSystemLoader

# Some parameter names might be VBA keywords
vba_restricted_keywords = {
    'currency': 'currency_visual_basic'
}


class SwaggerService:
    def __init__(self, udf_prefix, config):
        section = config[udf_prefix]
        self.udf_prefix = udf_prefix

        if 'host' not in section:
            raise Exception(f'"{udf_prefix}" configuration section must provide "host".')
        self.uri = section['host']

        if 'methods' not in section:
            raise Exception(f'"{udf_prefix}" configuration section must provide "methods".')
        self.methods = [method.strip() for method in section['methods'].split(',')]

        # Consider that swagger is provided by base url
        swagger_suffix = section['swaggerBasePath'] if 'swaggerBasePath' in section else '/'
        self.swagger = self._retrieve_swagger(swagger_suffix)

    def _retrieve_swagger(self, swagger_suffix):
        response = requests.get(self.uri + swagger_suffix)
        response.raise_for_status()
        swagger = response.json()
        for methods in swagger['paths'].values():
            for method in methods.values():
                for parameter in method['parameters']:
                    if parameter['name'] in vba_restricted_keywords:
                        parameter['name'] = vba_restricted_keywords[parameter['name']]
        return swagger


def load_services(config_file_path):
    config = ConfigParser()
    file_path = os.path.abspath(config_file_path)
    if not config.read(file_path):
        raise Exception(f'"{file_path}" configuration file cannot be read.')
    return [
        SwaggerService(service, config) for service in config.sections()
    ]


with open(os.path.join(os.path.dirname(__file__), 'user_defined_functions.py'), 'w') as generated_file:
    renderer = Environment(loader=FileSystemLoader(os.path.dirname(__file__)), trim_blocks=True)
    generated_file_content = renderer.get_template('user_defined_functions.tpl').render(
        current_utc_time=datetime.datetime.utcnow().isoformat(),
        services=load_services('resources/config/default.ini'),
        modified_parameters={value: key for key, value in vba_restricted_keywords.items()}
    )
    generated_file.write(generated_file_content)

from src.main.python.pyxelrest.user_defined_functions import *

# Uncomment to debug Microsoft Excel UDF calls
if __name__ == '__main__':
    xw.serve()

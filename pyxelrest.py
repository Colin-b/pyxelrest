import os
import requests
import datetime
from jinja2 import Environment, FileSystemLoader

# Some parameter names might be VBA keywords
vba_restricted_keywords = {
    'currency': 'currency_visual_basic'
}

class SwaggerService:
    def __init__(self, udf_prefix, uri, methods):
        self.udf_prefix = udf_prefix
        self.uri = uri
        self.methods = methods
        self.swagger = self._retrieve_swagger()

    def _retrieve_swagger(self):
        swagger = requests.get(self.uri + '/swagger.json').json()
        for method_path, methods in swagger['paths'].iteritems():
            for method_type, method in methods.iteritems():
                for parameter in method['parameters']:
                    if parameter['name'] in vba_restricted_keywords:
                        parameter['name'] = vba_restricted_keywords[parameter['name']]
        return swagger

# TODO Retrieve this list from configuration file?
services = [
    SwaggerService('ordosdev', 'http://rms.gdfsuez.net:8310/ordos-dev', ['get', 'post', 'put', 'delete']),
    SwaggerService('sds', 'http://rms.gdfsuez.net:8310/sds', ['get', 'post', 'put', 'delete']),
    SwaggerService('rms', 'http://rms.gdfsuez.net:8310/kernel', ['get', 'post', 'put', 'delete'])
]

with open(os.path.join(os.path.dirname(__file__), 'user_defined_functions.py'), 'w') as generated_file:
    renderer = Environment(loader=FileSystemLoader(os.path.dirname(__file__)), trim_blocks=True)
    generated_file_content = renderer.get_template('user_defined_functions.tpl').render(
        current_utc_time=datetime.datetime.utcnow().isoformat(),
        services=services,
        modified_parameters={value: key for key, value in vba_restricted_keywords.iteritems()}
    )
    generated_file.write(generated_file_content)

from user_defined_functions import *

# Uncomment to debug excel calls
# if __name__ == '__main__':
#     xw.serve()

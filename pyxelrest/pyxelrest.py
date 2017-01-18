"""
Each time the pyxelrest module is loaded it will generate xlwings User Defined Functions.
"""
import os
import datetime
import logging
import logging.config
import logging.handlers
import jinja2
import yaml

import vba
import swagger_service
from importlib import import_module
try:
    # Python 3
    from importlib import reload
except:
    # Python 2
    from imp import reload


def user_defined_functions(services):
    """
    Create xlwings User Defined Functions according to user_defined_functions template.
    :return: A string containing python code with all xlwings UDFs.
    """
    renderer = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), trim_blocks=True)
    renderer.tests['table_result'] = lambda produces: produces and ('application/json' in produces or 'application/msqpack' in produces)
    return renderer.get_template('user_defined_functions.jinja2').render(
        current_utc_time=datetime.datetime.utcnow().isoformat(),
        services=services,
        modified_parameters={value: key for key, value in vba.vba_restricted_keywords.items()}
    )


def generate_user_defined_functions(services):
    """
    Create user_defined_functions.py python file containing generated xlwings User Defined Functions.
    :return: None
    """
    logging.info('Generating user defined functions.')
    with open(os.path.join(os.path.dirname(__file__), 'user_defined_functions.py'), 'w') as generated_file:
        generated_file.write(user_defined_functions(services))

logging_configuration_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'logging_configuration.ini')
if os.path.isfile(logging_configuration_file_path):
    with open(logging_configuration_file_path, 'r') as config_file:
        log_config_dict=yaml.load(config_file)
        logging.config.dictConfig(log_config_dict)
else:
    logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
                        handlers=[logging.handlers.TimedRotatingFileHandler(os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'pyxelrest.log'), when='D')],
                        level=logging.INFO)
    logging.warning('Logging configuration file ({0}) cannot be found. Using default logging configuration.', logging_configuration_file_path)

services = swagger_service.load_services()
generate_user_defined_functions(services)

logging.info('Expose user defined functions through PyxelRest.')

try:
    # Force reload of module (even if this is first time, it should not take long) as reloading pyxelrest does not reload UDFs otherwise
    reload(import_module('user_defined_functions'))
    from user_defined_functions import *
except Exception:
    logging.warning('Failed to import UDFs relatively to module class. Trying relatively to module folder.')
    reload(import_module('pyxelrest.user_defined_functions'))
    # Occurs when calling pyxelrest via xlwings in non-debug mode
    from pyxelrest.user_defined_functions import *


# Uncomment to debug Microsoft Excel UDF calls.
# if __name__ == '__main__':
#     xw.serve()

"""
Each time this module is loaded it will generate xlwings User Defined Functions.
"""
import os
import re
import datetime
import jinja2
import yaml
import logging
import logging.config
import logging.handlers
from importlib import import_module
from builtins import open

try:
    # Python 3
    from importlib import reload
except ImportError:
    # Python 2
    from imp import reload

import vba
import _version
import authentication
import swagger


def init_logging():
    logging_configuration_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'logging.ini')
    if os.path.isfile(logging_configuration_file_path):
        with open(logging_configuration_file_path, 'r') as config_file:
            log_config_dict = yaml.load(config_file)
            logging.config.dictConfig(log_config_dict)
    else:
        default_log_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'logs', 'pyxelrest.log')
        logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
                            handlers=[logging.handlers.TimedRotatingFileHandler(default_log_file_path, when='D')],
                            level=logging.INFO)
        logging.warning('Logging configuration file ({0}) cannot be found. Using default logging configuration.'.format(
            logging_configuration_file_path))


def user_defined_functions(loaded_services):
    """
    Create xlwings User Defined Functions according to user_defined_functions template.
    :return: A string containing python code with all xlwings UDFs.
    """
    renderer = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__), encoding="utf-8"),
        trim_blocks=True,
        lstrip_blocks=True
    )

    renderer.tests['table_result'] = lambda produces: \
        produces and ('application/json' in produces or 'application/msqpack' in produces)
    return renderer.get_template('user_defined_functions.jinja2').render(
        current_utc_time=datetime.datetime.utcnow().isoformat(),
        services=loaded_services,
        modified_parameters={value: key for key, value in vba.vba_restricted_keywords.items()},
        support_pandas=support_pandas(),
        support_ujson=support_ujson(),
        extract_url=extract_url
    )


def support_pandas():
    try:
        import pandas
        return True
    except:
        return False


def support_ujson():
    try:
        import ujson
        return True
    except:
        return False


def extract_url(text):
    """
    Swagger URLs are interpreted thanks to the following format:
    [description of the url](url)
    :return: URL or None if no URL can be found.
    """
    if text:
        urls = re.findall('^.*\[.*\]\((.*)\).*$', text)
        if urls:
            return urls[0]


def generate_user_defined_functions():
    """
    Create user_defined_functions.py python file containing generated xlwings User Defined Functions.
    :return: None
    """
    logging.debug('Generating user defined functions.')
    services = swagger.load_services()
    with open(os.path.join(os.path.dirname(__file__), 'user_defined_functions.py'), 'w', encoding='utf-8') \
            as generated_file:
        generated_file.write(user_defined_functions(services))


init_logging()
logging.debug('Loading PyxelRest version {}'.format(_version.__version__))

try:
    authentication.stop_servers()
    authentication.oauth2_security_definitions_by_port = {}
    authentication.security_definitions = {}
    generate_user_defined_functions()
    authentication.start_servers()
except:
    logging.exception('Cannot generate user defined functions.')
    raise

try:
    logging.debug('Expose user defined functions through PyxelRest.')
    # Force reload of module (even if this is first time, it should not take long)
    # as reloading pyxelrest does not reload UDFs otherwise
    # TODO This is temporary until xlwings force a python reload instead
    reload(import_module('user_defined_functions'))
    from user_defined_functions import *
except:
    logging.exception('Error while importing UDFs.')


# Uncomment to debug Microsoft Excel UDF calls.
# if __name__ == '__main__':
#      xw.serve()

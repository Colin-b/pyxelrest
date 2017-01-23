"""
Each time the pyxelrest module is loaded it will generate xlwings User Defined Functions.
"""
import os
import datetime
import jinja2
from importlib import import_module
try:
    # Python 3
    from importlib import reload
except ImportError:
    # Python 2
    from imp import reload

import pyxelrestlogging
import logging
import logging.config
import logging.handlers
import vba
import swagger_service


def user_defined_functions(loaded_services):
    """
    Create xlwings User Defined Functions according to user_defined_functions template.
    :return: A string containing python code with all xlwings UDFs.
    """
    renderer = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), trim_blocks=True)
    renderer.tests['table_result'] = lambda produces: \
        produces and ('application/json' in produces or 'application/msqpack' in produces)
    return renderer.get_template('user_defined_functions.jinja2').render(
        current_utc_time=datetime.datetime.utcnow().isoformat(),
        services=loaded_services,
        modified_parameters={value: key for key, value in vba.vba_restricted_keywords.items()},
        support_pandas=support_pandas()
    )


def support_pandas():
    try:
        import pandas
        return True
    except:
        return False


def generate_user_defined_functions(loaded_services):
    """
    Create user_defined_functions.py python file containing generated xlwings User Defined Functions.
    :return: None
    """
    logging.info('Generating user defined functions.')
    with open(os.path.join(os.path.dirname(__file__), 'user_defined_functions.py'), 'w') as generated_file:
        generated_file.write(user_defined_functions(loaded_services))

services = swagger_service.load_services()
generate_user_defined_functions(services)

logging.info('Expose user defined functions through PyxelRest.')

try:
    # Force reload of module (even if this is first time, it should not take long)
    # as reloading pyxelrest does not reload UDFs otherwise
    # TODO This is temporary until xlwings force a python reload instead
    reload(import_module('user_defined_functions'))
    from user_defined_functions import *
except ImportError:
    logging.exception('Failed to import UDFs relatively to module class. Trying relatively to module folder.')
    # TODO This is temporary until xlwings force a python reload instead
    reload(import_module('pyxelrest.user_defined_functions'))
    # Occurs when calling pyxelrest via xlwings in non-debug mode
    from pyxelrest.user_defined_functions import *
except:
    logging.exception('Error while importing UDFs.')


# Uncomment to debug Microsoft Excel UDF calls.
# if __name__ == '__main__':
#     xw.serve()

"""
Each time this module is loaded it will generate xlwings User Defined Functions.
"""
import os
import sys
import jinja2
import logging.config
import logging.handlers
import datetime
import authentication
import pyxelrest.custom_logging
from importlib import import_module
from builtins import open

if sys.version_info.major > 2:
    # Python 3
    from importlib import reload
else:
    # Python 2
    from imp import reload

import vba
import authentication
import swagger

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
    return renderer.get_template('user_defined_functions.jinja2').render(
        current_utc_time=datetime.datetime.utcnow().isoformat(),
        services=loaded_services,
        modified_parameters={value: key for key, value in vba.vba_restricted_keywords.items()},
        support_pandas=swagger.support_pandas(),
        support_ujson=support_ujson(),
        authentication=authentication
    )


def support_ujson():
    try:
        import ujson
        return True
    except:
        return False


def generate_user_defined_functions():
    """
    Create user_defined_functions.py python file containing generated xlwings User Defined Functions.
    :return: None
    """
    services = swagger.load_services()
    logging.debug('Generating user defined functions.')
    with open(os.path.join(os.path.dirname(__file__), 'user_defined_functions.py'), 'w', encoding='utf-8') \
            as generated_file:
        generated_file.write(user_defined_functions(services))

try:
    authentication.security_definitions = {}
    authentication.custom_authentications = {}
    generate_user_defined_functions()
except Exception as e:
    logging.exception('Cannot generate user defined functions.')
    raise

try:
    logging.debug('Expose user defined functions through PyxelRest.')
    # Force reload of module (even if this is first time, it should not take long)
    # as reloading pyxelrest does not reload UDFs otherwise
    # TODO This is temporary until xlwings force a python reload instead
    reload(import_module('pyxelrest.user_defined_functions'))
    from pyxelrest.user_defined_functions import *
except:
    logging.exception('Error while importing UDFs.')


# Uncomment to debug Microsoft Excel UDF calls.
# if __name__ == '__main__':
#      xw.serve()

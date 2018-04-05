"""
Each time this module is loaded (and GENERATE_UDF_ON_IMPORT is True) it will generate xlwings User Defined Functions.
"""
import os
import sys
import jinja2
import logging.config
import logging.handlers
import datetime
from importlib import import_module
from pyxelrest import (
    vba,
    authentication,
    swagger,
    _version,
    GENERATE_UDF_ON_IMPORT,
    custom_logging
)

if sys.version_info.major > 2:
    # Python 3
    from builtins import open
    from importlib import reload
else:
    # Python 2
    from imp import reload


def user_defined_functions(loaded_services, pyxelrest_config, flattenize=True):
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
        pyxelrest_config=pyxelrest_config,
        modified_parameters={value: key for key, value in vba.vba_restricted_keywords.items()},
        support_pandas=swagger.support_pandas(),
        support_ujson=support_ujson(),
        authentication=authentication,
        flattenize=flattenize
    )


def support_ujson():
    try:
        import ujson
        return True
    except:
        return False


def generate_user_defined_functions(output='user_defined_functions.py', flattenize=True):
    """
    Load services and create user_defined_functions.py python file containing generated xlwings User Defined Functions.
    :param flattenize: Set to False if you want the JSON dictionary as result of your UDF call.
    :return: None
    """
    services, pyxelrest_config = swagger.load_services()
    logging.debug('Generating user defined functions.')
    with open(os.path.join(os.path.dirname(__file__), output), 'w', encoding='utf-8') \
            as generated_file:
        generated_file.write(user_defined_functions(services, pyxelrest_config, flattenize))
    return services


def reload_user_defined_functions(services):
    """
    Force reload of module (even if this is first time, it should not take long)
    as reloading pyxelrest does not reload UDFs otherwise
    TODO This is temporary until xlwings force a python reload instead
    :return: None
    """
    reload(import_module('pyxelrest.user_defined_functions'))
    from pyxelrest import user_defined_functions as udfs
    udfs.open_api_methods = {
        udf_name: method
        for service in services
        for udf_name, method in service.methods.items()
    }


def reset_authentication():
    authentication.security_definitions = {}
    authentication.custom_authentications = {}


if __name__ == '__main__':
    logger = logging.getLogger("pyxelrest.pyxelrestgenerator")
else:
    logger = logging.getLogger(__name__)

# TODO Generate one service per file instead of a full file
if GENERATE_UDF_ON_IMPORT:
    custom_logging.load_logging_configuration()
    reset_authentication()
    try:
        services = generate_user_defined_functions()
    except Exception as e:
        logger.exception('Cannot generate user defined functions.')
        raise

    try:
        logger.debug('Expose user defined functions through PyxelRest.')
        reload_user_defined_functions(services)
        from pyxelrest.user_defined_functions import *
    except:
        logger.exception('Error while importing UDFs.')

# Uncomment to debug Microsoft Excel UDF calls.
# if __name__ == '__main__':
#      xw.serve()

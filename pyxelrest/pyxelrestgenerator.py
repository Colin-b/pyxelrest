"""
Each time this module is loaded (and GENERATE_UDF_ON_IMPORT is True) it will generate xlwings User Defined Functions.
"""
import os
import jinja2
import logging.config
import logging.handlers
import datetime
import sys
from pyxelrest import (
    open_api,
    GENERATE_UDF_ON_IMPORT,
    custom_logging
)

if sys.version_info.major > 2:
    # Python 3
    from builtins import open


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
        services=loaded_services
    )


def generate_user_defined_functions(output='user_defined_functions.py', flattenize=True):
    """
    Load services and create user_defined_functions.py python file containing generated xlwings User Defined Functions.
    :param flattenize: Set to False if you want the JSON dictionary as result of your UDF call.
    :return: List of loaded services
    """
    services = open_api.load_services(flattenize)
    logging.debug('Generating user defined functions.')
    with open(os.path.join(os.path.dirname(__file__), output), 'w', encoding='utf-8') \
            as generated_file:
        generated_file.write(user_defined_functions(services))
    return services


def load_user_defined_functions(services):
    from pyxelrest import user_defined_functions as udfs
    udfs.udf_methods = {
        udf_name: method
        for service in services
        for udf_name, method in service.methods.items()
    }


if __name__ == '__main__':
    logger = logging.getLogger("pyxelrest.pyxelrestgenerator")
else:
    logger = logging.getLogger(__name__)

if GENERATE_UDF_ON_IMPORT:
    custom_logging.load_logging_configuration()
    try:
        services = generate_user_defined_functions()
    except Exception as e:
        logger.exception('Cannot generate user defined functions.')
        raise

    try:
        logger.debug('Expose user defined functions through PyxelRest.')
        load_user_defined_functions(services)
        from pyxelrest.user_defined_functions import *
    except:
        logger.exception('Error while importing UDFs.')

# Uncomment to debug Microsoft Excel UDF calls.
# if __name__ == '__main__':
#      xw.serve()

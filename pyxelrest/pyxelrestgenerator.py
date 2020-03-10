"""
Each time this module is loaded (and GENERATE_UDF_ON_IMPORT is True) it will generate xlwings User Defined Functions.
"""
import os
from importlib import reload, import_module
from typing import List, Union

import jinja2
import logging.config
import logging.handlers
import datetime
import sys
from pyxelrest import (
    open_api,
    GENERATE_UDF_ON_IMPORT,
    custom_logging,
    SERVICES_CONFIGURATION_FILE_PATH,
    LOGGING_CONFIGURATION_FILE_PATH,
)


def _user_defined_functions(
    loaded_services: List[Union[open_api.PyxelRestService, open_api.OpenAPI]]
) -> str:
    """
    Create xlwings User Defined Functions according to user_defined_functions template.
    :return: A string containing python code with all xlwings UDFs.
    """
    renderer = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__), encoding="utf-8"),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return renderer.get_template("user_defined_functions.jinja2").render(
        current_utc_time=datetime.datetime.utcnow().isoformat(),
        services=loaded_services,
    )


def generate_python_file(
    services: List[Union[open_api.PyxelRestService, open_api.OpenAPI]],
    file_name="user_defined_functions.py",
):
    """
    Create python file containing generated xlwings User Defined Functions.
    """
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    logging.debug(f"Generating {file_path}")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(_user_defined_functions(services))


def load_user_defined_functions(
    services: List[Union[open_api.PyxelRestService, open_api.OpenAPI]]
):
    # Ensure that newly generated file is reloaded as user_defined_functions
    user_defined_functions = reload(import_module("pyxelrest.user_defined_functions"))

    user_defined_functions.udf_methods = {
        udf_name: method
        for service in services
        for udf_name, method in service.methods.items()
    }


if __name__ == "__main__":
    logger = logging.getLogger("pyxelrest.pyxelrestgenerator")
else:
    logger = logging.getLogger(__name__)

if GENERATE_UDF_ON_IMPORT:
    custom_logging.load_logging_configuration(LOGGING_CONFIGURATION_FILE_PATH)
    try:
        services = open_api.load_services_from_yaml(SERVICES_CONFIGURATION_FILE_PATH)
        generate_python_file(services)
    except Exception as e:
        logger.exception("Cannot generate user defined functions.")
        raise

    try:
        logger.debug("Expose user defined functions through PyxelRest.")
        load_user_defined_functions(services)
        from pyxelrest.user_defined_functions import *
    except:
        logger.exception("Error while importing UDFs.")

# Uncomment to debug Microsoft Excel UDF calls.
# if __name__ == '__main__':
#      xw.serve()

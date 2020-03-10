"""
Each time this module is loaded (and GENERATE_UDF_ON_IMPORT is True) it will generate xlwings User Defined Functions.
"""
import os
from importlib import reload, import_module
from typing import List, Union
import logging.config
import logging.handlers
import datetime
import sys

import jinja2

from pyxelrest import (
    open_api,
    GENERATE_UDF_ON_IMPORT,
    custom_logging,
    SERVICES_CONFIGURATION_FILE_PATH,
    LOGGING_CONFIGURATION_FILE_PATH,
)


def _user_defined_functions(
    service: Union[open_api.PyxelRestService, open_api.OpenAPI]
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
        current_utc_time=datetime.datetime.utcnow().isoformat(), service=service
    )


def _user_defined_functions_init(
    services: List[Union[open_api.PyxelRestService, open_api.OpenAPI]]
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
    return renderer.get_template("user_defined_functions_init.jinja2").render(
        current_utc_time=datetime.datetime.utcnow().isoformat(), services=services
    )


def generate_python_file(
    services: List[Union[open_api.PyxelRestService, open_api.OpenAPI]]
):
    """
    Create python file containing generated xlwings User Defined Functions.
    """
    for service in services:
        file_path = os.path.join(
            os.path.dirname(__file__),
            "user_defined_functions",
            f"{service.config.name}.py",
        )
        logging.debug(f"Generating {file_path}")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(_user_defined_functions(service))

    file_path = os.path.join(
        os.path.dirname(__file__), "user_defined_functions", "__init__.py"
    )
    logging.debug(f"Generating {file_path}")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(_user_defined_functions_init(services))


def load_user_defined_functions(
    services: List[Union[open_api.PyxelRestService, open_api.OpenAPI]]
):
    # Ensure that newly generated file is reloaded as user_defined_functions
    user_defined_functions = reload(import_module("pyxelrest.user_defined_functions"))
    user_defined_functions.update_services(services)


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

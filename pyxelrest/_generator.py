"""
Each time this module is loaded (and GENERATE_UDF_ON_IMPORT is True) it will generate xlwings User Defined Functions.
"""
import os
from importlib import reload, import_module
from typing import List, Union
import logging.config
import logging.handlers
import datetime

import jinja2
import yaml

from pyxelrest import (
    GENERATE_UDF_ON_IMPORT,
    _custom_logging,
    SERVICES_CONFIGURATION_FILE_PATH,
    LOGGING_CONFIGURATION_FILE_PATH,
)
from pyxelrest._common import check_for_duplicates, Service
from pyxelrest._open_api import load_service
from pyxelrest._rest import PyxelRestService


def load_services_from_yaml(services_configuration_file_path: str) -> List[Service]:
    """
    Retrieve OpenAPI JSON definition for each service defined in configuration file.
    :return: List of OpenAPI and PyxelRestService instances, size is the same one as the number of sections within
    configuration file
    """
    if not os.path.isfile(services_configuration_file_path):
        logging.warning(f'No services will be available as "{services_configuration_file_path}" cannot be found.')
        return []

    with open(services_configuration_file_path, "r") as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)

    logging.debug(f'Loading services from "{services_configuration_file_path}"...')
    return load_services(config)


def load_services(config: dict) -> List[Service]:
    """
    Retrieve OpenAPI JSON definition for each service defined in configuration.
    :return: List of OpenAPI and PyxelRestService instances, size is the same one as the number of sections within
    configuration.
    """
    if not isinstance(config, dict):
        raise Exception("Configuration must be a dictionary.")

    loaded_services = []
    for service_name, service_config in config.items():
        if "pyxelrest" == service_name:
            pyxelrest_service = PyxelRestService(service_name, service_config)
            loaded_services.append(pyxelrest_service)
        else:
            service = load_service(service_name, service_config)
            if service:
                loaded_services.append(service)

    check_for_duplicates(loaded_services)
    return loaded_services


def _user_defined_functions(service: Service) -> str:
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


def _user_defined_functions_init(services: List[Service]) -> str:
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


def generate_python_file(services: List[Service]):
    """
    Create python file containing generated xlwings User Defined Functions.
    """
    user_defined_functions_path = os.path.join(
        os.path.dirname(__file__), "user_defined_functions"
    )
    if not os.path.exists(user_defined_functions_path):
        os.makedirs(user_defined_functions_path)

    for service in services:
        file_path = os.path.join(
            user_defined_functions_path, f"{service.config.name}.py"
        )
        logging.debug(f"Generating {file_path}")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(_user_defined_functions(service))

    file_path = os.path.join(user_defined_functions_path, "__init__.py")
    logging.debug(f"Generating {file_path}")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(_user_defined_functions_init(services))


def load_user_defined_functions(services: List[Service]):
    # Ensure that newly generated file is reloaded as user_defined_functions
    user_defined_functions = reload(import_module("pyxelrest.user_defined_functions"))
    user_defined_functions.update_services(services)


if __name__ == "__main__":
    logger = logging.getLogger("pyxelrest._generator")
else:
    logger = logging.getLogger(__name__)

if GENERATE_UDF_ON_IMPORT:
    _custom_logging.load_logging_configuration(LOGGING_CONFIGURATION_FILE_PATH)
    try:
        services = load_services_from_yaml(SERVICES_CONFIGURATION_FILE_PATH)
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

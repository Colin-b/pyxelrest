"""
Each time this module is loaded (and GENERATE_UDF_ON_IMPORT is True) it will generate xlwings User Defined Functions.
"""
import os
import sys
import platform
from importlib import reload, import_module
from typing import List
import logging.config
import logging.handlers
import datetime
from distutils import sysconfig

import jinja2
import yaml

from pyxelrest import (
    GENERATE_UDF_ON_IMPORT,
    version,
)
from pyxelrest._generator_config import (
    SERVICES_CONFIGURATION_FILE_PATH,
    LOGGING_CONFIGURATION_FILE_PATH,
)
from pyxelrest._common import check_for_duplicates, Service
from pyxelrest._open_api import load_service
from pyxelrest._rest import PyxelRest


def load_services(config: dict) -> List[Service]:
    """
    Retrieve OpenAPI definition for each service defined in configuration.
    :return: List of OpenAPI and PyxelRest instances, size should be the same one as the number of sections within
    configuration.
    """
    loaded_services = []
    for name, settings in config.items():
        if "pyxelrest" == name:
            pyxelrest_service = PyxelRest(settings)
            loaded_services.append(pyxelrest_service)
        else:
            service = load_service(name, settings)
            if service:
                loaded_services.append(service)

    check_for_duplicates(loaded_services)
    return loaded_services


def _generated_api(service: Service) -> str:
    """
    Create xlwings User Defined Functions for a REST API according to generated_api template.
    :return: A string containing python code with all xlwings UDFs.
    """
    renderer = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__), encoding="utf-8"),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return renderer.get_template("generated_api.jinja2").render(
        current_utc_time=datetime.datetime.utcnow().isoformat(), service=service
    )


def _generated_init(services: List[Service]) -> str:
    """
    Create __init__ file for the generated folder.
    :return: A string containing python code of the __init__ file.
    """
    renderer = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__), encoding="utf-8"),
        # https://jinja.palletsprojects.com/en/2.11.x/templates/?highlight=spaces#whitespace-control
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return renderer.get_template("generated_init.jinja2").render(
        current_utc_time=datetime.datetime.utcnow().isoformat(), services=services
    )


def generate_python_files(services: List[Service]):
    """
    Create python file containing generated xlwings User Defined Functions.
    """
    generated_folder_path = os.path.join(os.path.dirname(__file__), "generated")
    if not os.path.exists(generated_folder_path):
        os.makedirs(generated_folder_path)

    for service in services:
        file_path = os.path.join(generated_folder_path, f"{service.config.name}.py")
        logging.debug(f"Generating {file_path}")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(_generated_api(service))

    file_path = os.path.join(generated_folder_path, "__init__.py")
    logging.debug(f"Generating {file_path}")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(_generated_init(services))


def reload_generated(services: List[Service]):
    generated = reload(import_module("pyxelrest.generated"))
    generated.update_services(services)


if __name__ == "__main__":
    logger = logging.getLogger("pyxelrest._generator")
else:
    logger = logging.getLogger(__name__)


def load_logging_configuration():
    """
    Load YAML logging configuration if found.
    :return: None
    """
    logging_configuration_file_path = LOGGING_CONFIGURATION_FILE_PATH
    if os.path.isfile(logging_configuration_file_path):
        with open(logging_configuration_file_path, "r") as config_file:
            log_config_dict = yaml.load(config_file, Loader=yaml.SafeLoader)
            logging.config.dictConfig(log_config_dict)
    else:
        logger.warning(
            f"Logging configuration file ({logging_configuration_file_path}) cannot be found."
        )
    logger.info(
        f"Loading PyxelRest: {version.__version__} Python: {sys.version} OS: {platform.platform()} Lib: {sysconfig.get_python_lib()}"
    )


def load_services_from_yaml() -> List[Service]:
    """
    Retrieve OpenAPI JSON definition for each service defined in configuration file.
    :return: List of OpenAPI and PyxelRestService instances, size is the same one as the number of sections within
    configuration file
    """
    services_configuration_file_path = SERVICES_CONFIGURATION_FILE_PATH
    if not os.path.isfile(services_configuration_file_path):
        logging.warning(
            f'No services will be available as "{services_configuration_file_path}" cannot be found.'
        )
        return []

    with open(services_configuration_file_path, "r") as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)

    logging.debug(f'Loading services from "{services_configuration_file_path}"...')
    return load_services(config or {})


if GENERATE_UDF_ON_IMPORT:
    load_logging_configuration()
    try:
        services = load_services_from_yaml()
        generate_python_files(services)
    except Exception as e:
        logger.exception("Cannot generate python files.")
        raise

    try:
        logger.debug("Expose generated functions.")
        reload_generated(services)
        from pyxelrest.generated import *
    except:
        logger.exception("Cannot expose generated functions.")

# Uncomment to debug Microsoft Excel UDF calls.
# if __name__ == '__main__':
#      xw.serve()

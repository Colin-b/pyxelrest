import os
import sys
import platform
import logging.config
import logging.handlers
from distutils import sysconfig

import yaml

from pyxelrest import version

logger = logging.getLogger(__name__)


def log_uncaught_exception(exec_type, exex_value, traceback, logger=logging):
    logger.error(
        "Logging an uncaught exception", exc_info=(exec_type, exex_value, traceback)
    )


sys.excepthook = log_uncaught_exception


def load_logging_configuration(logging_configuration_file_path: str):
    """
    Load YAML logging configuration.
    If file is not found, then logging will be performed as INFO into %APPDATA%\\pyxelrest\\logs\\pyxelrest.log
    and file will be rolled every day.
    :return: None
    """
    if os.path.isfile(logging_configuration_file_path):
        with open(logging_configuration_file_path, "r") as config_file:
            log_config_dict = yaml.load(config_file, Loader=yaml.FullLoader)
            logging.config.dictConfig(log_config_dict)
            logger.info(
                f"Loading PyxelRest: {version.__version__} Python: {sys.version} OS: {platform.platform()} Lib: {sysconfig.get_python_lib()}"
            )
    else:
        set_file_logger("pyxelrest")
        logger.warning(
            f"Logging configuration file ({logging_configuration_file_path}) cannot be found. Using default logging configuration."
        )


def set_file_logger(filename: str, level=logging.INFO):
    default_log_file_path = os.path.join(
        os.getenv("APPDATA"), "pyxelrest", "logs", f"{filename}.log"
    )
    default_log_folder = os.path.dirname(default_log_file_path)
    if not os.path.exists(default_log_folder):
        os.makedirs(default_log_folder)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(process)d:%(thread)d - %(filename)s:%(lineno)d - %(message)s",
        handlers=[
            logging.handlers.TimedRotatingFileHandler(default_log_file_path, when="D")
        ],
        level=level,
    )
    logger.info(
        f"Loading PyxelRest: {version.__version__} Python: {sys.version} OS: {platform.platform()} Lib: {sysconfig.get_python_lib()}"
    )

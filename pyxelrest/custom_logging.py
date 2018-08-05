import os
import sys
import platform
import logging.config
import logging.handlers
import yaml

from pyxelrest import _version, LOGGING_CONFIGURATION_FILE_PATH
from distutils import sysconfig

logger = logging.getLogger(__name__)


def log_uncaught_exception(excType, excValue, traceback, logger=logging):
    logger.error("Logging an uncaught exception", exc_info=(excType, excValue, traceback))


sys.excepthook = log_uncaught_exception


def load_logging_configuration():
    """
    Load YAML logging configuration.
    If file is not found, then logging will be performed as INFO into %APPDATA%\pyxelrest\logs\pyxelrest.log
    and file will be rolled every day.
    :return: None
    """
    if os.path.isfile(LOGGING_CONFIGURATION_FILE_PATH):
        with open(LOGGING_CONFIGURATION_FILE_PATH, 'r') as config_file:
             log_config_dict = yaml.load(config_file)
             logging.config.dictConfig(log_config_dict)
             logger.info('Loading PyxelRest: {} Python: {} OS: {} Lib: {}'.format(
                 _version.__version__, sys.version, platform.platform(), sysconfig.get_python_lib()))
    else:
        set_file_logger('pyxelrest')
        logger.warning('Logging configuration file ({0}) cannot be found. Using default logging configuration.'.format(
            LOGGING_CONFIGURATION_FILE_PATH))


def set_file_logger(filename, level=logging.INFO):
    default_log_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'logs', filename + '.log')
    default_log_folder = os.path.dirname(default_log_file_path)
    if not os.path.exists(default_log_folder):
        os.makedirs(default_log_folder)
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(process)d:%(thread)d - %(filename)s:%(lineno)d - %(message)s',
        handlers=[logging.handlers.TimedRotatingFileHandler(default_log_file_path, when='D')],
        level=level)
    logger.info('Loading PyxelRest: {} Python: {} OS: {} Lib: {}'.format(
        _version.__version__, sys.version, platform.platform(), sysconfig.get_python_lib()))

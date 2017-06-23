import os
import sys
import yaml
import logging.config
import logging.handlers
from pyxelrest import gui


def my_excepthook(excType, excValue, traceback, logger=logging):
    logger.error("Logging an uncaught exception",
                 exc_info=(excType, excValue, traceback))
    gui.message_box("Python Error", str(excValue))


def init_logging():
    logging_configuration_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'logging.ini')
    if os.path.isfile(logging_configuration_file_path):
        with open(logging_configuration_file_path, 'r') as config_file:
            log_config_dict = yaml.load(config_file)
            logging.config.dictConfig(log_config_dict)
    else:
        default_log_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'logs', 'pyxelrest.log')
        logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
                            handlers=[logging.handlers.TimedRotatingFileHandler(default_log_file_path, when='D')],
                            level=logging.INFO)
        logging.warning('Logging configuration file ({0}) cannot be found. Using default logging configuration.'.format(
            logging_configuration_file_path))
    sys.excepthook = my_excepthook

init_logging()

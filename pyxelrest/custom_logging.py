import os
import sys
import logging.config
import logging.handlers

from pyxelrest import _version
from distutils import sysconfig


def my_excepthook(excType, excValue, traceback, logger=logging):
    from pyxelrest import alert
    logger.error("Logging an uncaught exception",
                 exc_info=(excType, excValue, traceback))
    alert.message_box("Python Error", str(excValue))

sys.excepthook = my_excepthook


def load_logging_configuration():
    """
    Load YAML logging configuration from %APPDATA%\pyxelrest\configuration\logging.ini
    If file is not found, then logging will be performed as INFO into %APPDATA%\pyxelrest\logs\pyxelrest.log
    and file will be rolled every day.
    :return: None
    """
    if len(logging.root.handlers) == 0:
        logging_configuration_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'logging.ini')
        if os.path.isfile(logging_configuration_file_path):
            # Only consider YAML as mandatory  in case a specific user logging configuration is provided.
            import yaml
            with open(logging_configuration_file_path, 'r') as config_file:
                 log_config_dict = yaml.load(config_file)
                 logging.config.dictConfig(log_config_dict)
        else:
            default_log_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'logs', 'pyxelrest.log')
            logging.basicConfig(format='%(asctime)s - %(levelname)s - %(process)d:%(thread)d - %(filename)s:%(lineno)d - %(message)s',
                                handlers=[logging.handlers.TimedRotatingFileHandler(default_log_file_path, when='D')],
                                level=logging.INFO)
            logging.warning('Logging configuration file ({0}) cannot be found. Using default logging configuration.'.format(
                logging_configuration_file_path))
        logging.info('Loading PyxelRest version {}'.format(_version.__version__))
        logging.info('Using Python lib at {}'.format(sysconfig.get_python_lib()))


def set_pid_file_logger(level=logging.INFO):
    if len(logging.root.handlers) == 0:
        default_log_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'logs', 'pyxelrest-' + str(os.getpid())                                        + '.log')
        logging.basicConfig(
            format='%(asctime)s - %(levelname)s - %(process)d:%(thread)d - %(filename)s:%(lineno)d - %(message)s',
            handlers=[logging.handlers.TimedRotatingFileHandler(default_log_file_path, when='D')],
            level=level)
        logging.info('Loading PyxelRest version {}'.format(_version.__version__))
        logging.info('Using Python lib at {}'.format(sysconfig.get_python_lib()))


def set_syslog_logger(host, port, level):
    handler = logging.handlers.SysLogHandler(address=(host, port))
    formatter = logging.Formatter('%(levelname)s - %(process)d:%(thread)d - %(filename)s:%(lineno)d - %(message)s')
    handler.setFormatter(formatter)
    handler.setLevel(level)
    logging.getLogger().addHandler(handler)


class StreamToLogger(object):
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """

    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    def flush(self):
        pass

import os
import sys
import logging.config
import logging.handlers


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
    logging_configuration_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'logging.ini')
    if os.path.isfile(logging_configuration_file_path):
        # Only consider YAML as mandatory in case a specific user logging configuration is provided.
        import yaml
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


def set_pid_file_logger():
    default_log_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'logs', 'pyxelrest-' + str(os.getpid())
                                         + '.log')
    logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
                        handlers=[logging.handlers.TimedRotatingFileHandler(default_log_file_path, when='D')],
                        level=logging.INFO)


def set_syslog_logger(host, port):
    logging.basicConfig(format='[%(levelname)s] - %(message)s',
                        handlers=[logging.handlers.SysLogHandler(host, port)],
                        level=logging.INFO)

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

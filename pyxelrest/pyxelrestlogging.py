import os
import logging
import logging.config
import logging.handlers
import yaml


logging_configuration_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'logging_configuration.ini')
if os.path.isfile(logging_configuration_file_path):
    with open(logging_configuration_file_path, 'r') as config_file:
        log_config_dict=yaml.load(config_file)
        logging.config.dictConfig(log_config_dict)
else:
    logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
                                 handlers=[logging.handlers.TimedRotatingFileHandler(os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'pyxelrest.log'), when='D')],
                                 level=logging.INFO)
    logging.warning('Logging configuration file ({0}) cannot be found. Using default logging configuration.'.format(logging_configuration_file_path))

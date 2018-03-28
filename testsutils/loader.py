from importlib import import_module
try:
    # Python 3
    from importlib import reload
except ImportError:
    # Python 2
    from imp import reload
import os
import pyxelrest


def load(new_configuration_file_name, remove_logging_config=False):
    if new_configuration_file_name:
        this_dir = os.path.abspath(os.path.dirname(__file__))
        pyxelrest.SERVICES_CONFIGURATION_FILE_PATH = os.path.join(this_dir, new_configuration_file_name)
    else:
        pyxelrest.SERVICES_CONFIGURATION_FILE_PATH = 'non_existing_configuration.ini'

    if remove_logging_config:
        pyxelrest.LOGGING_CONFIGURATION_FILE_PATH = 'non_existing_configuration.ini'

    reload(import_module('pyxelrest.pyxelrestgenerator'))

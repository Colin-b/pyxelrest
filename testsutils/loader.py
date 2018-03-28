from importlib import import_module
try:
    # Python 3
    from importlib import reload
except ImportError:
    # Python 2
    from imp import reload
import os
import pyxelrest


def load(new_configuration_file_name, logging_configuration_file_name=None):
    this_dir = os.path.abspath(os.path.dirname(__file__))
    pyxelrest.SERVICES_CONFIGURATION_FILE_PATH = os.path.join(this_dir, new_configuration_file_name)

    if logging_configuration_file_name:
        pyxelrest.LOGGING_CONFIGURATION_FILE_PATH = os.path.join(this_dir, logging_configuration_file_name)

    reload(import_module('pyxelrest.pyxelrestgenerator'))

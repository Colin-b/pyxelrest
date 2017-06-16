from importlib import import_module
try:
    # Python 3
    from importlib import reload
except ImportError:
    # Python 2
    from imp import reload
import testsutils.confighandler as confighandler


def load(new_configuration_file_name, remove_logging_config=False):
    confighandler.set_new_configuration(new_configuration_file_name, remove_logging_config)
    try:
        reload(import_module('pyxelrestgenerator'))
    except:
        confighandler.set_initial_configuration()
        raise


def unload():
    confighandler.set_initial_configuration()
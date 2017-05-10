import unittest
from importlib import import_module
import testsutils.confighandler as confighandler


try:
    # Python 3
    from importlib import reload
except ImportError:
    # Python 2
    from imp import reload


class PyxelRestNoServicesConfigurationTest(unittest.TestCase):
    def tearDown(self):
        confighandler.set_initial_configuration()

    def test_without_service_configuration_file(self):
        confighandler.set_new_configuration(None)
        try:
            reload(import_module('pyxelrestgenerator'))
            import pyxelrestgenerator
            self.fail('Loading should be forbidden without a configuration file.')
        except Exception as e:
            self.assertEqual(str(e), '"'+confighandler.services_config_file_path+'" configuration file cannot be read.')

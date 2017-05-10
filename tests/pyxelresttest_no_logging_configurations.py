import unittest
from importlib import import_module
import testsutils.confighandler as confighandler
import testsutils.serviceshandler as serviceshandler


try:
    # Python 3
    from importlib import reload
except ImportError:
    # Python 2
    from imp import reload


class PyxelRestNoLoggingConfigurationTest(unittest.TestCase):
    def setUp(self):
        import testsutils.usual_parameters_test_service as usual_parameters_test_service
        serviceshandler.start_services((usual_parameters_test_service, 8943))
        confighandler.set_new_configuration('pyxelresttest_no_logging_services_configuration.ini',
                                            remove_logging_config=True)

    def tearDown(self):
        serviceshandler.stop_services()
        confighandler.set_initial_configuration()

    def test_without_logging_configuration_file(self):
        """
        This test case assert that pyxelrest can be loaded without logging configuration
        """
        reload(import_module('pyxelrestgenerator'))
        self.assertTrue(True)

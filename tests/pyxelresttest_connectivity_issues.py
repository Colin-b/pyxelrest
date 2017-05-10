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


class PyxelRestConnectivityIssuesTest(unittest.TestCase):
    def setUp(self):
        confighandler.set_new_configuration('pyxelresttest_connectivity_issues_services_configuration.ini')

    def tearDown(self):
        confighandler.set_initial_configuration()

    def test_get_test_plain_text_with_service_down(self):
        import testsutils.without_parameter_test_service as without_parameter_test_service
        serviceshandler.start_services((without_parameter_test_service, 8950))
        reload(import_module('pyxelrestgenerator'))
        import pyxelrestgenerator
        serviceshandler.stop_services()
        self.assertEqual(pyxelrestgenerator.without_parameter_test_get_test_plain_text_without_parameter(),
                         'Cannot connect to service. Please retry once connection is re-established.')

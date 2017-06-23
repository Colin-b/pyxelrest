import unittest
import testsutils.serviceshandler as serviceshandler
import testsutils.loader as loader


class PyxelRestConnectivityIssuesTest(unittest.TestCase):
    def setUp(self):
        from testsutils import without_parameter_test_service
        serviceshandler.start_services((without_parameter_test_service, 8950))
        loader.load('pyxelresttest_connectivity_issues_services_configuration.ini')

    def tearDown(self):
        loader.unload()

    def test_get_test_plain_text_with_service_down(self):
        import pyxelrestgenerator
        serviceshandler.stop_services()
        self.assertEqual(pyxelrestgenerator.without_parameter_test_get_test_plain_text_without_parameter(),
                         'Cannot connect to service. Please retry once connection is re-established.')

if __name__ == '__main__':
    unittest.main()

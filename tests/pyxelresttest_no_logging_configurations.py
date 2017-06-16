import unittest
import testsutils.serviceshandler as serviceshandler
import testsutils.loader as loader


class PyxelRestNoLoggingConfigurationTest(unittest.TestCase):
    def setUp(self):
        import testsutils.usual_parameters_test_service as usual_parameters_test_service
        serviceshandler.start_services((usual_parameters_test_service, 8943))
        loader.load('pyxelresttest_no_logging_services_configuration.ini', remove_logging_config=True)

    def tearDown(self):
        loader.unload()
        serviceshandler.stop_services()

    def test_without_logging_configuration_file(self):
        """
        This test case assert that pyxelrest can be loaded without logging configuration
        """
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

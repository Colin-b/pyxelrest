import unittest
import testsutils.serviceshandler as serviceshandler
import testsutils.loader as loader


class PyxelRestNoLoggingConfigurationTest(unittest.TestCase):
    def setUp(self):
        from testsutils import usual_parameters_service
        serviceshandler.start_services((usual_parameters_service, 8943))
        loader.load('pyxelresttest_no_logging_services_configuration.ini', remove_logging_config=True)

    def tearDown(self):
        serviceshandler.stop_services()

    def test_without_logging_configuration_file(self):
        """
        This test case assert that pyxelrest can be loaded without logging configuration
        """
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

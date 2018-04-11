import unittest

from testsutils import (serviceshandler, loader)


class PyxelRestNoLoggingConfigurationTest(unittest.TestCase):
    def setUp(self):
        from testsutils import usual_parameters_service
        serviceshandler.start_services((usual_parameters_service, 8943))

    def tearDown(self):
        serviceshandler.stop_services()

    def test_without_logging_configuration_file(self):
        """
        This test case assert that pyxelrest can be loaded without logging configuration
        """
        loader.load('no_logging_services.yml', 'non_existing_configuration.yml')


if __name__ == '__main__':
    unittest.main()

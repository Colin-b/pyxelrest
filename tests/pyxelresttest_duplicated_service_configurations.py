import datetime
import unittest

from testsutils import (serviceshandler, loader)


class PyxelRestDuplicatedServiceConfigurationTest(unittest.TestCase):
    def setUp(self):
        from testsutils import usual_parameters_service
        serviceshandler.start_services((usual_parameters_service, 8943))

    def tearDown(self):
        serviceshandler.stop_services()

    def test_without_service_configuration_file(self):
        loader.load('duplicated_service.yml')
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                [datetime.datetime(2014, 3, 5, 0, 0)],
                [datetime.datetime(9999, 1, 1, 0, 0)],
                [datetime.datetime(3001, 1, 1, 0, 0)],
            ],
            pyxelrestgenerator.usual_parameters_get_date()
        )


if __name__ == '__main__':
    unittest.main()

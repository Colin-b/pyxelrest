import unittest

from testsutils import (serviceshandler, loader)


class PyxelRestConnectivityIssuesTest(unittest.TestCase):
    def setUp(self):
        from testsutils import without_parameter_service
        serviceshandler.start_services((without_parameter_service, 8950))
        loader.load('connectivity_issues_services.yml')

    def test_get_plain_text_with_service_down(self):
        from pyxelrest import pyxelrestgenerator
        serviceshandler.stop_services()
        self.assertEqual(pyxelrestgenerator.without_parameter_get_plain_text_without_parameter(),
                         'Cannot connect to service. Please retry once connection is re-established.')


if __name__ == '__main__':
    unittest.main()

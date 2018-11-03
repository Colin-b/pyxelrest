import timeit
import unittest

from testsutils import (serviceshandler, loader)


class PyxelRestOpenAPIDefinitionNotAvailableTest(unittest.TestCase):
    def setUp(self):
        from testsutils import open_api_definition_not_responding_service
        serviceshandler.start_services((open_api_definition_not_responding_service, 8950))
        loader.load('open_api_definition_not_available.yml')

    def tearDown(self):
        serviceshandler.stop_services()

    def test_service_can_be_loaded_without_hitting_timeout(self):
        nb_seconds = timeit.timeit('from pyxelrest import pyxelrestgenerator', number=1) * 1e6
        self.assertLess(nb_seconds, 8, 'Time to load pyxelrest should be around timeout.')


if __name__ == '__main__':
    unittest.main()

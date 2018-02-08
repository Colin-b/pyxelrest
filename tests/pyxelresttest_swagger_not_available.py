import unittest
import testsutils.serviceshandler as serviceshandler
import testsutils.loader as loader
import timeit


class PyxelRestSwaggerNotAvailableTest(unittest.TestCase):
    def setUp(self):
        from testsutils import swagger_not_responding_test_service
        serviceshandler.start_services((swagger_not_responding_test_service, 8950))
        loader.load('pyxelresttest_swagger_not_available_configuration.ini')

    def tearDown(self):
        loader.unload()
        serviceshandler.stop_services()

    def test_service_can_be_loaded_without_hitting_timeout(self):
        nb_seconds = timeit.timeit('from pyxelrest import pyxelrestgenerator', number=1) * 1e6
        self.assertTrue(nb_seconds < 8, 'Time to load pyxelrest should be around timeout.')


if __name__ == '__main__':
    unittest.main()

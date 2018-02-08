import unittest
import testsutils.loader as loader


class PyxelRestNoServicesConfigurationTest(unittest.TestCase):
    def tearDown(self):
        loader.unload()

    def test_without_service_configuration_file(self):
        try:
            loader.load(None)
            from pyxelrest import pyxelrestgenerator
            self.fail('Loading should be forbidden without a configuration file.')
        except Exception as e:
            self.assertEqual(str(e), '"{0}" configuration file cannot be read.'.format(
                loader.confighandler.services_config_file_path))


if __name__ == '__main__':
    unittest.main()

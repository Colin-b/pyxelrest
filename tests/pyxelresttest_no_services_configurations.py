import unittest

from testsutils import loader
import pyxelrest


class PyxelRestNoServicesConfigurationTest(unittest.TestCase):
    def test_without_service_configuration_file(self):
        with self.assertRaises(Exception) as cm:
            loader.load('non_existing.yml')
        self.assertEqual(
            cm.exception.args[0],
            f'"{pyxelrest.SERVICES_CONFIGURATION_FILE_PATH}" configuration file cannot be read.')


if __name__ == '__main__':
    unittest.main()

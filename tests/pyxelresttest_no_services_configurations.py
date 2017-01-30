import unittest
import os
import shutil
from importlib import import_module


try:
    # Python 3
    from importlib import reload
except ImportError:
    # Python 2
    from imp import reload


class PyxelRestNoServicesConfigurationTest(unittest.TestCase):
    def tearDown(self):
        self._add_back_initial_config()

    def test_without_service_configuration_file(self):
        self._remove_services_config()
        try:
            reload(import_module('pyxelrestgenerator'))
            import pyxelrestgenerator
            self.fail('Loading should be forbidden without a configuration file.')
        except Exception as e:
            config_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'services_configuration.ini')
            self.assertEqual(str(e), '"'+config_file_path+'" configuration file cannot be read.')

    def _remove_services_config(self):
        config_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'services_configuration.ini')
        self.backup_services_config_file_path = os.path.join(os.getenv('APPDATA'),
                                                    'pyxelrest',
                                                    'services_configuration.ini.back')
        shutil.move(config_file_path, self.backup_services_config_file_path)

    def _add_back_initial_config(self):
        config_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'services_configuration.ini')
        if os.path.isfile(self.backup_services_config_file_path):
            shutil.move(self.backup_services_config_file_path, config_file_path)

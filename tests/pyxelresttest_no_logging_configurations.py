import unittest
import os
import shutil
import datetime


# Test cases requires test_service to run prior to execution
class PyxelRestNoLoggingConfigurationTest(unittest.TestCase):
    def tearDown(self):
        self._add_back_initial_config()

    def test_without_logging_configuration_file(self):
        self._remove_logging_config()
        self._add_services_config()
        import pyxelrestgenerator
        # This test case assert that pyxelrest can be loaded without logging configuration

    def _remove_logging_config(self):
        config_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'logging_configuration.ini')
        self.backup_logging_config_file_path = os.path.join(os.getenv('APPDATA'),
                                                    'pyxelrest',
                                                    'logging_configuration.ini.back')
        shutil.move(config_file_path, self.backup_logging_config_file_path)

    def _add_services_config(self):
        config_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'services_configuration.ini')
        self.backup_services_config_file_path = os.path.join(os.getenv('APPDATA'),
                                                    'pyxelrest',
                                                    'services_configuration.ini.back')
        shutil.copyfile(config_file_path, self.backup_services_config_file_path)
        shutil.copyfile('test_services_configuration.ini', config_file_path)

    def _add_back_initial_config(self):
        config_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'services_configuration.ini')
        shutil.move(self.backup_services_config_file_path, config_file_path)
        config_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'logging_configuration.ini')
        shutil.move(self.backup_logging_config_file_path, config_file_path)

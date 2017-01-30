import multiprocessing
import os
import shutil
import unittest
from importlib import import_module


try:
    # Python 3
    from importlib import reload
except ImportError:
    # Python 2
    from imp import reload


class PyxelRestNoLoggingConfigurationTest(unittest.TestCase):
    def setUp(self):
        self.start_services()
        self._remove_logging_config()
        self._add_services_config()

    def tearDown(self):
        self.stop_services()
        self._add_back_initial_config()

    def start_services(self):
        from testsutils.test_service import start_server
        self.service_process = multiprocessing.Process(target=start_server, args=(8943,))
        self.service_process.start()

    def stop_services(self):
        self.service_process.terminate()
        self.service_process.join(timeout=0.5)

    def _remove_logging_config(self):
        self.logging_config_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'logging_configuration.ini')
        if os.path.isfile(self.logging_config_file_path):
            self.backup_logging_config_file_path = os.path.join(os.getenv('APPDATA'),
                                                                'pyxelrest',
                                                                'logging_configuration.ini.back')
            shutil.move(self.logging_config_file_path, self.backup_logging_config_file_path)

    def _add_services_config(self):
        self.services_config_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'services_configuration.ini')
        self.backup_services_config_file_path = os.path.join(os.getenv('APPDATA'),
                                                             'pyxelrest',
                                                             'services_configuration.ini.back')
        shutil.copyfile(self.services_config_file_path, self.backup_services_config_file_path)
        shutil.copyfile('test_services_configuration.ini', self.services_config_file_path)

    def _add_back_initial_config(self):
        shutil.move(self.backup_services_config_file_path, self.services_config_file_path)
        if hasattr(self, 'backup_logging_config_file_path') and os.path.isfile(self.backup_logging_config_file_path):
            shutil.move(self.backup_logging_config_file_path, self.logging_config_file_path)
        # TODO else remove it

    def test_without_logging_configuration_file(self):
        """
        This test case assert that pyxelrest can be loaded without logging configuration
        """
        reload(import_module('pyxelrestgenerator'))
        self.assertTrue(True)

import unittest
import os
import shutil
import datetime
import multiprocessing


class PyxelRestConnectivityIssuesTest(unittest.TestCase):
    services_config_file_path = os.path.join(os.getenv('APPDATA'),
                                             'pyxelrest',
                                             'services_configuration.ini')
    backup_services_config_file_path = os.path.join(os.getenv('APPDATA'),
                                                    'pyxelrest',
                                                    'services_configuration.ini.back')

    def setUp(self):
        self._add_test_config()

    def tearDown(self):
        self._add_back_initial_config()

    def start_services(self):
        from tests.test_service import start_server
        self.service_process = multiprocessing.Process(target=start_server, args=(8943,))
        self.service_process.start()

    def stop_services(self):
        self.service_process.terminate()
        self.service_process.join(timeout=0.5)

    def _add_test_config(self):
        shutil.copyfile(self.services_config_file_path, self.backup_services_config_file_path)
        shutil.copyfile('test_services_configuration.ini', self.services_config_file_path)

    def _add_back_initial_config(self):
        shutil.move(self.backup_services_config_file_path, self.services_config_file_path)

    def test_get_test_plain_text_with_service_down(self):
        self.start_services()
        import pyxelrestgenerator
        self.stop_services()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_plain_text_without_parameter(),
                         'Cannot connect to service. Please retry once connection is re-established.')

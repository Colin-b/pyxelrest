import multiprocessing
import os
import os.path
import shutil
import unittest
from importlib import import_module
import time

try:
    # Python 3
    from importlib import reload
except ImportError:
    # Python 2
    from imp import reload


class PyxelRestTest(unittest.TestCase):
    service_processes = []
    services_config_file_path = os.path.join(os.getenv('APPDATA'),
                                             'pyxelrest',
                                             'configuration',
                                             'services.ini')
    backup_services_config_file_path = os.path.join(os.getenv('APPDATA'),
                                                    'pyxelrest',
                                                    'configuration',
                                                    'services.ini.back')

    @classmethod
    def setUpClass(cls):
        cls.start_services()
        cls._add_test_config()
        reload(import_module('pyxelrestgenerator'))

    @classmethod
    def tearDownClass(cls):
        import authentication
        authentication.stop_servers()
        cls.stop_services()
        cls._add_back_initial_config()


    @classmethod
    def start_services(cls):
        import testsutils.test_authenticated_service as test_authenticated_service
        cls.service_processes.append(multiprocessing.Process(target=test_authenticated_service.start_server, args=(8946,)))
        import testsutils.test_authentication_service as test_authentication_service
        cls.service_processes.append(multiprocessing.Process(target=test_authentication_service.start_server, args=(8947,)))
        import testsutils.test_non_authenticated_service as test_non_authenticated_service
        cls.service_processes.append(multiprocessing.Process(target=test_non_authenticated_service.start_server, args=(8948,)))
        for service_process in cls.service_processes:
            service_process.start()
        time.sleep(5)

    @classmethod
    def stop_services(cls):
        for service_process in cls.service_processes:
            service_process.terminate()
            service_process.join(timeout=0.5)
        cls.service_processes[:] = []

    @classmethod
    def _add_test_config(cls):
        this_dir = os.path.abspath(os.path.dirname(__file__))
        shutil.copyfile(cls.services_config_file_path, cls.backup_services_config_file_path)
        shutil.copyfile(os.path.join(this_dir, 'test_services_configuration_authentication.ini'), cls.services_config_file_path)

    @classmethod
    def _add_back_initial_config(cls):
        shutil.move(cls.backup_services_config_file_path, cls.services_config_file_path)

    def test_authentication_token_sent(self):
        import pyxelrestgenerator
        self.assertEqual([
            ['received token'],
            [1]
        ],
            pyxelrestgenerator.auth_test_get_test_with_auth())

    def test_authentication_no_token_sent(self):
        import pyxelrestgenerator
        self.assertEqual([
            ['received token'],
            [0]
        ],
            pyxelrestgenerator.auth_test_no_auth_get_test_without_auth())

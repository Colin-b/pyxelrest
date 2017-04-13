import datetime
import multiprocessing
import os
import os.path
import shutil
import unittest
import platform
from importlib import import_module

try:
    # Python 3
    from importlib import reload
except ImportError:
    # Python 2
    from imp import reload


class PyxelRestNestedDataTest(unittest.TestCase):
    service_process = None
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
        cls.stop_services()
        cls._add_back_initial_config()

    @classmethod
    def start_services(cls):
        import testsutils.nested_data_test_service as nested_data_test_service
        cls.service_process = multiprocessing.Process(target=nested_data_test_service.start_server, args=(8947,))
        cls.service_process.start()

    @classmethod
    def stop_services(cls):
        cls.service_process.terminate()
        cls.service_process.join(timeout=0.5)

    @classmethod
    def _add_test_config(cls):
        this_dir = os.path.abspath(os.path.dirname(__file__))
        shutil.copyfile(cls.services_config_file_path, cls.backup_services_config_file_path)
        shutil.copyfile(os.path.join(this_dir, 'pyxelresttest_nested_data_services_configuration.ini'),
                        cls.services_config_file_path)

    @classmethod
    def _add_back_initial_config(cls):
        shutil.move(cls.backup_services_config_file_path, cls.services_config_file_path)

    def test_get_test_dict_with_empty_nested_list(self):
        import pyxelrestgenerator
        self.maxDiff = None
        self.assertEqual([
            ['Column 1', 'Column 2 / Column 1', 'Column 2 / Column 2 / Column 1', 'Column 2 / Column 2 / Column 3', 'Column 2 / Column 3', 'Column 3'],
            ['0-0-1', '0-0-2 / 1-0-1', '', '', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '0-0-2 / 1-1-1', '0-0-2 / 1-1-2 / 2-0-1', '0-0-2 / 1-1-2 / 2-0-3', '0-0-2 / 1-1-3', '0-0-3'],
            ['0-0-1', '0-0-2 / 1-1-1', '0-0-2 / 1-1-2 / 2-1-1', '0-0-2 / 1-1-2 / 2-1-3', '0-0-2 / 1-1-3', '0-0-3']
        ],
            pyxelrestgenerator.nested_data_test_get_test_dict_with_empty_nested_list())

    def test_get_test_dict_with_three_imbricated_levels(self):
        import pyxelrestgenerator
        self.maxDiff = None
        self.assertEqual([
            ['Column 1', 'Column 2 / Column 1', 'Column 2 / Column 2 / Column 1', 'Column 2 / Column 2 / Column 3', 'Column 2 / Column 3', 'Column 3'],
            ['0-0-1', '0-0-2 / 1-0-1', '0-0-2 / 1-0-2 / 2-0-1', '0-0-2 / 1-0-2 / 2-0-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '0-0-2 / 1-0-1', '0-0-2 / 1-0-2 / 2-1-1', '0-0-2 / 1-0-2 / 2-1-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '0-0-2 / 1-1-1', '0-0-2 / 1-1-2 / 2-0-1', '0-0-2 / 1-1-2 / 2-0-3', '0-0-2 / 1-1-3', '0-0-3'],
            ['0-0-1', '0-0-2 / 1-1-1', '0-0-2 / 1-1-2 / 2-1-1', '0-0-2 / 1-1-2 / 2-1-3', '0-0-2 / 1-1-3', '0-0-3']
        ],
            pyxelrestgenerator.nested_data_test_get_test_dict_with_three_imbricated_levels())

    def test_get_test_dict_with_four_imbricated_levels(self):
        import pyxelrestgenerator
        self.maxDiff = None
        self.assertEqual([
            ['Column 1', 'Column 2 / Column 1', 'Column 2 / Column 2 / Column 1', 'Column 2 / Column 2 / Column 2 / Column 1', 'Column 2 / Column 2 / Column 2 / Column 3', 'Column 2 / Column 2 / Column 3', 'Column 2 / Column 3', 'Column 3'],
            ['0-0-1', '0-0-2 / 1-0-1', '0-0-2 / 1-0-2 / 2-0-1', '0-0-2 / 1-0-2 / 2-0-2 / 3-0-1', '0-0-2 / 1-0-2 / 2-0-2 / 3-0-3', '0-0-2 / 1-0-2 / 2-0-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '0-0-2 / 1-0-1', '0-0-2 / 1-0-2 / 2-0-1', '0-0-2 / 1-0-2 / 2-0-2 / 3-1-1', '0-0-2 / 1-0-2 / 2-0-2 / 3-1-3', '0-0-2 / 1-0-2 / 2-0-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '0-0-2 / 1-0-1', '0-0-2 / 1-0-2 / 2-1-1', '', '', '0-0-2 / 1-0-2 / 2-1-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '0-0-2 / 1-1-1', '0-0-2 / 1-1-2 / 2-0-1', '', '', '0-0-2 / 1-1-2 / 2-0-3', '0-0-2 / 1-1-3', '0-0-3'],
            ['0-0-1', '0-0-2 / 1-1-1', '0-0-2 / 1-1-2 / 2-1-1', '', '', '0-0-2 / 1-1-2 / 2-1-3', '0-0-2 / 1-1-3', '0-0-3']
        ],
            pyxelrestgenerator.nested_data_test_get_test_dict_with_four_imbricated_levels())

    def test_get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys(self):
        import pyxelrestgenerator
        self.maxDiff = None
        self.assertEqual([
            ['Column 1', 'Column 2 / Column 1', 'Column 2 / Column 2 / Column 1', 'Column 2 / Column 2 / Column 2 / Column 1', 'Column 2 / Column 2 / Column 2 / Column 3', 'Column 2 / Column 2 / Column 3', 'Column 2 / Column 3', 'Column 3'],
            ['0-0-1', '0-0-2 / 1-0-1', '0-0-2 / 1-0-2 / 2-0-1', '0-0-2 / 1-0-2 / 2-0-2 / 3-0-1', '0-0-2 / 1-0-2 / 2-0-2 / 3-0-3', '0-0-2 / 1-0-2 / 2-0-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '0-0-2 / 1-0-1', '0-0-2 / 1-0-2 / 2-0-1', '0-0-2 / 1-0-2 / 2-0-2 / 3-1-1', '0-0-2 / 1-0-2 / 2-0-2 / 3-1-3', '0-0-2 / 1-0-2 / 2-0-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '0-0-2 / 1-0-1', '0-0-2 / 1-0-2 / 2-1-1', '', '', '0-0-2 / 1-0-2 / 2-1-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '0-0-2 / 1-1-1', '0-0-2 / 1-1-2 / 2-0-1', '', '', '0-0-2 / 1-1-2 / 2-0-3', '0-0-2 / 1-1-3', '0-0-3'],
            ['0-0-1', '0-0-2 / 1-1-1', '0-0-2 / 1-1-2 / 2-1-1', '', '', '0-0-2 / 1-1-2 / 2-1-3', '0-0-2 / 1-1-3', '0-0-3']
        ],
            pyxelrestgenerator.nested_data_test_get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys())

    def test_get_test_empty_dict(self):
        import pyxelrestgenerator
        self.assertEqual([''],
                         pyxelrestgenerator.nested_data_test_get_test_empty_dict())

    def test_get_test_empty_list(self):
        import pyxelrestgenerator
        self.assertEqual([''],
                         pyxelrestgenerator.nested_data_test_get_test_empty_list())

    def test_get_test_one_level_dict(self):
        import pyxelrestgenerator
        self.assertEqual([
            ['Column 1', 'Column 2'],
            ['value 1', 'value 2']
        ],
            pyxelrestgenerator.nested_data_test_get_test_one_level_dict())

    def test_get_test_one_level_list(self):
        import pyxelrestgenerator
        self.assertEqual([
            ['value 1'],
            ['value 2']
        ],
            pyxelrestgenerator.nested_data_test_get_test_one_level_list())

    def test_get_test_one_dict_entry_with_a_list(self):
        import pyxelrestgenerator
        self.assertEqual([
            ['Column 1', 'Column 1'],
            ['', 'value 1'],
            ['', 'value 2']
        ],
            pyxelrestgenerator.nested_data_test_get_test_one_dict_entry_with_a_list())

    def test_get_test_one_dict_entry_with_a_list_of_dict(self):
        import pyxelrestgenerator
        self.assertEqual([
            ['Column 1', 'Column 2', 'Column 3'],
            ['', 'value 12', 'value 13'],
            ['', 'value 22', 'value 23']
        ],
            pyxelrestgenerator.nested_data_test_get_test_one_dict_entry_with_a_list_of_dict())

    def test_get_test_list_of_dict(self):
        import pyxelrestgenerator
        self.assertEqual([
            ['Column 1', 'Column 2'],
            ['value 11', 'value 12'],
            ['value 21', 'value 22']
        ],
            pyxelrestgenerator.nested_data_test_get_test_list_of_dict())

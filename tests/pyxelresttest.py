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
        cls.stop_services()
        cls._add_back_initial_config()

    @classmethod
    def start_services(cls):
        import testsutils.filtered_tags_test_service as filtered_tags_test_service
        cls.service_processes.append(
            multiprocessing.Process(target=filtered_tags_test_service.start_server, args=(8944,)))
        import testsutils.values_false_test_service as values_false_test_service
        cls.service_processes.append(
            multiprocessing.Process(target=values_false_test_service.start_server, args=(8945,)))
        import testsutils.output_order_test_service as output_order_test_service
        cls.service_processes.append(
            multiprocessing.Process(target=output_order_test_service.start_server, args=(8946,)))
        import testsutils.nested_data_test_service as nested_data_test_service
        cls.service_processes.append(
            multiprocessing.Process(target=nested_data_test_service.start_server, args=(8947,)))
        import testsutils.swagger_parsing_test_service as swagger_parsing_test_service
        cls.service_processes.append(
            multiprocessing.Process(target=swagger_parsing_test_service.start_server, args=(8948,)))
        import testsutils.vba_keywords_test_service as vba_keywords_test_service
        cls.service_processes.append(
            multiprocessing.Process(target=vba_keywords_test_service.start_server, args=(8949,)))
        import testsutils.without_parameter_test_service as without_parameter_test_service
        cls.service_processes.append(
            multiprocessing.Process(target=without_parameter_test_service.start_server, args=(8950,)))
        import testsutils.header_parameter_test_service as header_parameter_test_service
        cls.service_processes.append(
            multiprocessing.Process(target=header_parameter_test_service.start_server, args=(8951,)))
        import testsutils.form_parameter_test_service as form_parameter_test_service
        cls.service_processes.append(
            multiprocessing.Process(target=form_parameter_test_service.start_server, args=(8952,)))
        import testsutils.array_parameter_test_service as array_parameter_test_service
        cls.service_processes.append(
            multiprocessing.Process(target=array_parameter_test_service.start_server, args=(8953,)))
        for service_process in cls.service_processes:
            service_process.start()

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
        shutil.copyfile(os.path.join(this_dir, 'test_services_configuration.ini'), cls.services_config_file_path)

    @classmethod
    def _add_back_initial_config(cls):
        shutil.move(cls.backup_services_config_file_path, cls.services_config_file_path)

    def test_vba_restricted_keywords(self):
        import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.vba_keywords_test_get_test_vba_restricted_keywords(
                currency_visual_basic='currency value',
                end_visual_basic='end value'),
            [['currency', 'end'], ['currency value', 'end value']])

    def test_string_array_parameter(self):
        import pyxelrestgenerator
        if platform.python_version()[0] == '3':
            result = 'query_array_string="[\'str1\', \'str2\']"'
        else:
            result = u'query_array_string="[u\'str1\', u\'str2\']"'
        self.assertEqual(pyxelrestgenerator.array_parameter_test_get_test_string_array_parameter(['str1', 'str2']),
                         result)

    def test_plain_text_without_parameter(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.without_parameter_test_get_test_plain_text_without_parameter(),
                         'string value returned should be truncated so that the following information cannot be seen by'
                         ' user, because of the fact that Excel does not allow more than 255 characters in a cell. '
                         'Only the 255 characters will be returned by the user defined functions:  ')

    def test_post_test_without_parameter(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.without_parameter_test_post_test_without_parameter(),
                         'POST performed properly')

    def test_put_test_without_parameter(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.without_parameter_test_put_test_without_parameter(),
                         'PUT performed properly')

    def test_delete_test_without_parameter(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.without_parameter_test_delete_test_without_parameter(),
                         'DELETE performed properly')

    def test_get_test_header_parameter(self):
        import pyxelrestgenerator
        headers = pyxelrestgenerator.header_parameter_test_get_test_header_parameter('sent header')
        header_param_index = None
        for header_index in range(0, len(headers[0])):
            if headers[0][header_index] == 'Header-String':
                header_param_index = header_index
                break
        self.assertEqual(headers[1][header_param_index], 'sent header')

    def test_post_test_form_parameter(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.form_parameter_test_post_test_form_parameter('sent string form data'), [
            ['form_string'],
            ['sent string form data']
        ])

    def test_get_test_dict_with_empty_nested_list(self):
        import pyxelrestgenerator
        self.maxDiff = None
        self.assertEqual([
            ['Column 1', 'Column 2', 'Column 2.1', 'Column 2.2', 'Column 3.1', 'Column 3.2', 'Column 3.3', 'Column 2.3',
             'Column 3'],
            ['0-0-1', '', '0-0-2 / 1-0-1', '', '', '', '', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-1-1', '', '0-0-2 / 1-1-2 / 2-0-1', '', '0-0-2 / 1-1-2 / 2-0-3', '0-0-2 / 1-1-3',
             '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-1-1', '', '0-0-2 / 1-1-2 / 2-1-1', '', '0-0-2 / 1-1-2 / 2-1-3', '0-0-2 / 1-1-3',
             '0-0-3']
        ],
            pyxelrestgenerator.nested_data_test_get_test_dict_with_empty_nested_list())

    def test_get_test_dict_with_three_imbricated_levels(self):
        import pyxelrestgenerator
        self.maxDiff = None
        self.assertEqual([
            ['Column 1', 'Column 2', 'Column 2.1', 'Column 2.2', 'Column 3.1', 'Column 3.2', 'Column 3.3', 'Column 2.3',
             'Column 3'],
            ['0-0-1', '', '0-0-2 / 1-0-1', '', '0-0-2 / 1-0-2 / 2-0-1', '', '0-0-2 / 1-0-2 / 2-0-3', '0-0-2 / 1-0-3',
             '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-0-1', '', '0-0-2 / 1-0-2 / 2-1-1', '', '0-0-2 / 1-0-2 / 2-1-3', '0-0-2 / 1-0-3',
             '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-1-1', '', '0-0-2 / 1-1-2 / 2-0-1', '', '0-0-2 / 1-1-2 / 2-0-3', '0-0-2 / 1-1-3',
             '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-1-1', '', '0-0-2 / 1-1-2 / 2-1-1', '', '0-0-2 / 1-1-2 / 2-1-3', '0-0-2 / 1-1-3',
             '0-0-3']
        ],
            pyxelrestgenerator.nested_data_test_get_test_dict_with_three_imbricated_levels())

    def test_get_test_dict_with_four_imbricated_levels(self):
        import pyxelrestgenerator
        self.maxDiff = None
        self.assertEqual([
            ['Column 1', 'Column 2', 'Column 2.1', 'Column 2.2', 'Column 3.1', 'Column 3.2', 'Column 4.1', 'Column 4.2',
             'Column 4.3', 'Column 3.3', 'Column 2.3', 'Column 3'],
            ['0-0-1', '', '0-0-2 / 1-0-1', '', '0-0-2 / 1-0-2 / 2-0-1', '', '0-0-2 / 1-0-2 / 2-0-2 / 3-0-1', '',
             '0-0-2 / 1-0-2 / 2-0-2 / 3-0-3', '0-0-2 / 1-0-2 / 2-0-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-0-1', '', '0-0-2 / 1-0-2 / 2-0-1', '', '0-0-2 / 1-0-2 / 2-0-2 / 3-1-1', '',
             '0-0-2 / 1-0-2 / 2-0-2 / 3-1-3', '0-0-2 / 1-0-2 / 2-0-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-0-1', '', '0-0-2 / 1-0-2 / 2-1-1', '', '', '', '', '0-0-2 / 1-0-2 / 2-1-3',
             '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-1-1', '', '0-0-2 / 1-1-2 / 2-0-1', '', '', '', '', '0-0-2 / 1-1-2 / 2-0-3',
             '0-0-2 / 1-1-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-1-1', '', '0-0-2 / 1-1-2 / 2-1-1', '', '', '', '', '0-0-2 / 1-1-2 / 2-1-3',
             '0-0-2 / 1-1-3', '0-0-3']
        ],
            pyxelrestgenerator.nested_data_test_get_test_dict_with_four_imbricated_levels())

    def test_get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys(self):
        import pyxelrestgenerator
        self.maxDiff = None
        self.assertEqual([
            ['Column 1', 'Column 2', 'Column 1', 'Column 2', 'Column 1', 'Column 2', 'Column 1', 'Column 2', 'Column 3',
             'Column 3', 'Column 3', 'Column 3'],
            ['0-0-1', '', '0-0-2 / 1-0-1', '', '0-0-2 / 1-0-2 / 2-0-1', '', '0-0-2 / 1-0-2 / 2-0-2 / 3-0-1', '',
             '0-0-2 / 1-0-2 / 2-0-2 / 3-0-3', '0-0-2 / 1-0-2 / 2-0-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-0-1', '', '0-0-2 / 1-0-2 / 2-0-1', '', '0-0-2 / 1-0-2 / 2-0-2 / 3-1-1', '',
             '0-0-2 / 1-0-2 / 2-0-2 / 3-1-3', '0-0-2 / 1-0-2 / 2-0-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-0-1', '', '0-0-2 / 1-0-2 / 2-1-1', '', '', '', '', '0-0-2 / 1-0-2 / 2-1-3',
             '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-1-1', '', '0-0-2 / 1-1-2 / 2-0-1', '', '', '', '', '0-0-2 / 1-1-2 / 2-0-3',
             '0-0-2 / 1-1-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-1-1', '', '0-0-2 / 1-1-2 / 2-1-1', '', '', '', '', '0-0-2 / 1-1-2 / 2-1-3',
             '0-0-2 / 1-1-3', '0-0-3']
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

    def test_get_test_with_tags(self):
        import pyxelrestgenerator
        self.assertEqual('Second tag is one of the accepted tags',
                         pyxelrestgenerator.filtered_tags_test_get_test_with_tags())

    def test_post_test_with_tags(self):
        import pyxelrestgenerator
        self.assertEqual('All tags are accepted',
                         pyxelrestgenerator.filtered_tags_test_post_test_with_tags())

    def test_put_test_with_tags(self):
        import pyxelrestgenerator
        self.assertEqual('First tag is one of the accepted tags',
                         pyxelrestgenerator.filtered_tags_test_put_test_with_tags())

    def test_delete_test_with_tags(self):
        import pyxelrestgenerator
        self.assertFalse(hasattr(pyxelrestgenerator, 'filtered_tags_test_delete_test_with_tags'))

    def test_get_test_with_zero_integer(self):
        import pyxelrestgenerator
        self.assertEqual([
            ['zero_integer'],
            [0]
        ],
            pyxelrestgenerator.values_false_test_get_test_with_zero_integer())

    def test_get_test_with_zero_float(self):
        import pyxelrestgenerator
        self.assertEqual([
            ['zero_float'],
            [0.0]
        ],
            pyxelrestgenerator.values_false_test_get_test_with_zero_float())

    def test_get_test_with_false_boolean(self):
        import pyxelrestgenerator
        self.assertEqual([
            ['false_boolean'],
            [False]
        ],
            pyxelrestgenerator.values_false_test_get_test_with_false_boolean())

    def test_get_test_with_empty_string(self):
        import pyxelrestgenerator
        self.assertEqual([
            ['empty_string'],
            ['']
        ],
            pyxelrestgenerator.values_false_test_get_test_with_empty_string())

    def test_get_test_with_empty_list(self):
        import pyxelrestgenerator
        self.assertEqual([
            ['empty_list'],
            ['']
        ],
            pyxelrestgenerator.values_false_test_get_test_with_empty_list())

    def test_get_test_with_empty_dictionary(self):
        import pyxelrestgenerator
        self.assertEqual([
            ['empty_dictionary'],
            ['']
        ],
            pyxelrestgenerator.values_false_test_get_test_with_empty_dictionary())

    def test_get_test_compare_output_order(self):
        import pyxelrestgenerator
        result_unordered = pyxelrestgenerator.output_order_test_get_test_price_unordered()
        header_definition = [u'ts', u'date', u'curve', u'mat']
        self.assertEqual(result_unordered[0], header_definition)

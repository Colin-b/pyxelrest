import datetime
import multiprocessing
import os
import os.path
import shutil
import unittest
from importlib import import_module


try:
    # Python 3
    from importlib import reload
except ImportError:
    # Python 2
    from imp import reload


class PyxelRestTest(unittest.TestCase):
    service_process = None
    services_config_file_path = os.path.join(os.getenv('APPDATA'),
                                             'pyxelrest',
                                             'services_configuration.ini')
    backup_services_config_file_path = os.path.join(os.getenv('APPDATA'),
                                                    'pyxelrest',
                                                    'services_configuration.ini.back')

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
        from testsutils.test_service import start_server
        cls.service_process = multiprocessing.Process(target=start_server, args=(8943,))
        cls.service_process.start()

    @classmethod
    def stop_services(cls):
        cls.service_process.terminate()
        cls.service_process.join(timeout=0.5)

    @classmethod
    def _add_test_config(cls):
        this_dir = os.path.abspath(os.path.dirname(__file__))
        shutil.copyfile(cls.services_config_file_path, cls.backup_services_config_file_path)
        shutil.copyfile(os.path.join(this_dir, 'test_services_configuration.ini'), cls.services_config_file_path)

    @classmethod
    def _add_back_initial_config(cls):
        shutil.move(cls.backup_services_config_file_path, cls.services_config_file_path)

    def test_generated_file(self):
        """
        Assert content of generated file.
        This test is mainly here to be aware that a change broke generated file.
        """
        expected_file = open(os.path.join(os.path.dirname(__file__),
                                          '..',
                                          'testsutils',
                                          'test_service_user_defined_functions.py'), 'r')
        expected = expected_file.readlines()
        expected_file.close()
        actual_file = open(os.path.join(os.path.dirname(__file__),
                                        r'..\pyxelrest\user_defined_functions.py'), 'r')
        actual = actual_file.readlines()
        actual_file.close()
        self.assertEqual(actual[:3], expected[:3])
        self.assertRegexpMatches(actual[3], expected[3])
        # PyCharm may rstrip lines without asking...
        self.assertEqual([line.rstrip() for line in actual[4:]], [line.rstrip() for line in expected[4:]])

    def test_vba_restricted_keywords(self):
        import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.valid_swagger_test_get_test_vba_restricted_keywords(
                currency_visual_basic='currency value',
                end_visual_basic='end value'),
            [['currency', 'end'], ['currency value', 'end value']])

    def test_mandatory_integer_parameter_not_provided(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=None,
            query_integer32=None,
            query_integer64=None,
            query_number=None,
            query_float=None,
            query_double=None,
            query_string=None,
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_integer is required.'])

    def test_mandatory_integer_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer='str value',
            query_integer32=None,
            query_integer64=None,
            query_number=None,
            query_float=None,
            query_double=None,
            query_string=None,
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
            ['query_integer must be an integer.'])

    def test_optional_integer_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
                query_integer='str value'),
            ['query_integer must be an integer.'])

    def test_mandatory_array_integer_parameter_not_provided(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_integer is required.'])

    def test_mandatory_array_integer_parameter_provided_as_empty_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[],
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_integer is required.'])

    def test_mandatory_array_integer_parameter_provided_as_none_filled_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[None],
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_integer is required.'])

    def test_mandatory_array_integer_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer='str value',
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_integer must be an integer.'])

    def test_mandatory_array_integer_parameter_with_wrong_type_in_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[
            'str value'
            ],
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_integer must contain integers.'])

    def test_optional_array_integer_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
            query_array_integer='str value'),
            ['query_array_integer must be an integer.'])

    def test_optional_array_integer_parameter_with_wrong_type_in_array(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
            query_array_integer=['str value']
        ),
            ['query_array_integer must contain integers.'])

    def test_mandatory_integer32_parameter_not_provided(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=None,
            query_integer64=None,
            query_number=None,
            query_float=None,
            query_double=None,
            query_string=None,
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_integer32 is required.'])

    def test_mandatory_integer32_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32='str value',
            query_integer64=None,
            query_number=None,
            query_float=None,
            query_double=None,
            query_string=None,
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_integer32 must be an integer.'])

    def test_optional_integer32_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
                query_integer32='str value'),
            ['query_integer32 must be an integer.'])

    def test_mandatory_array_integer32_parameter_not_provided(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_integer32 is required.'])

    def test_mandatory_array_integer32_parameter_provided_as_empty_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[],
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_integer32 is required.'])

    def test_mandatory_array_integer32_parameter_provided_as_none_filled_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[None],
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_integer32 is required.'])

    def test_mandatory_array_integer32_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32='str value',
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_integer32 must be an integer.'])

    def test_mandatory_array_integer32_parameter_with_wrong_type_in_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[
             'str value'],
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_integer32 must contain integers.'])

    def test_optional_array_integer32_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
            query_array_integer32='str value'),
            ['query_array_integer32 must be an integer.'])

    def test_optional_array_integer32_parameter_with_wrong_type_in_array(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
            query_array_integer32=['str value']),
            ['query_array_integer32 must contain integers.'])

    def test_mandatory_integer64_parameter_not_provided(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=None,
                                                                                         query_number=None,
                                                                                         query_float=None,
                                                                                         query_double=None,
                                                                                         query_string=None,
                                                                                         query_string_byte=None,
                                                                                         query_string_binary=None,
                                                                                         query_boolean=None,
                                                                                         query_date=None,
                                                                                         query_date_time=None,
                                                                                         query_password=None,
                                                                                         query_array_integer=None,
                                                                                         query_array_integer32=None,
                                                                                         query_array_integer64=None,
                                                                                         query_array_number=None,
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_integer64 is required.'])

    def test_mandatory_integer64_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64='str value',
                                                                                         query_number=None,
                                                                                         query_float=None,
                                                                                         query_double=None,
                                                                                         query_string=None,
                                                                                         query_string_byte=None,
                                                                                         query_string_binary=None,
                                                                                         query_boolean=None,
                                                                                         query_date=None,
                                                                                         query_date_time=None,
                                                                                         query_password=None,
                                                                                         query_array_integer=None,
                                                                                         query_array_integer32=None,
                                                                                         query_array_integer64=None,
                                                                                         query_array_number=None,
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_integer64 must be an integer.'])

    def test_optional_integer64_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(query_integer64='str value'),
            ['query_integer64 must be an integer.'])

    def test_mandatory_array_integer64_parameter_not_provided(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64=None,
                                                                                         query_array_number=None,
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_integer64 is required.'])

    def test_mandatory_array_integer64_parameter_provided_as_empty_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64=[],
                                                                                         query_array_number=None,
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_integer64 is required.'])

    def test_mandatory_array_integer64_parameter_provided_as_none_filled_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64=[None],
                                                                                         query_array_number=None,
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_integer64 is required.'])

    def test_mandatory_array_integer64_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64='str value',
                                                                                         query_array_number=None,
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_integer64 must be an integer.'])

    def test_mandatory_array_integer64_parameter_with_wrong_type_in_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64=[
                                                                                             'str value'],
                                                                                         query_array_number=None,
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_integer64 must contain integers.'])

    def test_optional_array_integer64_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
            query_array_integer64='str value'),
            ['query_array_integer64 must be an integer.'])

    def test_optional_array_integer64_parameter_with_wrong_type_in_array(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
            query_array_integer64=['str value']),
            ['query_array_integer64 must contain integers.'])

    def test_mandatory_number_parameter_not_provided(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=None,
                                                                                         query_float=None,
                                                                                         query_double=None,
                                                                                         query_string=None,
                                                                                         query_string_byte=None,
                                                                                         query_string_binary=None,
                                                                                         query_boolean=None,
                                                                                         query_date=None,
                                                                                         query_date_time=None,
                                                                                         query_password=None,
                                                                                         query_array_integer=None,
                                                                                         query_array_integer32=None,
                                                                                         query_array_integer64=None,
                                                                                         query_array_number=None,
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_number is required.'])

    def test_mandatory_number_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number='str value',
                                                                                         query_float=None,
                                                                                         query_double=None,
                                                                                         query_string=None,
                                                                                         query_string_byte=None,
                                                                                         query_string_binary=None,
                                                                                         query_boolean=None,
                                                                                         query_date=None,
                                                                                         query_date_time=None,
                                                                                         query_password=None,
                                                                                         query_array_integer=None,
                                                                                         query_array_integer32=None,
                                                                                         query_array_integer64=None,
                                                                                         query_array_number=None,
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_number must be a number.'])

    def test_optional_number_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(query_number='str value'),
            ['query_number must be a number.'])

    def test_mandatory_array_number_parameter_not_provided(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64=[0],
                                                                                         query_array_number=None,
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_number is required.'])

    def test_mandatory_array_number_parameter_provided_as_empty_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64=[0],
                                                                                         query_array_number=[],
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_number is required.'])

    def test_mandatory_array_number_parameter_provided_as_none_filled_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64=[0],
                                                                                         query_array_number=[None],
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_number is required.'])

    def test_mandatory_array_number_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64=[0],
                                                                                         query_array_number='str value',
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_number must be a number.'])

    def test_mandatory_array_number_parameter_with_wrong_type_in_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64=[0],
                                                                                         query_array_number=[
                                                                                             'str value'],
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_number must contain numbers.'])

    def test_optional_array_number_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
            query_array_number='str value'),
            ['query_array_number must be a number.'])

    def test_optional_array_number_parameter_with_wrong_type_in_array(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
            query_array_number=['str value']),
            ['query_array_number must contain numbers.'])

    def test_mandatory_float_parameter_not_provided(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=None,
                                                                                         query_double=None,
                                                                                         query_string=None,
                                                                                         query_string_byte=None,
                                                                                         query_string_binary=None,
                                                                                         query_boolean=None,
                                                                                         query_date=None,
                                                                                         query_date_time=None,
                                                                                         query_password=None,
                                                                                         query_array_integer=None,
                                                                                         query_array_integer32=None,
                                                                                         query_array_integer64=None,
                                                                                         query_array_number=None,
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_float is required.'])

    def test_mandatory_float_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float='str value',
                                                                                         query_double=None,
                                                                                         query_string=None,
                                                                                         query_string_byte=None,
                                                                                         query_string_binary=None,
                                                                                         query_boolean=None,
                                                                                         query_date=None,
                                                                                         query_date_time=None,
                                                                                         query_password=None,
                                                                                         query_array_integer=None,
                                                                                         query_array_integer32=None,
                                                                                         query_array_integer64=None,
                                                                                         query_array_number=None,
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_float must be a number.'])

    def test_optional_float_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(query_float='str value'),
            ['query_float must be a number.'])

    def test_mandatory_array_float_number_parameter_not_provided(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64=[0],
                                                                                         query_array_number=[0.0],
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_float is required.'])

    def test_mandatory_array_float_parameter_provided_as_empty_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64=[0],
                                                                                         query_array_number=[0.0],
                                                                                         query_array_float=[],
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_float is required.'])

    def test_mandatory_array_float_parameter_provided_as_none_filled_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64=[0],
                                                                                         query_array_number=[0.0],
                                                                                         query_array_float=[None],
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_float is required.'])

    def test_mandatory_array_float_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64=[0],
                                                                                         query_array_number=[0.0],
                                                                                         query_array_float='str value',
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_float must be a number.'])

    def test_mandatory_array_float_parameter_with_wrong_type_in_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64=[0],
                                                                                         query_array_number=[0.0],
                                                                                         query_array_float=[
                                                                                             'str value'],
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_float must contain numbers.'])

    def test_optional_array_float_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
                query_array_float='str value'),
            ['query_array_float must be a number.'])

    def test_optional_array_float_parameter_with_wrong_type_in_array(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
            query_array_float=['str value']),
            ['query_array_float must contain numbers.'])

    def test_mandatory_double_parameter_not_provided(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=None,
                                                                                         query_string=None,
                                                                                         query_string_byte=None,
                                                                                         query_string_binary=None,
                                                                                         query_boolean=None,
                                                                                         query_date=None,
                                                                                         query_date_time=None,
                                                                                         query_password=None,
                                                                                         query_array_integer=None,
                                                                                         query_array_integer32=None,
                                                                                         query_array_integer64=None,
                                                                                         query_array_number=None,
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_double is required.'])

    def test_mandatory_double_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double='str value',
                                                                                         query_string=None,
                                                                                         query_string_byte=None,
                                                                                         query_string_binary=None,
                                                                                         query_boolean=None,
                                                                                         query_date=None,
                                                                                         query_date_time=None,
                                                                                         query_password=None,
                                                                                         query_array_integer=None,
                                                                                         query_array_integer32=None,
                                                                                         query_array_integer64=None,
                                                                                         query_array_number=None,
                                                                                         query_array_float=None,
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_double must be a number.'])

    def test_optional_double_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
                query_double='str value'),
            ['query_double must be a number.'])

    def test_mandatory_array_double_number_parameter_not_provided(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64=[0],
                                                                                         query_array_number=[0.0],
                                                                                         query_array_float=[0.0],
                                                                                         query_array_double=None,
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_double is required.'])

    def test_mandatory_array_double_parameter_provided_as_empty_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64=[0],
                                                                                         query_array_number=[0.0],
                                                                                         query_array_float=[0.0],
                                                                                         query_array_double=[],
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_double is required.'])

    def test_mandatory_array_double_parameter_provided_as_none_filled_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64=[0],
                                                                                         query_array_number=[0.0],
                                                                                         query_array_float=[0.0],
                                                                                         query_array_double=[None],
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_double is required.'])

    def test_mandatory_array_double_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
                                                                                         query_integer32=0,
                                                                                         query_integer64=0,
                                                                                         query_number=0.0,
                                                                                         query_float=0.0,
                                                                                         query_double=0.0,
                                                                                         query_string='str value',
                                                                                         query_string_byte='str value',
                                                                                         query_string_binary='str value',
                                                                                         query_boolean='true',
                                                                                         query_date=today_date,
                                                                                         query_date_time=today_datetime,
                                                                                         query_password='str value',
                                                                                         query_array_integer=[0],
                                                                                         query_array_integer32=[0],
                                                                                         query_array_integer64=[0],
                                                                                         query_array_number=[0.0],
                                                                                         query_array_float=[0.0],
                                                                                         query_array_double='str value',
                                                                                         query_array_string=None,
                                                                                         query_array_string_byte=None,
                                                                                         query_array_string_binary=None,
                                                                                         query_array_boolean=None,
                                                                                         query_array_date=None,
                                                                                         query_array_date_time=None,
                                                                                         query_array_password=None),
                         ['query_array_double must be a number.'])

    def test_mandatory_array_double_parameter_with_wrong_type_in_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[
             'str value'],
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_double must contain numbers.'])

    def test_optional_array_double_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
            query_array_double='str value'),
            ['query_array_double must be a number.'])

    def test_optional_array_double_parameter_with_wrong_type_in_array(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
            query_array_double=['str value']),
            ['query_array_double must contain numbers.'])

    def test_mandatory_string_parameter_not_provided(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string=None,
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_string is required.'])

    def test_mandatory_string_parameter_provided_as_empty_array(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string=[],
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_string is required.'])

    def test_mandatory_string_parameter_provided_as_none_filled_array(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string=[None],
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_string is required.'])

    def test_mandatory_array_string_parameter_not_provided(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_string is required.'])

    def test_mandatory_array_string_parameter_provided_as_empty_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[],
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_string is required.'])

    def test_mandatory_array_string_parameter_provided_as_none_filled_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[None],
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_string is required.'])

    def test_mandatory_string_byte_parameter_not_provided(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_string_byte is required.'])

    def test_mandatory_string_byte_parameter_provided_as_empty_array(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte=[],
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_string_byte is required.'])

    def test_mandatory_string_byte_parameter_provided_as_none_filled_array(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte=[None],
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_string_byte is required.'])

    def test_mandatory_array_string_byte_parameter_not_provided(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_string_byte is required.'])

    def test_mandatory_array_string_byte_parameter_provided_as_empty_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=[],
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_string_byte is required.'])

    def test_mandatory_array_string_byte_parameter_provided_as_none_filled_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
            'str value'],
            query_array_string_byte=[None],
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_string_byte is required.'])

    def test_mandatory_string_binary_parameter_not_provided(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_string_binary is required.'])

    def test_mandatory_string_binary_parameter_provided_as_empty_array(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary=[],
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_string_binary is required.'])

    def test_mandatory_string_binary_parameter_provided_as_none_filled_array(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary=[None],
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_string_binary is required.'])

    def test_mandatory_array_string_binary_parameter_not_provided(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=[
             'str value'],
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_string_binary is required.'])

    def test_mandatory_array_string_binary_parameter_provided_as_empty_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=[
             'str value'],
            query_array_string_binary=[],
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_string_binary is required.'])

    def test_mandatory_array_string_binary_parameter_provided_as_none_filled_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=[
             'str value'],
            query_array_string_binary=[
             None],
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_string_binary is required.'])

    def test_mandatory_boolean_parameter_not_provided(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_boolean is required.'])

    def test_mandatory_boolean_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='non boolean',
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_boolean must be either "true" or "false".'])

    def test_optional_boolean_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
                query_boolean='non boolean'),
            ['query_boolean must be either "true" or "false".'])

    def test_mandatory_array_boolean_parameter_not_provided(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=[
             'str value'],
            query_array_string_binary=[
             'str value'],
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_boolean is required.'])

    def test_mandatory_array_boolean_parameter_provided_as_empty_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=[
             'str value'],
            query_array_string_binary=[
             'str value'],
            query_array_boolean=[],
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_boolean is required.'])

    def test_mandatory_array_boolean_parameter_provided_as_none_filled_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=[
             'str value'],
            query_array_string_binary=[
             'str value'],
            query_array_boolean=[None],
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_boolean is required.'])

    def test_mandatory_array_boolean_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
            'str value'],
            query_array_string_byte=[
            'str value'],
            query_array_string_binary=[
            'str value'],
            query_array_boolean='non boolean',
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_boolean must contain "true" or "false".'])

    def test_mandatory_array_boolean_parameter_with_wrong_type_in_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=[
             'str value'],
            query_array_string_binary=[
             'str value'],
            query_array_boolean=[
             'non boolean'],
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_boolean must be either "true" or "false".'])

    def test_optional_array_boolean_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
            query_array_boolean='non boolean'),
            ['query_array_boolean must contain "true" or "false".'])

    def test_optional_array_boolean_parameter_with_wrong_type_in_array(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
            query_array_boolean=['non boolean']),
            ['query_array_boolean must be either "true" or "false".'])

    def test_mandatory_date_parameter_not_provided(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_date is required.'])

    def test_mandatory_date_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date='str value',
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_date must be a date.'])

    def test_optional_date_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(query_date='str value'),
            ['query_date must be a date.'])

    def test_mandatory_array_date_parameter_not_provided(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=[
             'str value'],
            query_array_string_binary=[
             'str value'],
            query_array_boolean=['true'],
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_date is required.'])

    def test_mandatory_array_date_parameter_provided_as_empty_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=[
             'str value'],
            query_array_string_binary=[
             'str value'],
            query_array_boolean=['true'],
            query_array_date=[],
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_date is required.'])

    def test_mandatory_array_date_parameter_provided_as_none_filled_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=[
             'str value'],
            query_array_string_binary=[
             'str value'],
            query_array_boolean=['true'],
            query_array_date=[None],
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_date is required.'])

    def test_mandatory_array_date_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=[
             'str value'],
            query_array_string_binary=[
             'str value'],
            query_array_boolean=['true'],
            query_array_date='str value',
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_date must be a date.'])

    def test_mandatory_array_date_parameter_with_wrong_type_in_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=[
             'str value'],
            query_array_string_binary=[
             'str value'],
            query_array_boolean=['true'],
            query_array_date=['str value'],
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_date must contain dates.'])

    def test_optional_array_date_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(query_array_date='str value'),
            ['query_array_date must be a date.'])

    def test_optional_array_date_parameter_with_wrong_type_in_array(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
            query_array_date=['str value']),
            ['query_array_date must contain dates.'])

    def test_mandatory_date_time_parameter_not_provided(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_date_time is required.'])

    def test_mandatory_date_time_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time='str value',
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
                         ['query_date_time must be a date time.'])

    def test_optional_date_time_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(query_date_time='str value'),
            ['query_date_time must be a date time.'])

    def test_mandatory_array_date_time_parameter_not_provided(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=[
             'str value'],
            query_array_string_binary=[
             'str value'],
            query_array_boolean=['true'],
            query_array_date=[today_date],
            query_array_date_time=None,
            query_array_password=None),
                         ['query_array_date_time is required.'])

    def test_mandatory_array_date_time_parameter_provided_as_empty_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=[
             'str value'],
            query_array_string_binary=[
             'str value'],
            query_array_boolean=['true'],
            query_array_date=[today_date],
            query_array_date_time=[],
            query_array_password=None),
                         ['query_array_date_time is required.'])

    def test_mandatory_array_date_time_parameter_provided_as_none_filled_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=[
             'str value'],
            query_array_string_binary=[
             'str value'],
            query_array_boolean=['true'],
            query_array_date=[today_date],
            query_array_date_time=[None],
            query_array_password=None),
                         ['query_array_date_time is required.'])

    def test_mandatory_array_date_time_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=[
             'str value'],
            query_array_string_binary=[
             'str value'],
            query_array_boolean=['true'],
            query_array_date=[today_date],
            query_array_date_time='str value',
            query_array_password=None),
                         ['query_array_date_time must be a date time.'])

    def test_mandatory_array_date_time_parameter_with_wrong_type_in_array(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='str value',
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[
             'str value'],
            query_array_string_byte=[
             'str value'],
            query_array_string_binary=[
             'str value'],
            query_array_boolean=['true'],
            query_array_date=[today_date],
            query_array_date_time=[
             'str value'],
            query_array_password=None),
                         ['query_array_date_time must contain date times.'])

    def test_valid_mandatory_parameters(self):
        import pyxelrestgenerator
        today_date = datetime.date.today()
        tomorrow_date = today_date + datetime.timedelta(days=1)
        today_datetime = datetime.datetime.today()
        tomorrow_datetime = today_datetime + datetime.timedelta(days=1)
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_parameters_types(
            query_integer=1,
            query_integer32=10,
            query_integer64=100,
            query_number=0.1,
            query_float=1.01,
            query_double=1.1,
            query_string='string',
            query_string_byte='string bytes',
            query_string_binary='string binary',
            query_boolean='true',
            query_date=today_date,
            query_date_time=today_datetime,
            query_password='password',
            query_array_integer=[1, 2],
            query_array_integer32=[10, 20],
            query_array_integer64=[100,
                                200],
            query_array_number=[0.1, 0.2],
            query_array_float=[1.01, 2.01],
            query_array_double=[1.1, 2.1],
            query_array_string=[
             'string 1',
             'string 2'
            ],
            query_array_string_byte=[
             'string bytes 1',
             'string bytes 2'
            ],
            query_array_string_binary=[
             'string binary 1',
             'string binary 2'
            ],
            query_array_boolean=['true',
                              'false'],
            query_array_date=[
             today_date,
             tomorrow_date
            ],
            query_array_date_time=[
             today_datetime,
             tomorrow_datetime
            ],
            query_array_password=[
             'password 1',
             'password 2'
            ]),
                         [
                             [
                                 'query_array_boolean', 'query_array_date', 'query_array_date_time',
                                 'query_array_double', 'query_array_float', 'query_array_integer',
                                 'query_array_integer32', 'query_array_integer64',
                                 'query_array_number', 'query_array_password', 'query_array_string',
                                 'query_array_string_binary', 'query_array_string_byte', 'query_boolean',
                                 'query_date', 'query_date_time', 'query_double', 'query_float', 'query_integer',
                                 'query_integer32', 'query_integer64', 'query_number', 'query_password',
                                 'query_string', 'query_string_binary', 'query_string_byte'
                             ],
                             [
                                 'true', str(today_date), str(today_datetime),
                                 '1.1', '1.01', '1',
                                 '10', '100',
                                 '0.1', 'password 1', 'string 1',
                                 'string binary 1', 'string bytes 1', 'True',
                                 str(today_date), str(today_datetime), '1.1', '1.01', '1',
                                 '10', '100', '0.1', 'password',
                                 'string', 'string binary', 'string bytes'
                             ]
                         ])

    def test_optional_array_date_time_parameter_with_wrong_type(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
            query_array_date_time='str value'),
            ['query_array_date_time must be a date time.'])

    def test_optional_array_date_time_parameter_with_wrong_type_in_array(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_json_with_all_optional_parameters_types(
            query_array_date_time=['str value']),
            ['query_array_date_time must contain date times.'])

    def test_string_array_parameter(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_string_array_parameter(['str1', 'str2']),
                         'query_array_string="[\'str1\', \'str2\']"')

    def test_plain_text_without_parameter(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_get_test_plain_text_without_parameter(),
                         'string value returned should be truncated so that the following information cannot be seen by'
                         ' user, because of the fact that Excel does not allow more than 255 characters in a cell. '
                         'Only the 255 characters will be returned by the user defined functions:  ')

    def test_post_test_without_parameter(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_post_test_without_parameter(),
                         'POST performed properly')

    def test_put_test_without_parameter(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_put_test_without_parameter(),
                         'PUT performed properly')

    def test_delete_test_without_parameter(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_delete_test_without_parameter(),
                         'DELETE performed properly')

    def test_get_test_header_parameter(self):
        import pyxelrestgenerator
        headers = pyxelrestgenerator.valid_swagger_test_get_test_header_parameter('sent header')
        header_param_index = None
        for header_index in range(0, len(headers[0])):
            if headers[0][header_index] == 'Header-String':
                header_param_index = header_index
                break
        self.assertEqual(headers[1][header_param_index], 'sent header')

    def test_post_test_form_parameter(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.valid_swagger_test_post_test_form_parameter('sent string form data'), [
            ['form_string'],
            ['sent string form data']
        ])

    def test_get_test_dict_with_empty_nested_list(self):
        import pyxelrestgenerator
        self.maxDiff = None
        self.assertEqual([
            ['Column 1', 'Column 2', 'Column 2.1', 'Column 2.2', 'Column 3.1', 'Column 3.2', 'Column 3.3', 'Column 2.3', 'Column 3'],
            ['0-0-1', '', '0-0-2 / 1-0-1', '', '', '', '', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-1-1', '', '0-0-2 / 1-1-2 / 2-0-1', '', '0-0-2 / 1-1-2 / 2-0-3', '0-0-2 / 1-1-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-1-1', '', '0-0-2 / 1-1-2 / 2-1-1', '', '0-0-2 / 1-1-2 / 2-1-3', '0-0-2 / 1-1-3', '0-0-3']
        ],
            pyxelrestgenerator.valid_swagger_test_get_test_dict_with_empty_nested_list())

    def test_get_test_dict_with_three_imbricated_levels(self):
        import pyxelrestgenerator
        self.maxDiff = None
        self.assertEqual([
            ['Column 1', 'Column 2', 'Column 2.1', 'Column 2.2', 'Column 3.1', 'Column 3.2', 'Column 3.3', 'Column 2.3', 'Column 3'],
            ['0-0-1', '', '0-0-2 / 1-0-1', '', '0-0-2 / 1-0-2 / 2-0-1', '', '0-0-2 / 1-0-2 / 2-0-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-0-1', '', '0-0-2 / 1-0-2 / 2-1-1', '', '0-0-2 / 1-0-2 / 2-1-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-1-1', '', '0-0-2 / 1-1-2 / 2-0-1', '', '0-0-2 / 1-1-2 / 2-0-3', '0-0-2 / 1-1-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-1-1', '', '0-0-2 / 1-1-2 / 2-1-1', '', '0-0-2 / 1-1-2 / 2-1-3', '0-0-2 / 1-1-3', '0-0-3']
        ],
            pyxelrestgenerator.valid_swagger_test_get_test_dict_with_three_imbricated_levels())

    def test_get_test_dict_with_four_imbricated_levels(self):
        import pyxelrestgenerator
        self.maxDiff = None
        self.assertEqual([
            ['Column 1', 'Column 2', 'Column 2.1', 'Column 2.2', 'Column 3.1', 'Column 3.2', 'Column 4.1', 'Column 4.2', 'Column 4.3', 'Column 3.3', 'Column 2.3', 'Column 3'],
            ['0-0-1', '', '0-0-2 / 1-0-1', '', '0-0-2 / 1-0-2 / 2-0-1', '', '0-0-2 / 1-0-2 / 2-0-2 / 3-0-1', '', '0-0-2 / 1-0-2 / 2-0-2 / 3-0-3', '0-0-2 / 1-0-2 / 2-0-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-0-1', '', '0-0-2 / 1-0-2 / 2-0-1', '', '0-0-2 / 1-0-2 / 2-0-2 / 3-1-1', '', '0-0-2 / 1-0-2 / 2-0-2 / 3-1-3', '0-0-2 / 1-0-2 / 2-0-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-0-1', '', '0-0-2 / 1-0-2 / 2-1-1', '', '', '', '', '0-0-2 / 1-0-2 / 2-1-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-1-1', '', '0-0-2 / 1-1-2 / 2-0-1', '', '', '', '', '0-0-2 / 1-1-2 / 2-0-3', '0-0-2 / 1-1-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-1-1', '', '0-0-2 / 1-1-2 / 2-1-1', '', '', '', '', '0-0-2 / 1-1-2 / 2-1-3', '0-0-2 / 1-1-3', '0-0-3']
        ],
            pyxelrestgenerator.valid_swagger_test_get_test_dict_with_four_imbricated_levels())

    def test_get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys(self):
        import pyxelrestgenerator
        self.maxDiff = None
        self.assertEqual([
            ['Column 1', 'Column 2', 'Column 1', 'Column 2', 'Column 1', 'Column 2', 'Column 1', 'Column 2', 'Column 3', 'Column 3', 'Column 3', 'Column 3'],
            ['0-0-1', '', '0-0-2 / 1-0-1', '', '0-0-2 / 1-0-2 / 2-0-1', '', '0-0-2 / 1-0-2 / 2-0-2 / 3-0-1', '', '0-0-2 / 1-0-2 / 2-0-2 / 3-0-3', '0-0-2 / 1-0-2 / 2-0-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-0-1', '', '0-0-2 / 1-0-2 / 2-0-1', '', '0-0-2 / 1-0-2 / 2-0-2 / 3-1-1', '', '0-0-2 / 1-0-2 / 2-0-2 / 3-1-3', '0-0-2 / 1-0-2 / 2-0-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-0-1', '', '0-0-2 / 1-0-2 / 2-1-1', '', '', '', '', '0-0-2 / 1-0-2 / 2-1-3', '0-0-2 / 1-0-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-1-1', '', '0-0-2 / 1-1-2 / 2-0-1', '', '', '', '', '0-0-2 / 1-1-2 / 2-0-3', '0-0-2 / 1-1-3', '0-0-3'],
            ['0-0-1', '', '0-0-2 / 1-1-1', '', '0-0-2 / 1-1-2 / 2-1-1', '', '', '', '', '0-0-2 / 1-1-2 / 2-1-3', '0-0-2 / 1-1-3', '0-0-3']
        ],
            pyxelrestgenerator.valid_swagger_test_get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys())

    def test_get_test_empty_dict(self):
        import pyxelrestgenerator
        self.assertEqual([''],
            pyxelrestgenerator.valid_swagger_test_get_test_empty_dict())

    def test_get_test_empty_list(self):
        import pyxelrestgenerator
        self.assertEqual([''],
            pyxelrestgenerator.valid_swagger_test_get_test_empty_list())

    def test_get_test_one_level_dict(self):
        import pyxelrestgenerator
        self.assertEqual([
            ['Column 1', 'Column 2'],
            ['value 1', 'value 2']
        ],
            pyxelrestgenerator.valid_swagger_test_get_test_one_level_dict())

    def test_get_test_one_level_list(self):
        import pyxelrestgenerator
        self.assertEqual([
            ['value 1'],
            ['value 2']
        ],
            pyxelrestgenerator.valid_swagger_test_get_test_one_level_list())

    def test_get_test_one_dict_entry_with_a_list(self):
        import pyxelrestgenerator
        self.assertEqual([
            ['Column 1', 'Column 1'],
            ['', 'value 1'],
            ['', 'value 2']
        ],
            pyxelrestgenerator.valid_swagger_test_get_test_one_dict_entry_with_a_list())

    def test_get_test_one_dict_entry_with_a_list_of_dict(self):
        import pyxelrestgenerator
        self.assertEqual([
            ['Column 1', 'Column 2', 'Column 3'],
            ['', 'value 12', 'value 13'],
            ['', 'value 22', 'value 23']
        ],
            pyxelrestgenerator.valid_swagger_test_get_test_one_dict_entry_with_a_list_of_dict())

    def test_get_test_list_of_dict(self):
        import pyxelrestgenerator
        self.assertEqual([
            ['Column 1', 'Column 2'],
            ['value 11', 'value 12'],
            ['value 21', 'value 22']
        ],
            pyxelrestgenerator.valid_swagger_test_get_test_list_of_dict())

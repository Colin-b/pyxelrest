import datetime
import unittest

from testsutils import (serviceshandler, loader)


class PyxelRestJsonNoFlattenizerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import testsutils.json_service as json_service
        serviceshandler.start_services((json_service, 8954))
        loader.load('json_services.yml')
        import pyxelrest
        pyxelrest.GENERATE_UDF_ON_IMPORT = False
        from pyxelrest import pyxelrestgenerator
        services = pyxelrestgenerator.generate_user_defined_functions(flattenize=False)
        pyxelrestgenerator.reload_user_defined_functions(services)

    @classmethod
    def tearDownClass(cls):
        serviceshandler.stop_services()

    def test_mandatory_integer_parameter_not_provided(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
            ['query_integer value "str value" must be an integer.'])

    def test_optional_integer_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(
            user_defined_functions.json_get_all_optional_parameters_types(
                query_integer='str value'),
            ['query_integer value "str value" must be an integer.'])

    def test_mandatory_array_integer_parameter_not_provided(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            ['query_array_integer value "str value" must be an integer.'])

    def test_mandatory_array_integer_parameter_with_wrong_type_in_array(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            ['query_array_integer value "str value" must be an integer.'])

    def test_optional_array_integer_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_optional_parameters_types(
            query_array_integer='str value'),
            ['query_array_integer value "str value" must be an integer.'])

    def test_optional_array_integer_parameter_with_wrong_type_in_array(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_optional_parameters_types(
            query_array_integer=['str value']
        ),
            ['query_array_integer value "str value" must be an integer.'])

    def test_mandatory_integer32_parameter_not_provided(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
            ['query_integer32 value "str value" must be an integer.'])

    def test_optional_integer32_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(
            user_defined_functions.json_get_all_optional_parameters_types(
                query_integer32='str value'),
            ['query_integer32 value "str value" must be an integer.'])

    def test_mandatory_array_integer32_parameter_not_provided(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            ['query_array_integer32 value "str value" must be an integer.'])

    def test_mandatory_array_integer32_parameter_with_wrong_type_in_array(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            ['query_array_integer32 value "str value" must be an integer.'])

    def test_optional_array_integer32_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_optional_parameters_types(
            query_array_integer32='str value'),
            ['query_array_integer32 value "str value" must be an integer.'])

    def test_optional_array_integer32_parameter_with_wrong_type_in_array(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_optional_parameters_types(
            query_array_integer32=['str value']),
            ['query_array_integer32 value "str value" must be an integer.'])

    def test_mandatory_integer64_parameter_not_provided(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
            ['query_integer64 value "str value" must be an integer.'])

    def test_optional_integer64_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(
            user_defined_functions.json_get_all_optional_parameters_types(
                query_integer64='str value'),
            ['query_integer64 value "str value" must be an integer.'])

    def test_mandatory_array_integer64_parameter_not_provided(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            ['query_array_integer64 value "str value" must be an integer.'])

    def test_mandatory_array_integer64_parameter_with_wrong_type_in_array(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            ['query_array_integer64 value "str value" must be an integer.'])

    def test_optional_array_integer64_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_optional_parameters_types(
            query_array_integer64='str value'),
            ['query_array_integer64 value "str value" must be an integer.'])

    def test_optional_array_integer64_parameter_with_wrong_type_in_array(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_optional_parameters_types(
            query_array_integer64=['str value']),
            ['query_array_integer64 value "str value" must be an integer.'])

    def test_mandatory_number_parameter_not_provided(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
            ['query_number value "str value" must be a number.'])

    def test_optional_number_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(
            user_defined_functions.json_get_all_optional_parameters_types(
                query_number='str value'),
            ['query_number value "str value" must be a number.'])

    def test_mandatory_array_number_parameter_not_provided(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            ['query_array_number value "str value" must be a number.'])

    def test_mandatory_array_number_parameter_with_wrong_type_in_array(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            ['query_array_number value "str value" must be a number.'])

    def test_optional_array_number_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_optional_parameters_types(
            query_array_number='str value'),
            ['query_array_number value "str value" must be a number.'])

    def test_optional_array_number_parameter_with_wrong_type_in_array(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_optional_parameters_types(
            query_array_number=['str value']),
            ['query_array_number value "str value" must be a number.'])

    def test_mandatory_float_parameter_not_provided(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
            ['query_float value "str value" must be a number.'])

    def test_optional_float_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(
            user_defined_functions.json_get_all_optional_parameters_types(
                query_float='str value'),
            ['query_float value "str value" must be a number.'])

    def test_mandatory_array_float_number_parameter_not_provided(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            ['query_array_float value "str value" must be a number.'])

    def test_mandatory_array_float_parameter_with_wrong_type_in_array(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            ['query_array_float value "str value" must be a number.'])

    def test_optional_array_float_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(
            user_defined_functions.json_get_all_optional_parameters_types(
                query_array_float='str value'),
            ['query_array_float value "str value" must be a number.'])

    def test_optional_array_float_parameter_with_wrong_type_in_array(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_optional_parameters_types(
            query_array_float=['str value']),
            ['query_array_float value "str value" must be a number.'])

    def test_mandatory_double_parameter_not_provided(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
            ['query_double value "str value" must be a number.'])

    def test_optional_double_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(
            user_defined_functions.json_get_all_optional_parameters_types(
                query_double='str value'),
            ['query_double value "str value" must be a number.'])

    def test_mandatory_array_double_number_parameter_not_provided(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            ['query_array_double value "str value" must be a number.'])

    def test_mandatory_array_double_parameter_with_wrong_type_in_array(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            ['query_array_double value "str value" must be a number.'])

    def test_optional_array_double_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_optional_parameters_types(
            query_array_double='str value'),
            ['query_array_double value "str value" must be a number.'])

    def test_optional_array_double_parameter_with_wrong_type_in_array(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_optional_parameters_types(
            query_array_double=['str value']),
            ['query_array_double value "str value" must be a number.'])

    def test_mandatory_string_parameter_not_provided(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
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
            ['query_boolean value "non boolean" must be a boolean.'])

    def test_optional_boolean_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(
            user_defined_functions.json_get_all_optional_parameters_types(
                query_boolean='non boolean'),
            ['query_boolean value "non boolean" must be a boolean.'])

    def test_mandatory_array_boolean_parameter_not_provided(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            ['query_array_boolean value "non boolean" must be a boolean.'])

    def test_mandatory_array_boolean_parameter_with_wrong_type_in_array(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            ['query_array_boolean value "non boolean" must be a boolean.'])

    def test_optional_array_boolean_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_optional_parameters_types(
            query_array_boolean='non boolean'),
            ['query_array_boolean value "non boolean" must be a boolean.'])

    def test_optional_array_boolean_parameter_with_wrong_type_in_array(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_optional_parameters_types(
            query_array_boolean=['non boolean']),
            ['query_array_boolean value "non boolean" must be a boolean.'])

    def test_mandatory_date_parameter_not_provided(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            ['query_date value "str value" must be a date.'])

    def test_optional_date_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(
            user_defined_functions.json_get_all_optional_parameters_types(
                query_date='str value'),
            ['query_date value "str value" must be a date.'])

    def test_mandatory_array_date_parameter_not_provided(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            query_array_boolean=[True],
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None),
            ['query_array_date is required.'])

    def test_mandatory_array_date_parameter_provided_as_empty_array(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            query_array_boolean=[True],
            query_array_date=[],
            query_array_date_time=None,
            query_array_password=None),
            ['query_array_date is required.'])

    def test_mandatory_array_date_parameter_provided_as_none_filled_array(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            query_array_boolean=[True],
            query_array_date=[None],
            query_array_date_time=None,
            query_array_password=None),
            ['query_array_date is required.'])

    def test_mandatory_array_date_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            query_array_boolean=[True],
            query_array_date='str value',
            query_array_date_time=None,
            query_array_password=None),
            ['query_array_date value "str value" must be a date.'])

    def test_mandatory_array_date_parameter_with_wrong_type_in_array(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            query_array_boolean=[True],
            query_array_date=['str value'],
            query_array_date_time=None,
            query_array_password=None),
            ['query_array_date value "str value" must be a date.'])

    def test_optional_array_date_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(
            user_defined_functions.json_get_all_optional_parameters_types(
                query_array_date='str value'),
            ['query_array_date value "str value" must be a date.'])

    def test_optional_array_date_parameter_with_wrong_type_in_array(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_optional_parameters_types(
            query_array_date=['str value']),
            ['query_array_date value "str value" must be a date.'])

    def test_mandatory_date_time_parameter_not_provided(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            ['query_date_time value "str value" must be a date time.'])

    def test_optional_date_time_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(
            user_defined_functions.json_get_all_optional_parameters_types(
                query_date_time='str value'),
            ['query_date_time value "str value" must be a date time.'])

    def test_mandatory_array_date_time_parameter_not_provided(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            query_array_boolean=[True],
            query_array_date=[today_date],
            query_array_date_time=None,
            query_array_password=None),
            ['query_array_date_time is required.'])

    def test_mandatory_array_date_time_parameter_provided_as_empty_array(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            query_array_boolean=[True],
            query_array_date=[today_date],
            query_array_date_time=[],
            query_array_password=None),
            ['query_array_date_time is required.'])

    def test_mandatory_array_date_time_parameter_provided_as_none_filled_array(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            query_array_boolean=[True],
            query_array_date=[today_date],
            query_array_date_time=[None],
            query_array_password=None),
            ['query_array_date_time is required.'])

    def test_mandatory_array_date_time_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            query_array_boolean=[True],
            query_array_date=[today_date],
            query_array_date_time='str value',
            query_array_password=None),
            ['query_array_date_time value "str value" must be a date time.'])

    def test_mandatory_array_date_time_parameter_with_wrong_type_in_array(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        today_datetime = datetime.datetime.today()
        self.assertEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string='str value',
            query_string_byte='str value',
            query_string_binary='str value',
            query_boolean=True,
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
            query_array_boolean=[True],
            query_array_date=[today_date],
            query_array_date_time=[
                'str value'],
            query_array_password=None),
            ['query_array_date_time value "str value" must be a date time.'])

    def test_valid_mandatory_parameters(self):
        from pyxelrest import user_defined_functions
        today_date = datetime.date.today()
        tomorrow_date = today_date + datetime.timedelta(days=1)
        today_datetime = datetime.datetime.combine(today_date, datetime.datetime.min.time())
        today_date_str = today_datetime.strftime('%Y-%m-%d')
        today_datetime_str_T = today_datetime.strftime('%Y-%m-%dT%H:%M:%S')
        tomorrow_datetime = datetime.datetime.combine(tomorrow_date, datetime.datetime.min.time())
        from collections import OrderedDict
        import sys
        if sys.version_info[0] == 2:
            today_date_str = unicode(today_date_str)
            today_datetime_str_T = unicode(today_datetime.strftime('%Y-%m-%dT%H:%M:%S'))
        self.maxDiff = None
        expected = \
            OrderedDict([(u'query_array_boolean', u'True'), (u'query_array_date', today_date_str),
                     (u'query_array_date_time', today_datetime_str_T), (u'query_array_double', u'1.1'),
                     (u'query_array_float', u'1.01'), (u'query_array_integer', u'1'), (u'query_array_integer32', u'10'),
                     (u'query_array_integer64', u'100'), (u'query_array_number', u'0.1'),
                     (u'query_array_password', u'password 1'), (u'query_array_string', u'string 1'),
                     (u'query_array_string_binary', u'string binary 1'),
                     (u'query_array_string_byte', u'string bytes 1'), (u'query_boolean', u'True'),
                     (u'query_date', today_date_str), (u'query_date_time', today_datetime_str_T),
                     (u'query_double', u'1.1'), (u'query_float', u'1.01'), (u'query_integer', u'1'),
                     (u'query_integer32', u'10'), (u'query_integer64', u'100'), (u'query_number', u'0.1'),
                     (u'query_password', u'password'), (u'query_string', u'string'),
                     (u'query_string_binary', u'string binary'), (u'query_string_byte', u'string bytes')]) \
            if sys.version_info[0] == 2 else \
            OrderedDict([('query_array_boolean', 'True'), ('query_array_date', today_date_str),
                     ('query_array_date_time', today_datetime_str_T), ('query_array_double', '1.1'),
                     ('query_array_float', '1.01'), ('query_array_integer', '1'), ('query_array_integer32', '10'),
                     ('query_array_integer64', '100'), ('query_array_number', '0.1'),
                     ('query_array_password', 'password 1'), ('query_array_string', 'string 1'),
                     ('query_array_string_binary', 'string binary 1'),
                     ('query_array_string_byte', 'string bytes 1'), ('query_boolean', 'True'),
                     ('query_date', today_date_str), ('query_date_time', today_datetime_str_T),
                     ('query_double', '1.1'), ('query_float', '1.01'), ('query_integer', '1'),
                     ('query_integer32', '10'), ('query_integer64', '100'), ('query_number', '0.1'),
                     ('query_password', 'password'), ('query_string', 'string'),
                     ('query_string_binary', 'string binary'), ('query_string_byte', 'string bytes')])
        self.assertDictEqual(user_defined_functions.json_get_all_parameters_types(
            query_integer=1,
            query_integer32=10,
            query_integer64=100,
            query_number=0.1,
            query_float=1.01,
            query_double=1.1,
            query_string='string',
            query_string_byte='string bytes',
            query_string_binary='string binary',
            query_boolean=True,
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
            query_array_boolean=[True, False],
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
            expected)

    def test_optional_array_date_time_parameter_with_wrong_type(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_optional_parameters_types(
            query_array_date_time='str value'),
            ['query_array_date_time value "str value" must be a date time.'])

    def test_optional_array_date_time_parameter_with_wrong_type_in_array(self):
        from pyxelrest import user_defined_functions
        self.assertEqual(user_defined_functions.json_get_all_optional_parameters_types(
            query_array_date_time=['str value']),
            ['query_array_date_time value "str value" must be a date time.'])


if __name__ == '__main__':
    unittest.main()

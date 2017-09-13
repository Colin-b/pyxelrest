import datetime
import unittest
import platform
from dateutil.tz import tzutc
import testsutils.serviceshandler as serviceshandler
import testsutils.loader as loader


def support_pandas():
    try:
        import pandas
        return True
    except:
        return False


class PyxelRestTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.start_services()
        loader.load('pyxelresttest_services_configuration.ini')

    @classmethod
    def tearDownClass(cls):
        loader.unload()
        serviceshandler.stop_services()

    @classmethod
    def start_services(cls):
        from testsutils import (
            usual_parameters_test_service,
            filtered_tags_test_service,
            values_false_test_service,
            output_order_test_service,
            swagger_parsing_test_service,
            without_parameter_test_service,
            header_parameter_test_service,
            form_parameter_test_service,
            array_parameter_test_service,
            static_file_call_test_service,
            http_methods_test_service,
            content_type_test_service,
        )
        serviceshandler.start_services(
            (usual_parameters_test_service, 8943),
            (filtered_tags_test_service, 8944),
            (values_false_test_service, 8945),
            (output_order_test_service, 8946),
            (swagger_parsing_test_service, 8948),
            (without_parameter_test_service, 8950),
            (header_parameter_test_service, 8951),
            (form_parameter_test_service, 8952),
            (array_parameter_test_service, 8953),
            (static_file_call_test_service, 8954),
            (http_methods_test_service, 8955),
            (content_type_test_service, 8956),
        )

    def test_string_array_parameter(self):
        from pyxelrest import pyxelrestgenerator
        if platform.python_version()[0] == '3':
            result = 'query_array_string="[\'str1\', \'str2\']"'
        else:
            result = u'query_array_string="[u\'str1\', u\'str2\']"'
        self.assertEqual(pyxelrestgenerator.array_parameter_test_get_test_string_array_parameter(['str1', 'str2']),
                         result)

    def test_plain_text_without_parameter(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.without_parameter_test_get_test_plain_text_without_parameter(),
            'string value returned should be truncated so that the following information cannot be seen by'
            ' user, because of the fact that Excel does not allow more than 255 characters in a cell. '
            'Only the 255 characters will be returned by the user defined functions:  '
        )

    def test_post_test_without_parameter(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.without_parameter_test_post_test_without_parameter(),
            'POST performed properly'
        )

    def test_put_test_without_parameter(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.without_parameter_test_put_test_without_parameter(),
            'PUT performed properly'
        )

    def test_delete_test_without_parameter(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.without_parameter_test_delete_test_without_parameter(),
                         'DELETE performed properly')

    def test_get_test_header_parameter(self):
        from pyxelrest import pyxelrestgenerator
        headers = pyxelrestgenerator.header_parameter_test_get_test_header_parameter('sent header')
        header_param_index = headers[0].index('Header-String')
        self.assertEqual(headers[1][header_param_index], 'sent header')

    def test_get_test_header_advanced_configuration(self):
        from pyxelrest import pyxelrestgenerator
        headers = pyxelrestgenerator.header_advanced_configuration_test_get_test_header_parameter('sent header')

        custom_header_index = headers[0].index('X-Pxl-Custom')
        self.assertEqual(headers[1][custom_header_index], 'MyCustomValue')

        other_header_index = headers[0].index('X-Pxl-Other')
        self.assertEqual(headers[1][other_header_index], 'MyOtherValue')

        request_header_index = headers[0].index('X-Pxl-Request')
        self.assertIsNotNone(request_header_index)

        session_header_index = headers[0].index('X-Pxl-Session')
        self.assertRegexpMatches(headers[1][session_header_index], '\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d.\d\d\d\d\d\d')

        user_agent_index = headers[0].index('User-Agent')
        self.assertEqual(headers[1][user_agent_index], 'PyxelRest v0.63')

    def test_post_test_form_parameter(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.form_parameter_test_post_test_form_parameter('sent string form data'),
            [
                ['form_string'],
                ['sent string form data']
            ]
        )

    def test_get_test_with_tags(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'Second tag is one of the accepted tags',
            pyxelrestgenerator.filtered_tags_test_get_test_with_tags()
        )

    def test_post_test_with_tags(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'All tags are accepted',
            pyxelrestgenerator.filtered_tags_test_post_test_with_tags()
        )

    def test_put_test_with_tags(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'First tag is one of the accepted tags',
            pyxelrestgenerator.filtered_tags_test_put_test_with_tags()
        )

    def test_delete_test_with_tags(self):
        from pyxelrest import pyxelrestgenerator
        self.assertFalse(hasattr(pyxelrestgenerator, 'filtered_tags_test_delete_test_with_tags'))

    def test_get_test_with_zero_integer(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['zero_integer'],
                [0]
            ],
            pyxelrestgenerator.values_false_test_get_test_with_zero_integer()
        )

    def test_get_test_with_zero_float(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['zero_float'],
                [0.0]
            ],
            pyxelrestgenerator.values_false_test_get_test_with_zero_float()
        )

    def test_get_test_with_false_boolean(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['false_boolean'],
                [False]
            ],
            pyxelrestgenerator.values_false_test_get_test_with_false_boolean()
        )

    def test_get_test_with_empty_string(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['empty_string'],
                ['']
            ],
            pyxelrestgenerator.values_false_test_get_test_with_empty_string()
        )

    def test_get_test_with_empty_list(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['empty_list'],
                ['']
            ],
            pyxelrestgenerator.values_false_test_get_test_with_empty_list()
        )

    def test_get_test_with_empty_dictionary(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['empty_dictionary'],
                ['']
            ],
            pyxelrestgenerator.values_false_test_get_test_with_empty_dictionary()
        )

    def test_get_test_compare_output_order(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                [u'curve', u'date', u'mat', u'ts'],
                [u'PW_FR', datetime.datetime(2017, 4, 5, 0, 0), u'H01', u''],
                [u'PW_FR', datetime.datetime(2017, 4, 5, 0, 0), u'H02', u'2017-04-05 12:03:15'],
                [u'PW_FR', datetime.datetime(2017, 4, 5, 0, 0), u'H03', u'']
            ],
            pyxelrestgenerator.output_order_test_get_test_price_unordered()
        )

    def test_get_test_date(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                [datetime.datetime(2014, 3, 5, 0, 0)]
            ],
            pyxelrestgenerator.usual_parameters_test_get_test_date()
        )

    def test_get_test_datetime(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
                [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
                [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
                [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
                [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())]
            ],
            pyxelrestgenerator.usual_parameters_test_get_test_date_time()
        )

    def test_get_static_swagger_file(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'success',
            pyxelrestgenerator.swagger_loaded_from_file_test_get_test_static_file_call()
        )

    def test_get_http_method(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'GET',
            pyxelrestgenerator.http_methods_test_get_test_all_http_methods()
        )

    def test_post_http_method(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'POST',
            pyxelrestgenerator.http_methods_test_post_test_all_http_methods()
        )

    def test_put_http_method(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'PUT',
            pyxelrestgenerator.http_methods_test_put_test_all_http_methods()
        )

    def test_delete_http_method(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'DELETE',
            pyxelrestgenerator.http_methods_test_delete_test_all_http_methods()
        )

    def test_patch_http_method(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'PATCH',
            pyxelrestgenerator.http_methods_test_patch_test_all_http_methods()
        )

    def test_options_http_method(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            # OPTIONS is already handled by Flask
            '',
            pyxelrestgenerator.http_methods_test_options_test_all_http_methods()
        )

    def test_head_http_method(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            # HEAD is already handled by Flask
            '',
            pyxelrestgenerator.http_methods_test_head_test_all_http_methods()
        )

    def test_msgpackpandas_content_type(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'application/msgpackpandas' if support_pandas() else '*/*',
            pyxelrestgenerator.content_type_test_get_test_msgpackpandas()
        )

    def test_json_content_type(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'application/json',
            pyxelrestgenerator.content_type_test_get_test_json()
        )

    def test_missing_operation_id(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            '/test/without/operationId called.',
            pyxelrestgenerator.operation_id_not_provided_test_get_test_without_operationId()
        )

    def test_mixed_operation_id(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            '/test/with/operationId called.',
            pyxelrestgenerator.operation_id_not_always_provided_test_get_test_without_operationId()
        )
        self.assertEqual(
            '/test/without/operationId called.',
            pyxelrestgenerator.operation_id_not_always_provided_test_duplicated_get_test_without_operationId()
        )


if __name__ == '__main__':
    unittest.main()

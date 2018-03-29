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
        serviceshandler.stop_services()

    @classmethod
    def start_services(cls):
        from testsutils import (
            usual_parameters_service,
            filtered_tags_service,
            values_false_service,
            output_order_service,
            swagger_parsing_service,
            without_parameter_service,
            header_parameter_service,
            form_parameter_service,
            array_parameter_service,
            static_file_call_service,
            http_methods_service,
            content_type_service,
            base_path_ending_with_slash_service,
            async_service,
        )
        serviceshandler.start_services(
            (usual_parameters_service, 8943),
            (filtered_tags_service, 8944),
            (values_false_service, 8945),
            (output_order_service, 8946),
            (swagger_parsing_service, 8948),
            (without_parameter_service, 8950),
            (header_parameter_service, 8951),
            (form_parameter_service, 8952),
            (array_parameter_service, 8953),
            (static_file_call_service, 8954),
            (http_methods_service, 8955),
            (content_type_service, 8956),
            (base_path_ending_with_slash_service, 8957),
            (async_service, 8958),
        )

    def test_string_array_parameter(self):
        from pyxelrest import pyxelrestgenerator
        if platform.python_version()[0] == '3':
            result = 'string_array="[\'str1\', \'str2\']"'
        else:
            result = u'string_array="[u\'str1\', u\'str2\']"'
        self.assertEqual(pyxelrestgenerator.array_parameter_get_string_array_parameter(['str1', 'str2']),
                         result)

    def test_plain_without_parameter(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.without_parameter_get_plain_text_without_parameter(),
            'string value returned should be truncated so that the following information cannot be seen by'
            ' user, because of the fact that Excel does not allow more than 255 characters in a cell. '
            'Only the 255 characters will be returned by the user defined functions:  '
        )

    def test_post_without_parameter(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.without_parameter_post_without_parameter(),
            'POST performed properly'
        )

    def test_put_without_parameter(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.without_parameter_put_without_parameter(),
            'PUT performed properly'
        )

    def test_delete_without_parameter(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.without_parameter_delete_without_parameter(),
                         'DELETE performed properly')

    def test_service_without_sync_does_not_have_sync(self):
        from pyxelrest import pyxelrestgenerator
        with self.assertRaises(AttributeError) as cm:
            pyxelrestgenerator.sync_without_parameter_delete_without_parameter()
        self.assertEqual(cm.exception.args[0], "module 'pyxelrest.pyxelrestgenerator' has no attribute 'sync_without_parameter_delete_without_parameter'")

    def test_get_header_parameter(self):
        from pyxelrest import pyxelrestgenerator
        headers = pyxelrestgenerator.header_parameter_get_header('sent header')
        header_param_index = headers[0].index('Header-String')
        self.assertEqual(headers[1][header_param_index], 'sent header')

    def test_get_header_parameter_sync(self):
        from pyxelrest import pyxelrestgenerator
        headers = pyxelrestgenerator.sync_header_parameter_get_header('sent header')
        header_param_index = headers[0].index('Header-String')
        self.assertEqual(headers[1][header_param_index], 'sent header')

    def test_service_only_sync_does_not_have_sync_prefix(self):
        from pyxelrest import pyxelrestgenerator
        with self.assertRaises(AttributeError) as cm:
            pyxelrestgenerator.sync_header_advanced_configuration_get_header('sent header')
        self.assertEqual(cm.exception.args[0], "module 'pyxelrest.pyxelrestgenerator' has no attribute 'sync_header_advanced_configuration_get_header'")

    def test_get_header_advanced_configuration(self):
        from pyxelrest import pyxelrestgenerator
        headers = pyxelrestgenerator.header_advanced_configuration_get_header('sent header')

        custom_header_index = headers[0].index('X-Pxl-Custom')
        self.assertEqual(headers[1][custom_header_index], 'MyCustomValue')

        other_header_index = headers[0].index('X-Pxl-Other')
        self.assertEqual(headers[1][other_header_index], 'MyOtherValue')

        request_header_index = headers[0].index('X-Pxl-Request')
        self.assertIsNotNone(request_header_index)

        session_header_index = headers[0].index('X-Pxl-Session')
        self.assertRegexpMatches(headers[1][session_header_index], '\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d.\d\d\d\d\d\d')

        user_agent_index = headers[0].index('User-Agent')
        self.assertEqual(headers[1][user_agent_index], 'PyxelRest v0.66.0')

    def test_post_form_parameter(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.form_parameter_post_form('sent string form data'),
            [
                ['form_string'],
                ['sent string form data']
            ]
        )

    def test_get_with_tags(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'Second tag is one of the accepted tags',
            pyxelrestgenerator.filtered_tags_get_tags()
        )

    def test_post_with_tags(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'All tags are accepted',
            pyxelrestgenerator.filtered_tags_post_tags()
        )

    def test_put_with_tags(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'First tag is one of the accepted tags',
            pyxelrestgenerator.filtered_tags_put_tags()
        )

    def test_delete_with_tags(self):
        from pyxelrest import pyxelrestgenerator
        self.assertFalse(hasattr(pyxelrestgenerator, 'filtered_tags_delete_with_tags'))

    def test_get_with_zero_integer(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['zero_integer'],
                [0]
            ],
            pyxelrestgenerator.values_false_get_with_zero_integer()
        )

    def test_get_with_zero_float(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['zero_float'],
                [0.0]
            ],
            pyxelrestgenerator.values_false_get_with_zero_float()
        )

    def test_get_with_false_boolean(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['false_boolean'],
                [False]
            ],
            pyxelrestgenerator.values_false_get_with_false_boolean()
        )

    def test_get_with_empty_string(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['empty_string'],
                ['']
            ],
            pyxelrestgenerator.values_false_get_with_empty_string()
        )

    def test_get_with_empty_list(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['empty_list'],
                ['']
            ],
            pyxelrestgenerator.values_false_get_with_empty_list()
        )

    def test_get_with_empty_dictionary(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['empty_dictionary'],
                ['']
            ],
            pyxelrestgenerator.values_false_get_with_empty_dictionary()
        )

    def test_get_compare_output_order(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                [u'curve', u'date', u'mat', u'ts'],
                [u'PW_FR', datetime.datetime(2017, 4, 5, 0, 0), u'H01', u''],
                [u'PW_FR', datetime.datetime(2017, 4, 5, 0, 0), u'H02', u'2017-04-05 12:03:15'],
                [u'PW_FR', datetime.datetime(2017, 4, 5, 0, 0), u'H03', u'']
            ],
            pyxelrestgenerator.output_order_get_price_unordered()
        )

    def test_get_date(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                [datetime.datetime(2014, 3, 5, 0, 0)],
                [datetime.datetime(9999, 1, 1, 0, 0)],
                [datetime.datetime(3001, 1, 1, 0, 0)],
            ],
            pyxelrestgenerator.usual_parameters_get_date()
        )

    def test_get_datetime(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
                [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
                [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
                [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
                [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
                [datetime.datetime(9999, 1, 1, 0, 0, 0, 0, tzinfo=tzutc())],
                [datetime.datetime(3001, 1, 1, 8, 0, 0, 0, tzinfo=tzutc())],
            ],
            pyxelrestgenerator.usual_parameters_get_date_time()
        )

    def test_get_datetime_encoding(self):
        from pyxelrest import pyxelrestgenerator
        date_time = datetime.datetime.strptime('2017-09-13T15:20:35', '%Y-%m-%dT%H:%M:%S')
        self.assertEqual('2017-09-13T15:20:35',
            pyxelrestgenerator.usual_parameters_get_date_time_encoding(encoded_date_time=date_time)
        )
        date_time = datetime.datetime.strptime('2017-09-13T15:20', '%Y-%m-%dT%H:%M')
        self.assertEqual('2017-09-13T15:20:00',
            pyxelrestgenerator.usual_parameters_get_date_time_encoding(encoded_date_time=date_time)
        )
        date_time = datetime.datetime.strptime('2017-09-13 15', '%Y-%m-%d %H')
        self.assertEqual('2017-09-13T15:00:00',
            pyxelrestgenerator.usual_parameters_get_date_time_encoding(encoded_date_time=date_time)
        )

    def test_get_static_swagger_file(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'success',
            pyxelrestgenerator.swagger_loaded_from_file_get_static_file_call()
        )

    def test_get_http_method(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'GET',
            pyxelrestgenerator.http_methods_get_http_methods()
        )

    def test_post_http_method(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'POST',
            pyxelrestgenerator.http_methods_post_http_methods()
        )

    def test_put_http_method(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'PUT',
            pyxelrestgenerator.http_methods_put_http_methods()
        )

    def test_delete_http_method(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'DELETE',
            pyxelrestgenerator.http_methods_delete_http_methods()
        )

    def test_patch_http_method(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'PATCH',
            pyxelrestgenerator.http_methods_patch_http_methods()
        )

    def test_options_http_method(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'OPTIONS',
            pyxelrestgenerator.http_methods_options_http_methods()
        )

    def test_head_http_method(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            # HEAD is already handled by Flask
            '',
            pyxelrestgenerator.http_methods_head_http_methods()
        )

    def test_msgpackpandas_content_type(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'application/msgpackpandas' if support_pandas() else '*/*',
            pyxelrestgenerator.content_type_get_msgpackpandas()
        )

    def test_json_content_type(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'application/json',
            pyxelrestgenerator.content_type_get_json()
        )

    def test_missing_operation_id(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            '/without_operationId called.',
            pyxelrestgenerator.operation_id_not_provided_get_without_operationId()
        )

    def test_mixed_operation_id(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            '/with_operationId called.',
            pyxelrestgenerator.operation_id_not_always_provided_get_without_operationId()
        )
        self.assertEqual(
            '/without_operationId called.',
            pyxelrestgenerator.operation_id_not_always_provided_duplicated_get_without_operationId()
        )

    def test_get_base_path_ending_with_slash(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'http://localhost:8957/method',
            pyxelrestgenerator.base_path_ending_with_slash_get_method()
        )

    def test_post_base_path_ending_with_slash(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'http://localhost:8957/method',
            pyxelrestgenerator.base_path_ending_with_slash_post_method()
        )

    def test_put_base_path_ending_with_slash(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'http://localhost:8957/method',
            pyxelrestgenerator.base_path_ending_with_slash_put_method()
        )

    def test_delete_base_path_ending_with_slash(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            'http://localhost:8957/method',
            pyxelrestgenerator.base_path_ending_with_slash_delete_method()
        )

    def test_get_async_url(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [['Status URL'], ['http://localhost:8958/async/status']],
            pyxelrestgenerator.async_get_async()
        )

    def test_get_custom_url_sync(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['X-Custom-Header1', 'X-Custom-Header2'],
                ['custom1', 'custom2']
            ],
            pyxelrestgenerator.sync_pyxelrest_get_url(
                'http://localhost:8958/async/status',
                extra_headers=[
                    ['X-Custom-Header1', 'custom1'],
                    ['X-Custom-Header2', 'custom2'],
                ],
            )
        )

    def test_get_custom_url(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['X-Custom-Header1', 'X-Custom-Header2'],
                ['custom1', 'custom2']
            ],
            pyxelrestgenerator.pyxelrest_get_url(
                'http://localhost:8958/async/status',
                extra_headers=[
                    ['X-Custom-Header1', 'custom1'],
                    ['X-Custom-Header2', 'custom2'],
                ],
            )
        )

    def test_delete_custom_url_sync(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['X-Custom-Header1', 'X-Custom-Header2'],
                ['custom1', 'custom2']
            ],
            pyxelrestgenerator.sync_pyxelrest_delete_url(
                'http://localhost:8958/unlisted',
                extra_headers=[
                    ['X-Custom-Header1', 'custom1'],
                    ['X-Custom-Header2', 'custom2'],
                ],
            )
        )

    def test_delete_custom_url(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['X-Custom-Header1', 'X-Custom-Header2'],
                ['custom1', 'custom2']
            ],
            pyxelrestgenerator.pyxelrest_delete_url(
                'http://localhost:8958/unlisted',
                extra_headers=[
                    ['X-Custom-Header1', 'custom1'],
                    ['X-Custom-Header2', 'custom2'],
                ],
            )
        )

    def test_post_custom_url_dict(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['key1', 'key2', 'key3'],
                ['value1', 1, 'value3'],
            ],
            pyxelrestgenerator.pyxelrest_post_url(
                'http://localhost:8958/dict',
                [
                    ['key1', 'key2', 'key3'],
                    ['value1', 1, 'value3'],
                ],
                extra_headers=[
                    ['Content-Type', 'application/json'],
                ],
                parse_body_as='dict',
            )
        )

    def test_post_custom_url_dict_list_sync(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['key1', 'key2', 'key3'],
                ['value1', 1, 'value3'],
                ['other1', 2, 'other3'],
            ],
            pyxelrestgenerator.sync_pyxelrest_post_url(
                'http://localhost:8958/dict',
                [
                    ['key1', 'key2', 'key3'],
                    ['value1', 1, 'value3'],
                    ['other1', 2, 'other3'],
                ],
                extra_headers=[
                    ['Content-Type', 'application/json'],
                ],
                parse_body_as='dict_list',
            )
        )

    def test_post_custom_url_dict_list(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['key1', 'key2', 'key3'],
                ['value1', 1, 'value3'],
                ['other1', 2, 'other3'],
            ],
            pyxelrestgenerator.pyxelrest_post_url(
                'http://localhost:8958/dict',
                [
                    ['key1', 'key2', 'key3'],
                    ['value1', 1, 'value3'],
                    ['other1', 2, 'other3'],
                ],
                extra_headers=[
                    ['Content-Type', 'application/json'],
                ],
                parse_body_as='dict_list',
            )
        )

    def test_put_custom_url_dict_list(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['key1', 'key2', 'key3'],
                ['value1', 1, 'value3'],
                ['other1', 2, 'other3'],
            ],
            pyxelrestgenerator.pyxelrest_put_url(
                'http://localhost:8958/dict',
                [
                    ['key1', 'key2', 'key3'],
                    ['value1', 1, 'value3'],
                    ['other1', 2, 'other3'],
                ],
                extra_headers=[
                    ['Content-Type', 'application/json'],
                ],
                parse_body_as='dict_list',
            )
        )

    def test_put_custom_url_dict(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['key1', 'key2', 'key3'],
                ['value1', 1, 'value3'],
            ],
            pyxelrestgenerator.pyxelrest_put_url(
                'http://localhost:8958/dict',
                [
                    ['key1', 'key2', 'key3'],
                    ['value1', 1, 'value3'],
                ],
                extra_headers=[
                    ['Content-Type', 'application/json'],
                ],
                parse_body_as='dict',
            )
        )

    def test_put_custom_url_dict_sync(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['key1', 'key2', 'key3'],
                ['value1', 1, 'value3'],
            ],
            pyxelrestgenerator.sync_pyxelrest_put_url(
                'http://localhost:8958/dict',
                [
                    ['key1', 'key2', 'key3'],
                    ['value1', 1, 'value3'],
                ],
                extra_headers=[
                    ['Content-Type', 'application/json'],
                ],
                parse_body_as='dict',
            )
        )


if __name__ == '__main__':
    unittest.main()

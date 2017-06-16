import datetime
import unittest
import platform
from dateutil.tz import tzutc
import testsutils.serviceshandler as serviceshandler
import testsutils.loader as loader


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
            without_parameter_test_service,
            header_parameter_test_service,
            form_parameter_test_service,
            array_parameter_test_service,
            static_file_call_test_service
        )
        serviceshandler.start_services(
            (usual_parameters_test_service, 8943),
            (filtered_tags_test_service, 8944),
            (values_false_test_service, 8945),
            (output_order_test_service, 8946),
            (without_parameter_test_service, 8950),
            (header_parameter_test_service, 8951),
            (form_parameter_test_service, 8952),
            (array_parameter_test_service, 8953),
            (static_file_call_test_service, 8954)
        )

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
        self.assertEqual(
            pyxelrestgenerator.without_parameter_test_get_test_plain_text_without_parameter(),
            'string value returned should be truncated so that the following information cannot be seen by'
            ' user, because of the fact that Excel does not allow more than 255 characters in a cell. '
            'Only the 255 characters will be returned by the user defined functions:  '
        )

    def test_post_test_without_parameter(self):
        import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.without_parameter_test_post_test_without_parameter(),
            'POST performed properly'
        )

    def test_put_test_without_parameter(self):
        import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.without_parameter_test_put_test_without_parameter(),
            'PUT performed properly'
        )

    def test_delete_test_without_parameter(self):
        import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.without_parameter_test_delete_test_without_parameter(),
                         'DELETE performed properly')

    def test_get_test_header_parameter(self):
        import pyxelrestgenerator
        headers = pyxelrestgenerator.header_parameter_test_get_test_header_parameter('sent header')
        header_param_index = headers[0].index('Header-String')
        self.assertEqual(headers[1][header_param_index], 'sent header')

    def test_post_test_form_parameter(self):
        import pyxelrestgenerator
        self.assertEqual(
            pyxelrestgenerator.form_parameter_test_post_test_form_parameter('sent string form data'),
            [
                ['form_string'],
                ['sent string form data']
            ]
        )

    def test_get_test_with_tags(self):
        import pyxelrestgenerator
        self.assertEqual(
            'Second tag is one of the accepted tags',
            pyxelrestgenerator.filtered_tags_test_get_test_with_tags()
        )

    def test_post_test_with_tags(self):
        import pyxelrestgenerator
        self.assertEqual(
            'All tags are accepted',
            pyxelrestgenerator.filtered_tags_test_post_test_with_tags()
        )

    def test_put_test_with_tags(self):
        import pyxelrestgenerator
        self.assertEqual(
            'First tag is one of the accepted tags',
            pyxelrestgenerator.filtered_tags_test_put_test_with_tags()
        )

    def test_delete_test_with_tags(self):
        import pyxelrestgenerator
        self.assertFalse(hasattr(pyxelrestgenerator, 'filtered_tags_test_delete_test_with_tags'))

    def test_get_test_with_zero_integer(self):
        import pyxelrestgenerator
        self.assertEqual(
            [
                ['zero_integer'],
                [0]
            ],
            pyxelrestgenerator.values_false_test_get_test_with_zero_integer()
        )

    def test_get_test_with_zero_float(self):
        import pyxelrestgenerator
        self.assertEqual(
            [
                ['zero_float'],
                [0.0]
            ],
            pyxelrestgenerator.values_false_test_get_test_with_zero_float()
        )

    def test_get_test_with_false_boolean(self):
        import pyxelrestgenerator
        self.assertEqual(
            [
                ['false_boolean'],
                [False]
            ],
            pyxelrestgenerator.values_false_test_get_test_with_false_boolean()
        )

    def test_get_test_with_empty_string(self):
        import pyxelrestgenerator
        self.assertEqual(
            [
                ['empty_string'],
                ['']
            ],
            pyxelrestgenerator.values_false_test_get_test_with_empty_string()
        )

    def test_get_test_with_empty_list(self):
        import pyxelrestgenerator
        self.assertEqual(
            [
                ['empty_list'],
                ['']
            ],
            pyxelrestgenerator.values_false_test_get_test_with_empty_list()
        )

    def test_get_test_with_empty_dictionary(self):
        import pyxelrestgenerator
        self.assertEqual(
            [
                ['empty_dictionary'],
                ['']
            ],
            pyxelrestgenerator.values_false_test_get_test_with_empty_dictionary()
        )

    def test_get_test_compare_output_order(self):
        import pyxelrestgenerator
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
        import pyxelrestgenerator
        self.assertEqual(
            [
                [datetime.datetime(2014, 3, 5, 0, 0)]
            ],
            pyxelrestgenerator.usual_parameters_test_get_test_date()
        )

    def test_get_test_datetime(self):
        import pyxelrestgenerator
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
        import pyxelrestgenerator
        self.assertEqual(
            'success',
            pyxelrestgenerator.swagger_loaded_from_file_test_get_test_static_file_call()
        )

if __name__ == '__main__':
    unittest.main()

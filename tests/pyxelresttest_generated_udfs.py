import os
import os.path
import unittest
import testsutils.serviceshandler as serviceshandler
import testsutils.loader as loader
import sys


def support_pandas():
    try:
        import pandas
        return True
    except:
        return False


class PyxelRestUdfsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.start_services()
        loader.load('pyxelresttest_generated_udfs_services_configuration.ini')

    @classmethod
    def tearDownClass(cls):
        loader.unload()
        serviceshandler.stop_services()

    @classmethod
    def start_services(cls):
        import testsutils.usual_parameters_test_service as usual_parameters_test_service
        import testsutils.filtered_tags_test_service as filtered_tags_test_service
        import testsutils.values_false_test_service as values_false_test_service
        import testsutils.output_order_test_service as output_order_test_service
        import testsutils.nested_data_test_service as nested_data_test_service
        import testsutils.swagger_parsing_test_service as swagger_parsing_test_service
        import testsutils.vba_keywords_test_service as vba_keywords_test_service
        import testsutils.without_parameter_test_service as without_parameter_test_service
        import testsutils.header_parameter_test_service as header_parameter_test_service
        import testsutils.form_parameter_test_service as form_parameter_test_service
        import testsutils.array_parameter_test_service as array_parameter_test_service
        import testsutils.json_test_service as json_test_service
        import testsutils.plain_text_test_service as plain_text_test_service
        import testsutils.octet_stream_test_service as octet_stream_test_service
        serviceshandler.start_services((usual_parameters_test_service, 8943),
                                       (filtered_tags_test_service, 8944),
                                       (values_false_test_service, 8945),
                                       (output_order_test_service, 8946),
                                       (nested_data_test_service, 8947),
                                       (swagger_parsing_test_service, 8948),
                                       (vba_keywords_test_service, 8949),
                                       (without_parameter_test_service, 8950),
                                       (header_parameter_test_service, 8951),
                                       (form_parameter_test_service, 8952),
                                       (array_parameter_test_service, 8953),
                                       (json_test_service, 8954),
                                       (plain_text_test_service, 8955),
                                       (octet_stream_test_service, 8956))

    def test_generated_file(self):
        """
        Assert content of generated file.
        This test is mainly here to be aware that a change broke generated file.
        """
        if sys.version_info[0] == 2:
            filename = 'user_defined_functions_python27_pandas.py' if support_pandas() else 'user_defined_functions_python27.py'
        else:
            filename = 'user_defined_functions_python36_pandas.py' if support_pandas() else 'user_defined_functions_python36.py'
        expected_file = open(os.path.join(os.path.dirname(__file__), '..', 'testsutils', filename), 'r')
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

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


def support_pandas():
    try:
        import pandas
        return True
    except:
        return False


class PyxelRestUdfsTest(unittest.TestCase):
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
        import testsutils.usual_parameters_test_service as usual_parameters_test_service
        cls.service_processes.append(
            multiprocessing.Process(target=usual_parameters_test_service.start_server, args=(8943,)))
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
        import testsutils.json_test_service as json_test_service
        cls.service_processes.append(
            multiprocessing.Process(target=json_test_service.start_server, args=(8954,)))
        import testsutils.plain_text_test_service as plain_text_test_service
        cls.service_processes.append(
            multiprocessing.Process(target=plain_text_test_service.start_server, args=(8955,)))
        import testsutils.octet_stream_test_service as octet_stream_test_service
        cls.service_processes.append(
            multiprocessing.Process(target=octet_stream_test_service.start_server, args=(8956,)))
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
        shutil.copyfile(os.path.join(this_dir, 'pyxelresttest_generated_udfs_services_configuration.ini'),
                        cls.services_config_file_path)

    @classmethod
    def _add_back_initial_config(cls):
        shutil.move(cls.backup_services_config_file_path, cls.services_config_file_path)

    def test_generated_file(self):
        """
        Assert content of generated file.
        This test is mainly here to be aware that a change broke generated file.
        """
        # TODO Also handle the difference when tests are run using python 2.7
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

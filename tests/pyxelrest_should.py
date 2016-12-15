import unittest
import os
import shutil


# Test cases requires test_service to run prior to execution
class PyxelRestShould(unittest.TestCase):
    def setUp(self):
        self.add_config()
        import pyxelrest

    def tearDown(self):
        self.add_back_initial_config()

    def test_server(self):
        expected_file = open(os.path.join(os.path.dirname(__file__),
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

    def add_config(self):
        config_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'pixelrest_config.ini')
        self.backup_config_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'pixelrest_config.ini.back')
        shutil.copyfile(config_file_path, self.backup_config_file_path)
        shutil.copyfile('test_config.ini', config_file_path)

    def add_back_initial_config(self):
        config_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'pixelrest_config.ini')
        shutil.move(self.backup_config_file_path, config_file_path)

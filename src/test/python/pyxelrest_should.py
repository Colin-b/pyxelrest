import unittest
import os


# Test cases requires test_service to run prior to execution
class PyxelRestShould(unittest.TestCase):
    def setUp(self):
        import pyxelrest

    def test_server(self):
        expected_file = open(os.path.join(os.path.dirname(__file__),
                                          'test_service_user_defined_functions.py'), 'r')
        expected = expected_file.readlines()
        expected_file.close()
        actual_file = open(os.path.join(os.path.dirname(__file__),
                                        '..\..\main\python\pyxelrest\user_defined_functions.py'), 'r')
        actual = actual_file.readlines()
        actual_file.close()
        self.assertEqual(actual[:3], expected[:3])
        self.assertRegexpMatches(actual[3], expected[3])
        # PyCharm may rstrip lines without asking...
        self.assertEqual([line.rstrip() for line in actual[4:]], [line.rstrip() for line in expected[4:]])

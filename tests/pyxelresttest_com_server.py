import os
import unittest
import win32com.server.exception
from pyxelrest import (
    com_server,
    alert
)


def my_function(arg1, arg2):
    return '{0} {1}'.format(arg1, arg2)


def my_function_process(arg1, arg2, other_arg):
    alert.HIDE_MESSAGE_BOX = True
    return my_function(arg1, arg2, other_arg)


class PyxelRestTestComServer(unittest.TestCase):
    srv = com_server.PythonServer()

    def test_direct(self):
        self.srv.add_path(os.path.dirname(__file__))
        res = self.srv.direct_call('pyxelresttest_com_server', 'my_function', 'arg', 0)
        self.assertEqual(res, 'arg 0')

    def test_direct_module_not_existing(self):
        alert.HIDE_MESSAGE_BOX = True
        with self.assertRaises(win32com.server.exception.COMException):
            self.srv.direct_call('module_not_existing', 'my_function', 'arg', 0)

    def test_direct_function_not_existing(self):
        alert.HIDE_MESSAGE_BOX = True
        self.srv.add_path(os.path.dirname(__file__))
        with self.assertRaises(win32com.server.exception.COMException):
            self.srv.direct_call('pyxelresttest_com_server', 'function_not_existing', 'arg', 0)

    def test_direct_parameter_not_existing(self):
        alert.HIDE_MESSAGE_BOX = True
        self.srv.add_path(os.path.dirname(__file__))
        with self.assertRaises(win32com.server.exception.COMException):
            self.srv.direct_call('pyxelresttest_com_server', 'my_function', 'arg', 0, 'parameter_not_existing')

    def test_thread(self):
        self.srv.add_path(os.path.dirname(__file__))
        self.srv.thread_call('a', 'pyxelresttest_com_server', 'my_function', 'arg', 0)
        res = self.srv.result('a')
        self.assertEqual(res, 'arg 0')

    def test_thread_module_not_existing(self):
        alert.HIDE_MESSAGE_BOX = True
        try:
            self.srv.thread_call('a', 'module_not_existing', 'my_function', 'arg', 0)
            self.fail('An error should be raised in case module is not existing.')
        except Exception as e:
            self.assertEqual(str(e), "(None, \"No module named 'module_not_existing'\", None, -1)")

    def test_thread_function_not_existing(self):
        alert.HIDE_MESSAGE_BOX = True
        self.srv.add_path(os.path.dirname(__file__))
        try:
            self.srv.thread_call('a', 'pyxelresttest_com_server', 'function_not_existing', 'arg', 0)
            self.fail('An error should be raised in case function is not existing.')
        except Exception as e:
            self.assertEqual(str(e), "(None, \"module 'pyxelresttest_com_server' has no attribute 'function_not_existing'\", None, -1)")

    def test_thread_parameter_not_existing(self):
        alert.HIDE_MESSAGE_BOX = True
        self.srv.add_path(os.path.dirname(__file__))
        self.srv.thread_call('a', 'pyxelresttest_com_server', 'my_function', 'arg', 0, 'parameter_not_existing')
        try:
            self.srv.result('a')
            self.fail('An error should be raised in case parameter is not existing.')
        except Exception as e:
            self.assertEqual(str(e), "(0, 'my_function() takes 2 positional arguments but 3 were given', None, -1)")

    def test_process(self):
        self.srv.add_path(os.path.dirname(__file__))
        self.srv.process_call('a', 'pyxelresttest_com_server', 'my_function', 'arg', 0)
        res = self.srv.result('a')
        self.assertEqual(res, 'arg 0')

    def test_process_module_not_existing(self):
        alert.HIDE_MESSAGE_BOX = True
        try:
            self.srv.process_call('a', 'module_not_existing', 'my_function', 'arg', 0)
            self.fail('An error should be raised in case module is not existing.')
        except Exception as e:
            self.assertEqual(str(e), "(None, \"No module named 'module_not_existing'\", None, -1)")

    def test_process_function_not_existing(self):
        alert.HIDE_MESSAGE_BOX = True
        self.srv.add_path(os.path.dirname(__file__))
        try:
            self.srv.process_call('a', 'pyxelresttest_com_server', 'function_not_existing', 'arg', 0)
            self.fail('An error should be raised in case function is not existing.')
        except Exception as e:
            self.assertEqual(str(e), "(None, \"module 'pyxelresttest_com_server' has no attribute 'function_not_existing'\", None, -1)")

    def test_process_parameter_not_existing(self):
        alert.HIDE_MESSAGE_BOX = True
        self.srv.add_path(os.path.dirname(__file__))
        self.srv.process_call('a', 'pyxelresttest_com_server', 'my_function_process', 'arg', 0, 'parameter_not_existing')
        try:
            self.srv.result('a')
            self.fail('An error should be raised in case parameter is not existing.')
        except Exception as e:
            self.assertEqual(str(e), "(0, 'my_function() takes 2 positional arguments but 3 were given', None, -1)")


if __name__ == '__main__':
    unittest.main()

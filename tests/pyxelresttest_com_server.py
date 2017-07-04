import os
import unittest
from pyxelrest import com_server


def my_function(arg1, arg2):
    return '{0} {1}'.format(arg1, arg2)


class PyxelRestTestComServer(unittest.TestCase):
    srv = com_server.PythonServer()

    def test_direct(self):
        self.srv.add_path(os.path.dirname(__file__))
        res = self.srv.direct_call('pyxelresttest_com_server', 'my_function', 'arg', 0)
        self.assertEqual(res, 'arg 0')

    def test_thread(self):
        self.srv.add_path(os.path.dirname(__file__))
        self.srv.thread_call('a', 'pyxelresttest_com_server', 'my_function', 'arg', 0)
        res = self.srv.result('a')
        self.assertEqual(res, 'arg 0')

    def test_process(self):
        self.srv.add_path(os.path.dirname(__file__))
        self.srv.process_call('a', 'pyxelresttest_com_server', 'my_function', 'arg', 0)
        res = self.srv.result('a')
        self.assertEqual(res, 'arg 0')


if __name__ == '__main__':
    unittest.main()

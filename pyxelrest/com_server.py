import multiprocessing
import sys
import threading
import logging
from pyxelrest import custom_logging, gui

if sys.version_info.major > 2:
    # Python 3
    from importlib import util
else:
    # Python 2
    from imp import load_source


class PythonServer:
    """
    The Python Server COM object allows direct communication between VB and python without
    starting the python command line. Keeping data between two calls.
    """

    _reg_clsid_ = '{38CB8241-D698-11D2-B806-0060974AB8A9}'
    _reg_progid_ = 'pyxelrest.PythonServer'
    _public_methods_ = ['import_file', 'direct_call', 'thread_call', 'process_call', 'running', 'result']

    modules = {}
    module_paths = {}
    threads = {}
    results = {}

    def __init__(self):
        from pyxelrest import pyxelrestgenerator
        pass

    def import_file(self, module_name, file_name):
        """
        Load a python file as a module
        :param module_name: name used
        :param file_name: full path to the python file
        """
        try:
            if sys.version_info.major > 2:
                spec = util.spec_from_file_location(module_name, file_name)
                m = util.module_from_spec(spec)
                spec.loader.exec_module(m)
            else:
                m = load_source(module_name, file_name)
            self.module_paths[module_name] = file_name
            self.modules[module_name] = m
        except Exception as e:
            logging.exception("Logging an uncaught exception")
            gui.message_box("Python Error", str(e))

    def direct_call(self, module_name, func_name, *args):
        """
        Synchronous call toa function
        :param module_name: module of the function
        :param func_name: name of the function
        :param args: arguments of the function
        :return: the result of the function
        """
        try:
            if module_name not in self.modules:
                raise Exception('module {0} not found'.format(module_name))
            m = self.modules[module_name]
            f = getattr(m, func_name)
            return f(*args)
        except Exception as e:
            logging.exception("Logging an uncaught exception")
            gui.message_box("Python Error", str(e))
            return str(e)

    def call2(self, call_name, func, *args):
        try:
            self.results[call_name] = func(*args)
        except Exception as e:
            logging.exception("Logging an uncaught exception")
            self.results[call_name] = str(e)
            gui.message_box("Python Error", str(e))

    def call3(self, queue, file_name, module_name, func_name, *args):
        self.import_file(module_name, file_name)
        res = self.direct_call(module_name, func_name, *args)
        queue.put(res)

    def thread_call(self, call_name, module_name, func_name, *args):
        """
        Asynchronous call to a function
        :param call_name: name of the call
        :param module_name: module of the function
        :param func_name: Name of the function
        :param args: Arguments of the function
        """
        if call_name in self.threads:
            p = self.threads[call_name]
            if p.is_alive():
                return False
        try:
            if module_name not in self.modules:
                raise Exception('module {0} not found'.format(module_name))
            m = self.modules[module_name]
            f = getattr(m, func_name)
            p = threading.Thread(target=self.call2, args=(call_name, f, *args))
            self.threads[call_name] = p
            p.start()
            return True
        except Exception as e:
            logging.exception("Bad call")
            gui.message_box("Python Error", str(e))
            return False

    def process_call(self, call_name, module_name, func_name, *args):
        """
        Asynchronous call to a function using a process
        :param call_name: name of the call
        :param module_name: module of the function
        :param func_name: Name of the function
        :param args: Arguments of the function
        """
        if call_name in self.threads:
            p = self.threads[call_name]
            if p.is_alive():
                return False
        try:
            if module_name not in self.modules:
                raise Exception('module {0} not found'.format(module_name))
            m = self.modules[module_name]
            # check that the function exists
            f = getattr(m, func_name)
            q = multiprocessing.Queue()
            p = multiprocessing.Process(target=self.call3, args=(q, self.module_paths[module_name], module_name,
                                                                 func_name, *args))
            self.results[call_name] = q
            self.threads[call_name] = p
            p.start()
            return True
        except Exception as e:
            logging.exception("Bad call")
            gui.message_box("Python Error", str(e))
            return False

    def running(self, call_name):
        """
        Check if an asynchronous call is still running
        :param call_name: name of the call
        :return: whether the call is still running
        """
        if call_name in self.threads:
            p = self.threads[call_name]
            if p.is_alive():
                return True
        return False

    def result(self, call_name, timeout=60):
        """
        Gives the result back for an asynchronous call
        :param call_name: name of the call
        :param timeout: timeout in second
        :return: the result or None
        """
        res = None
        if call_name in self.threads:
            p = self.threads[call_name]
            if p.is_alive() and timeout > 0:
                p.join(timeout)
            if not p.is_alive():
                res = self.results[call_name]
                if type(res) is multiprocessing.Queue:
                    res = res.get()
                del self.results[call_name]
                del self.threads[call_name]
        return res

if __name__ == '__main__':
    import win32com.server.register
    win32com.server.register.UseCommandLine(PythonServer)

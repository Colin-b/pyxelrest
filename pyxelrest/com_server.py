import multiprocessing
import sys
import threading
import logging

import pythoncom

from pyxelrest import custom_logging, alert


class PythonServer:
    """
    The Python Server COM object allows direct communication between VB and python without
    starting the python command line. Keeping data between two calls.
    """

    _reg_clsid_ = '{38CB8241-D698-11D2-B806-0060974AB8A9}'
    _reg_progid_ = 'pyxelrest.PythonServer'
    _public_methods_ = ['add_path', 'import_module', 'generate_udf', 'direct_call', 'thread_call', 'process_call',
                        'running', 'result', 'set_syslog', 'set_level', 'init_disk_cache', 'init_memory_cache']

    threads = {}
    results = {}
    sources = []
    host = None
    port = None

    def __init__(self):
        custom_logging.set_pid_file_logger(logging.DEBUG)
        sys.stdout = custom_logging.StreamToLogger(logging, logging.INFO)
        sys.stderr = custom_logging.StreamToLogger(logging, logging.ERROR)
        pass

    def generate_udf(self):
        from pyxelrest import pyxelrestgenerator
        pyxelrestgenerator.generate_user_defined_functions()

    def set_syslog(self, host, port, level="INFO"):
        self.host = host
        self.port = port
        custom_logging.set_syslog_logger(host, port, logging.getLevelName(level))

    def set_level(self, level):
        logging.getLogger().setLevel(logging.getLevelName(level))

    def init_disk_cache(self, filename):
        import pyxelrest.caching
        pyxelrest.caching.init_disk_cache(filename)

    def init_memory_cache(self, size, ttl):
        import pyxelrest.caching
        pyxelrest.caching.init_memory_cache(size, ttl)

    def add_path(self, path):
        """
        Extend PYTHONPATH
        :param path: path to add
        """
        sys.path.append(path)
        self.sources.append(path)

    def direct_call(self, module_name, func_name, *args):
        """
        Synchronous call toa function
        :param module_name: module of the function
        :param func_name: name of the function
        :param args: arguments of the function
        :return: the result of the function
        """
        try:
            if module_name not in sys.modules:
                __import__(module_name)
            m = sys.modules[module_name]
            f = getattr(m, func_name)
            return f(*args)
        except Exception as e:
            logging.exception("Logging an uncaught exception")
            alert.message_box("Python Error", str(e))
            return str(e)

    def thread_call2(self, call_name, func, *args):
        try:
            pythoncom.CoInitialize()
            import xlwings
            self.results[call_name] = func(*args)
        except Exception as e:
            logging.exception("Logging an uncaught exception")
            self.results[call_name] = str(e)
            alert.message_box("Python Error", str(e))
        finally:
            pythoncom.CoUninitialize()

    def process_call2(self, queue, sources, module_name, func_name, *args):
        sys.path.extend(sources)
        pythoncom.CoInitialize()
        if self.host is None:
            custom_logging.set_pid_file_logger()
        else:
            custom_logging.set_syslog_logger(self.host, self.port)
        sys.stdout = custom_logging.StreamToLogger(logging, logging.INFO)
        sys.stderr = custom_logging.StreamToLogger(logging, logging.ERROR)
        res = self.direct_call(module_name, func_name, *args)
        queue.put(res)
        pythoncom.CoUninitialize()

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
            if module_name not in sys.modules:
                __import__(module_name)
            m = sys.modules[module_name]
            f = getattr(m, func_name)
            p = threading.Thread(target=self.thread_call2, args=(call_name, f, *args))
            self.threads[call_name] = p
            p.start()
            return True
        except Exception as e:
            logging.exception("Bad call")
            alert.message_box("Python Error", str(e))
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
            if module_name not in sys.modules:
                __import__(module_name)
            m = sys.modules[module_name]
            # check that the function exists
            f = getattr(m, func_name)
            q = multiprocessing.Queue()
            p = multiprocessing.Process(target=self.process_call2, args=(q, self.sources, module_name, func_name, *args))
            self.results[call_name] = q
            self.threads[call_name] = p
            p.start()
            return True
        except Exception as e:
            logging.exception("Bad call")
            alert.message_box("Python Error", str(e))
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
        Gives the result back for an asynchronous call and waits if necessary
        :param call_name: name of the call
        :param timeout: timeout in second, 0 means no blocking call
        :return: the result or None
        """
        res = None
        if call_name in self.threads:
            p = self.threads[call_name]
            if p.is_alive() and timeout > 0:
                p.join(timeout)
            if not p.is_alive():
                res = self.results[call_name]
                if type(p) is multiprocessing.Process:
                    res = res.get()
                del self.results[call_name]
                del self.threads[call_name]
        return res


def register_com():
    # Make the installation local to the user without admin rights
    import win32api
    import win32con
    default_base = win32api.RegCreateKey(win32con.HKEY_CURRENT_USER, "Software\\Classes")
    win32api.RegOverridePredefKey(win32con.HKEY_CLASSES_ROOT, default_base)

    import win32com.server.register
    win32com.server.register.UseCommandLine(PythonServer)

    win32api.RegOverridePredefKey(win32con.HKEY_CLASSES_ROOT, None)
    win32api.RegCloseKey(default_base)

if __name__ == '__main__':
    register_com()

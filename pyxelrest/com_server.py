import multiprocessing
import os
import sys
import threading
import logging

import pythoncom
import xlwings
from win32com.server.exception import COMException

from pyxelrest import custom_logging, alert, pyxelresterrors


class PythonServer:
    """
    The Python Server COM object allows direct communication between VB and python without
    starting the python command line. Keeping data between two calls.
    """

    _reg_clsid_ = '{AC87AC53-2291-4155-8505-37FE4BFEBDC3}'
    _reg_progid_ = 'pyxelrest.PythonServer'
    _public_methods_ = ['add_path', 'import_module', 'generate_udf', 'direct_call', 'thread_call', 'process_call',
                        'running', 'result', 'set_syslog', 'set_level', 'init_disk_cache', 'init_memory_cache',
                        'clear_cache', 'install_module', 'get_running_calls', 'get_finished_calls']

    threads = {}
    results = {}
    sources = []
    syslog_host = None
    syslog_port = None
    syslog_level = None
    filelog_level = logging.DEBUG
    disk_cache = None

    def __init__(self):
        custom_logging.set_file_logger('comserver-' + str(os.getpid()), self.filelog_level)
        sys.stdout = custom_logging.StreamToLogger(logging, logging.INFO)
        sys.stderr = custom_logging.StreamToLogger(logging, logging.ERROR)
        pass

    def generate_udf(self):
        from pyxelrest import pyxelrestgenerator
        pyxelrestgenerator.generate_user_defined_functions()

    def set_syslog(self, host, port, level="INFO"):
        self.syslog_host = host
        self.syslog_port = port
        self.syslog_level = level
        custom_logging.set_syslog_logger(host, port, logging.getLevelName(level))

    def set_level(self, level):
        logging.getLogger().setLevel(logging.getLevelName(level))

    def init_disk_cache(self, filename):
        import pyxelrest.caching
        self.disk_cache = filename
        pyxelrest.caching.init_disk_cache(filename)

    def clear_cache(self):
        import pyxelrest.caching
        pyxelrest.caching.clear_cache()

    def init_memory_cache(self, size, ttl):
        import pyxelrest.caching
        pyxelrest.caching.init_memory_cache(size, ttl)

    def add_path(self, path):
        """
        Extend PYTHONPATH
        :param path: path to add
        """
        if path not in self.sources:
            sys.path.append(path)
            self.sources.append(path)

    def install_module(self, module_name, module_ver=None):
        try:
            if module_name not in sys.modules:
                __import__(module_name)
        except ImportError:
            try:
                import pip
                pip.main(['install', module_name if module_ver is None else module_name + '>=' + module_ver])
                __import__(module_name)
            except Exception as e:
                msg = "Cannot import module {}".format(module_name)
                logging.exception(msg)
                alert.message_box("Python Error", msg)
                raise COMException(msg)

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
        except COMException as e:
            raise e
        except Exception as e:
            msg, code = pyxelresterrors.extract_error(e)
            logging.exception(msg)
            alert.message_box("Python Error", msg)
            raise COMException(desc=msg, hresult=code)

    def _thread_call_within_thread(self, call_name, func, *args):
        try:
            pythoncom.CoInitialize()
            self.results[call_name] = func(*args)
        except COMException as e:
            self.results[call_name] = e
        except Exception as e:
            msg, code = pyxelresterrors.extract_error(e)
            logging.exception(msg)
            self.results[call_name] = e
            alert.message_box("Python Error", msg)
        finally:
            pythoncom.CoUninitialize()

    def _process_call_within_process(self, queue, sources, module_name, func_name, *args):
        sys.path.extend(sources)
        pythoncom.CoInitialize()
        custom_logging.set_file_logger('com_server-' + str(os.getpid()), self.filelog_level)
        if self.syslog_host is not None:
            custom_logging.set_syslog_logger(self.syslog_host, self.syslog_port, self.syslog_level)
        if self.disk_cache is not None:
            from pyxelrest import caching
            caching.init_disk_cache(self.disk_cache + '-' + os.getpid())
        sys.stdout = custom_logging.StreamToLogger(logging, logging.INFO)
        sys.stderr = custom_logging.StreamToLogger(logging, logging.ERROR)
        try:
            if module_name not in sys.modules:
                __import__(module_name)
            m = sys.modules[module_name]
            f = getattr(m, func_name)
            queue.put(f(*args))
        except COMException as e:
            queue.put(e)
        except Exception as e:
            msg, code = pyxelresterrors.extract_error(e)
            logging.exception(msg)
            alert.message_box("Python Error", msg)
            queue.put(e)
        finally:
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
            p = threading.Thread(target=self._thread_call_within_thread, args=(call_name, f, *args))
            self.threads[call_name] = p
            p.start()
            return True
        except COMException as e:
            raise e
        except Exception as e:
            logging.exception("Bad call")
            alert.message_box("Python Error", str(e))
            raise COMException(str(e))

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
            p = multiprocessing.Process(target=self._process_call_within_process, args=(q, self.sources, module_name, func_name, *args))
            self.results[call_name] = q
            self.threads[call_name] = p
            p.start()
            return True
        except COMException as e:
            raise e
        except Exception as e:
            logging.exception("Bad call")
            alert.message_box("Python Error", str(e))
            raise COMException(str(e))

    def running(self, call_name):
        """
        Check if an asynchronous call is still running
        :param call_name: name of the call
        :return: whether the call is still running
        """
        if call_name in self.threads:
            return self.threads[call_name].is_alive()
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
                if isinstance(res, COMException):
                    raise res
                if isinstance(res, Exception):
                    msg, code = pyxelresterrors.extract_error(res)
                    raise COMException(desc=msg, hresult=code)
        return res

    def get_running_calls(self):
        return [k for k, v in self.threads.items() if v.is_alive()]

    def get_finished_calls(self):
        return xlwings.server.ToVariant([k for k, v in self.threads.items() if not v.is_alive()])


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

import multiprocessing
import os
import sys
import threading
import logging

import pythoncom
import win32com
from win32com.server.exception import COMException

from pyxelrest import custom_logging, alert, pyxelresterrors
from pyxelrest import _version

logger = logging.getLogger(__name__)


class PythonServer:
    """
    The Python Server COM object allows direct communication between VB and python without
    starting the python command line. Keeping data between two calls.
    """

    _reg_clsid_ = _version.python_server_reg_clsid
    _reg_progid_ = 'pyxelrest.PythonServer'
    _public_methods_ = ['add_path', 'import_module', 'generate_udf', 'direct_call', 'thread_call', 'process_call',
                        'running', 'result', 'set_syslog', 'set_loglevel', 'set_filelog', 'set_alertlog', 'set_consolelog', 'init_disk_cache', 'init_memory_cache',
                        'clear_cache', 'install_module', 'get_running_calls', 'get_finished_calls']

    threads = {}
    results = {}
    sources = []
    log_level = logging.DEBUG
    syslog_host = None
    syslog_port = None
    syslog_level = None
    filelog_filename = None
    filelog_level = None
    console = None
    disk_cache = None
    alert_level = None

    def __init__(self):
        sys.stdout = custom_logging.StreamToLogger(logging, logging.INFO)
        sys.stderr = custom_logging.StreamToLogger(logging, logging.WARNING)
        pass

    def generate_udf(self):
        from pyxelrest import pyxelrestgenerator
        pyxelrestgenerator.generate_user_defined_functions()

    def set_filelog(self, filename, level="DEBUG"):
        self.filelog_filename = filename
        self.filelog_level = level
        custom_logging.set_file_logger(filename, logging.getLevelName(level))

    def set_syslog(self, host, port, level="INFO"):
        self.syslog_host = host
        self.syslog_port = port
        self.syslog_level = level
        custom_logging.set_syslog_logger(host, port, logging.getLevelName(level))

    def set_alertlog(self, level="ERROR"):
        self.alert_level = level
        h = alert.AlertHandler()
        h.setLevel(logging.getLevelName(level))
        logging.getLogger().addHandler(h)

    def set_consolelog(self, level="INFO"):
        try:
            if self.console is None:
                from pyxelrest import qt_console
                self.console = qt_console.QtHandler()
                self.console.start()
                logging.getLogger().addHandler(self.console)
            self.console.setLevel(logging.getLevelName(level))
            self.console.show()
        except ImportError:
            logging.error('Cannot setup console')

    def set_loglevel(self, level, logger=None):
        self.log_level = level
        logging.getLogger(logger).setLevel(logging.getLevelName(level))

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
                logger.exception(msg)
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
            args = tuple(from_variant(arg) for arg in args)
            return f(*args)
        except COMException as e:
            raise e
        except Exception as e:
            msg, code = pyxelresterrors.extract_error(e)
            logger.exception(msg)
            raise COMException(desc=msg, hresult=code)

    def _thread_call_within_thread(self, call_name, func, *args):
        try:
            pythoncom.CoInitialize()
            self.results[call_name] = func(*args)
        except COMException as e:
            self.results[call_name] = e
        except Exception as e:
            msg, code = pyxelresterrors.extract_error(e)
            logger.exception(msg)
            self.results[call_name] = e
        finally:
            pythoncom.CoUninitialize()

    def _process_call_within_process(self, queue, sources, module_name, func_name, *args):
        sys.path.extend(sources)
        pythoncom.CoInitialize()

        if self.filelog_filename is not None:
            custom_logging.set_file_logger(self.filelog_filename + '-' + str(os.getpid()), self.filelog_level)
        if self.syslog_host is not None:
            custom_logging.set_syslog_logger(self.syslog_host, self.syslog_port, self.syslog_level)
        if self.disk_cache is not None:
            from pyxelrest import caching
            caching.init_disk_cache(self.disk_cache + '-' + os.getpid())
        if self.alert_level is not None:
            self.set_alertlog(self.alert_level)
        logging.getLogger().setLevel(logging.getLevelName(self.log_level))
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
            logger.exception(msg)
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
            logging.info("{}: {}.{}{}".format(call_name, module_name, func_name, args))
            if module_name not in sys.modules:
                __import__(module_name)
            m = sys.modules[module_name]
            f = getattr(m, func_name)
            args = tuple(from_variant(arg) for arg in args)
            p = threading.Thread(target=self._thread_call_within_thread, args=(call_name, f, *args))
            self.threads[call_name] = p
            p.start()
            return True
        except COMException as e:
            raise e
        except Exception as e:
            logger.exception("Bad call: {}.{}{}".format(module_name, func_name, args))
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
            args = tuple(from_variant(arg) for arg in args)
            q = multiprocessing.Queue()
            p = multiprocessing.Process(target=self._process_call_within_process, args=(q, self.sources, module_name, func_name, *args))
            self.results[call_name] = q
            self.threads[call_name] = p
            p.start()
            return True
        except COMException as e:
            raise e
        except Exception as e:
            logger.exception("Bad call: {}.{}{}".format(module_name, func_name, args))
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
        return [k for k, v in self.threads.items() if not v.is_alive()]


def from_variant(var):
    try:
        if isinstance(var, tuple):
            return tuple(from_variant(x) for x in var)
        if isinstance(var, list):
            return list(from_variant(x) for x in var)
        return win32com.server.util.unwrap(var).obj
    except:
        return var


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

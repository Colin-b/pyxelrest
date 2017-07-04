import threading
import traceback
import sys

import logging
import pywintypes
import win32api
import pythoncom
from distutils import sysconfig

from pyxelrest import alert
from winerror import RPC_E_SERVERCALL_RETRYLATER

class InvalidSwaggerDefinition(Exception):
    """ Invalid Swagger Definition. """
    def __init__(self, message, *args, **kwargs):  # real signature unknown
        Exception.__init__(self, 'Invalid Definition: ' + message)


class SwaggerVersionNotProvided(InvalidSwaggerDefinition):
    """ Swagger version is not provided. """
    def __init__(self, *args, **kwargs):
        InvalidSwaggerDefinition.__init__(self, 'Version not provided.')


class UnsupportedSwaggerVersion(InvalidSwaggerDefinition):
    """ Swagger version is not supported. """
    def __init__(self, version, *args, **kwargs):
        InvalidSwaggerDefinition.__init__(self, 'Version {} not supported.'.format(version))


class MandatoryPropertyNotProvided(Exception):
    """ Mandatory property not provided. """
    def __init__(self, section, property_name, *args, **kwargs):
        Exception.__init__(self, '"{0}" configuration section must provide "{1}".'.format(section, property_name))


class NoMethodsProvided(Exception):
    """ No Methods provided. """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, 'At least one method must be provided amongst [get, post, put, delete].')


class PortNotAvailable(Exception):
    """ Port is already taken. """
    def __init__(self, port, *args, **kwargs):
        Exception.__init__(self, 'The port {0} is not available.'.format(port))


class ConfigurationFileNotFound(Exception):
    """ Configuration file not found. """
    def __init__(self, file_path, *args, **kwargs):
        Exception.__init__(self, '"{0}" configuration file cannot be read.'.format(file_path))


class DuplicatedParameters(Exception):
    """ Method contains duplicated parameters. """
    def __init__(self, method, *args, **kwargs):
        Exception.__init__(self, '"{0}" parameters are not unique: {1}.'.format(method['operationId'],
                                                                                method['parameters']))


class EmptyResponses(InvalidSwaggerDefinition):
    """ Responses are not set in Swagger. """
    def __init__(self, method_name, *args, **kwargs):
        Exception.__init__(self, 'At least one response must be specified for "{0}".'.format(method_name))


class AuthenticationFailed(Exception):
    """ User was not authenticated. """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, 'User was not authenticated.')


class InvalidToken(Exception):
    """ Token is invalid. """
    def __init__(self, token_name, *args, **kwargs):
        Exception.__init__(self, '{0} is invalid.'.format(token_name))


class TokenNotProvided(Exception):
    """ Token was not provided. """
    def __init__(self, token_name, dictionary_without_token, *args, **kwargs):
        Exception.__init__(self, '{0} not provided within {1}.'.format(token_name, dictionary_without_token))


class TokenExpiryNotProvided(Exception):
    """ Token expiry was not provided. """
    def __init__(self, token_body, *args, **kwargs):
        Exception.__init__(self, 'Expiry (exp) is not provided in {0}.'.format(token_body))


def extract_error(e, debug=True):
    """
    Convert an error to a msg
    :param e: exception thrown
    :param debug: to include debug info
    :return: msg along with debug info
    """
    if isinstance(e, pywintypes.com_error):
        code = e.excepinfo[5]
        msg = win32api.FormatMessage(code).strip()
    else:
        msg = str(e)
        code = 0
    if debug:
        libpath = sysconfig.get_python_lib().replace('\\\\', '\\').lower()
        ex_type, ex, tb = sys.exc_info()
        st = traceback.extract_tb(tb)
        p = len(st) - 1
        # take the first non lib code
        while p >= 0 and st[p].filename.lower().startswith(libpath):
            p -= 1
        if p > -1:
            return '{0} in function {1.name}() file {1.filename}:{1.lineno} with "{1.line}"'.format(msg, st[p]), code
    return msg, code


def retry_com_exception(delay=1):
    """
    Decorator to retry when there is a com exception RPC_E_SERVERCALL_RETRYLATER
    Function cannot have a return result
    :param delay: delay in second
    """
    def decorator(f):
        def wrapper(*args, **kwargs):
            def retry_wrapper(*args, **kwargs):
                try:
                    pythoncom.CoInitialize()
                    wrapper(*args, **kwargs)
                except Exception as e2:
                    msg, code = extract_error(e2)
                    logging.exception(msg)
                    alert.message_box("Python Error", msg)
                finally:
                    pythoncom.CoUninitialize()

            try:
                f(*args, **kwargs)
            except Exception as e:
                if hasattr(e, 'hresult') and e.hresult == RPC_E_SERVERCALL_RETRYLATER:
                    logging.warning('Retrying execution of function {}'.format(f.__name__))
                    t = threading.Timer(delay, function=retry_wrapper, args=args, kwargs=kwargs)
                    t.start()
                else:
                    raise e
        return wrapper
    return decorator

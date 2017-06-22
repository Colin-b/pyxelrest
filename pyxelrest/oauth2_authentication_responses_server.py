import flask
import webbrowser
import threading
import logging
import sys
import requests
import socket
import time
from contextlib import closing

from pyxelrest import auth_token_map
from pyxelrest.pyxelresterrors import *

auth_tokens = auth_token_map.AuthTokenMap()
authentication_server = threading.Semaphore(value=0)
authentication_response = threading.Semaphore(value=0)
app = flask.Flask(__name__)

DEFAULT_SERVER_PORT = 5000
DEFAULT_AUTHENTICATION_TIMEOUT = 20  # Time is expressed in seconds
DEFAULT_SUCCESS_DISPLAY_TIME = 1  # Time is expressed in milliseconds
DEFAULT_FAILURE_DISPLAY_TIME = 5000  # Time is expressed in milliseconds
DEFAULT_TOKEN_NAME = 'token'


class DefaultSecurityDefinition:
    failure_display_time = DEFAULT_FAILURE_DISPLAY_TIME
    success_display_time = DEFAULT_SUCCESS_DISPLAY_TIME
    token_name = DEFAULT_TOKEN_NAME

current_security_definition = DefaultSecurityDefinition


@app.route("/<service_name>/<security_definition_key>", methods=['GET'])
def auth_get(service_name, security_definition_key):
    key = service_name + '/' + security_definition_key
    logging.exception("Unable to properly perform authentication on {0}. GET is not supported for now.".format(key))
    return error_page("Unable to properly perform authentication on {0}. GET is not supported for now.".format(key),
                      current_security_definition.failure_display_time)


@app.route("/<service_name>/<security_definition_key>", methods=['POST'])
def auth_post(service_name, security_definition_key):
    key = service_name + '/' + security_definition_key
    try:
        if current_security_definition.token_name not in flask.request.form:
            raise TokenNotProvided(current_security_definition.token_name)
        id_token = flask.request.form[current_security_definition.token_name]
        auth_tokens.set_token(key, id_token)
        return success_page("You are now authenticated on {0}. You may close this tab.".format(key),
                            current_security_definition.success_display_time)
    except Exception as e:
        logging.exception("Unable to properly perform authentication on {0}.".format(key))
        return error_page("Unable to properly perform authentication on {0}: {1}".format(key, e),
                          current_security_definition.failure_display_time)
    finally:
        try:
            authentication_response.release()
            shutdown()
        except:
            logging.error('An error occurred while signaling that an authentication was received.')
            pass


@app.route("/shutdown", methods=['POST'])
def shutdown():
    flask_server_shutdown = flask.request.environ.get('werkzeug.server.shutdown')
    if flask_server_shutdown is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    flask_server_shutdown()
    logging.info('Stopping OAuth2 authentication responses server')
    return success_page("OAuth 2 authentication response server is now closed.",
                        current_security_definition.success_display_time)


def acquire_with_timeout(lock_obj, timeout):
    if sys.version_info.major > 2:
        # Python 3
        return lock_obj.acquire(timeout=timeout)
    else:
        # Python 2
        res = [True]
        t = threading.Timer(timeout, function=auto_release, args=(lock_obj, res))
        t.start()
        lock_obj.acquire()
        t.cancel()
        return res[0]


def auto_release(lock_obj, res):
    lock_obj.release()
    res[0] = False


def get_bearer(security_definition):
    return auth_tokens.get_bearer(security_definition.key, request_new_token, security_definition)


def request_new_token(security_definition):
    logging.debug('Requesting user authentication...')
    start_server(security_definition.port)
    global current_security_definition
    current_security_definition = security_definition

    # Default to Microsoft Internet Explorer to be able to open a new window
    # otherwise this parameter is not taken into account by most browsers
    # Opening a new window allows to focus back to Microsoft Excel once authenticated (JS is closing the only tab)
    ie = webbrowser.get(webbrowser.iexplore)
    if not ie.open(security_definition.full_url, 1):
        response = requests.get(security_definition.full_url)

    logging.debug('Waiting for user authentication...')
    res = acquire_with_timeout(authentication_response, security_definition.timeout)
    if not res:
        logging.debug('No response received within {0} seconds. Aborting...'.format(security_definition.timeout))
        try:
            requests.post('http://localhost:{0}/shutdown'.format(security_definition.port), json='', timeout=1)
        except:
            pass


def success_page(text, display_time):
    return """<body onload="window.open('', '_self', ''); window.setTimeout(close, {0})" style="
    color: #4F8A10;
    background-color: #DFF2BF;
    font-size: xx-large;
    display: flex;
    align-items: center;
    justify-content: center;">
        <div style="border: 1px solid;">{1}</div>
    </body>""".format(display_time, text)


def error_page(text, display_time):
    return """<body onload="window.open('', '_self', ''); window.setTimeout(close, {0})" style="
    color: #D8000C;
    background-color: #FFBABA;
    font-size: xx-large;
    display: flex;
    align-items: center;
    justify-content: center;">
        <div style="border: 1px solid;">{1}</div>
    </body>""".format(display_time, text)


def start_server(port):
    threading.Thread(target=start_server_sync, args=[port]).start()
    authentication_server.acquire()
    time.sleep(0.1)


def start_server_sync(port):
    logging.debug('Starting OAuth2 authentication responses server...')
    wait_for_port('127.0.0.1', port)
    authentication_server.release()
    app.run(port=port)


def wait_for_port(host, port):
    retry_number = 0
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        while check_bind(sock, host, port):
            time.sleep(0.1)
            retry_number += 1
            if retry_number > 20:
                raise PortNotAvailable(port)


def check_bind(sock, host, port):
    try:
        return sock.bind((host, port)) != 0
    except:
        return False

if __name__ == "__main__":
    start_server(5000)

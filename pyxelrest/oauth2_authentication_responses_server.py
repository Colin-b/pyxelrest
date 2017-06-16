"""
This file was generated. DO NOT EDIT manually.
Source file: oauth2_authentication_responses_server.jinja2
Generation date (UTC): 2017-06-13T14:04:07.067000
"""
import flask
import webbrowser
import threading
import logging
import sys
import os
import base64
import json
import datetime
import requests
import socket
import time
from contextlib import closing

import auth_token_map
from pyxelresterrors import *

auth_tokens = auth_token_map.AuthTokenMap()
authentication_server = threading.Semaphore(value=0)
authentication_response = threading.Semaphore(value=0)
app = flask.Flask(__name__)


@app.route("/<service_name>/<security_definition_key>", methods=['POST'])
def auth_post(service_name, security_definition_key):
    try:
        key = service_name + '/' + security_definition_key
        token = 'id_token'
        if token not in flask.request.form:
            raise TokenNotProvided(token)
        id_token = flask.request.form[token]
        auth_tokens.set_token(key, id_token)
        shutdown()
        return success_page("You are now authenticated on {0}. You may close this tab.".format(key))
    except Exception as e:
        logging.exception("Unable to properly perform authentication on {0}.".format(key))
        return error_page("Unable to properly perform authentication on {0}: {1}".format(key, e))
    finally:
        try:
            authentication_response.release()
        except:
            logging.error('An error occurred while signaling that an authentication was received.')
            pass


@app.route("/shutdown", methods=['POST'])
def shutdown():
    flask_server_shutdown = flask.request.environ.get('werkzeug.server.shutdown')
    if flask_server_shutdown is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    flask_server_shutdown()
    logging.info('Starting OAuth2 authentication responses server')


def acquire_with_timeout(obj, timeout):
    if sys.version_info.major > 2:
        # Python 3
        return obj.acquire(timeout=timeout)
    else:
        # Python 2
        res = [True]
        t = threading.Timer(timeout, function=auto_release, args=(obj, res))
        t.start()
        obj.acquire()
        t.cancel()
        return res[0]


def auto_release(obj, res):
    obj.release()
    res[0] = False


def get_bearer(security_definition):
    return auth_tokens.get_bearer(security_definition.key, request_new_token, security_definition)


def request_new_token(security_definition):
    logging.debug('Requesting user authentication...')
    # if fails, use default browser
    # if not browser_was_opened :

    start_server(security_definition.port)
    browser_was_opened = webbrowser.open(security_definition.full_url)
    # fallback on simple request if no browser was opened (unit tests only)
    if not browser_was_opened:
        response = requests.get(security_definition.full_url)
    logging.debug('Waiting for user authentication...')

    res = acquire_with_timeout(authentication_response, security_definition.timeout)
    if not res:
        requests.post('http://localhost:{0}/shutdown'.format(security_definition.port))
        logging.debug('No response received within {0} seconds. Aborting...'.format(security_definition.timeout))


def success_page(text):
    return """<body onload="window.open('', '_self', ''); window.setTimeout(close, 2000)" style="
    color: #4F8A10;
    background-color: #DFF2BF;
    font-size: xx-large;
    display: flex;
    align-items: center;
    justify-content: center;">
        <div style="border: 1px solid;">{0}</div>
    </body>""".format(text)


def error_page(text):
    return """<body onload="window.open('', '_self', ''); window.setTimeout(close, 5000)" style="
    color: #D8000C;
    background-color: #FFBABA;
    font-size: xx-large;
    display: flex;
    align-items: center;
    justify-content: center;">
        <div style="border: 1px solid;">{0}</div>
    </body>""".format(text)


def start_server(port):
    threading.Thread(target=start_server_sync, args=[port]).start()
    authentication_server.acquire()


def start_server_sync(port):
    logging.debug('Starting OAuth2 authentication responses server...')
    wait_for_port('127.0.0.1', port)
    authentication_server.release()
    app.run(port=port)


def wait_for_port(host, port):
    n = 0
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        while check_bind(sock, host, port):
            time.sleep(0.1)
            n += 1
            if n > 20:
                raise PortNotAvailable(port)


def check_bind(sock, host, port):
    try:
        return sock.bind((host, port)) != 0
    except:
        return False

if __name__ == "__main__":
    start_server(5000)

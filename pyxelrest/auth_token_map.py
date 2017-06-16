import base64
import json
import os
import datetime
import threading

import logging
from pyxelresterrors import TokenExpiryNotProvided, InvalidToken, AuthenticationFailed


class AuthTokenMap:
    """
    Class to manage tokens
    """

    data = {}
    tokens_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'tokens.json')
    lock = threading.Lock()
    last_modif = 0

    def __init__(self):
        self.load_tokens()

    def get_bearer(self, name, func=None, *args):
        """
        get the bearer token
        :param name: name of the token
        :param func: function to call when missing
        :param arg: arg of the function
        :return: the token
        """
        with self.lock:
            self.load_tokens()
            if name in self.data:
                bearer, expiry = self.data[name]
                if datetime.datetime.utcfromtimestamp(expiry) < datetime.datetime.utcnow():
                    logging.debug('Authentication token is expired.')
                    del self.data[name]
                else:
                    logging.debug('Using already received authentication, will expire in {0} (UTC).'.format(expiry))
                    return bearer
        if func is not None:
            func(*args)
            with self.lock:
                if name in self.data:

                    bearer, expiry = self.data[name]
                    return bearer
        logging.debug('User was not authenticated.')
        raise AuthenticationFailed()

    def set_token(self, name, token):
        """
        Set the bearer token and save it
        :param name: name of the token
        :param token: value
        """
        if not token:
            raise InvalidToken(token)
        with self.lock:
            header, body, other = token.split('.')
            body = json.loads(AuthTokenMap.decode_base64(body))
            if 'exp' not in body:
                raise TokenExpiryNotProvided(body)
            expiry = body['exp']
            self.data[name] = token, expiry
            self.save_tokens()
            logging.debug("{0} authentication response received: '{1}'. Expiry is {2} (UTC).".format(name, token, expiry))

    def clear(self):
        with self.lock:
            self.data = {}
            self.last_modif = 0
            try:
                os.remove(self.tokens_path)
            except:
                pass

    # private methods

    def save_tokens(self):
        try:
            with open(self.tokens_path, 'w') as f:
               json.dump(self.data, f)
            self.last_modif = os.path.getmtime(self.tokens_path)
        except Exception as e:
            logging.warn('Cannot save tokens')

    def load_tokens(self):
        try:
            modif = os.path.getmtime(self.tokens_path)
            if modif > self.last_modif:
                self.last_modif = modif
                with open(self.tokens_path, 'r') as f:
                    self.data = json.load(f)
        except Exception as e:
            pass

    @staticmethod
    def decode_base64(base64_encoded_string):
        """
        Decode base64, padding being optional.

        :param base64_encoded_string: Base64 data as an ASCII byte string
        :returns: The decoded byte string.
        """
        missing_padding = len(base64_encoded_string) % 4
        if missing_padding != 0:
            base64_encoded_string += '=' * (4 - missing_padding)
        return base64.b64decode(base64_encoded_string).decode('unicode_escape')

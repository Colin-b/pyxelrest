import os
import datetime
import platform
import requests
from requests.adapters import HTTPAdapter
from pyxelrest import _version

session = None
nb = 1


def get():
    """
    Get the global session object
    :return: the session object
    """
    global session, nb
    if session is None:
        session = requests.Session()
        session.mount('http://', HTTPAdapter(max_retries=5))
        session.mount('https://', HTTPAdapter(max_retries=5))
        session.headers['User-Agent'] = 'PyxelRest v{0}'.format(_version.__version__)
        session.headers['X-PXL-HOSTNAME'] = platform.node()
        session.headers['X-PXL-LOGIN'] = os.getlogin()
        session.headers['X-PXL-SESSION'] = datetime.datetime.today().isoformat()
    session.headers['X-PXL-REQUEST'] = nb
    nb += 1
    return session

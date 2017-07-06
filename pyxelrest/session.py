import os
import datetime
import platform
import requests
from requests.adapters import HTTPAdapter
from pyxelrest import _version

session = None
nb = 1
max_retries = 5
hostname = platform.node()
login = os.getlogin()


def setup(cfg):
    global max_retries, hostname, login
    max_retries = cfg.get('max_retries', max_retries)
    hostname = cfg.get('hostname', hostname)
    login = cfg.get('login', login)


def get():
    """
    Get the global session object
    :return: the session object
    """
    global session, nb
    if session is None:
        session = requests.Session()
        session.mount('http://', HTTPAdapter(max_retries=max_retries))
        session.mount('https://', HTTPAdapter(max_retries=max_retries))
        session.headers['User-Agent'] = 'PyxelRest v{0}'.format(_version.__version__)
        session.headers['X-PXL-HOSTNAME'] = hostname
        session.headers['X-PXL-LOGIN'] = login
        session.headers['X-PXL-SESSION'] = datetime.datetime.today().isoformat()
    session.headers['X-PXL-REQUEST'] = str(nb)
    nb += 1
    return session

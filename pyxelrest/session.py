import datetime
import os
import platform
import requests
from requests.adapters import HTTPAdapter
from pyxelrest import _version

sessions = {}
nb_requests_sent = 0
hostname = platform.node()
login = os.getlogin()
session_start = datetime.datetime.today().isoformat()


def get(max_retries):
    """
    Get the global session object
    :return: the session object
    """
    global nb_requests_sent
    session = sessions.get(max_retries)
    if session is None:
        session = requests.Session()
        session.mount('http://', HTTPAdapter(max_retries=max_retries))
        session.mount('https://', HTTPAdapter(max_retries=max_retries))
        session.headers['User-Agent'] = 'PyxelRest v{0}'.format(_version.__version__)
        session.headers['X-PXL-HOSTNAME'] = hostname
        session.headers['X-PXL-LOGIN'] = login
        session.headers['X-PXL-SESSION'] = session_start
        sessions[max_retries] = session
    nb_requests_sent += 1
    session.headers['X-PXL-REQUEST'] = str(nb_requests_sent)
    return session

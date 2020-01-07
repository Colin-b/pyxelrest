import datetime
import requests
from requests.adapters import HTTPAdapter
from pyxelrest import version

sessions = {}
nb_requests_sent = 0


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
        session.headers['User-Agent'] = 'PyxelRest v{0}'.format(version.__version__)
        session.headers['X-PXL-SESSION'] = datetime.datetime.today().isoformat()
        sessions[max_retries] = session
    nb_requests_sent += 1
    session.headers['X-PXL-REQUEST'] = str(nb_requests_sent)
    return session

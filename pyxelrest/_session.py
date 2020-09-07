import datetime

import requests
from requests.adapters import HTTPAdapter

from pyxelrest.version import __version__
from pyxelrest._fileadapter import LocalFileAdapter

sessions = {}
nb_requests_sent = 0


def get(max_retries: int) -> requests.Session:
    """Return a session allowing that much retry."""
    global nb_requests_sent
    session = sessions.get(max_retries)
    if session is None:
        session = _create_session(max_retries)
        sessions[max_retries] = session
    nb_requests_sent += 1
    session.headers["X-PXL-REQUEST"] = str(nb_requests_sent)
    return session


def _create_session(max_retries: int) -> requests.Session:
    session = requests.Session()
    session.mount("http://", HTTPAdapter(max_retries=max_retries))
    session.mount("https://", HTTPAdapter(max_retries=max_retries))
    session.mount("file:///", LocalFileAdapter())
    session.headers["User-Agent"] = f"PyxelRest v{__version__}"
    session.headers["X-PXL-SESSION"] = datetime.datetime.today().isoformat()
    return session

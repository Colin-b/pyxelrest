import requests
from requests.adapters import HTTPAdapter

from pyxelrest.version import __version__
from pyxelrest._fileadapter import LocalFileAdapter

_sessions = {}


def get(max_retries: int) -> requests.Session:
    """Return a session allowing that much retry."""
    session = _sessions.get(max_retries)
    if session is None:
        session = _create_session(max_retries)
        _sessions[max_retries] = session
    return session


def _create_session(max_retries: int) -> requests.Session:
    session = requests.Session()
    session.mount("http://", HTTPAdapter(max_retries=max_retries))
    session.mount("https://", HTTPAdapter(max_retries=max_retries))
    session.mount("file:///", LocalFileAdapter())
    session.headers["User-Agent"] = f"pyxelrest/{__version__}"
    return session

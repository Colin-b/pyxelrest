import requests
from requests.adapters import HTTPAdapter

session = None


def get():
    """
    Get the global session object
    :return: the session object
    """
    global session
    if session is None:
        session = requests.Session()
        session.mount('http://', HTTPAdapter(max_retries=5))
        session.mount('https://', HTTPAdapter(max_retries=5))
    return session

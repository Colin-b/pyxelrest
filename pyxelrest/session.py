import requests
from requests.adapters import HTTPAdapter

session = None


def get():
    global session
    if session is None:
        session = requests.Session()
        session.mount('http://', HTTPAdapter(max_retries=5))
        session.mount('https://', HTTPAdapter(max_retries=5))
    return session

from typing import Tuple
import os

import requests
import requests.adapters


class LocalFileAdapter(requests.adapters.BaseAdapter):
    """
    Protocol Adapter to allow Requests to GET file:/// URLs

    Example: file:///C:\\path\\to\\open_api_definition.json
    """

    @staticmethod
    def _check_path(path: str) -> Tuple[int, str]:
        """Return an HTTP status for the given filesystem path."""
        if os.path.isdir(path):
            return 400, "Path Not A File"
        elif not os.path.isfile(path):
            return 404, "File Not Found"
        else:
            return 200, "OK"

    def send(self, request: requests.Request, *args, **kwargs):
        """Return the file specified by the given request"""
        path = os.path.normcase(os.path.normpath(request.url[8:]))
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        response = requests.Response()
        response.status_code, response.reason = self._check_path(path)
        if response.status_code == 200:
            response.raw = open(path, "rb")

        response.url = path
        response.request = request
        response.connection = self

        return response

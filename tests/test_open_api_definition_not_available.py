import os
import timeit
import time

import pytest
import pyxelrest
from responses import RequestsMock

from testsutils import loader


@pytest.fixture
def open_api_definition_not_responding_service(responses: RequestsMock):
    def reply_after_one_hour():
        # Do not respond to this call (simulate service down behind a reverse proxy)
        time.sleep(3600)

    responses.add_callback(
        responses.GET,
        url="http://localhost:8950/swagger.json",
        callback=reply_after_one_hour,
    )


def test_service_can_be_loaded_without_hitting_timeout(
    open_api_definition_not_responding_service,
):
    this_dir = os.path.abspath(os.path.dirname(__file__))
    pyxelrest.SERVICES_CONFIGURATION_FILE_PATH = os.path.join(
        this_dir, "open_api_definition_not_available.yml"
    )
    nb_seconds = timeit.timeit("from pyxelrest import pyxelrestgenerator", number=1)
    assert nb_seconds < 8, "Time to load pyxelrest should be around timeout."

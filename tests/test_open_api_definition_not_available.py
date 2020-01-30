import timeit
import time

import pytest
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
    loader.load("open_api_definition_not_available.yml", load_pyxelrest=False)
    nb_seconds = timeit.timeit("from pyxelrest import pyxelrestgenerator", number=1)
    assert nb_seconds < 8, "Time to load pyxelrest should be around timeout."

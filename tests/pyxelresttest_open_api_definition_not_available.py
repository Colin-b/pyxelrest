import timeit

import pytest
from responses import RequestsMock

from testsutils import serviceshandler, loader


@pytest.fixture
def open_api_definition_not_responding_service(responses: RequestsMock):
    from testsutils import open_api_definition_not_responding_service

    serviceshandler.start_services((open_api_definition_not_responding_service, 8950))
    loader.load("open_api_definition_not_available.yml", load_pyxelrest=False)
    yield 1
    serviceshandler.stop_services()


def test_service_can_be_loaded_without_hitting_timeout(
    open_api_definition_not_responding_service,
):
    nb_seconds = timeit.timeit("from pyxelrest import pyxelrestgenerator", number=1)
    assert nb_seconds < 8, "Time to load pyxelrest should be around timeout."

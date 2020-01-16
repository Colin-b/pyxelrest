import pytest
from responses import RequestsMock

from testsutils import serviceshandler, loader


@pytest.fixture
def without_parameter_service(responses: RequestsMock):
    from testsutils import without_parameter_service

    serviceshandler.start_services((without_parameter_service, 8950))
    loader.load("connectivity_issues_services.yml")


def test_get_plain_text_with_service_down(without_parameter_service):
    from pyxelrest import pyxelrestgenerator

    serviceshandler.stop_services()
    assert (
        pyxelrestgenerator.without_parameter_get_plain_text_without_parameter()
        == "Cannot connect to service. Please retry once connection is re-established."
    )

import pytest
from responses import RequestsMock

from testsutils import serviceshandler, loader


@pytest.fixture
def usual_parameters_service(responses: RequestsMock):
    from testsutils import usual_parameters_service

    serviceshandler.start_services((usual_parameters_service, 8943))
    yield 1
    serviceshandler.stop_services()


def test_without_logging_configuration_file(usual_parameters_service):
    """
    This test case assert that pyxelrest can be loaded without logging configuration
    """
    loader.load("no_logging_services.yml", "non_existing_configuration.yml")

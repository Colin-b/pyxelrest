import datetime

import pytest
from responses import RequestsMock

from testsutils import serviceshandler, loader


@pytest.fixture
def usual_parameters_service(responses: RequestsMock):
    from testsutils import usual_parameters_service

    serviceshandler.start_services((usual_parameters_service, 8943))
    yield 1
    serviceshandler.stop_services()


def test_without_service_configuration_file(usual_parameters_service):
    loader.load("duplicated_service.yml")
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.usual_parameters_get_date() == [
        [datetime.datetime(2014, 3, 5, 0, 0)],
        [datetime.datetime(9999, 1, 1, 0, 0)],
        [datetime.datetime(3001, 1, 1, 0, 0)],
        [datetime.datetime(1970, 1, 1, 0, 0)],
        [datetime.datetime(1900, 1, 1, 0, 0)],
    ]

import pytest
from responses import RequestsMock

from testsutils import loader


@pytest.fixture
def async_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8958/",
        json={
            "swagger": "2.0",
            "paths": {
                "/async": {
                    "get": {
                        "operationId": "get_async",
                        "responses": {
                            "202": {
                                "description": "return value",
                                "schema": {"type": "string"},
                            }
                        },
                    }
                }
            },
        },
        match_querystring=True,
    )
    loader.load("async_service.yml")


def test_get_async_url(responses: RequestsMock, async_service):
    responses.add(
        responses.GET,
        url="http://localhost:8958/async",
        json={},
        headers={"location": "http://localhost:8958/async/status"},
        status=202,
        match_querystring=True,
    )

    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.async_get_async() == [
        ["Status URL"],
        ["http://localhost:8958/async/status"],
    ]

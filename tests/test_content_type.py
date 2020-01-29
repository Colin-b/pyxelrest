import pytest
from requests import PreparedRequest
from responses import RequestsMock

from testsutils import loader


def _get_request(responses: RequestsMock, url: str) -> PreparedRequest:
    for call in responses.calls:
        if call.request.url == url:
            # Pop out verified request (to be able to check multiple requests)
            responses.calls._calls.remove(call)
            return call.request


def support_pandas():
    try:
        import pandas

        return True
    except:
        return False


@pytest.fixture
def content_type_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8956/",
        json={
            "swagger": "2.0",
            "paths": {
                "/msgpackpandas": {
                    "get": {
                        "operationId": "get_msgpackpandas",
                        "responses": {200: {"description": "successful operation"}},
                        "produces": ["application/msgpackpandas"],
                    }
                },
                "/json": {
                    "get": {
                        "operationId": "get_json",
                        "responses": {200: {"description": "successful operation"}},
                        "produces": ["application/json"],
                    }
                },
            },
        },
        match_querystring=True,
    )
    loader.load("content_type_service.yml")


def test_msgpackpandas_content_type(responses: RequestsMock, content_type_service):
    responses.add(
        responses.GET,
        url="http://localhost:8956/msgpackpandas",
        json={},
        match_querystring=True,
    )

    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.content_type_get_msgpackpandas() == [[""]]
    # TODO Add separate test case with and without pandas
    assert _get_request(responses, "http://localhost:8956/msgpackpandas").headers[
        "Accept"
    ] == ("application/msgpackpandas" if support_pandas() else "*/*")


def test_json_content_type(responses: RequestsMock, content_type_service):
    responses.add(
        responses.GET, url="http://localhost:8956/json", json={}, match_querystring=True
    )

    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.content_type_get_json() == [[""]]
    assert (
        _get_request(responses, "http://localhost:8956/json").headers["Accept"]
        == "application/json"
    )

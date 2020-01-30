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


def test_msgpackpandas_content_type_with_pandas(
    responses: RequestsMock, content_type_service
):
    pyxelrestgenerator = loader.load("content_type_service.yml")
    responses.add(
        responses.GET,
        url="http://localhost:8956/msgpackpandas",
        json={},
        match_querystring=True,
    )

    assert pyxelrestgenerator.content_type_get_msgpackpandas() == [[""]]
    assert (
        _get_request(responses, "http://localhost:8956/msgpackpandas").headers["Accept"]
        == "application/msgpackpandas"
    )


def test_msgpackpandas_content_type_without_pandas(
    responses: RequestsMock, content_type_service
):
    pyxelrestgenerator = loader.load("content_type_service.yml")
    responses.add(
        responses.GET,
        url="http://localhost:8956/msgpackpandas",
        json={},
        match_querystring=True,
    )

    assert pyxelrestgenerator.content_type_get_msgpackpandas() == [[""]]
    assert (
        _get_request(responses, "http://localhost:8956/msgpackpandas").headers["Accept"]
        == "*/*"
    )


def test_json_content_type(responses: RequestsMock, content_type_service):
    pyxelrestgenerator = loader.load("content_type_service.yml")
    responses.add(
        responses.GET, url="http://localhost:8956/json", json={}, match_querystring=True
    )

    assert pyxelrestgenerator.content_type_get_json() == [[""]]
    assert (
        _get_request(responses, "http://localhost:8956/json").headers["Accept"]
        == "application/json"
    )

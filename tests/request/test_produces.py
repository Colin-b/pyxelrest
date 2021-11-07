import pytest
from responses import RequestsMock

from tests import loader
from tests.request._request import _get_request


@pytest.fixture
def content_type_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8956/",
        json={
            "swagger": "2.0",
            "paths": {
                "/json": {
                    "get": {
                        "operationId": "get_json",
                        "responses": {200: {"description": "successful operation"}},
                        "produces": ["application/json"],
                    }
                }
            },
        },
        match_querystring=True,
    )


def test_json_content_type(responses: RequestsMock, content_type_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "content_type": {
                "open_api": {"definition": "http://localhost:8956/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET, url="http://localhost:8956/json", json={}, match_querystring=True
    )

    assert generated_functions.content_type_get_json() == [[""]]
    assert (
        _get_request(responses, "http://localhost:8956/json").headers["Accept"]
        == "application/json"
    )

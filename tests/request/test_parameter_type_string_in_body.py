import pytest
from responses import RequestsMock

from tests import loader
from tests.request._request import _get_request


@pytest.fixture
def json_service(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://localhost:8954/",
        json={
            "swagger": "2.0",
            "definitions": {
                "string_body": {
                    "type": "string",
                },
            },
            "paths": {
                "/string": {
                    "post": {
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "payload",
                                "required": True,
                                "in": "body",
                                "schema": {"$ref": "#/definitions/string_body"},
                            }
                        ],
                    }
                },
            },
        },
        match_querystring=True,
    )


def test_post_string_parameter(json_service, tmpdir, responses: RequestsMock):
    generated_functions = loader.load(
        tmpdir,
        {
            "string": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.POST,
        url="http://localhost:8954/string",
        json=[],
        match_querystring=True,
    )
    assert generated_functions.string_post_string("test value") == [[""]]
    assert (
        _get_request(responses, "http://localhost:8954/string").body == b'"test value"'
    )

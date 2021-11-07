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
                "integer_body": {
                    "type": "integer",
                },
            },
            "paths": {
                "/integer": {
                    "post": {
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "payload",
                                "required": True,
                                "in": "body",
                                "schema": {"$ref": "#/definitions/integer_body"},
                            }
                        ],
                    }
                },
            },
        },
        match_querystring=True,
    )


def test_post_integer_parameter(json_service, tmpdir, responses: RequestsMock):
    generated_functions = loader.load(
        tmpdir,
        {
            "integer": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.POST,
        url="http://localhost:8954/integer",
        json=[],
        match_querystring=True,
    )
    assert generated_functions.integer_post_integer(3) == [[""]]
    assert _get_request(responses, "http://localhost:8954/integer").body == b"3"

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
                "boolean_body": {
                    "type": "boolean",
                },
            },
            "paths": {
                "/boolean": {
                    "post": {
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "payload",
                                "required": True,
                                "in": "body",
                                "schema": {"$ref": "#/definitions/boolean_body"},
                            }
                        ],
                    }
                },
            },
        },
        match_querystring=True,
    )


def test_post_boolean_parameter_true(json_service, tmpdir, responses: RequestsMock):
    generated_functions = loader.load(
        tmpdir,
        {
            "boolean": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.POST,
        url="http://localhost:8954/boolean",
        json=[],
        match_querystring=True,
    )
    assert generated_functions.boolean_post_boolean(True) == [[""]]
    assert _get_request(responses, "http://localhost:8954/boolean").body == b"true"


def test_post_boolean_parameter_false(json_service, tmpdir, responses: RequestsMock):
    generated_functions = loader.load(
        tmpdir,
        {
            "boolean": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.POST,
        url="http://localhost:8954/boolean",
        json=[],
        match_querystring=True,
    )
    assert generated_functions.boolean_post_boolean(False) == [[""]]
    assert _get_request(responses, "http://localhost:8954/boolean").body == b"false"

import pytest
from responses import RequestsMock

from tests import loader
from tests.request._request import _get_request


@pytest.fixture
def form_parameter_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8952/",
        json={
            "swagger": "2.0",
            "definitions": {
                "Form": {
                    "type": "object",
                    "properties": {"form_string": {"type": "string"}},
                    "title": "Test",
                }
            },
            "paths": {
                "/form": {
                    "post": {
                        "operationId": "post_form",
                        "parameters": [
                            {
                                "description": "form parameter",
                                "in": "formData",
                                "name": "form_string",
                                "required": True,
                                "type": "string",
                            }
                        ],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {"$ref": "#/definitions/Form"},
                            }
                        },
                    }
                }
            },
        },
        match_querystring=True,
    )


def test_post_form_parameter(responses: RequestsMock, form_parameter_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "form_parameter": {
                "open_api": {"definition": "http://localhost:8952/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.POST,
        url="http://localhost:8952/form",
        json={},
        match_querystring=True,
    )

    assert generated_functions.form_parameter_post_form("sent string form data") == [
        [""]
    ]
    assert (
        _get_request(responses, "http://localhost:8952/form").body
        == b'{"form_string": "sent string form data"}'
    )

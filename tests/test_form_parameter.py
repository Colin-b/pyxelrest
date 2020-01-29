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
    loader.load("form_parameter_service.yml")


def test_post_form_parameter(responses: RequestsMock, form_parameter_service):
    responses.add(
        responses.POST,
        url="http://localhost:8952/form",
        json={},
        match_querystring=True,
    )

    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.form_parameter_post_form("sent string form data") == [
        [""]
    ]
    assert (
        _get_request(responses, "http://localhost:8952/form").body
        == b'{"form_string": "sent string form data"}'
    )

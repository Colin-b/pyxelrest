import inspect

import pytest
from requests import PreparedRequest
from responses import RequestsMock

from tests import loader


def _get_request(responses: RequestsMock, url: str) -> PreparedRequest:
    for call in responses.calls:
        if call.request.url == url:
            # Pop out verified request (to be able to check multiple requests)
            responses.calls._calls.remove(call)
            return call.request


@pytest.fixture
def parameter_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8951/",
        json={
            "swagger": "2.0",
            "paths": {
                "/header": {
                    "get": {
                        "operationId": "get_header",
                        "parameters": [
                            {
                                "in": "header",
                                "name": "mandatory",
                                "required": True,
                                "type": "string",
                            },
                            {
                                "in": "header",
                                "name": "optional1",
                                "required": False,
                                "type": "string",
                            },
                            {
                                "in": "header",
                                "name": "optional2",
                                "required": False,
                                "type": "string",
                            },
                        ],
                        "responses": {
                            200: {
                                "description": "successful operation",
                            }
                        },
                    }
                }
            },
        },
        match_querystring=True,
    )


def test_selected_parameters(responses: RequestsMock, parameter_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "selected_parameters": {
                "open_api": {
                    "definition": "http://localhost:8951/",
                    "selected_parameters": [
                        "mandatory",
                        "*1",
                    ],
                },
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                },
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8951/header",
        json={},
        match_querystring=True,
    )

    assert (
        "optional2"
        not in inspect.getfullargspec(
            generated_functions.selected_parameters_get_header
        ).args
    )
    assert generated_functions.selected_parameters_get_header(
        mandatory="mandatory", optional1="opt"
    ) == [[""]]
    sent_headers = _get_request(responses, "http://localhost:8951/header").headers
    assert sent_headers["mandatory"] == "mandatory"
    assert sent_headers["optional1"] == "opt"
    assert "optional2" not in sent_headers


def test_excluded_parameters(responses: RequestsMock, parameter_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "excluded_parameters": {
                "open_api": {
                    "definition": "http://localhost:8951/",
                    "excluded_parameters": [
                        "*2",
                    ],
                },
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                },
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8951/header",
        json={},
        match_querystring=True,
    )

    assert (
        "optional2"
        not in inspect.getfullargspec(
            generated_functions.excluded_parameters_get_header
        ).args
    )
    assert generated_functions.excluded_parameters_get_header(
        mandatory="mandatory", optional1="opt"
    ) == [[""]]
    sent_headers = _get_request(responses, "http://localhost:8951/header").headers
    assert sent_headers["mandatory"] == "mandatory"
    assert sent_headers["optional1"] == "opt"
    assert "optional2" not in sent_headers

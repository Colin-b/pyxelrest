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
def json_service(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://localhost:8954/",
        json={
            "swagger": "2.0",
            "paths": {
                "/dict": {
                    "post": {
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "payload",
                                "required": True,
                                "in": "body",
                                "type": "object",
                            }
                        ],
                    }
                },
            },
        },
        match_querystring=True,
    )


def test_post_dict_parameter_without_list(
    json_service, tmpdir, responses: RequestsMock
):
    generated_functions = loader.load(
        tmpdir,
        {
            "dict": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    assert (
        generated_functions.dict_post_dict("value")
        == """payload value "value" (<class 'str'> type) must be a list."""
    )


def test_post_dict_parameter_with_less_than_2_rows(
    json_service, tmpdir, responses: RequestsMock
):
    generated_functions = loader.load(
        tmpdir,
        {
            "dict": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.dict_post_dict([["h1", "h2"]])
        == "payload value should contains only two rows. Header and values."
    )


def test_post_dict_parameter_with_more_than_2_rows(
    json_service, tmpdir, responses: RequestsMock
):
    generated_functions = loader.load(
        tmpdir,
        {
            "dict": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.dict_post_dict([["h1", "h2"], ["v1", "v2"], ["v10", "v20"]])
        == "payload value should contains only two rows. Header and values."
    )


def test_post_dict_parameter_with_a_single_item(
    json_service, tmpdir, responses: RequestsMock
):
    generated_functions = loader.load(
        tmpdir,
        {
            "dict": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.POST,
        url="http://localhost:8954/dict",
        json=[],
        match_querystring=True,
    )
    assert generated_functions.dict_post_dict(["header", "value"]) == [[""]]
    assert (
        _get_request(responses, "http://localhost:8954/dict").body
        == b"""{"payload": {"header": "value"}}"""
    )

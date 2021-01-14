import pytest
from responses import RequestsMock

from tests import loader


@pytest.fixture
def without_parameter_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "responses": {
                            "200": {
                                "description": "return value",
                                "type": "string",
                            }
                        },
                    },
                },
            },
        },
        match_querystring=True,
    )


def test_get_with_http_failure(without_parameter_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "http": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.http_get_test()
        == "Cannot connect to service. Please retry once connection is re-established."
    )


def test_get_with_http_error(without_parameter_service, tmpdir, responses):
    generated_functions = loader.load(
        tmpdir,
        {
            "http": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test",
        body=b"This is the error description",
        status=500,
        match_querystring=True,
    )

    assert (
        generated_functions.http_get_test()
        == 'An error occurred. Please check logs for full details: "This is the error description"'
    )

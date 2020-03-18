from responses import RequestsMock

from tests import loader


def test_get_async_url(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_async",
                        "responses": {
                            "202": {
                                "description": "return value",
                                "schema": {"type": "string"},
                            }
                        },
                    }
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "async_test": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test",
        json={},
        headers={"location": "http://localhost:8958/async/status"},
        status=202,
        match_querystring=True,
    )

    assert generated_functions.async_test_get_async() == [
        ["Status URL"],
        ["http://localhost:8958/async/status"],
    ]

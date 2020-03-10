from responses import RequestsMock

from tests import loader


def test_https_is_used_whenever_possible(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_scheme",
                        "responses": {200: {"description": "successful operation"}},
                    }
                }
            },
            "schemes": ["http", "https"],
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "scheme": {
                "open_api": {"definition": "http://test/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET, url="https://test/test", json={}, match_querystring=True
    )
    assert generated_functions.scheme_get_scheme() == [[""]]

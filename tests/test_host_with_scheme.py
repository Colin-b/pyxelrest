from responses import RequestsMock

from tests import loader


def test_host_with_scheme_and_no_scheme_in_definition(responses: RequestsMock, tmpdir):
    """
    Assert that if there is not host in OpenAPI definition and host is provided by client.
    This host is used, but if no scheme is provided in the OpenAPI definition, the scheme used is the one of
    the host (if provided).
    """
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
                                "type": "string",
                            }
                        },
                    }
                },
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "host_with_scheme": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
                "network": {"host": "https://test_host/path"},
            }
        },
    )
    responses.add(
        responses.GET,
        url="https://test_host/path/test",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.host_with_scheme_get_test() == [[""]]

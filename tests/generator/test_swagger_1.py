from responses import RequestsMock

from tests import loader


def test_swagger_1_is_not_supported(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://localhost:8948/swagger_version_not_supported",
        json={
            "swagger": "1.0",
            "paths": {
                "/should_not_be_available": {
                    "get": {
                        "operationId": "get_should_not_be_available",
                        "responses": {200: {"description": "successful operation"}},
                    }
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "not_supported": {
                "open_api": {
                    "definition": "http://localhost:8948/swagger_version_not_supported"
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert not hasattr(generated_functions, "not_supported_get_should_not_be_available")

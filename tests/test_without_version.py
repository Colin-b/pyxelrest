from responses import RequestsMock

from tests import loader


def test_swagger_version_is_mandatory(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://localhost:8948/swagger_version_not_provided",
        json={
            "paths": {
                "/should_not_be_available": {
                    "get": {
                        "operationId": "get_should_not_be_available",
                        "responses": {200: {"description": "successful operation"}},
                    }
                }
            }
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "not_provided": {
                "open_api": {
                    "definition": "http://localhost:8948/swagger_version_not_provided"
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    assert not hasattr(generated_functions, "not_provided_get_should_not_be_available")

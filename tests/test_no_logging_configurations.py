from responses import RequestsMock

from testsutils import loader


def test_without_logging_configuration_file(responses: RequestsMock):
    """
    This test case assert that pyxelrest can be loaded without logging configuration
    """
    responses.add(
        responses.GET,
        url="http://localhost:8943/",
        json={
            "swagger": "2.0",
            "paths": {
                "/date": {
                    "get": {
                        "operationId": "get_date",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {
                                    "type": "array",
                                    "items": {"type": "string", "format": "date"},
                                },
                            }
                        },
                    }
                }
            },
        },
        match_querystring=True,
    )
    loader.load("no_logging_services.yml", "non_existing_configuration.yml")

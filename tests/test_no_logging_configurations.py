import os

import pyxelrest
from responses import RequestsMock

from testsutils import loader


def test_without_logging_configuration_file(responses: RequestsMock, tmpdir):
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
    this_dir = os.path.abspath(os.path.dirname(__file__))
    pyxelrest.LOGGING_CONFIGURATION_FILE_PATH = os.path.join(
        this_dir, "non_existing_configuration.yml"
    )
    loader.load2(
        tmpdir,
        {
            "usual_parameters": {
                "open_api": {"definition": "http://localhost:8943/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

import os

from responses import RequestsMock

from tests import loader


def test_get_static_open_api_definition(responses: RequestsMock, tmpdir):
    open_api_definition_file_path = os.path.join(
        tmpdir, "static_open_api_definition.json"
    )
    with open(open_api_definition_file_path, "wt") as open_api_definition_file:
        open_api_definition_file.write(
            """{
  "swagger": "2.0",
  "schemes": [
    "http"
  ],
  "host": "localhost:8954",
  "basePath": "/sub",
  "paths": {
    "/static/file/call": {
      "get": {
        "operationId": "get_static_file_call",
        "responses": {
          "200": {
            "description": ""
          }
        }
      }
    }
  }
}
"""
        )

    pyxelrestgenerator = loader.load(
        tmpdir,
        {
            "open_api_definition_loaded_from_file": {
                "open_api": {"definition": f"file://{open_api_definition_file_path}"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8954/sub/static/file/call",
        json={},
        match_querystring=True,
    )

    assert pyxelrestgenerator.open_api_definition_loaded_from_file_get_static_file_call() == [
        [""]
    ]

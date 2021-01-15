import logging
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

    generated_functions = loader.load(
        tmpdir,
        {
            "open_api_definition_loaded_from_file": {
                "open_api": {"definition": f"file:///{open_api_definition_file_path}"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8954/sub/static/file/call",
        json={},
        match_querystring=True,
    )

    assert (
        generated_functions.open_api_definition_loaded_from_file_get_static_file_call()
        == [[""]]
    )


def test_get_static_open_api_definition_as_directory(
    responses: RequestsMock, tmpdir, caplog
):
    caplog.set_level(logging.ERROR, logger="pyxelrest")
    loader.load(
        tmpdir,
        {
            "open_api_definition_loaded_from_file": {
                "open_api": {"definition": f"file:///{tmpdir}"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    assert caplog.messages == [
        f'"open_api_definition_loaded_from_file" will not be available: 400 Client Error: Path Not A File for url: {str(tmpdir).lower()}'
    ]


def test_get_static_open_api_definition_not_found(
    responses: RequestsMock, tmpdir, caplog
):
    caplog.set_level(logging.ERROR, logger="pyxelrest")
    not_found = os.path.join(tmpdir, "static_open_api_definition.json")

    loader.load(
        tmpdir,
        {
            "open_api_definition_loaded_from_file": {
                "open_api": {"definition": f"file:///{not_found}"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    assert caplog.messages == [
        f'"open_api_definition_loaded_from_file" will not be available: 404 Client Error: File Not Found for url: {not_found.lower()}'
    ]


def test_get_static_open_api_definition_relative_path(
    responses: RequestsMock, tmpdir, caplog
):
    caplog.set_level(logging.ERROR, logger="pyxelrest")

    loader.load(
        tmpdir,
        {
            "open_api_definition_loaded_from_file": {
                "open_api": {"definition": f"file:///ko_existing_file.json"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    import os

    assert caplog.messages == [
        f'"open_api_definition_loaded_from_file" will not be available: 404 Client Error: File Not Found for url: {os.getcwd()}\\ko_existing_file.json'
    ]

import pytest
from responses import RequestsMock

from testsutils import loader


@pytest.fixture
def without_parameter_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8950/",
        json={
            "swagger": "2.0",
            "definitions": {"Test": {"properties": {}}},
            "paths": {
                "/without_parameter": {
                    "get": {
                        "operationId": "get_without_parameter",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {"type": "string"},
                            }
                        },
                    },
                    "post": {
                        "operationId": "post_without_parameter",
                        "responses": {
                            "200": {"description": "POST performed properly"}
                        },
                    },
                    "put": {
                        "operationId": "put_without_parameter",
                        "responses": {"200": {"description": "PUT performed properly"}},
                    },
                    "delete": {
                        "operationId": "delete_without_parameter",
                        "responses": {
                            "200": {"description": "DELETE performed properly"}
                        },
                    },
                },
                "/plain_text_without_parameter": {
                    "get": {
                        "operationId": "get_plain_text_without_parameter",
                        "produces": ["text/plain"],
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {"type": "string"},
                            }
                        },
                    },
                    "post": {
                        "operationId": "post_plain_text_without_parameter",
                        "produces": ["text/plain"],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "put": {
                        "operationId": "put_plain_text_without_parameter",
                        "produces": ["text/plain"],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "delete": {
                        "operationId": "delete_plain_text_without_parameter",
                        "produces": ["text/plain"],
                        "responses": {"200": {"description": "return value"}},
                    },
                },
                "/json_without_parameter": {
                    "get": {
                        "operationId": "get_json_without_parameter",
                        "produces": ["application/json"],
                        "responses": {
                            "200": {
                                "description": "return value",
                                "$ref": "#/definitions/Test",
                            }
                        },
                    },
                    "post": {
                        "operationId": "post_json_without_parameter",
                        "produces": ["application/json"],
                        "responses": {
                            "200": {
                                "description": "return value",
                                "$ref": "#/definitions/Test",
                            }
                        },
                    },
                    "put": {
                        "operationId": "put_json_without_parameter",
                        "produces": ["application/json"],
                        "responses": {
                            "200": {
                                "description": "return value",
                                "$ref": "#/definitions/Test",
                            }
                        },
                    },
                    "delete": {
                        "operationId": "delete_json_without_parameter",
                        "produces": ["application/json"],
                        "responses": {
                            "200": {
                                "description": "return value",
                                "$ref": "#/definitions/Test",
                            }
                        },
                    },
                },
                "/octet_without_parameter": {
                    "get": {
                        "operationId": "get_octet_without_parameter",
                        "produces": ["application/octet-stream"],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "post": {
                        "operationId": "post_octet_without_parameter",
                        "produces": ["application/octet-stream"],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "put": {
                        "operationId": "put_octet_without_parameter",
                        "produces": ["application/octet-stream"],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "delete": {
                        "operationId": "delete_octet_without_parameter",
                        "produces": ["application/octet-stream"],
                        "responses": {"200": {"description": "return value"}},
                    },
                },
            },
        },
        match_querystring=True,
    )


def test_get_plain_text_with_service_down(without_parameter_service):
    loader.load("connectivity_issues_services.yml")
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.without_parameter_get_plain_text_without_parameter()
        == "Cannot connect to service. Please retry once connection is re-established."
    )

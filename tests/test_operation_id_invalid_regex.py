import inspect

import pytest
from responses import RequestsMock

from tests import loader


@pytest.fixture
def filtered_operation_id_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8944/",
        json={
            "swagger": "2.0",
            "definitions": {
                "TestObject": {
                    "type": "object",
                    "properties": {"test": {"type": "string", "description": "test"}},
                    "title": "Test",
                }
            },
            "paths": {
                "/tags": {
                    "get": {
                        "operationId": "get_tags",
                        "tags": ["tag 0", "tag 1"],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"$ref": "#/definitions/TestObject"},
                                    "type": "array",
                                },
                            }
                        },
                    },
                    "post": {
                        "operationId": "post_tags",
                        "tags": ["tag 1", "tag 2"],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"$ref": "#/definitions/TestObject"},
                                    "type": "array",
                                },
                            }
                        },
                    },
                    "put": {
                        "operationId": "put_tags",
                        "tags": ["tag 2", "tag 3"],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"$ref": "#/definitions/TestObject"},
                                    "type": "array",
                                },
                            }
                        },
                    },
                    "delete": {
                        "operationId": "delete_tags",
                        "tags": ["tag 3", "tag 4"],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"$ref": "#/definitions/TestObject"},
                                    "type": "array",
                                },
                            }
                        },
                    },
                }
            },
        },
        match_querystring=True,
    )


def test_post_with_selected_operation_ids_invalid_regex(
    responses: RequestsMock, filtered_operation_id_service, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "selected_operation_ids": {
                "open_api": {
                    "definition": "http://localhost:8944/",
                    "selected_operation_ids": ["["],
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert not hasattr(generated_functions, "selected_operation_ids_post_tags")


def test_get_with_excluded_operation_ids_invalid_regex(
    filtered_operation_id_service, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "excluded_operation_ids": {
                "open_api": {
                    "definition": "http://localhost:8944/",
                    "excluded_operation_ids": ["["],
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert hasattr(generated_functions, "excluded_operation_ids_get_tags")

import pytest
from responses import RequestsMock

from tests import loader


def test_missing_operation_id(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test",
        json={
            "swagger": "2.0",
            "paths": {
                "/without_operationId": {
                    "get": {"responses": {200: {"description": "successful operation"}}}
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "operation_id_not_provided": {
                "open_api": {"definition": "http://test"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/without_operationId",
        json={},
        match_querystring=True,
    )

    assert generated_functions.operation_id_not_provided_get_without_operationId() == [
        [""]
    ]


def test_mixed_operation_id(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test",
        json={
            "swagger": "2.0",
            "paths": {
                "/without_operationId": {
                    "get": {"responses": {200: {"description": "successful operation"}}}
                },
                "/with_operationId": {
                    "get": {
                        # This is obviously misleading but it can happen...
                        "operationId": "get_without_operationId",
                        "responses": {200: {"description": "successful operation"}},
                    }
                },
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "operation_id_not_always_provided": {
                "open_api": {"definition": "http://test"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/without_operationId",
        json=["first"],
        match_querystring=True,
    )

    assert (
        generated_functions.operation_id_not_always_provided_get_without_operationId()
        == [["first"]]
    )

    responses.add(
        responses.GET,
        url="http://test/with_operationId",
        json=["second"],
        match_querystring=True,
    )
    assert generated_functions.operation_id_not_always_provided_duplicated_get_without_operationId() == [
        ["second"]
    ]


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


def test_get_with_selected_operation_ids(
    responses: RequestsMock, filtered_operation_id_service, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "selected_operation_ids": {
                "open_api": {
                    "definition": "http://localhost:8944/",
                    "selected_operation_ids": ["get_tags", "post_tags", "put_tags"],
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET, url="http://localhost:8944/tags", json={}, match_querystring=True
    )

    assert generated_functions.selected_operation_ids_get_tags() == [[""]]


def test_post_with_selected_operation_ids(
    responses: RequestsMock, filtered_operation_id_service, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "selected_operation_ids": {
                "open_api": {
                    "definition": "http://localhost:8944/",
                    "selected_operation_ids": ["get_tags", "post_tags", "put_tags"],
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.POST,
        url="http://localhost:8944/tags",
        json={},
        match_querystring=True,
    )

    assert generated_functions.selected_operation_ids_post_tags() == [[""]]


def test_put_with_selected_operation_ids(
    responses: RequestsMock, filtered_operation_id_service, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "selected_operation_ids": {
                "open_api": {
                    "definition": "http://localhost:8944/",
                    "selected_operation_ids": ["get_tags", "post_tags", "put_tags"],
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.PUT, url="http://localhost:8944/tags", json={}, match_querystring=True
    )

    assert generated_functions.selected_operation_ids_put_tags() == [[""]]


def test_delete_with_selected_operation_ids(filtered_operation_id_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "selected_operation_ids": {
                "open_api": {
                    "definition": "http://localhost:8944/",
                    "selected_operation_ids": ["get_tags", "post_tags", "put_tags"],
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert not hasattr(generated_functions, "selected_operation_ids_delete_tags")


def test_get_with_excluded_operation_ids(filtered_operation_id_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "excluded_operation_ids": {
                "open_api": {
                    "definition": "http://localhost:8944/",
                    "excluded_operation_ids": ["get_tags", "post_tags", "put_tags"],
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert not hasattr(generated_functions, "excluded_operation_ids_get_tags")


def test_post_with_excluded_operation_ids(filtered_operation_id_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "excluded_operation_ids": {
                "open_api": {
                    "definition": "http://localhost:8944/",
                    "excluded_operation_ids": ["get_tags", "post_tags", "put_tags"],
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert not hasattr(generated_functions, "excluded_operation_ids_post_tags")


def test_put_with_excluded_operation_ids(filtered_operation_id_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "excluded_operation_ids": {
                "open_api": {
                    "definition": "http://localhost:8944/",
                    "excluded_operation_ids": ["get_tags", "post_tags", "put_tags"],
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert not hasattr(generated_functions, "excluded_operation_ids_put_tags")


def test_delete_with_excluded_operation_ids(
    responses: RequestsMock, filtered_operation_id_service, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "excluded_operation_ids": {
                "open_api": {
                    "definition": "http://localhost:8944/",
                    "excluded_operation_ids": ["get_tags", "post_tags", "put_tags"],
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.DELETE,
        url="http://localhost:8944/tags",
        json={},
        match_querystring=True,
    )

    assert generated_functions.excluded_operation_ids_delete_tags() == [[""]]

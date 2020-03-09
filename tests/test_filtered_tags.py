import pytest
from requests import PreparedRequest
from responses import RequestsMock

from tests import loader


@pytest.fixture
def filtered_tags_service(responses: RequestsMock):
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


def test_get_with_selected_tags(responses: RequestsMock, filtered_tags_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "selected_tags": {
                "open_api": {
                    "definition": "http://localhost:8944/",
                    "selected_tags": ["tag 1", "tag 2"],
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.GET, url="http://localhost:8944/tags", json={}, match_querystring=True
    )

    # Second tag is one of the accepted tags
    assert generated_functions.selected_tags_get_tags() == [[""]]


def test_post_with_selected_tags(
    responses: RequestsMock, filtered_tags_service, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "selected_tags": {
                "open_api": {
                    "definition": "http://localhost:8944/",
                    "selected_tags": ["tag 1", "tag 2"],
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.POST,
        url="http://localhost:8944/tags",
        json={},
        match_querystring=True,
    )

    # All tags are accepted
    assert generated_functions.selected_tags_post_tags() == [[""]]


def test_put_with_selected_tags(responses: RequestsMock, filtered_tags_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "selected_tags": {
                "open_api": {
                    "definition": "http://localhost:8944/",
                    "selected_tags": ["tag 1", "tag 2"],
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.PUT, url="http://localhost:8944/tags", json={}, match_querystring=True
    )

    # First tag is one of the accepted tags
    assert generated_functions.selected_tags_put_tags() == [[""]]


def test_delete_with_selected_tags(filtered_tags_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "selected_tags": {
                "open_api": {
                    "definition": "http://localhost:8944/",
                    "selected_tags": ["tag 1", "tag 2"],
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    assert not hasattr(generated_functions, "selected_tags_delete_tags")


def test_get_with_excluded_tags(filtered_tags_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "excluded_tags": {
                "open_api": {
                    "definition": "http://localhost:8944/",
                    "excluded_tags": ["tag 1", "tag 2"],
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    assert not hasattr(generated_functions, "excluded_tags_get_tags")


def test_post_with_excluded_tags(filtered_tags_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "excluded_tags": {
                "open_api": {
                    "definition": "http://localhost:8944/",
                    "excluded_tags": ["tag 1", "tag 2"],
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    assert not hasattr(generated_functions, "excluded_tags_post_tags")


def test_put_with_excluded_tags(filtered_tags_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "excluded_tags": {
                "open_api": {
                    "definition": "http://localhost:8944/",
                    "excluded_tags": ["tag 1", "tag 2"],
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    assert not hasattr(generated_functions, "excluded_tags_put_tags")


def test_delete_with_excluded_tags(
    responses: RequestsMock, filtered_tags_service, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "excluded_tags": {
                "open_api": {
                    "definition": "http://localhost:8944/",
                    "excluded_tags": ["tag 1", "tag 2"],
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.DELETE,
        url="http://localhost:8944/tags",
        json={},
        match_querystring=True,
    )

    assert generated_functions.excluded_tags_delete_tags() == [[""]]

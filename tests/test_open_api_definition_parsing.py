import pytest
from responses import RequestsMock

from tests import loader


@pytest.fixture
def open_api_definition_parsing_service(responses: RequestsMock):
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
    responses.add(
        responses.GET,
        url="http://localhost:8948/operation_id_not_provided",
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
    responses.add(
        responses.GET,
        url="http://localhost:8948/operation_id_not_always_provided",
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


def test_missing_operation_id(
    responses: RequestsMock, open_api_definition_parsing_service, tmpdir
):
    pyxelrestgenerator = loader.load(
        tmpdir,
        {
            "operation_id_not_provided": {
                "open_api": {
                    "definition": "http://localhost:8948/operation_id_not_provided"
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            },
            "operation_id_not_always_provided": {
                "open_api": {
                    "definition": "http://localhost:8948/operation_id_not_always_provided"
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            },
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8948/without_operationId",
        json={},
        match_querystring=True,
    )

    assert pyxelrestgenerator.operation_id_not_provided_get_without_operationId() == [
        [""]
    ]


def test_mixed_operation_id(
    responses: RequestsMock, open_api_definition_parsing_service, tmpdir
):
    pyxelrestgenerator = loader.load(
        tmpdir,
        {
            "operation_id_not_provided": {
                "open_api": {
                    "definition": "http://localhost:8948/operation_id_not_provided"
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            },
            "operation_id_not_always_provided": {
                "open_api": {
                    "definition": "http://localhost:8948/operation_id_not_always_provided"
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            },
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8948/with_operationId",
        json=["first"],
        match_querystring=True,
    )

    assert pyxelrestgenerator.operation_id_not_always_provided_get_without_operationId() == [
        "first"
    ]

    responses.add(
        responses.GET,
        url="http://localhost:8948/without_operationId",
        json=["second"],
        match_querystring=True,
    )
    assert pyxelrestgenerator.operation_id_not_always_provided_duplicated_get_without_operationId() == [
        "second"
    ]

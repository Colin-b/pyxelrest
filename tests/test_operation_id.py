import pytest
from responses import RequestsMock

from tests import loader


@pytest.fixture
def operation_id_services(responses: RequestsMock):
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


def test_missing_operation_id(responses: RequestsMock, operation_id_services, tmpdir):
    generated_functions = loader.load(
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

    assert generated_functions.operation_id_not_provided_get_without_operationId() == [
        [""]
    ]


def test_mixed_operation_id(responses: RequestsMock, operation_id_services, tmpdir):
    generated_functions = loader.load(
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
        json=["first"],
        match_querystring=True,
    )

    assert generated_functions.operation_id_not_always_provided_get_without_operationId() == [
        ["first"]
    ]

    responses.add(
        responses.GET,
        url="http://localhost:8948/with_operationId",
        json=["second"],
        match_querystring=True,
    )
    assert generated_functions.operation_id_not_always_provided_duplicated_get_without_operationId() == [
        ["second"]
    ]

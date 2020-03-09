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
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
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
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/without_operationId",
        json=["first"],
        match_querystring=True,
    )

    assert generated_functions.operation_id_not_always_provided_get_without_operationId() == [
        ["first"]
    ]

    responses.add(
        responses.GET,
        url="http://test/with_operationId",
        json=["second"],
        match_querystring=True,
    )
    assert generated_functions.operation_id_not_always_provided_duplicated_get_without_operationId() == [
        ["second"]
    ]

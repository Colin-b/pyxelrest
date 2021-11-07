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
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_test",
                        "responses": {
                            200: {
                                "type": "string",
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

    assert not hasattr(generated_functions, "selected_operation_ids_get_test")


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

    assert hasattr(generated_functions, "excluded_operation_ids_get_test")

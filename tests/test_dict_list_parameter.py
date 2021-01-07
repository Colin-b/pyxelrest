import pytest
from responses import RequestsMock

from tests import loader


@pytest.fixture
def json_service(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://localhost:8954/",
        json={
            "swagger": "2.0",
            "paths": {
                "/dicts": {
                    "post": {
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "payload",
                                "required": True,
                                "in": "body",
                                "type": "array",
                                "items": {
                                    "type": "object",
                                },
                            }
                        ],
                    }
                },
            },
        },
        match_querystring=True,
    )


def test_post_dict_list_parameter_without_list(
    json_service, tmpdir, responses: RequestsMock
):
    generated_functions = loader.load(
        tmpdir,
        {
            "dicts": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    assert (
        generated_functions.dicts_post_dicts("value")
        == """payload value "value" (<class 'str'> type) must be a list."""
    )


def test_post_dict_list_parameter_with_less_than_2_rows(
    json_service, tmpdir, responses: RequestsMock
):
    generated_functions = loader.load(
        tmpdir,
        {
            "dicts": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.dicts_post_dicts([["h1", "h2"]])
        == "payload value should contains at least two rows. Header and values."
    )

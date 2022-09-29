import pytest
from responses import RequestsMock

from tests import loader
from tests.request._request import _get_request


@pytest.fixture
def json_service(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://localhost:8954/",
        json={
            "swagger": "2.0",
            "definitions": {
                "min_and_max_items": {
                    "required": ["items", "rule_set"],
                    "properties": {
                        "rule_set": {
                            "type": "array",
                            "items": {
                                "type": "array",
                                "minItems": 2,
                                "maxItems": 3,
                                "items": {"type": "string"},
                            },
                        },
                        "items": {
                            "type": "array",
                            "items": {"type": "array", "items": {"type": "string"}},
                        },
                    },
                },
            },
            "paths": {
                "/min_and_max_items": {
                    "post": {
                        "operationId": "post_min_and_max_items",
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "payload",
                                "required": True,
                                "in": "body",
                                "schema": {"$ref": "#/definitions/min_and_max_items"},
                            }
                        ],
                    }
                },
            },
        },
        match_querystring=True,
    )


def test_post_min_and_max_items(json_service, responses, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(
        responses.POST,
        url="http://localhost:8954/min_and_max_items",
        json="OK",
        match_querystring=True,
    )

    assert generated_functions.json_post_min_and_max_items(
        items=[
            ["value10", "value11", "value12"],
            ["value20", "value21", "value22"],
            ["value30", "value31", "value32"],
        ],
        rule_set=[
            ["value10", "value11", "value12"],
            ["value20", "value21", "value22"],
            ["value30", "value31", "value32"],
        ],
    ) == [["OK"]]

    assert (
        _get_request(responses, "http://localhost:8954/min_and_max_items").body
        == b'{"rule_set": "value10,value11,value12,value20,value21,value22,value30,value31,value32", "items": "value10,value11,value12,value20,value21,value22,value30,value31,value32"}'
    )

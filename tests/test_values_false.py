import pytest
from requests import PreparedRequest
from responses import RequestsMock

from tests import loader


def _get_request(responses: RequestsMock, url: str) -> PreparedRequest:
    for call in responses.calls:
        if call.request.url == url:
            # Pop out verified request (to be able to check multiple requests)
            responses.calls._calls.remove(call)
            return call.request


@pytest.fixture
def values_false_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8945/",
        json={
            "swagger": "2.0",
            "definitions": {
                "ZeroInteger": {
                    "properties": {
                        "zero_integer": {"type": "integer", "format": "int32"}
                    }
                },
                "ZeroFloat": {
                    "properties": {"zero_float": {"type": "number", "format": "float"}}
                },
                "FalseBoolean": {"properties": {"false_boolean": {"type": "boolean"}}},
                "EmptyString": {"properties": {"empty_string": {"type": "string"}}},
                "EmptyList": {
                    "properties": {
                        "empty_list": {
                            "type": "array",
                            "items": {"$ref": "#/definitions/Empty"},
                        }
                    }
                },
                "EmptyDictionary": {
                    "properties": {
                        "empty_dictionary": {
                            "type": "object",
                            "$ref": "#/definitions/Empty",
                        }
                    }
                },
                "Empty": {"properties": {}},
            },
            "paths": {
                "/with/zero/integer": {
                    "get": {
                        "operationId": "get_with_zero_integer",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/definitions/ZeroInteger"},
                                },
                            }
                        },
                    }
                },
                "/with/zero/float": {
                    "get": {
                        "operationId": "get_with_zero_float",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/definitions/ZeroFloat"},
                                },
                            }
                        },
                    }
                },
                "/with/false/boolean": {
                    "get": {
                        "operationId": "get_with_false_boolean",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/definitions/FalseBoolean"},
                                },
                            }
                        },
                    }
                },
                "/with/empty/string": {
                    "get": {
                        "operationId": "get_with_empty_string",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/definitions/EmptyString"},
                                },
                            }
                        },
                    }
                },
                "/with/empty/list": {
                    "get": {
                        "operationId": "get_with_empty_list",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/definitions/EmptyList"},
                                },
                            }
                        },
                    }
                },
                "/with/empty/dictionary": {
                    "get": {
                        "operationId": "get_with_empty_dictionary",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/definitions/EmptyDictionary"},
                                },
                            }
                        },
                    }
                },
            },
        },
        match_querystring=True,
    )


@pytest.mark.parametrize(
    "service_config",
    [
        {
            "values_false": {
                "open_api": {"definition": "http://localhost:8945/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
        {
            "values_false": {
                "open_api": {
                    "definition": "http://localhost:8945/",
                    "rely_on_definitions": True,
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    ],
)
def test_get_with_zero_integer(
    responses: RequestsMock, values_false_service, tmpdir, service_config
):
    generated_functions = loader.load(tmpdir, service_config)
    responses.add(
        responses.GET,
        url="http://localhost:8945/with/zero/integer",
        json=[{"zero_integer": 0}],
        match_querystring=True,
    )

    assert generated_functions.values_false_get_with_zero_integer() == [
        ["zero_integer"],
        [0],
    ]


@pytest.mark.parametrize(
    "service_config",
    [
        {
            "values_false": {
                "open_api": {"definition": "http://localhost:8945/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
        {
            "values_false": {
                "open_api": {
                    "definition": "http://localhost:8945/",
                    "rely_on_definitions": True,
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    ],
)
def test_get_with_zero_float(
    responses: RequestsMock, values_false_service, tmpdir, service_config
):
    generated_functions = loader.load(tmpdir, service_config)
    responses.add(
        responses.GET,
        url="http://localhost:8945/with/zero/float",
        json=[{"zero_float": 0.0}],
        match_querystring=True,
    )

    assert generated_functions.values_false_get_with_zero_float() == [
        ["zero_float"],
        [0.0],
    ]


@pytest.mark.parametrize(
    "service_config",
    [
        {
            "values_false": {
                "open_api": {"definition": "http://localhost:8945/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
        {
            "values_false": {
                "open_api": {
                    "definition": "http://localhost:8945/",
                    "rely_on_definitions": True,
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    ],
)
def test_get_with_false_boolean(
    responses: RequestsMock, values_false_service, tmpdir, service_config
):
    generated_functions = loader.load(tmpdir, service_config)
    responses.add(
        responses.GET,
        url="http://localhost:8945/with/false/boolean",
        json=[{"false_boolean": False}],
        match_querystring=True,
    )

    assert generated_functions.values_false_get_with_false_boolean() == [
        ["false_boolean"],
        [False],
    ]


@pytest.mark.parametrize(
    "service_config",
    [
        {
            "values_false": {
                "open_api": {"definition": "http://localhost:8945/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
        {
            "values_false": {
                "open_api": {
                    "definition": "http://localhost:8945/",
                    "rely_on_definitions": True,
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    ],
)
def test_get_with_empty_string(
    responses: RequestsMock, values_false_service, tmpdir, service_config
):
    generated_functions = loader.load(tmpdir, service_config)
    responses.add(
        responses.GET,
        url="http://localhost:8945/with/empty/string",
        json=[{"empty_string": ""}],
        match_querystring=True,
    )

    assert generated_functions.values_false_get_with_empty_string() == [
        ["empty_string"],
        [""],
    ]


def test_get_with_empty_list(responses: RequestsMock, values_false_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "values_false": {
                "open_api": {"definition": "http://localhost:8945/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8945/with/empty/list",
        json=[{"empty_list": []}],
        match_querystring=True,
    )

    assert generated_functions.values_false_get_with_empty_list() == [
        ["empty_list"],
        [""],
    ]


def test_get_with_empty_dictionary(
    responses: RequestsMock, values_false_service, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "values_false": {
                "open_api": {"definition": "http://localhost:8945/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8945/with/empty/dictionary",
        json=[{"empty_dictionary": {}}],
        match_querystring=True,
    )

    assert generated_functions.values_false_get_with_empty_dictionary() == [
        ["empty_dictionary"],
        [""],
    ]

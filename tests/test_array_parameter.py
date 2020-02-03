import pytest
from requests import PreparedRequest
from responses import RequestsMock

from testsutils import loader


def _get_request(responses: RequestsMock, url: str) -> PreparedRequest:
    for call in responses.calls:
        if call.request.url == url:
            # Pop out verified request (to be able to check multiple requests)
            responses.calls._calls.remove(call)
            return call.request


@pytest.fixture
def array_parameter_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8953/",
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
                "/string_multi_array_parameter": {
                    "get": {
                        "operationId": "get_string_multi_array_parameter",
                        "parameters": [
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "string_array",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                                "collectionFormat": "multi",
                            }
                        ],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"$ref": "#/definitions/TestObject"},
                                    "type": "array",
                                },
                            }
                        },
                    }
                },
                "/string_default_array_parameter": {
                    "get": {
                        "operationId": "get_string_default_array_parameter",
                        "parameters": [
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "string_array",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                            }
                        ],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"$ref": "#/definitions/TestObject"},
                                    "type": "array",
                                },
                            }
                        },
                    }
                },
                "/string_csv_array_parameter": {
                    "get": {
                        "operationId": "get_string_csv_array_parameter",
                        "parameters": [
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "string_array",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                                "collectionFormat": "csv",
                            }
                        ],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"$ref": "#/definitions/TestObject"},
                                    "type": "array",
                                },
                            }
                        },
                    }
                },
                "/string_ssv_array_parameter": {
                    "get": {
                        "operationId": "get_string_ssv_array_parameter",
                        "parameters": [
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "string_array",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                                "collectionFormat": "ssv",
                            }
                        ],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"$ref": "#/definitions/TestObject"},
                                    "type": "array",
                                },
                            }
                        },
                    }
                },
                "/string_tsv_array_parameter": {
                    "get": {
                        "operationId": "get_string_tsv_array_parameter",
                        "parameters": [
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "string_array",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                                "collectionFormat": "tsv",
                            }
                        ],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"$ref": "#/definitions/TestObject"},
                                    "type": "array",
                                },
                            }
                        },
                    }
                },
                "/string_pipes_array_parameter": {
                    "get": {
                        "operationId": "get_string_pipes_array_parameter",
                        "parameters": [
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "string_array",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                                "collectionFormat": "pipes",
                            }
                        ],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"$ref": "#/definitions/TestObject"},
                                    "type": "array",
                                },
                            }
                        },
                    }
                },
            },
        },
        match_querystring=True,
    )


def test_string_multi_array_parameter(
    responses: RequestsMock, array_parameter_service, tmpdir
):
    pyxelrestgenerator = loader.load(
        tmpdir,
        {
            "array_parameter": {
                "open_api": {"definition": "http://localhost:8953/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8953/string_multi_array_parameter?string_array=str1&string_array=str2",
        json=[],
        match_querystring=True,
    )

    assert pyxelrestgenerator.array_parameter_get_string_multi_array_parameter(
        ["str1", "str2"]
    ) == [[""]]


def test_string_default_array_parameter(
    responses: RequestsMock, array_parameter_service, tmpdir
):
    pyxelrestgenerator = loader.load(
        tmpdir,
        {
            "array_parameter": {
                "open_api": {"definition": "http://localhost:8953/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8953/string_default_array_parameter?string_array=str1,str2",
        json=[],
        match_querystring=True,
    )

    assert pyxelrestgenerator.array_parameter_get_string_default_array_parameter(
        ["str1", "str2"]
    ) == [[""]]


def test_string_csv_array_parameter(
    responses: RequestsMock, array_parameter_service, tmpdir
):
    pyxelrestgenerator = loader.load(
        tmpdir,
        {
            "array_parameter": {
                "open_api": {"definition": "http://localhost:8953/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8953/string_csv_array_parameter?string_array=str1,str2",
        json=[],
        match_querystring=True,
    )

    assert pyxelrestgenerator.array_parameter_get_string_csv_array_parameter(
        ["str1", "str2"]
    ) == [[""]]


def test_string_ssv_array_parameter(
    responses: RequestsMock, array_parameter_service, tmpdir
):
    pyxelrestgenerator = loader.load(
        tmpdir,
        {
            "array_parameter": {
                "open_api": {"definition": "http://localhost:8953/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8953/string_ssv_array_parameter?string_array=str1 str2",
        json=[],
        match_querystring=True,
    )

    assert pyxelrestgenerator.array_parameter_get_string_ssv_array_parameter(
        ["str1", "str2"]
    ) == [[""]]


def test_string_tsv_array_parameter(
    responses: RequestsMock, array_parameter_service, tmpdir
):
    pyxelrestgenerator = loader.load(
        tmpdir,
        {
            "array_parameter": {
                "open_api": {"definition": "http://localhost:8953/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8953/string_tsv_array_parameter?string_array=str1\tstr2",
        json=[],
        match_querystring=True,
    )

    assert pyxelrestgenerator.array_parameter_get_string_tsv_array_parameter(
        ["str1", "str2"]
    ) == [[""]]


def test_string_pipes_array_parameter(
    responses: RequestsMock, array_parameter_service, tmpdir
):
    pyxelrestgenerator = loader.load(
        tmpdir,
        {
            "array_parameter": {
                "open_api": {"definition": "http://localhost:8953/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8953/string_pipes_array_parameter?string_array=str1|str2",
        json=[],
        match_querystring=True,
    )

    assert pyxelrestgenerator.array_parameter_get_string_pipes_array_parameter(
        ["str1", "str2"]
    ) == [[""]]

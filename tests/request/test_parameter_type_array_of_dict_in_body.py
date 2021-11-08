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
                "DictWithDict": {
                    "type": "object",
                    "properties": {
                        "inner_dict": {"type": "object"},
                        "dict_field1": {"type": "string"},
                        "dict_field2": {"type": "string"},
                    },
                    "title": "Test",
                },
                "DictWithDictAllowingNull": {
                    "type": "object",
                    "properties": {
                        "inner_dict": {"type": "object"},
                        "dict_field1": {"type": ["string", "null"]},
                        "dict_field2": {"type": ["null", "string"]},
                    },
                    "title": "Test",
                },
                "DictWithReadOnly": {
                    "type": "object",
                    "required": ["dict_field1"],
                    "properties": {
                        "dict_field1": {"type": "integer"},
                        "read_only_field": {"type": "string", "readOnly": True},
                        "dict_field3": {"type": "boolean"},
                    },
                    "title": "Test",
                },
            },
            "paths": {
                "/list_of_dict_with_dict": {
                    "post": {
                        "operationId": "post_list_of_dict_with_dict",
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "payload",
                                "required": True,
                                "in": "body",
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/definitions/DictWithDict"},
                                    "collectionFormat": "multi",
                                },
                            }
                        ],
                    }
                },
                "/list_of_dict_with_dict_allowing_null": {
                    "post": {
                        "operationId": "post_list_of_dict_with_dict_allowing_null",
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "payload",
                                "required": True,
                                "in": "body",
                                "schema": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/DictWithDictAllowingNull"
                                    },
                                    "collectionFormat": "multi",
                                },
                            }
                        ],
                    }
                },
                "/dict_with_read_only": {
                    "post": {
                        "operationId": "post_dict_with_read_only",
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "payload",
                                "required": True,
                                "in": "body",
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/definitions/DictWithReadOnly"},
                                    "collectionFormat": "multi",
                                },
                            }
                        ],
                    }
                },
            },
        },
        match_querystring=True,
    )


def test_list_of_dict_with_dict_json_post(
    json_service, tmpdir, responses: RequestsMock
):
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
        url="http://localhost:8954/list_of_dict_with_dict",
        json=[],
        match_querystring=True,
    )

    assert (
        generated_functions.json_post_list_of_dict_with_dict(
            inner_dict=[
                ["key1", "key2", "key3"],
                ["value10", "value20", "value30"],
                ["value11", "value21", "value31"],
                ["value12", "value22", "value32"],
            ],
            dict_field1=["value000", "value001", "value002"],
            dict_field2=["value010", "value011", "value012"],
        )
        == [[""]]
    )
    assert (
        _get_request(responses, "http://localhost:8954/list_of_dict_with_dict").body
        == b"""[{"inner_dict": {"key1": "value10", "key2": "value20", "key3": "value30"}, "dict_field1": "value000", "dict_field2": "value010"}, {"inner_dict": {"key1": "value11", "key2": "value21", "key3": "value31"}, "dict_field1": "value001", "dict_field2": "value011"}, {"inner_dict": {"key1": "value12", "key2": "value22", "key3": "value32"}, "dict_field1": "value002", "dict_field2": "value012"}]"""
    )


def test_list_of_dict_with_dict_json_post_without_any_required(
    json_service, tmpdir, responses: RequestsMock
):
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
        url="http://localhost:8954/list_of_dict_with_dict",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.json_post_list_of_dict_with_dict() == [[""]]
    assert (
        _get_request(responses, "http://localhost:8954/list_of_dict_with_dict").body
        == b"""[]"""
    )


def test_list_of_dict_with_dict_json_post_with_empty_lists(
    json_service, tmpdir, responses: RequestsMock
):
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
        url="http://localhost:8954/list_of_dict_with_dict",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.json_post_list_of_dict_with_dict(
        dict_field2=["1", None, "4"]
    ) == [[""]]
    assert (
        _get_request(responses, "http://localhost:8954/list_of_dict_with_dict").body
        == b"""[{"inner_dict": null, "dict_field1": null, "dict_field2": "1"}, {"inner_dict": null, "dict_field1": null, "dict_field2": "4"}]"""
    )


def test_list_of_dict_with_dict_json_post_with_different_list_length(
    json_service, tmpdir, responses: RequestsMock
):
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
        url="http://localhost:8954/list_of_dict_with_dict",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.json_post_list_of_dict_with_dict(
        dict_field1="000", dict_field2=["1", None, "4"]
    ) == [[""]]
    assert (
        _get_request(responses, "http://localhost:8954/list_of_dict_with_dict").body
        == b"""[{"inner_dict": null, "dict_field1": "000", "dict_field2": "1"}, {"inner_dict": null, "dict_field1": null, "dict_field2": "4"}]"""
    )


def test_list_of_dict_with_dict_allowing_null_json_post_without_any_required(
    json_service, tmpdir, responses: RequestsMock
):
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
        url="http://localhost:8954/list_of_dict_with_dict_allowing_null",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.json_post_list_of_dict_with_dict_allowing_null() == [
        [""]
    ]
    assert (
        _get_request(
            responses, "http://localhost:8954/list_of_dict_with_dict_allowing_null"
        ).body
        == b"[]"
    )


def test_list_of_dict_with_dict_allowing_null_json_post_with_empty_lists(
    json_service, tmpdir, responses: RequestsMock
):
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
        url="http://localhost:8954/list_of_dict_with_dict_allowing_null",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.json_post_list_of_dict_with_dict_allowing_null(
        dict_field2=["1", None, "4"]
    ) == [[""]]
    assert (
        _get_request(
            responses, "http://localhost:8954/list_of_dict_with_dict_allowing_null"
        ).body
        == b"""[{"inner_dict": null, "dict_field1": null, "dict_field2": "1"}, {"inner_dict": null, "dict_field1": null, "dict_field2": null}, {"inner_dict": null, "dict_field1": null, "dict_field2": "4"}]"""
    )


def test_list_of_dict_with_dict_allowing_null_json_post_with_different_list_length(
    json_service, tmpdir, responses: RequestsMock
):
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
        url="http://localhost:8954/list_of_dict_with_dict_allowing_null",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.json_post_list_of_dict_with_dict_allowing_null(
        dict_field1="000", dict_field2=["1", None, "4"]
    ) == [[""]]
    assert (
        _get_request(
            responses, "http://localhost:8954/list_of_dict_with_dict_allowing_null"
        ).body
        == b"""[{"inner_dict": null, "dict_field1": "000", "dict_field2": "1"}, {"inner_dict": null, "dict_field1": null, "dict_field2": null}, {"inner_dict": null, "dict_field1": null, "dict_field2": "4"}]"""
    )


def test_dict_with_read_only_json_post(json_service, tmpdir, responses: RequestsMock):
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
        url="http://localhost:8954/dict_with_read_only",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.json_post_dict_with_read_only(
        dict_field1=34, dict_field3=[False, True, True]
    ) == [[""]]

    assert (
        _get_request(responses, "http://localhost:8954/dict_with_read_only").body
        == b"""[{"dict_field1": 34, "dict_field3": false}, {"dict_field1": null, "dict_field3": true}, {"dict_field1": null, "dict_field3": true}]"""
    )


def test_dict_with_read_only_json_post_do_not_provide_read_only_parameter(
    json_service, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    with pytest.raises(Exception) as exception_info:
        generated_functions.json_post_dict_with_read_only(
            dict_field1=34, read_only_field="test", dict_field3=[False, True, True]
        )
    assert (
        str(exception_info.value)
        == "json_post_dict_with_read_only() got an unexpected keyword argument 'read_only_field'"
    )

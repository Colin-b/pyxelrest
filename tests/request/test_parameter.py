import datetime

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
                "Dict": {
                    "type": "object",
                    "required": ["dict_field1"],
                    "properties": {
                        "dict_field1": {"type": "string"},
                        "dict_field2": {"type": "string"},
                    },
                    "title": "Test",
                },
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
                "DictWithDictList": {
                    "type": "object",
                    "properties": {
                        "inner_dict_list": {
                            "type": "array",
                            "items": {"$ref": "#/definitions/Dict"},
                            "collectionFormat": "multi",
                        },
                        "dict_field1": {"type": "string"},
                        "dict_field2": {"type": "string"},
                    },
                    "title": "Test",
                },
                "DictWithListOfList": {
                    "type": "object",
                    "properties": {
                        "inner_list_of_list": {
                            "type": "array",
                            "items": {
                                "type": "array",
                                "items": {"type": "string"},
                                "collectionFormat": "multi",
                            },
                            "collectionFormat": "multi",
                        },
                        "dict_field1": {"type": "string"},
                        "dict_field2": {"type": "string"},
                    },
                    "title": "Test",
                },
                "TestObject": {
                    "type": "object",
                    "properties": {"test": {"type": "string", "description": "test"}},
                    "title": "Test",
                },
                "AllMandatoryParameters": {
                    "properties": {
                        "query_array_boolean": {},
                        "query_array_date": {
                            "type": "array",
                            "items": {"type": "string", "format": "date"},
                            "collectionFormat": "multi",
                        },
                        "query_array_date_time": {
                            "type": "array",
                            "items": {"type": "string", "format": "date-time"},
                            "collectionFormat": "multi",
                        },
                        "query_array_double": {},
                        "query_array_float": {},
                        "query_array_integer": {},
                        "query_array_integer32": {},
                        "query_array_integer64": {},
                        "query_array_number": {},
                        "query_array_password": {},
                        "query_array_string": {},
                        "query_array_string_binary": {},
                        "query_array_string_byte": {},
                        "query_boolean": {},
                        "query_date": {"type": "string", "format": "date"},
                        "query_date_time": {"type": "string", "format": "date-time"},
                        "query_double": {},
                        "query_float": {},
                        "query_integer": {},
                        "query_integer32": {},
                        "query_integer64": {},
                        "query_number": {},
                        "query_password": {},
                        "query_string": {},
                        "query_string_binary": {},
                        "query_string_byte": {},
                    }
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
                "/list_dict_no_ref": {
                    "post": {
                        "operationId": "post_list_dict_no_ref",
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "payload",
                                "required": True,
                                "in": "body",
                                "schema": {
                                    "type": "array",
                                    "items": {"type": "object"},
                                },
                            }
                        ],
                    }
                },
                "/different_location_same_name/{dict_field1}": {
                    "post": {
                        "operationId": "post_different_location_same_name",
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "payload",
                                "required": True,
                                "in": "body",
                                "schema": {"$ref": "#/definitions/Dict"},
                            },
                            {
                                "name": "dict_field1",
                                "required": True,
                                "in": "header",
                                "type": "string",
                            },
                            {
                                "name": "dict_field1",
                                "required": True,
                                "in": "query",
                                "type": "string",
                            },
                            {
                                "name": "dict_field1",
                                "required": True,
                                "in": "path",
                                "type": "string",
                            },
                        ],
                    }
                },
                "/list_parameter": {
                    "get": {
                        "operationId": "get_list_parameter",
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "list_parameter",
                                "required": True,
                                "in": "query",
                                "type": "string",
                            }
                        ],
                    },
                    "delete": {
                        "operationId": "delete_list_parameter",
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "list_parameter",
                                "required": True,
                                "in": "query",
                                "type": "string",
                            }
                        ],
                    },
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
                "/dict_string": {
                    "post": {
                        "operationId": "post_dict_string",
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "payload",
                                "required": True,
                                "in": "body",
                                "schema": {"$ref": "#/definitions/Dict"},
                            }
                        ],
                    }
                },
                "/dict_with_list_of_list": {
                    "post": {
                        "operationId": "post_dict_with_list_of_list",
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "payload",
                                "required": True,
                                "in": "body",
                                "schema": {"$ref": "#/definitions/DictWithListOfList"},
                            }
                        ],
                    }
                },
                "/dict_with_dict_list": {
                    "post": {
                        "operationId": "post_dict_with_dict_list",
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "payload",
                                "required": True,
                                "in": "body",
                                "schema": {"$ref": "#/definitions/DictWithDictList"},
                            }
                        ],
                    }
                },
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
                "/dict_with_dict": {
                    "post": {
                        "operationId": "post_dict_with_dict",
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "payload",
                                "required": True,
                                "in": "body",
                                "schema": {"$ref": "#/definitions/DictWithDict"},
                            }
                        ],
                    }
                },
                "/list_of_list_form": {
                    "post": {
                        "operationId": "post_list_of_list_form",
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {"name": "all_matching", "in": "query", "type": "boolean"},
                            {
                                "name": "rules",
                                "in": "formData",
                                "collectionFormat": "multi",
                                "type": "array",
                                "items": {"items": {"type": "string"}, "type": "array"},
                            },
                            {
                                "name": "items",
                                "in": "formData",
                                "collectionFormat": "multi",
                                "type": "array",
                                "items": {"items": {"type": "string"}, "type": "array"},
                            },
                        ],
                        "consumes": [
                            "application/x-www-form-urlencoded",
                            "multipart/form-data",
                        ],
                    }
                },
                "/all_parameters_types": {
                    "get": {
                        "operationId": "get_all_parameters_types",
                        "produces": ["application/json"],
                        "parameters": [
                            {
                                "description": "integer parameter",
                                "in": "query",
                                "name": "query_integer",
                                "required": True,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 parameter",
                                "in": "query",
                                "name": "query_integer32",
                                "required": True,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 parameter",
                                "in": "query",
                                "name": "query_integer64",
                                "required": True,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number parameter",
                                "in": "query",
                                "name": "query_number",
                                "required": True,
                                "type": "number",
                            },
                            {
                                "description": "number float parameter",
                                "in": "query",
                                "name": "query_float",
                                "required": True,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double parameter",
                                "in": "query",
                                "name": "query_double",
                                "required": True,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string parameter",
                                "in": "query",
                                "name": "query_string",
                                "required": True,
                                "type": "string",
                            },
                            {
                                "description": "string byte parameter",
                                "in": "query",
                                "name": "query_string_byte",
                                "required": True,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary parameter",
                                "in": "query",
                                "name": "query_string_binary",
                                "required": True,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean parameter",
                                "in": "query",
                                "name": "query_boolean",
                                "required": True,
                                "type": "boolean",
                            },
                            {
                                "description": "date parameter",
                                "in": "query",
                                "name": "query_date",
                                "required": True,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time parameter",
                                "in": "query",
                                "name": "query_date_time",
                                "required": True,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password parameter",
                                "in": "query",
                                "name": "query_password",
                                "required": True,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array parameter",
                                "in": "query",
                                "name": "query_array_integer",
                                "required": True,
                                "items": {"type": "integer"},
                                "type": "array",
                                "collectionFormat": "multi",
                            },
                            {
                                "description": "integer 32 array parameter",
                                "in": "query",
                                "name": "query_array_integer32",
                                "required": True,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                                "collectionFormat": "multi",
                            },
                            {
                                "description": "integer 64 array parameter",
                                "in": "query",
                                "name": "query_array_integer64",
                                "required": True,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                                "collectionFormat": "multi",
                            },
                            {
                                "description": "number array parameter",
                                "in": "query",
                                "name": "query_array_number",
                                "required": True,
                                "items": {"type": "number"},
                                "type": "array",
                                "collectionFormat": "multi",
                            },
                            {
                                "description": "number float array parameter",
                                "in": "query",
                                "name": "query_array_float",
                                "required": True,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                                "collectionFormat": "multi",
                            },
                            {
                                "description": "number double array parameter",
                                "in": "query",
                                "name": "query_array_double",
                                "required": True,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                                "collectionFormat": "multi",
                            },
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "query_array_string",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                                "collectionFormat": "multi",
                            },
                            {
                                "description": "string byte array parameter",
                                "in": "query",
                                "name": "query_array_string_byte",
                                "required": True,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                                "collectionFormat": "multi",
                            },
                            {
                                "description": "string binary array parameter",
                                "in": "query",
                                "name": "query_array_string_binary",
                                "required": True,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                                "collectionFormat": "multi",
                            },
                            {
                                "description": "boolean array parameter",
                                "in": "query",
                                "name": "query_array_boolean",
                                "required": True,
                                "items": {"type": "boolean"},
                                "type": "array",
                                "collectionFormat": "multi",
                            },
                            {
                                "description": "date array parameter",
                                "in": "query",
                                "name": "query_array_date",
                                "required": True,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                                "collectionFormat": "multi",
                            },
                            {
                                "description": "date time array parameter",
                                "in": "query",
                                "name": "query_array_date_time",
                                "required": True,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                                "collectionFormat": "multi",
                            },
                            {
                                "description": "password array parameter",
                                "in": "query",
                                "name": "query_array_password",
                                "required": True,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                                "collectionFormat": "multi",
                            },
                        ],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "$ref": "#/definitions/AllMandatoryParameters"
                                },
                            }
                        },
                    },
                    "post": {
                        "operationId": "post_all_parameters_types",
                        "produces": ["application/json"],
                        "parameters": [
                            {
                                "description": "integer parameter",
                                "in": "query",
                                "name": "query_integer",
                                "required": True,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 parameter",
                                "in": "query",
                                "name": "query_integer32",
                                "required": True,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 parameter",
                                "in": "query",
                                "name": "query_integer64",
                                "required": True,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number parameter",
                                "in": "query",
                                "name": "query_number",
                                "required": True,
                                "type": "number",
                            },
                            {
                                "description": "number float parameter",
                                "in": "query",
                                "name": "query_float",
                                "required": True,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double parameter",
                                "in": "query",
                                "name": "query_double",
                                "required": True,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string parameter",
                                "in": "query",
                                "name": "query_string",
                                "required": True,
                                "type": "string",
                            },
                            {
                                "description": "string byte parameter",
                                "in": "query",
                                "name": "query_string_byte",
                                "required": True,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary parameter",
                                "in": "query",
                                "name": "query_string_binary",
                                "required": True,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean parameter",
                                "in": "query",
                                "name": "query_boolean",
                                "required": True,
                                "type": "boolean",
                            },
                            {
                                "description": "date parameter",
                                "in": "query",
                                "name": "query_date",
                                "required": True,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time parameter",
                                "in": "query",
                                "name": "query_date_time",
                                "required": True,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password parameter",
                                "in": "query",
                                "name": "query_password",
                                "required": True,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array parameter",
                                "in": "query",
                                "name": "query_array_integer",
                                "required": True,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array parameter",
                                "in": "query",
                                "name": "query_array_integer32",
                                "required": True,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array parameter",
                                "in": "query",
                                "name": "query_array_integer64",
                                "required": True,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array parameter",
                                "in": "query",
                                "name": "query_array_number",
                                "required": True,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array parameter",
                                "in": "query",
                                "name": "query_array_float",
                                "required": True,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array parameter",
                                "in": "query",
                                "name": "query_array_double",
                                "required": True,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "query_array_string",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array parameter",
                                "in": "query",
                                "name": "query_array_string_byte",
                                "required": True,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array parameter",
                                "in": "query",
                                "name": "query_array_string_binary",
                                "required": True,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array parameter",
                                "in": "query",
                                "name": "query_array_boolean",
                                "required": True,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array parameter",
                                "in": "query",
                                "name": "query_array_date",
                                "required": True,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array parameter",
                                "in": "query",
                                "name": "query_array_date_time",
                                "required": True,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array parameter",
                                "in": "query",
                                "name": "query_array_password",
                                "required": True,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
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
                    },
                    "put": {
                        "operationId": "put_all_parameters_types",
                        "produces": ["application/json"],
                        "parameters": [
                            {
                                "description": "integer parameter",
                                "in": "query",
                                "name": "query_integer",
                                "required": True,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 parameter",
                                "in": "query",
                                "name": "query_integer32",
                                "required": True,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 parameter",
                                "in": "query",
                                "name": "query_integer64",
                                "required": True,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number parameter",
                                "in": "query",
                                "name": "query_number",
                                "required": True,
                                "type": "number",
                            },
                            {
                                "description": "number float parameter",
                                "in": "query",
                                "name": "query_float",
                                "required": True,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double parameter",
                                "in": "query",
                                "name": "query_double",
                                "required": True,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string parameter",
                                "in": "query",
                                "name": "query_string",
                                "required": True,
                                "type": "string",
                            },
                            {
                                "description": "string byte parameter",
                                "in": "query",
                                "name": "query_string_byte",
                                "required": True,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary parameter",
                                "in": "query",
                                "name": "query_string_binary",
                                "required": True,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean parameter",
                                "in": "query",
                                "name": "query_boolean",
                                "required": True,
                                "type": "boolean",
                            },
                            {
                                "description": "date parameter",
                                "in": "query",
                                "name": "query_date",
                                "required": True,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time parameter",
                                "in": "query",
                                "name": "query_date_time",
                                "required": True,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password parameter",
                                "in": "query",
                                "name": "query_password",
                                "required": True,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array parameter",
                                "in": "query",
                                "name": "query_array_integer",
                                "required": True,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array parameter",
                                "in": "query",
                                "name": "query_array_integer32",
                                "required": True,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array parameter",
                                "in": "query",
                                "name": "query_array_integer64",
                                "required": True,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array parameter",
                                "in": "query",
                                "name": "query_array_number",
                                "required": True,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array parameter",
                                "in": "query",
                                "name": "query_array_float",
                                "required": True,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array parameter",
                                "in": "query",
                                "name": "query_array_double",
                                "required": True,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "query_array_string",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array parameter",
                                "in": "query",
                                "name": "query_array_string_byte",
                                "required": True,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array parameter",
                                "in": "query",
                                "name": "query_array_string_binary",
                                "required": True,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array parameter",
                                "in": "query",
                                "name": "query_array_boolean",
                                "required": True,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array parameter",
                                "in": "query",
                                "name": "query_array_date",
                                "required": True,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array parameter",
                                "in": "query",
                                "name": "query_array_date_time",
                                "required": True,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array parameter",
                                "in": "query",
                                "name": "query_array_password",
                                "required": True,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
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
                    },
                    "delete": {
                        "operationId": "delete_all_parameters_types",
                        "produces": ["application/json"],
                        "parameters": [
                            {
                                "description": "integer parameter",
                                "in": "query",
                                "name": "query_integer",
                                "required": True,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 parameter",
                                "in": "query",
                                "name": "query_integer32",
                                "required": True,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 parameter",
                                "in": "query",
                                "name": "query_integer64",
                                "required": True,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number parameter",
                                "in": "query",
                                "name": "query_number",
                                "required": True,
                                "type": "number",
                            },
                            {
                                "description": "number float parameter",
                                "in": "query",
                                "name": "query_float",
                                "required": True,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double parameter",
                                "in": "query",
                                "name": "query_double",
                                "required": True,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string parameter",
                                "in": "query",
                                "name": "query_string",
                                "required": True,
                                "type": "string",
                            },
                            {
                                "description": "string byte parameter",
                                "in": "query",
                                "name": "query_string_byte",
                                "required": True,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary parameter",
                                "in": "query",
                                "name": "query_string_binary",
                                "required": True,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean parameter",
                                "in": "query",
                                "name": "query_boolean",
                                "required": True,
                                "type": "boolean",
                            },
                            {
                                "description": "date parameter",
                                "in": "query",
                                "name": "query_date",
                                "required": True,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time parameter",
                                "in": "query",
                                "name": "query_date_time",
                                "required": True,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password parameter",
                                "in": "query",
                                "name": "query_password",
                                "required": True,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array parameter",
                                "in": "query",
                                "name": "query_array_integer",
                                "required": True,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array parameter",
                                "in": "query",
                                "name": "query_array_integer32",
                                "required": True,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array parameter",
                                "in": "query",
                                "name": "query_array_integer64",
                                "required": True,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array parameter",
                                "in": "query",
                                "name": "query_array_number",
                                "required": True,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array parameter",
                                "in": "query",
                                "name": "query_array_float",
                                "required": True,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array parameter",
                                "in": "query",
                                "name": "query_array_double",
                                "required": True,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "query_array_string",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array parameter",
                                "in": "query",
                                "name": "query_array_string_byte",
                                "required": True,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array parameter",
                                "in": "query",
                                "name": "query_array_string_binary",
                                "required": True,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array parameter",
                                "in": "query",
                                "name": "query_array_boolean",
                                "required": True,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array parameter",
                                "in": "query",
                                "name": "query_array_date",
                                "required": True,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array parameter",
                                "in": "query",
                                "name": "query_array_date_time",
                                "required": True,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array parameter",
                                "in": "query",
                                "name": "query_array_password",
                                "required": True,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
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
                    },
                },
                "/all_optional_parameters_types": {
                    "get": {
                        "operationId": "get_all_optional_parameters_types",
                        "produces": ["application/json"],
                        "parameters": [
                            {
                                "description": "integer parameter",
                                "in": "query",
                                "name": "query_integer",
                                "required": False,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 parameter",
                                "in": "query",
                                "name": "query_integer32",
                                "required": False,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 parameter",
                                "in": "query",
                                "name": "query_integer64",
                                "required": False,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number parameter",
                                "in": "query",
                                "name": "query_number",
                                "required": False,
                                "type": "number",
                            },
                            {
                                "description": "number float parameter",
                                "in": "query",
                                "name": "query_float",
                                "required": False,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double parameter",
                                "in": "query",
                                "name": "query_double",
                                "required": False,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string parameter",
                                "in": "query",
                                "name": "query_string",
                                "required": False,
                                "type": "string",
                            },
                            {
                                "description": "string byte parameter",
                                "in": "query",
                                "name": "query_string_byte",
                                "required": False,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary parameter",
                                "in": "query",
                                "name": "query_string_binary",
                                "required": False,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean parameter",
                                "in": "query",
                                "name": "query_boolean",
                                "required": False,
                                "type": "boolean",
                            },
                            {
                                "description": "date parameter",
                                "in": "query",
                                "name": "query_date",
                                "required": False,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time parameter",
                                "in": "query",
                                "name": "query_date_time",
                                "required": False,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password parameter",
                                "in": "query",
                                "name": "query_password",
                                "required": False,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array parameter",
                                "in": "query",
                                "name": "query_array_integer",
                                "required": False,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array parameter",
                                "in": "query",
                                "name": "query_array_integer32",
                                "required": False,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array parameter",
                                "in": "query",
                                "name": "query_array_integer64",
                                "required": False,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array parameter",
                                "in": "query",
                                "name": "query_array_number",
                                "required": False,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array parameter",
                                "in": "query",
                                "name": "query_array_float",
                                "required": False,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array parameter",
                                "in": "query",
                                "name": "query_array_double",
                                "required": False,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "query_array_string",
                                "required": False,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array parameter",
                                "in": "query",
                                "name": "query_array_string_byte",
                                "required": False,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array parameter",
                                "in": "query",
                                "name": "query_array_string_binary",
                                "required": False,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array parameter",
                                "in": "query",
                                "name": "query_array_boolean",
                                "required": False,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array parameter",
                                "in": "query",
                                "name": "query_array_date",
                                "required": False,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array parameter",
                                "in": "query",
                                "name": "query_array_date_time",
                                "required": False,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array parameter",
                                "in": "query",
                                "name": "query_array_password",
                                "required": False,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
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
                    },
                    "post": {
                        "operationId": "post_all_optional_parameters_types",
                        "produces": ["application/json"],
                        "parameters": [
                            {
                                "description": "integer parameter",
                                "in": "query",
                                "name": "query_integer",
                                "required": False,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 parameter",
                                "in": "query",
                                "name": "query_integer32",
                                "required": False,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 parameter",
                                "in": "query",
                                "name": "query_integer64",
                                "required": False,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number parameter",
                                "in": "query",
                                "name": "query_number",
                                "required": False,
                                "type": "number",
                            },
                            {
                                "description": "number float parameter",
                                "in": "query",
                                "name": "query_float",
                                "required": False,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double parameter",
                                "in": "query",
                                "name": "query_double",
                                "required": False,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string parameter",
                                "in": "query",
                                "name": "query_string",
                                "required": False,
                                "type": "string",
                            },
                            {
                                "description": "string byte parameter",
                                "in": "query",
                                "name": "query_string_byte",
                                "required": False,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary parameter",
                                "in": "query",
                                "name": "query_string_binary",
                                "required": False,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean parameter",
                                "in": "query",
                                "name": "query_boolean",
                                "required": False,
                                "type": "boolean",
                            },
                            {
                                "description": "date parameter",
                                "in": "query",
                                "name": "query_date",
                                "required": False,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time parameter",
                                "in": "query",
                                "name": "query_date_time",
                                "required": False,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password parameter",
                                "in": "query",
                                "name": "query_password",
                                "required": False,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array parameter",
                                "in": "query",
                                "name": "query_array_integer",
                                "required": False,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array parameter",
                                "in": "query",
                                "name": "query_array_integer32",
                                "required": False,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array parameter",
                                "in": "query",
                                "name": "query_array_integer64",
                                "required": False,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array parameter",
                                "in": "query",
                                "name": "query_array_number",
                                "required": False,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array parameter",
                                "in": "query",
                                "name": "query_array_float",
                                "required": False,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array parameter",
                                "in": "query",
                                "name": "query_array_double",
                                "required": False,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "query_array_string",
                                "required": False,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array parameter",
                                "in": "query",
                                "name": "query_array_string_byte",
                                "required": False,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array parameter",
                                "in": "query",
                                "name": "query_array_string_binary",
                                "required": False,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array parameter",
                                "in": "query",
                                "name": "query_array_boolean",
                                "required": False,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array parameter",
                                "in": "query",
                                "name": "query_array_date",
                                "required": False,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array parameter",
                                "in": "query",
                                "name": "query_array_date_time",
                                "required": False,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array parameter",
                                "in": "query",
                                "name": "query_array_password",
                                "required": False,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
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
                    },
                    "put": {
                        "operationId": "put_all_optional_parameters_types",
                        "produces": ["application/json"],
                        "parameters": [
                            {
                                "description": "integer parameter",
                                "in": "query",
                                "name": "query_integer",
                                "required": False,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 parameter",
                                "in": "query",
                                "name": "query_integer32",
                                "required": False,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 parameter",
                                "in": "query",
                                "name": "query_integer64",
                                "required": False,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number parameter",
                                "in": "query",
                                "name": "query_number",
                                "required": False,
                                "type": "number",
                            },
                            {
                                "description": "number float parameter",
                                "in": "query",
                                "name": "query_float",
                                "required": False,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double parameter",
                                "in": "query",
                                "name": "query_double",
                                "required": False,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string parameter",
                                "in": "query",
                                "name": "query_string",
                                "required": False,
                                "type": "string",
                            },
                            {
                                "description": "string byte parameter",
                                "in": "query",
                                "name": "query_string_byte",
                                "required": False,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary parameter",
                                "in": "query",
                                "name": "query_string_binary",
                                "required": False,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean parameter",
                                "in": "query",
                                "name": "query_boolean",
                                "required": False,
                                "type": "boolean",
                            },
                            {
                                "description": "date parameter",
                                "in": "query",
                                "name": "query_date",
                                "required": False,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time parameter",
                                "in": "query",
                                "name": "query_date_time",
                                "required": False,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password parameter",
                                "in": "query",
                                "name": "query_password",
                                "required": False,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array parameter",
                                "in": "query",
                                "name": "query_array_integer",
                                "required": False,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array parameter",
                                "in": "query",
                                "name": "query_array_integer32",
                                "required": False,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array parameter",
                                "in": "query",
                                "name": "query_array_integer64",
                                "required": False,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array parameter",
                                "in": "query",
                                "name": "query_array_number",
                                "required": False,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array parameter",
                                "in": "query",
                                "name": "query_array_float",
                                "required": False,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array parameter",
                                "in": "query",
                                "name": "query_array_double",
                                "required": False,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "query_array_string",
                                "required": False,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array parameter",
                                "in": "query",
                                "name": "query_array_string_byte",
                                "required": False,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array parameter",
                                "in": "query",
                                "name": "query_array_string_binary",
                                "required": False,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array parameter",
                                "in": "query",
                                "name": "query_array_boolean",
                                "required": False,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array parameter",
                                "in": "query",
                                "name": "query_array_date",
                                "required": False,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array parameter",
                                "in": "query",
                                "name": "query_array_date_time",
                                "required": False,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array parameter",
                                "in": "query",
                                "name": "query_array_password",
                                "required": False,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
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
                    },
                    "delete": {
                        "operationId": "delete_all_optional_parameters_types",
                        "produces": ["application/json"],
                        "parameters": [
                            {
                                "description": "integer parameter",
                                "in": "query",
                                "name": "query_integer",
                                "required": False,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 parameter",
                                "in": "query",
                                "name": "query_integer32",
                                "required": False,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 parameter",
                                "in": "query",
                                "name": "query_integer64",
                                "required": False,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number parameter",
                                "in": "query",
                                "name": "query_number",
                                "required": False,
                                "type": "number",
                            },
                            {
                                "description": "number float parameter",
                                "in": "query",
                                "name": "query_float",
                                "required": False,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double parameter",
                                "in": "query",
                                "name": "query_double",
                                "required": False,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string parameter",
                                "in": "query",
                                "name": "query_string",
                                "required": False,
                                "type": "string",
                            },
                            {
                                "description": "string byte parameter",
                                "in": "query",
                                "name": "query_string_byte",
                                "required": False,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary parameter",
                                "in": "query",
                                "name": "query_string_binary",
                                "required": False,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean parameter",
                                "in": "query",
                                "name": "query_boolean",
                                "required": False,
                                "type": "boolean",
                            },
                            {
                                "description": "date parameter",
                                "in": "query",
                                "name": "query_date",
                                "required": False,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time parameter",
                                "in": "query",
                                "name": "query_date_time",
                                "required": False,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password parameter",
                                "in": "query",
                                "name": "query_password",
                                "required": False,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array parameter",
                                "in": "query",
                                "name": "query_array_integer",
                                "required": False,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array parameter",
                                "in": "query",
                                "name": "query_array_integer32",
                                "required": False,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array parameter",
                                "in": "query",
                                "name": "query_array_integer64",
                                "required": False,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array parameter",
                                "in": "query",
                                "name": "query_array_number",
                                "required": False,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array parameter",
                                "in": "query",
                                "name": "query_array_float",
                                "required": False,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array parameter",
                                "in": "query",
                                "name": "query_array_double",
                                "required": False,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "query_array_string",
                                "required": False,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array parameter",
                                "in": "query",
                                "name": "query_array_string_byte",
                                "required": False,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array parameter",
                                "in": "query",
                                "name": "query_array_string_binary",
                                "required": False,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array parameter",
                                "in": "query",
                                "name": "query_array_boolean",
                                "required": False,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array parameter",
                                "in": "query",
                                "name": "query_array_date",
                                "required": False,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array parameter",
                                "in": "query",
                                "name": "query_array_date_time",
                                "required": False,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array parameter",
                                "in": "query",
                                "name": "query_array_password",
                                "required": False,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
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
                    },
                },
                "/all_paths_types": {
                    "get": {
                        "operationId": "get_all_paths_types",
                        "produces": ["application/json"],
                        "parameters": [
                            {
                                "description": "integer path",
                                "in": "path",
                                "name": "path_integer",
                                "required": True,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 path",
                                "in": "path",
                                "name": "path_integer32",
                                "required": True,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 path",
                                "in": "path",
                                "name": "path_integer64",
                                "required": True,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number path",
                                "in": "path",
                                "name": "path_number",
                                "required": True,
                                "type": "number",
                            },
                            {
                                "description": "number float path",
                                "in": "path",
                                "name": "path_float",
                                "required": True,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double path",
                                "in": "path",
                                "name": "path_double",
                                "required": True,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string path",
                                "in": "path",
                                "name": "path_string",
                                "required": True,
                                "type": "string",
                            },
                            {
                                "description": "string byte path",
                                "in": "path",
                                "name": "path_string_byte",
                                "required": True,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary path",
                                "in": "path",
                                "name": "path_string_binary",
                                "required": True,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean path",
                                "in": "path",
                                "name": "path_boolean",
                                "required": True,
                                "type": "boolean",
                            },
                            {
                                "description": "date path",
                                "in": "path",
                                "name": "path_date",
                                "required": True,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time path",
                                "in": "path",
                                "name": "path_date_time",
                                "required": True,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password path",
                                "in": "path",
                                "name": "path_password",
                                "required": True,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array path",
                                "in": "path",
                                "name": "path_array_integer",
                                "required": True,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array path",
                                "in": "path",
                                "name": "path_array_integer32",
                                "required": True,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array path",
                                "in": "path",
                                "name": "path_array_integer64",
                                "required": True,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array path",
                                "in": "path",
                                "name": "path_array_number",
                                "required": True,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array path",
                                "in": "path",
                                "name": "path_array_float",
                                "required": True,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array path",
                                "in": "path",
                                "name": "path_array_double",
                                "required": True,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array path",
                                "in": "path",
                                "name": "path_array_string",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array path",
                                "in": "path",
                                "name": "path_array_string_byte",
                                "required": True,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array path",
                                "in": "path",
                                "name": "path_array_string_binary",
                                "required": True,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array path",
                                "in": "path",
                                "name": "path_array_boolean",
                                "required": True,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array path",
                                "in": "path",
                                "name": "path_array_date",
                                "required": True,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array path",
                                "in": "path",
                                "name": "path_array_date_time",
                                "required": True,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array path",
                                "in": "path",
                                "name": "path_array_password",
                                "required": True,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
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
                    },
                    "post": {
                        "operationId": "post_all_paths_types",
                        "produces": ["application/json"],
                        "parameters": [
                            {
                                "description": "integer path",
                                "in": "path",
                                "name": "path_integer",
                                "required": True,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 path",
                                "in": "path",
                                "name": "path_integer32",
                                "required": True,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 path",
                                "in": "path",
                                "name": "path_integer64",
                                "required": True,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number path",
                                "in": "path",
                                "name": "path_number",
                                "required": True,
                                "type": "number",
                            },
                            {
                                "description": "number float path",
                                "in": "path",
                                "name": "path_float",
                                "required": True,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double path",
                                "in": "path",
                                "name": "path_double",
                                "required": True,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string path",
                                "in": "path",
                                "name": "path_string",
                                "required": True,
                                "type": "string",
                            },
                            {
                                "description": "string byte path",
                                "in": "path",
                                "name": "path_string_byte",
                                "required": True,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary path",
                                "in": "path",
                                "name": "path_string_binary",
                                "required": True,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean path",
                                "in": "path",
                                "name": "path_boolean",
                                "required": True,
                                "type": "boolean",
                            },
                            {
                                "description": "date path",
                                "in": "path",
                                "name": "path_date",
                                "required": True,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time path",
                                "in": "path",
                                "name": "path_date_time",
                                "required": True,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password path",
                                "in": "path",
                                "name": "path_password",
                                "required": True,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array path",
                                "in": "path",
                                "name": "path_array_integer",
                                "required": True,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array path",
                                "in": "path",
                                "name": "path_array_integer32",
                                "required": True,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array path",
                                "in": "path",
                                "name": "path_array_integer64",
                                "required": True,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array path",
                                "in": "path",
                                "name": "path_array_number",
                                "required": True,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array path",
                                "in": "path",
                                "name": "path_array_float",
                                "required": True,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array path",
                                "in": "path",
                                "name": "path_array_double",
                                "required": True,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array path",
                                "in": "path",
                                "name": "path_array_string",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array path",
                                "in": "path",
                                "name": "path_array_string_byte",
                                "required": True,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array path",
                                "in": "path",
                                "name": "path_array_string_binary",
                                "required": True,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array path",
                                "in": "path",
                                "name": "path_array_boolean",
                                "required": True,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array path",
                                "in": "path",
                                "name": "path_array_date",
                                "required": True,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array path",
                                "in": "path",
                                "name": "path_array_date_time",
                                "required": True,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array path",
                                "in": "path",
                                "name": "path_array_password",
                                "required": True,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
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
                    },
                    "put": {
                        "operationId": "put_all_paths_types",
                        "produces": ["application/json"],
                        "parameters": [
                            {
                                "description": "integer path",
                                "in": "path",
                                "name": "path_integer",
                                "required": True,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 path",
                                "in": "path",
                                "name": "path_integer32",
                                "required": True,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 path",
                                "in": "path",
                                "name": "path_integer64",
                                "required": True,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number path",
                                "in": "path",
                                "name": "path_number",
                                "required": True,
                                "type": "number",
                            },
                            {
                                "description": "number float path",
                                "in": "path",
                                "name": "path_float",
                                "required": True,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double path",
                                "in": "path",
                                "name": "path_double",
                                "required": True,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string path",
                                "in": "path",
                                "name": "path_string",
                                "required": True,
                                "type": "string",
                            },
                            {
                                "description": "string byte path",
                                "in": "path",
                                "name": "path_string_byte",
                                "required": True,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary path",
                                "in": "path",
                                "name": "path_string_binary",
                                "required": True,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean path",
                                "in": "path",
                                "name": "path_boolean",
                                "required": True,
                                "type": "boolean",
                            },
                            {
                                "description": "date path",
                                "in": "path",
                                "name": "path_date",
                                "required": True,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time path",
                                "in": "path",
                                "name": "path_date_time",
                                "required": True,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password path",
                                "in": "path",
                                "name": "path_password",
                                "required": True,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array path",
                                "in": "path",
                                "name": "path_array_integer",
                                "required": True,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array path",
                                "in": "path",
                                "name": "path_array_integer32",
                                "required": True,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array path",
                                "in": "path",
                                "name": "path_array_integer64",
                                "required": True,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array path",
                                "in": "path",
                                "name": "path_array_number",
                                "required": True,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array path",
                                "in": "path",
                                "name": "path_array_float",
                                "required": True,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array path",
                                "in": "path",
                                "name": "path_array_double",
                                "required": True,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array path",
                                "in": "path",
                                "name": "path_array_string",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array path",
                                "in": "path",
                                "name": "path_array_string_byte",
                                "required": True,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array path",
                                "in": "path",
                                "name": "path_array_string_binary",
                                "required": True,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array path",
                                "in": "path",
                                "name": "path_array_boolean",
                                "required": True,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array path",
                                "in": "path",
                                "name": "path_array_date",
                                "required": True,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array path",
                                "in": "path",
                                "name": "path_array_date_time",
                                "required": True,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array path",
                                "in": "path",
                                "name": "path_array_password",
                                "required": True,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
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
                    },
                    "delete": {
                        "operationId": "delete_all_paths_types",
                        "produces": ["application/json"],
                        "parameters": [
                            {
                                "description": "integer path",
                                "in": "path",
                                "name": "path_integer",
                                "required": True,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 path",
                                "in": "path",
                                "name": "path_integer32",
                                "required": True,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 path",
                                "in": "path",
                                "name": "path_integer64",
                                "required": True,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number path",
                                "in": "path",
                                "name": "path_number",
                                "required": True,
                                "type": "number",
                            },
                            {
                                "description": "number float path",
                                "in": "path",
                                "name": "path_float",
                                "required": True,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double path",
                                "in": "path",
                                "name": "path_double",
                                "required": True,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string path",
                                "in": "path",
                                "name": "path_string",
                                "required": True,
                                "type": "string",
                            },
                            {
                                "description": "string byte path",
                                "in": "path",
                                "name": "path_string_byte",
                                "required": True,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary path",
                                "in": "path",
                                "name": "path_string_binary",
                                "required": True,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean path",
                                "in": "path",
                                "name": "path_boolean",
                                "required": True,
                                "type": "boolean",
                            },
                            {
                                "description": "date path",
                                "in": "path",
                                "name": "path_date",
                                "required": True,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time path",
                                "in": "path",
                                "name": "path_date_time",
                                "required": True,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password path",
                                "in": "path",
                                "name": "path_password",
                                "required": True,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array path",
                                "in": "path",
                                "name": "path_array_integer",
                                "required": True,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array path",
                                "in": "path",
                                "name": "path_array_integer32",
                                "required": True,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array path",
                                "in": "path",
                                "name": "path_array_integer64",
                                "required": True,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array path",
                                "in": "path",
                                "name": "path_array_number",
                                "required": True,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array path",
                                "in": "path",
                                "name": "path_array_float",
                                "required": True,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array path",
                                "in": "path",
                                "name": "path_array_double",
                                "required": True,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array path",
                                "in": "path",
                                "name": "path_array_string",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array path",
                                "in": "path",
                                "name": "path_array_string_byte",
                                "required": True,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array path",
                                "in": "path",
                                "name": "path_array_string_binary",
                                "required": True,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array path",
                                "in": "path",
                                "name": "path_array_boolean",
                                "required": True,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array path",
                                "in": "path",
                                "name": "path_array_date",
                                "required": True,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array path",
                                "in": "path",
                                "name": "path_array_date_time",
                                "required": True,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array path",
                                "in": "path",
                                "name": "path_array_password",
                                "required": True,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
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
                    },
                },
                "/body_with_properties": {
                    "post": {
                        "operationId": "post_body_with_properties",
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "payload",
                                "required": True,
                                "in": "body",
                                "schema": {
                                    "properties": {
                                        "int_field": {"type": "integer"},
                                        "str_field": {"type": "string"},
                                        "bool_field": {"type": "boolean"},
                                    },
                                    "required": ["bool_field"],
                                },
                            }
                        ],
                    }
                },
                "/int_choices": {
                    "get": {
                        "operationId": "get_int_choices",
                        "parameters": [
                            {
                                "description": "restricted int values",
                                "in": "query",
                                "name": "int_param",
                                "required": True,
                                "enum": [1, 10, 100],
                                "type": "integer",
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


def test_mandatory_integer_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=None,
            query_integer32=None,
            query_integer64=None,
            query_number=None,
            query_float=None,
            query_double=None,
            query_string=None,
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_integer is required."]
    )


def test_mandatory_integer_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer="str value",
            query_integer32=None,
            query_integer64=None,
            query_number=None,
            query_float=None,
            query_double=None,
            query_string=None,
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == [
            "query_integer value \"str value\" (<class 'str'> type) must be an integer."
        ]
    )


def test_optional_integer_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_integer="str value"
    ) == ["query_integer value \"str value\" (<class 'str'> type) must be an integer."]


def test_mandatory_array_integer_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_integer is required."]
    )


def test_mandatory_array_integer_parameter_provided_as_empty_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[],
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_integer is required."]
    )


def test_mandatory_array_integer_parameter_provided_as_none_filled_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[None],
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_integer is required."]
    )


def test_mandatory_array_integer_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32=0,
        query_integer64=0,
        query_number=0.0,
        query_float=0.0,
        query_double=0.0,
        query_string="str value",
        query_string_byte="str value",
        query_string_binary="str value",
        query_boolean=True,
        query_date=today_date,
        query_date_time=today_datetime,
        query_password="str value",
        query_array_integer="str value",
        query_array_integer32=None,
        query_array_integer64=None,
        query_array_number=None,
        query_array_float=None,
        query_array_double=None,
        query_array_string=None,
        query_array_string_byte=None,
        query_array_string_binary=None,
        query_array_boolean=None,
        query_array_date=None,
        query_array_date_time=None,
        query_array_password=None,
    ) == [
        "query_array_integer value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_mandatory_array_integer_parameter_with_wrong_type_in_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32=0,
        query_integer64=0,
        query_number=0.0,
        query_float=0.0,
        query_double=0.0,
        query_string="str value",
        query_string_byte="str value",
        query_string_binary="str value",
        query_boolean=True,
        query_date=today_date,
        query_date_time=today_datetime,
        query_password="str value",
        query_array_integer=["str value"],
        query_array_integer32=None,
        query_array_integer64=None,
        query_array_number=None,
        query_array_float=None,
        query_array_double=None,
        query_array_string=None,
        query_array_string_byte=None,
        query_array_string_binary=None,
        query_array_boolean=None,
        query_array_date=None,
        query_array_date_time=None,
        query_array_password=None,
    ) == [
        "query_array_integer value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_optional_array_integer_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_array_integer="str value"
    ) == [
        "query_array_integer value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_optional_array_integer_parameter_with_wrong_type_in_array(
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

    assert generated_functions.json_get_all_optional_parameters_types(
        query_array_integer=["str value"]
    ) == [
        "query_array_integer value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_mandatory_integer32_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=None,
            query_integer64=None,
            query_number=None,
            query_float=None,
            query_double=None,
            query_string=None,
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_integer32 is required."]
    )


def test_mandatory_integer32_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32="str value",
        query_integer64=None,
        query_number=None,
        query_float=None,
        query_double=None,
        query_string=None,
        query_string_byte=None,
        query_string_binary=None,
        query_boolean=None,
        query_date=None,
        query_date_time=None,
        query_password=None,
        query_array_integer=None,
        query_array_integer32=None,
        query_array_integer64=None,
        query_array_number=None,
        query_array_float=None,
        query_array_double=None,
        query_array_string=None,
        query_array_string_byte=None,
        query_array_string_binary=None,
        query_array_boolean=None,
        query_array_date=None,
        query_array_date_time=None,
        query_array_password=None,
    ) == [
        "query_integer32 value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_optional_integer32_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_integer32="str value"
    ) == [
        "query_integer32 value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_mandatory_array_integer32_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_integer32 is required."]
    )


def test_mandatory_array_integer32_parameter_provided_as_empty_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[],
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_integer32 is required."]
    )


def test_mandatory_array_integer32_parameter_provided_as_none_filled_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[None],
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_integer32 is required."]
    )


def test_mandatory_array_integer32_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32=0,
        query_integer64=0,
        query_number=0.0,
        query_float=0.0,
        query_double=0.0,
        query_string="str value",
        query_string_byte="str value",
        query_string_binary="str value",
        query_boolean=True,
        query_date=today_date,
        query_date_time=today_datetime,
        query_password="str value",
        query_array_integer=[0],
        query_array_integer32="str value",
        query_array_integer64=None,
        query_array_number=None,
        query_array_float=None,
        query_array_double=None,
        query_array_string=None,
        query_array_string_byte=None,
        query_array_string_binary=None,
        query_array_boolean=None,
        query_array_date=None,
        query_array_date_time=None,
        query_array_password=None,
    ) == [
        "query_array_integer32 value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_mandatory_array_integer32_parameter_with_wrong_type_in_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32=0,
        query_integer64=0,
        query_number=0.0,
        query_float=0.0,
        query_double=0.0,
        query_string="str value",
        query_string_byte="str value",
        query_string_binary="str value",
        query_boolean=True,
        query_date=today_date,
        query_date_time=today_datetime,
        query_password="str value",
        query_array_integer=[0],
        query_array_integer32=["str value"],
        query_array_integer64=None,
        query_array_number=None,
        query_array_float=None,
        query_array_double=None,
        query_array_string=None,
        query_array_string_byte=None,
        query_array_string_binary=None,
        query_array_boolean=None,
        query_array_date=None,
        query_array_date_time=None,
        query_array_password=None,
    ) == [
        "query_array_integer32 value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_optional_array_integer32_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_array_integer32="str value"
    ) == [
        "query_array_integer32 value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_optional_array_integer32_parameter_with_wrong_type_in_array(
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

    assert generated_functions.json_get_all_optional_parameters_types(
        query_array_integer32=["str value"]
    ) == [
        "query_array_integer32 value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_mandatory_integer64_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=None,
            query_number=None,
            query_float=None,
            query_double=None,
            query_string=None,
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_integer64 is required."]
    )


def test_mandatory_integer64_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32=0,
        query_integer64="str value",
        query_number=None,
        query_float=None,
        query_double=None,
        query_string=None,
        query_string_byte=None,
        query_string_binary=None,
        query_boolean=None,
        query_date=None,
        query_date_time=None,
        query_password=None,
        query_array_integer=None,
        query_array_integer32=None,
        query_array_integer64=None,
        query_array_number=None,
        query_array_float=None,
        query_array_double=None,
        query_array_string=None,
        query_array_string_byte=None,
        query_array_string_binary=None,
        query_array_boolean=None,
        query_array_date=None,
        query_array_date_time=None,
        query_array_password=None,
    ) == [
        "query_integer64 value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_optional_integer64_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_integer64="str value"
    ) == [
        "query_integer64 value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_mandatory_array_integer64_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_integer64 is required."]
    )


def test_mandatory_array_integer64_parameter_provided_as_empty_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[],
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_integer64 is required."]
    )


def test_mandatory_array_integer64_parameter_provided_as_none_filled_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[None],
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_integer64 is required."]
    )


def test_mandatory_array_integer64_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32=0,
        query_integer64=0,
        query_number=0.0,
        query_float=0.0,
        query_double=0.0,
        query_string="str value",
        query_string_byte="str value",
        query_string_binary="str value",
        query_boolean=True,
        query_date=today_date,
        query_date_time=today_datetime,
        query_password="str value",
        query_array_integer=[0],
        query_array_integer32=[0],
        query_array_integer64="str value",
        query_array_number=None,
        query_array_float=None,
        query_array_double=None,
        query_array_string=None,
        query_array_string_byte=None,
        query_array_string_binary=None,
        query_array_boolean=None,
        query_array_date=None,
        query_array_date_time=None,
        query_array_password=None,
    ) == [
        "query_array_integer64 value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_mandatory_array_integer64_parameter_with_wrong_type_in_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32=0,
        query_integer64=0,
        query_number=0.0,
        query_float=0.0,
        query_double=0.0,
        query_string="str value",
        query_string_byte="str value",
        query_string_binary="str value",
        query_boolean=True,
        query_date=today_date,
        query_date_time=today_datetime,
        query_password="str value",
        query_array_integer=[0],
        query_array_integer32=[0],
        query_array_integer64=["str value"],
        query_array_number=None,
        query_array_float=None,
        query_array_double=None,
        query_array_string=None,
        query_array_string_byte=None,
        query_array_string_binary=None,
        query_array_boolean=None,
        query_array_date=None,
        query_array_date_time=None,
        query_array_password=None,
    ) == [
        "query_array_integer64 value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_optional_array_integer64_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_array_integer64="str value"
    ) == [
        "query_array_integer64 value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_optional_array_integer64_parameter_with_wrong_type_in_array(
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

    assert generated_functions.json_get_all_optional_parameters_types(
        query_array_integer64=["str value"]
    ) == [
        "query_array_integer64 value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_mandatory_number_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=None,
            query_float=None,
            query_double=None,
            query_string=None,
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_number is required."]
    )


def test_mandatory_number_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number="str value",
            query_float=None,
            query_double=None,
            query_string=None,
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_number value \"str value\" (<class 'str'> type) must be a number."]
    )


def test_optional_number_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_number="str value"
    ) == ["query_number value \"str value\" (<class 'str'> type) must be a number."]


def test_mandatory_array_number_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_number is required."]
    )


def test_mandatory_array_number_parameter_provided_as_empty_array(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[],
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_number is required."]
    )


def test_mandatory_array_number_parameter_provided_as_none_filled_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[None],
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_number is required."]
    )


def test_mandatory_array_number_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32=0,
        query_integer64=0,
        query_number=0.0,
        query_float=0.0,
        query_double=0.0,
        query_string="str value",
        query_string_byte="str value",
        query_string_binary="str value",
        query_boolean=True,
        query_date=today_date,
        query_date_time=today_datetime,
        query_password="str value",
        query_array_integer=[0],
        query_array_integer32=[0],
        query_array_integer64=[0],
        query_array_number="str value",
        query_array_float=None,
        query_array_double=None,
        query_array_string=None,
        query_array_string_byte=None,
        query_array_string_binary=None,
        query_array_boolean=None,
        query_array_date=None,
        query_array_date_time=None,
        query_array_password=None,
    ) == [
        "query_array_number value \"str value\" (<class 'str'> type) must be a number."
    ]


def test_mandatory_array_number_parameter_with_wrong_type_in_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32=0,
        query_integer64=0,
        query_number=0.0,
        query_float=0.0,
        query_double=0.0,
        query_string="str value",
        query_string_byte="str value",
        query_string_binary="str value",
        query_boolean=True,
        query_date=today_date,
        query_date_time=today_datetime,
        query_password="str value",
        query_array_integer=[0],
        query_array_integer32=[0],
        query_array_integer64=[0],
        query_array_number=["str value"],
        query_array_float=None,
        query_array_double=None,
        query_array_string=None,
        query_array_string_byte=None,
        query_array_string_binary=None,
        query_array_boolean=None,
        query_array_date=None,
        query_array_date_time=None,
        query_array_password=None,
    ) == [
        "query_array_number value \"str value\" (<class 'str'> type) must be a number."
    ]


def test_optional_array_number_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_array_number="str value"
    ) == [
        "query_array_number value \"str value\" (<class 'str'> type) must be a number."
    ]


def test_optional_array_number_parameter_with_wrong_type_in_array(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_array_number=["str value"]
    ) == [
        "query_array_number value \"str value\" (<class 'str'> type) must be a number."
    ]


def test_mandatory_float_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=None,
            query_double=None,
            query_string=None,
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_float is required."]
    )


def test_mandatory_float_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float="str value",
            query_double=None,
            query_string=None,
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_float value \"str value\" (<class 'str'> type) must be a number."]
    )


def test_optional_float_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_float="str value"
    ) == ["query_float value \"str value\" (<class 'str'> type) must be a number."]


def test_mandatory_array_float_number_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_float is required."]
    )


def test_mandatory_array_float_parameter_provided_as_empty_array(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[],
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_float is required."]
    )


def test_mandatory_array_float_parameter_provided_as_none_filled_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[None],
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_float is required."]
    )


def test_mandatory_array_float_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32=0,
        query_integer64=0,
        query_number=0.0,
        query_float=0.0,
        query_double=0.0,
        query_string="str value",
        query_string_byte="str value",
        query_string_binary="str value",
        query_boolean=True,
        query_date=today_date,
        query_date_time=today_datetime,
        query_password="str value",
        query_array_integer=[0],
        query_array_integer32=[0],
        query_array_integer64=[0],
        query_array_number=[0.0],
        query_array_float="str value",
        query_array_double=None,
        query_array_string=None,
        query_array_string_byte=None,
        query_array_string_binary=None,
        query_array_boolean=None,
        query_array_date=None,
        query_array_date_time=None,
        query_array_password=None,
    ) == [
        "query_array_float value \"str value\" (<class 'str'> type) must be a number."
    ]


def test_mandatory_array_float_parameter_with_wrong_type_in_array(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32=0,
        query_integer64=0,
        query_number=0.0,
        query_float=0.0,
        query_double=0.0,
        query_string="str value",
        query_string_byte="str value",
        query_string_binary="str value",
        query_boolean=True,
        query_date=today_date,
        query_date_time=today_datetime,
        query_password="str value",
        query_array_integer=[0],
        query_array_integer32=[0],
        query_array_integer64=[0],
        query_array_number=[0.0],
        query_array_float=["str value"],
        query_array_double=None,
        query_array_string=None,
        query_array_string_byte=None,
        query_array_string_binary=None,
        query_array_boolean=None,
        query_array_date=None,
        query_array_date_time=None,
        query_array_password=None,
    ) == [
        "query_array_float value \"str value\" (<class 'str'> type) must be a number."
    ]


def test_optional_array_float_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_array_float="str value"
    ) == [
        "query_array_float value \"str value\" (<class 'str'> type) must be a number."
    ]


def test_optional_array_float_parameter_with_wrong_type_in_array(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_array_float=["str value"]
    ) == [
        "query_array_float value \"str value\" (<class 'str'> type) must be a number."
    ]


def test_mandatory_double_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=None,
            query_string=None,
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_double is required."]
    )


def test_mandatory_double_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double="str value",
            query_string=None,
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_double value \"str value\" (<class 'str'> type) must be a number."]
    )


def test_optional_double_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_double="str value"
    ) == ["query_double value \"str value\" (<class 'str'> type) must be a number."]


def test_mandatory_array_double_number_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_double is required."]
    )


def test_mandatory_array_double_parameter_provided_as_empty_array(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[],
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_double is required."]
    )


def test_mandatory_array_double_parameter_provided_as_none_filled_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[None],
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_double is required."]
    )


def test_mandatory_array_double_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32=0,
        query_integer64=0,
        query_number=0.0,
        query_float=0.0,
        query_double=0.0,
        query_string="str value",
        query_string_byte="str value",
        query_string_binary="str value",
        query_boolean=True,
        query_date=today_date,
        query_date_time=today_datetime,
        query_password="str value",
        query_array_integer=[0],
        query_array_integer32=[0],
        query_array_integer64=[0],
        query_array_number=[0.0],
        query_array_float=[0.0],
        query_array_double="str value",
        query_array_string=None,
        query_array_string_byte=None,
        query_array_string_binary=None,
        query_array_boolean=None,
        query_array_date=None,
        query_array_date_time=None,
        query_array_password=None,
    ) == [
        "query_array_double value \"str value\" (<class 'str'> type) must be a number."
    ]


def test_mandatory_array_double_parameter_with_wrong_type_in_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32=0,
        query_integer64=0,
        query_number=0.0,
        query_float=0.0,
        query_double=0.0,
        query_string="str value",
        query_string_byte="str value",
        query_string_binary="str value",
        query_boolean=True,
        query_date=today_date,
        query_date_time=today_datetime,
        query_password="str value",
        query_array_integer=[0],
        query_array_integer32=[0],
        query_array_integer64=[0],
        query_array_number=[0.0],
        query_array_float=[0.0],
        query_array_double=["str value"],
        query_array_string=None,
        query_array_string_byte=None,
        query_array_string_binary=None,
        query_array_boolean=None,
        query_array_date=None,
        query_array_date_time=None,
        query_array_password=None,
    ) == [
        "query_array_double value \"str value\" (<class 'str'> type) must be a number."
    ]


def test_optional_array_double_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_array_double="str value"
    ) == [
        "query_array_double value \"str value\" (<class 'str'> type) must be a number."
    ]


def test_optional_array_double_parameter_with_wrong_type_in_array(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_array_double=["str value"]
    ) == [
        "query_array_double value \"str value\" (<class 'str'> type) must be a number."
    ]


def test_mandatory_string_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string=None,
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_string is required."]
    )


def test_mandatory_string_parameter_provided_as_empty_array(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string=[],
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_string is required."]
    )


def test_mandatory_string_parameter_provided_as_none_filled_array(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string=[None],
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_string is required."]
    )


def test_mandatory_array_string_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_string is required."]
    )


def test_mandatory_array_string_parameter_provided_as_empty_array(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[],
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_string is required."]
    )


def test_mandatory_array_string_parameter_provided_as_none_filled_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=[None],
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_string is required."]
    )


def test_mandatory_string_byte_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte=None,
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_string_byte is required."]
    )


def test_mandatory_string_byte_parameter_provided_as_empty_array(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte=[],
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_string_byte is required."]
    )


def test_mandatory_string_byte_parameter_provided_as_none_filled_array(
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

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte=[None],
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_string_byte is required."]
    )


def test_mandatory_array_string_byte_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=["str value"],
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_string_byte is required."]
    )


def test_mandatory_array_string_byte_parameter_provided_as_empty_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=["str value"],
            query_array_string_byte=[],
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_string_byte is required."]
    )


def test_mandatory_array_string_byte_parameter_provided_as_none_filled_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=["str value"],
            query_array_string_byte=[None],
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_string_byte is required."]
    )


def test_mandatory_string_binary_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary=None,
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_string_binary is required."]
    )


def test_mandatory_string_binary_parameter_provided_as_empty_array(
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

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary=[],
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_string_binary is required."]
    )


def test_mandatory_string_binary_parameter_provided_as_none_filled_array(
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

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary=[None],
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_string_binary is required."]
    )


def test_mandatory_array_string_binary_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=["str value"],
            query_array_string_byte=["str value"],
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_string_binary is required."]
    )


def test_mandatory_array_string_binary_parameter_provided_as_empty_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=["str value"],
            query_array_string_byte=["str value"],
            query_array_string_binary=[],
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_string_binary is required."]
    )


def test_mandatory_array_string_binary_parameter_provided_as_none_filled_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=["str value"],
            query_array_string_byte=["str value"],
            query_array_string_binary=[None],
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_string_binary is required."]
    )


def test_mandatory_boolean_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=None,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_boolean is required."]
    )


def test_mandatory_boolean_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean="non boolean",
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == [
            "query_boolean value \"non boolean\" (<class 'str'> type) must be a boolean."
        ]
    )


def test_optional_boolean_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_boolean="non boolean"
    ) == ["query_boolean value \"non boolean\" (<class 'str'> type) must be a boolean."]


def test_mandatory_array_boolean_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=["str value"],
            query_array_string_byte=["str value"],
            query_array_string_binary=["str value"],
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_boolean is required."]
    )


def test_mandatory_array_boolean_parameter_provided_as_empty_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=["str value"],
            query_array_string_byte=["str value"],
            query_array_string_binary=["str value"],
            query_array_boolean=[],
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_boolean is required."]
    )


def test_mandatory_array_boolean_parameter_provided_as_none_filled_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=["str value"],
            query_array_string_byte=["str value"],
            query_array_string_binary=["str value"],
            query_array_boolean=[None],
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_boolean is required."]
    )


def test_mandatory_array_boolean_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32=0,
        query_integer64=0,
        query_number=0.0,
        query_float=0.0,
        query_double=0.0,
        query_string="str value",
        query_string_byte="str value",
        query_string_binary="str value",
        query_boolean=True,
        query_date=today_date,
        query_date_time=today_datetime,
        query_password="str value",
        query_array_integer=[0],
        query_array_integer32=[0],
        query_array_integer64=[0],
        query_array_number=[0.0],
        query_array_float=[0.0],
        query_array_double=[0.0],
        query_array_string=["str value"],
        query_array_string_byte=["str value"],
        query_array_string_binary=["str value"],
        query_array_boolean="non boolean",
        query_array_date=None,
        query_array_date_time=None,
        query_array_password=None,
    ) == [
        "query_array_boolean value \"non boolean\" (<class 'str'> type) must be a boolean."
    ]


def test_mandatory_array_boolean_parameter_with_wrong_type_in_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32=0,
        query_integer64=0,
        query_number=0.0,
        query_float=0.0,
        query_double=0.0,
        query_string="str value",
        query_string_byte="str value",
        query_string_binary="str value",
        query_boolean=True,
        query_date=today_date,
        query_date_time=today_datetime,
        query_password="str value",
        query_array_integer=[0],
        query_array_integer32=[0],
        query_array_integer64=[0],
        query_array_number=[0.0],
        query_array_float=[0.0],
        query_array_double=[0.0],
        query_array_string=["str value"],
        query_array_string_byte=["str value"],
        query_array_string_binary=["str value"],
        query_array_boolean=["non boolean"],
        query_array_date=None,
        query_array_date_time=None,
        query_array_password=None,
    ) == [
        "query_array_boolean value \"non boolean\" (<class 'str'> type) must be a boolean."
    ]


def test_optional_array_boolean_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_array_boolean="non boolean"
    ) == [
        "query_array_boolean value \"non boolean\" (<class 'str'> type) must be a boolean."
    ]


def test_optional_array_boolean_parameter_with_wrong_type_in_array(
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

    assert generated_functions.json_get_all_optional_parameters_types(
        query_array_boolean=["non boolean"]
    ) == [
        "query_array_boolean value \"non boolean\" (<class 'str'> type) must be a boolean."
    ]


def test_mandatory_date_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=None,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_date is required."]
    )


def test_mandatory_date_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date="str value",
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_date value \"str value\" (<class 'str'> type) must be a date."]
    )


def test_optional_date_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_date="str value"
    ) == ["query_date value \"str value\" (<class 'str'> type) must be a date."]


def test_mandatory_array_date_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=["str value"],
            query_array_string_byte=["str value"],
            query_array_string_binary=["str value"],
            query_array_boolean=[True],
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_date is required."]
    )


def test_mandatory_array_date_parameter_provided_as_empty_array(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=["str value"],
            query_array_string_byte=["str value"],
            query_array_string_binary=["str value"],
            query_array_boolean=[True],
            query_array_date=[],
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_date is required."]
    )


def test_mandatory_array_date_parameter_provided_as_none_filled_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=["str value"],
            query_array_string_byte=["str value"],
            query_array_string_binary=["str value"],
            query_array_boolean=[True],
            query_array_date=[None],
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_date is required."]
    )


def test_mandatory_array_date_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=["str value"],
            query_array_string_byte=["str value"],
            query_array_string_binary=["str value"],
            query_array_boolean=[True],
            query_array_date="str value",
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_date value \"str value\" (<class 'str'> type) must be a date."]
    )


def test_mandatory_array_date_parameter_with_wrong_type_in_array(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=["str value"],
            query_array_string_byte=["str value"],
            query_array_string_binary=["str value"],
            query_array_boolean=[True],
            query_array_date=["str value"],
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_date value \"str value\" (<class 'str'> type) must be a date."]
    )


def test_optional_array_date_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_array_date="str value"
    ) == ["query_array_date value \"str value\" (<class 'str'> type) must be a date."]


def test_optional_array_date_parameter_with_wrong_type_in_array(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_array_date=["str value"]
    ) == ["query_array_date value \"str value\" (<class 'str'> type) must be a date."]


def test_mandatory_date_time_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=None,
            query_password=None,
            query_array_integer=None,
            query_array_integer32=None,
            query_array_integer64=None,
            query_array_number=None,
            query_array_float=None,
            query_array_double=None,
            query_array_string=None,
            query_array_string_byte=None,
            query_array_string_binary=None,
            query_array_boolean=None,
            query_array_date=None,
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_date_time is required."]
    )


def test_mandatory_date_time_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32=0,
        query_integer64=0,
        query_number=0.0,
        query_float=0.0,
        query_double=0.0,
        query_string="str value",
        query_string_byte="str value",
        query_string_binary="str value",
        query_boolean=True,
        query_date=today_date,
        query_date_time="str value",
        query_password=None,
        query_array_integer=None,
        query_array_integer32=None,
        query_array_integer64=None,
        query_array_number=None,
        query_array_float=None,
        query_array_double=None,
        query_array_string=None,
        query_array_string_byte=None,
        query_array_string_binary=None,
        query_array_boolean=None,
        query_array_date=None,
        query_array_date_time=None,
        query_array_password=None,
    ) == [
        "query_date_time value \"str value\" (<class 'str'> type) must be a date time."
    ]


def test_optional_date_time_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_date_time="str value"
    ) == [
        "query_date_time value \"str value\" (<class 'str'> type) must be a date time."
    ]


def test_mandatory_array_date_time_parameter_not_provided(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=["str value"],
            query_array_string_byte=["str value"],
            query_array_string_binary=["str value"],
            query_array_boolean=[True],
            query_array_date=[today_date],
            query_array_date_time=None,
            query_array_password=None,
        )
        == ["query_array_date_time is required."]
    )


def test_mandatory_array_date_time_parameter_provided_as_empty_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=["str value"],
            query_array_string_byte=["str value"],
            query_array_string_binary=["str value"],
            query_array_boolean=[True],
            query_array_date=[today_date],
            query_array_date_time=[],
            query_array_password=None,
        )
        == ["query_array_date_time is required."]
    )


def test_mandatory_array_date_time_parameter_provided_as_none_filled_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=0,
            query_integer32=0,
            query_integer64=0,
            query_number=0.0,
            query_float=0.0,
            query_double=0.0,
            query_string="str value",
            query_string_byte="str value",
            query_string_binary="str value",
            query_boolean=True,
            query_date=today_date,
            query_date_time=today_datetime,
            query_password="str value",
            query_array_integer=[0],
            query_array_integer32=[0],
            query_array_integer64=[0],
            query_array_number=[0.0],
            query_array_float=[0.0],
            query_array_double=[0.0],
            query_array_string=["str value"],
            query_array_string_byte=["str value"],
            query_array_string_binary=["str value"],
            query_array_boolean=[True],
            query_array_date=[today_date],
            query_array_date_time=[None],
            query_array_password=None,
        )
        == ["query_array_date_time is required."]
    )


def test_mandatory_array_date_time_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32=0,
        query_integer64=0,
        query_number=0.0,
        query_float=0.0,
        query_double=0.0,
        query_string="str value",
        query_string_byte="str value",
        query_string_binary="str value",
        query_boolean=True,
        query_date=today_date,
        query_date_time=today_datetime,
        query_password="str value",
        query_array_integer=[0],
        query_array_integer32=[0],
        query_array_integer64=[0],
        query_array_number=[0.0],
        query_array_float=[0.0],
        query_array_double=[0.0],
        query_array_string=["str value"],
        query_array_string_byte=["str value"],
        query_array_string_binary=["str value"],
        query_array_boolean=[True],
        query_array_date=[today_date],
        query_array_date_time="str value",
        query_array_password=None,
    ) == [
        "query_array_date_time value \"str value\" (<class 'str'> type) must be a date time."
    ]


def test_mandatory_array_date_time_parameter_with_wrong_type_in_array(
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

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert generated_functions.json_get_all_parameters_types(
        query_integer=0,
        query_integer32=0,
        query_integer64=0,
        query_number=0.0,
        query_float=0.0,
        query_double=0.0,
        query_string="str value",
        query_string_byte="str value",
        query_string_binary="str value",
        query_boolean=True,
        query_date=today_date,
        query_date_time=today_datetime,
        query_password="str value",
        query_array_integer=[0],
        query_array_integer32=[0],
        query_array_integer64=[0],
        query_array_number=[0.0],
        query_array_float=[0.0],
        query_array_double=[0.0],
        query_array_string=["str value"],
        query_array_string_byte=["str value"],
        query_array_string_binary=["str value"],
        query_array_boolean=[True],
        query_array_date=[today_date],
        query_array_date_time=["str value"],
        query_array_password=None,
    ) == [
        "query_array_date_time value \"str value\" (<class 'str'> type) must be a date time."
    ]


def test_valid_mandatory_parameters(json_service, tmpdir, responses: RequestsMock):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    first_date = datetime.date(year=2020, month=3, day=4)
    second_date = datetime.date(year=2020, month=3, day=5)
    first_datetime = datetime.datetime(year=2020, month=3, day=4)
    second_datetime = datetime.datetime(year=2020, month=3, day=5)
    responses.add(
        responses.GET,
        url="http://localhost:8954/all_parameters_types?query_integer=1&query_integer32=10&query_integer64=100&query_number=0.1&query_float=1.01&query_double=1.1&query_string=string&query_string_byte=string+bytes&query_string_binary=string+binary&query_boolean=True&query_date=2020-03-04&query_date_time=2020-03-04T00%3A00%3A00&query_password=password&query_array_integer=1&query_array_integer=2&query_array_integer32=10&query_array_integer32=20&query_array_integer64=100&query_array_integer64=200&query_array_number=0.1&query_array_number=0.2&query_array_float=1.01&query_array_float=2.01&query_array_double=1.1&query_array_double=2.1&query_array_string=string+1&query_array_string=string+2&query_array_string_byte=string+bytes+1&query_array_string_byte=string+bytes+2&query_array_string_binary=string+binary+1&query_array_string_binary=string+binary+2&query_array_boolean=True&query_array_boolean=False&query_array_date=2020-03-04&query_array_date=2020-03-05&query_array_date_time=2020-03-04T00%3A00%3A00&query_array_date_time=2020-03-05T00%3A00%3A00&query_array_password=password+1&query_array_password=password+2",
        json=[],
        match_querystring=True,
    )
    assert (
        generated_functions.json_get_all_parameters_types(
            query_integer=1,
            query_integer32=10,
            query_integer64=100,
            query_number=0.1,
            query_float=1.01,
            query_double=1.1,
            query_string="string",
            query_string_byte="string bytes",
            query_string_binary="string binary",
            query_boolean=True,
            query_date=first_date,
            query_date_time=first_datetime,
            query_password="password",
            query_array_integer=[1, 2],
            query_array_integer32=[10, 20],
            query_array_integer64=[100, 200],
            query_array_number=[0.1, 0.2],
            query_array_float=[1.01, 2.01],
            query_array_double=[1.1, 2.1],
            query_array_string=["string 1", "string 2"],
            query_array_string_byte=["string bytes 1", "string bytes 2"],
            query_array_string_binary=["string binary 1", "string binary 2"],
            query_array_boolean=[True, False],
            query_array_date=[first_date, second_date],
            query_array_date_time=[first_datetime, second_datetime],
            query_array_password=["password 1", "password 2"],
        )
        == [[""]]
    )


def test_optional_array_date_time_parameter_with_wrong_type(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert generated_functions.json_get_all_optional_parameters_types(
        query_array_date_time="str value"
    ) == [
        "query_array_date_time value \"str value\" (<class 'str'> type) must be a date time."
    ]


def test_optional_array_date_time_parameter_with_wrong_type_in_array(
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

    assert generated_functions.json_get_all_optional_parameters_types(
        query_array_date_time=["str value"]
    ) == [
        "query_array_date_time value \"str value\" (<class 'str'> type) must be a date time."
    ]


def test_list_of_list_form_post(json_service, tmpdir, responses: RequestsMock):
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
        url="http://localhost:8954/list_of_list_form",
        json=[],
        match_querystring=True,
    )

    assert (
        generated_functions.json_post_list_of_list_form(
            rules=[
                ["1", "EBE", "SNCF", "rule_1", "output_1"],
                ["1", "EFR,EDE", "ENGIE", "rule_2", "output_2"],
            ],
            items=[
                ["Deal Number", "Underlying", "Client"],
                ["0001", "EBE", "SNCF"],
                ["0002", "EFR", "ENGIE"],
                ["0003", "EDE", "ENGIE"],
            ],
        )
        == [[""]]
    )
    assert (
        _get_request(responses, "http://localhost:8954/list_of_list_form").body
        == b"""{"rules": [["1", "EBE", "SNCF", "rule_1", "output_1"], ["1", "EFR,EDE", "ENGIE", "rule_2", "output_2"]], "items": [["Deal Number", "Underlying", "Client"], ["0001", "EBE", "SNCF"], ["0002", "EFR", "ENGIE"], ["0003", "EDE", "ENGIE"]]}"""
    )


def test_list_of_list_form_post_with_non_str_date_failure(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_post_list_of_list_form(
            rules=[
                ["1", "EBE", "SNCF", "rule_1", "output_1"],
                ["1", "EFR,EDE", "ENGIE", "rule_2", "output_2"],
            ],
            items=[
                ["Deal Number", "Underlying", "Client"],
                [1, datetime.datetime.strptime("2017-03-04", "%Y-%m-%d"), "SNCF"],
                [2, datetime.datetime.strptime("2017-03-05", "%Y-%m-%d"), "ENGIE"],
                [3, datetime.datetime.strptime("2017-03-06", "%Y-%m-%d"), "ENGIE"],
            ],
        )
        == "items value \"2017-03-04 00:00:00\" (<class 'datetime.datetime'> type) must be formatted as text."
    )


def test_list_of_list_form_post_with_non_str(
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
        url="http://localhost:8954/list_of_list_form",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.json_post_list_of_list_form(
        items=[[1.0, 1.2, "SNCF"]]
    ) == [[""]]
    assert (
        _get_request(responses, "http://localhost:8954/list_of_list_form").body
        == b"""{"rules": null, "items": [["1", "1.2", "SNCF"]]}"""
    )


def test_list_of_list_form_post_with_single_list(
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
        url="http://localhost:8954/list_of_list_form",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.json_post_list_of_list_form(
        rules=[["rule1", "rule2", "rule3"]], items=[["item1", "item2", "item3"]]
    ) == [[""]]
    assert (
        _get_request(responses, "http://localhost:8954/list_of_list_form").body
        == b"""{"rules": [["rule1", "rule2", "rule3"]], "items": [["item1", "item2", "item3"]]}"""
    )


def test_dict_with_dict_json_post(json_service, tmpdir, responses: RequestsMock):
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
        url="http://localhost:8954/dict_with_dict",
        json=[],
        match_querystring=True,
    )

    assert (
        generated_functions.json_post_dict_with_dict(
            inner_dict=[["key1", "key2", "key3"], ["value10", "value20", "value30"]],
            dict_field1="value1",
            dict_field2="value2",
        )
        == [[""]]
    )
    assert (
        _get_request(responses, "http://localhost:8954/dict_with_dict").body
        == b"""{"inner_dict": {"key1": "value10", "key2": "value20", "key3": "value30"}, "dict_field1": "value1", "dict_field2": "value2"}"""
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


def test_dict_with_dict_list_json_post(json_service, tmpdir, responses: RequestsMock):
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
        url="http://localhost:8954/dict_with_dict_list",
        json=[],
        match_querystring=True,
    )

    assert (
        generated_functions.json_post_dict_with_dict_list(
            inner_dict_list=[
                ["key1", "key2", "key3"],
                ["value10", "value20", "value30"],
                ["value11", "value21", "value31"],
                ["value12", "value22", "value32"],
            ],
            dict_field1="value000",
            dict_field2="value010",
        )
        == [[""]]
    )
    assert (
        _get_request(responses, "http://localhost:8954/dict_with_dict_list").body
        == b"""{"inner_dict_list": [{"key1": "value10", "key2": "value20", "key3": "value30"}, {"key1": "value11", "key2": "value21", "key3": "value31"}, {"key1": "value12", "key2": "value22", "key3": "value32"}], "dict_field1": "value000", "dict_field2": "value010"}"""
    )


def test_dict_with_list_of_list_json_post(
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
        url="http://localhost:8954/dict_with_list_of_list",
        json=[],
        match_querystring=True,
    )

    assert (
        generated_functions.json_post_dict_with_list_of_list(
            inner_list_of_list=[
                ["key1", "key2", "key3"],
                ["value10", "value20", "value30"],
                ["value11", "value21", "value31"],
                ["value12", "value22", "value32"],
            ],
            dict_field1="value000",
            dict_field2="value010",
        )
        == [[""]]
    )
    assert (
        _get_request(responses, "http://localhost:8954/dict_with_list_of_list").body
        == b"""{"inner_list_of_list": [["key1", "key2", "key3"], ["value10", "value20", "value30"], ["value11", "value21", "value31"], ["value12", "value22", "value32"]], "dict_field1": "value000", "dict_field2": "value010"}"""
    )


def test_dict_with_list_of_list_json_post_a_single_list(
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
        url="http://localhost:8954/dict_with_list_of_list",
        json=[],
        match_querystring=True,
    )

    assert (
        generated_functions.json_post_dict_with_list_of_list(
            inner_list_of_list=[["key1", "key2", "key3"]],
            dict_field1="value000",
            dict_field2="value010",
        )
        == [[""]]
    )
    assert (
        _get_request(responses, "http://localhost:8954/dict_with_list_of_list").body
        == b"""{"inner_list_of_list": [["key1", "key2", "key3"]], "dict_field1": "value000", "dict_field2": "value010"}"""
    )


def test_dict_string_json_post(json_service, tmpdir, responses: RequestsMock):
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
        url="http://localhost:8954/dict_string",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.json_post_dict_string(
        dict_field1=34, dict_field2=890.32  # Send as integer
    ) == [[""]]
    assert (
        _get_request(responses, "http://localhost:8954/dict_string").body
        == b"""{"dict_field1": "34", "dict_field2": "890.32"}"""
    )


def test_dict_string_json_post_without_non_required(
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
        url="http://localhost:8954/dict_string",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.json_post_dict_string(dict_field1=34) == [[""]]
    assert (
        _get_request(responses, "http://localhost:8954/dict_string").body
        == b"""{"dict_field1": "34", "dict_field2": null}"""
    )


def test_dict_string_json_post_without_required(json_service, tmpdir):
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
        generated_functions.json_post_dict_string(dict_field2=34.5)
    assert (
        str(exception_info.value)
        == "json_post_dict_string() missing 1 required positional argument: 'dict_field1'"
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


def test_get_empty_list_parameter(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_list_parameter(list_parameter=[])
        == "list_parameter is required."
    )


def test_get_none_filled_list_parameter(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_list_parameter(list_parameter=[None, None, None])
        == "list_parameter is required."
    )


def test_get_none_as_first_list_parameter(
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
        responses.GET,
        url="http://localhost:8954/list_parameter?list_parameter=valid",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.json_get_list_parameter(
        list_parameter=[None, "valid"]
    ) == [[""]]


def test_get_none_as_last_list_parameter(json_service, tmpdir, responses: RequestsMock):
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
        responses.GET,
        url="http://localhost:8954/list_parameter?list_parameter=valid",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.json_get_list_parameter(
        list_parameter=["valid", None]
    ) == [[""]]


def test_get_none_in_list_parameter(json_service, tmpdir, responses: RequestsMock):
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
        responses.GET,
        url="http://localhost:8954/list_parameter?list_parameter=valid1&list_parameter=valid2",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.json_get_list_parameter(
        list_parameter=["valid1", None, "valid2"]
    ) == [[""]]


def test_get_none_as_list_parameter(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_list_parameter(list_parameter=None)
        == "list_parameter is required."
    )


def test_different_location_same_name(json_service, responses, tmpdir):
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
        url="http://localhost:8954/different_location_same_name/path%20value?dict_field1=query value",
        json=[],
        match_querystring=True,
    )

    assert (
        generated_functions.json_post_different_location_same_name(
            dict_field1=34,
            dict_field2="test",
            header_dict_field1="header value",
            query_dict_field1="query value",
            path_dict_field1="path value",
        )
        == [[""]]
    )

    request = _get_request(
        responses,
        "http://localhost:8954/different_location_same_name/path%20value?dict_field1=query+value",
    )
    assert request.body == b'{"dict_field1": "34", "dict_field2": "test"}'
    assert request.headers["dict_field1"] == "header value"


def test_post_list_dict_no_ref(json_service, responses, tmpdir):
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
        url="http://localhost:8954/list_dict_no_ref",
        json=[
            {"header1": "value1", "header2": "value2"},
            {"header1": "value10", "header2": "value20"},
        ],
        match_querystring=True,
    )

    assert generated_functions.json_post_list_dict_no_ref(
        payload=[["header1", "header2"], ["value1", "value2"], ["value10", "value20"]]
    ) == [["header1", "header2"], ["value1", "value2"], ["value10", "value20"]]

    assert (
        _get_request(responses, "http://localhost:8954/list_dict_no_ref").body
        == b'[{"header1": "value1", "header2": "value2"}, {"header1": "value10", "header2": "value20"}]'
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

    assert (
        generated_functions.json_post_min_and_max_items(
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
        )
        == [["OK"]]
    )

    assert (
        _get_request(responses, "http://localhost:8954/min_and_max_items").body
        == b'{"rule_set": "value10,value11,value12,value20,value21,value22,value30,value31,value32", "items": "value10,value11,value12,value20,value21,value22,value30,value31,value32"}'
    )


def test_post_body_with_properties(json_service, responses, tmpdir):
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
        url="http://localhost:8954/body_with_properties",
        json={"bool_field": True, "int_field": None, "str_field": None},
        match_querystring=True,
    )

    assert generated_functions.json_post_body_with_properties(bool_field=True) == [
        ["bool_field", "int_field", "str_field"],
        [True, "", ""],
    ]

    assert (
        _get_request(responses, "http://localhost:8954/body_with_properties").body
        == b'{"bool_field": true, "int_field": null, "str_field": null}'
    )


def test_get_valid_int_choice(json_service, responses, tmpdir):
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
        responses.GET,
        url="http://localhost:8954/int_choices?int_param=1",
        json={"int_param": "1"},
        match_querystring=True,
    )

    assert generated_functions.json_get_int_choices(int_param=1) == [
        ["int_param"],
        ["1"],
    ]


def test_get_invalid_int_choice(json_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.json_get_int_choices(int_param=2)
        == 'int_param value "2" should be 1 or 10 or 100.'
    )

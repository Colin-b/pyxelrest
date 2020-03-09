import datetime

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
    loader.load(
        tmpdir,
        {
            "json": {
                "open_api": {"definition": "http://localhost:8954/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
                "result": {"flatten": False},
            }
        },
    )


def test_mandatory_integer_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_integer is required."]


def test_mandatory_integer_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_integer value \"str value\" (<class 'str'> type) must be an integer."]


def test_optional_integer_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_integer="str value"
    ) == ["query_integer value \"str value\" (<class 'str'> type) must be an integer."]


def test_mandatory_array_integer_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_integer is required."]


def test_mandatory_array_integer_parameter_provided_as_empty_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_integer is required."]


def test_mandatory_array_integer_parameter_provided_as_none_filled_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_integer is required."]


def test_mandatory_array_integer_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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


def test_mandatory_array_integer_parameter_with_wrong_type_in_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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


def test_optional_array_integer_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_array_integer="str value"
    ) == [
        "query_array_integer value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_optional_array_integer_parameter_with_wrong_type_in_array(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_array_integer=["str value"]
    ) == [
        "query_array_integer value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_mandatory_integer32_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_integer32 is required."]


def test_mandatory_integer32_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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


def test_optional_integer32_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_integer32="str value"
    ) == [
        "query_integer32 value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_mandatory_array_integer32_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_integer32 is required."]


def test_mandatory_array_integer32_parameter_provided_as_empty_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_integer32 is required."]


def test_mandatory_array_integer32_parameter_provided_as_none_filled_array(
    json_service,
):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_integer32 is required."]


def test_mandatory_array_integer32_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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


def test_mandatory_array_integer32_parameter_with_wrong_type_in_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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


def test_optional_array_integer32_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_array_integer32="str value"
    ) == [
        "query_array_integer32 value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_optional_array_integer32_parameter_with_wrong_type_in_array(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_array_integer32=["str value"]
    ) == [
        "query_array_integer32 value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_mandatory_integer64_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_integer64 is required."]


def test_mandatory_integer64_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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


def test_optional_integer64_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_integer64="str value"
    ) == [
        "query_integer64 value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_mandatory_array_integer64_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_integer64 is required."]


def test_mandatory_array_integer64_parameter_provided_as_empty_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_integer64 is required."]


def test_mandatory_array_integer64_parameter_provided_as_none_filled_array(
    json_service,
):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_integer64 is required."]


def test_mandatory_array_integer64_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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


def test_mandatory_array_integer64_parameter_with_wrong_type_in_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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


def test_optional_array_integer64_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_array_integer64="str value"
    ) == [
        "query_array_integer64 value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_optional_array_integer64_parameter_with_wrong_type_in_array(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_array_integer64=["str value"]
    ) == [
        "query_array_integer64 value \"str value\" (<class 'str'> type) must be an integer."
    ]


def test_mandatory_number_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_number is required."]


def test_mandatory_number_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_number value \"str value\" (<class 'str'> type) must be a number."]


def test_optional_number_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_number="str value"
    ) == ["query_number value \"str value\" (<class 'str'> type) must be a number."]


def test_mandatory_array_number_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_number is required."]


def test_mandatory_array_number_parameter_provided_as_empty_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_number is required."]


def test_mandatory_array_number_parameter_provided_as_none_filled_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_number is required."]


def test_mandatory_array_number_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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


def test_mandatory_array_number_parameter_with_wrong_type_in_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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


def test_optional_array_number_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_array_number="str value"
    ) == [
        "query_array_number value \"str value\" (<class 'str'> type) must be a number."
    ]


def test_optional_array_number_parameter_with_wrong_type_in_array(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_array_number=["str value"]
    ) == [
        "query_array_number value \"str value\" (<class 'str'> type) must be a number."
    ]


def test_mandatory_float_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_float is required."]


def test_mandatory_float_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_float value \"str value\" (<class 'str'> type) must be a number."]


def test_optional_float_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_float="str value"
    ) == ["query_float value \"str value\" (<class 'str'> type) must be a number."]


def test_mandatory_array_float_number_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_float is required."]


def test_mandatory_array_float_parameter_provided_as_empty_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_float is required."]


def test_mandatory_array_float_parameter_provided_as_none_filled_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_float is required."]


def test_mandatory_array_float_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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


def test_mandatory_array_float_parameter_with_wrong_type_in_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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


def test_optional_array_float_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_array_float="str value"
    ) == [
        "query_array_float value \"str value\" (<class 'str'> type) must be a number."
    ]


def test_optional_array_float_parameter_with_wrong_type_in_array(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_array_float=["str value"]
    ) == [
        "query_array_float value \"str value\" (<class 'str'> type) must be a number."
    ]


def test_mandatory_double_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_double is required."]


def test_mandatory_double_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_double value \"str value\" (<class 'str'> type) must be a number."]


def test_optional_double_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_double="str value"
    ) == ["query_double value \"str value\" (<class 'str'> type) must be a number."]


def test_mandatory_array_double_number_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_double is required."]


def test_mandatory_array_double_parameter_provided_as_empty_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_double is required."]


def test_mandatory_array_double_parameter_provided_as_none_filled_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_double is required."]


def test_mandatory_array_double_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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


def test_mandatory_array_double_parameter_with_wrong_type_in_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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


def test_optional_array_double_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_array_double="str value"
    ) == [
        "query_array_double value \"str value\" (<class 'str'> type) must be a number."
    ]


def test_optional_array_double_parameter_with_wrong_type_in_array(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_array_double=["str value"]
    ) == [
        "query_array_double value \"str value\" (<class 'str'> type) must be a number."
    ]


def test_mandatory_string_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_string is required."]


def test_mandatory_string_parameter_provided_as_empty_array(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_string is required."]


def test_mandatory_string_parameter_provided_as_none_filled_array(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_string is required."]


def test_mandatory_array_string_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_string is required."]


def test_mandatory_array_string_parameter_provided_as_empty_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_string is required."]


def test_mandatory_array_string_parameter_provided_as_none_filled_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_string is required."]


def test_mandatory_string_byte_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_string_byte is required."]


def test_mandatory_string_byte_parameter_provided_as_empty_array(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_string_byte is required."]


def test_mandatory_string_byte_parameter_provided_as_none_filled_array(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_string_byte is required."]


def test_mandatory_array_string_byte_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_string_byte is required."]


def test_mandatory_array_string_byte_parameter_provided_as_empty_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_string_byte is required."]


def test_mandatory_array_string_byte_parameter_provided_as_none_filled_array(
    json_service,
):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_string_byte is required."]


def test_mandatory_string_binary_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_string_binary is required."]


def test_mandatory_string_binary_parameter_provided_as_empty_array(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_string_binary is required."]


def test_mandatory_string_binary_parameter_provided_as_none_filled_array(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_string_binary is required."]


def test_mandatory_array_string_binary_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_string_binary is required."]


def test_mandatory_array_string_binary_parameter_provided_as_empty_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_string_binary is required."]


def test_mandatory_array_string_binary_parameter_provided_as_none_filled_array(
    json_service,
):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_string_binary is required."]


def test_mandatory_boolean_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_boolean is required."]


def test_mandatory_boolean_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_boolean value \"non boolean\" (<class 'str'> type) must be a boolean."]


def test_optional_boolean_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_boolean="non boolean"
    ) == ["query_boolean value \"non boolean\" (<class 'str'> type) must be a boolean."]


def test_mandatory_array_boolean_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_boolean is required."]


def test_mandatory_array_boolean_parameter_provided_as_empty_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_boolean is required."]


def test_mandatory_array_boolean_parameter_provided_as_none_filled_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_boolean is required."]


def test_mandatory_array_boolean_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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


def test_mandatory_array_boolean_parameter_with_wrong_type_in_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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


def test_optional_array_boolean_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_array_boolean="non boolean"
    ) == [
        "query_array_boolean value \"non boolean\" (<class 'str'> type) must be a boolean."
    ]


def test_optional_array_boolean_parameter_with_wrong_type_in_array(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_array_boolean=["non boolean"]
    ) == [
        "query_array_boolean value \"non boolean\" (<class 'str'> type) must be a boolean."
    ]


def test_mandatory_date_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_date is required."]


def test_mandatory_date_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_date value \"str value\" (<class 'str'> type) must be a date."]


def test_optional_date_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_date="str value"
    ) == ["query_date value \"str value\" (<class 'str'> type) must be a date."]


def test_mandatory_array_date_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_date is required."]


def test_mandatory_array_date_parameter_provided_as_empty_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_date is required."]


def test_mandatory_array_date_parameter_provided_as_none_filled_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_date is required."]


def test_mandatory_array_date_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_date value \"str value\" (<class 'str'> type) must be a date."]


def test_mandatory_array_date_parameter_with_wrong_type_in_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_date value \"str value\" (<class 'str'> type) must be a date."]


def test_optional_array_date_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_array_date="str value"
    ) == ["query_array_date value \"str value\" (<class 'str'> type) must be a date."]


def test_optional_array_date_parameter_with_wrong_type_in_array(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_array_date=["str value"]
    ) == ["query_array_date value \"str value\" (<class 'str'> type) must be a date."]


def test_mandatory_date_time_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_date_time is required."]


def test_mandatory_date_time_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    assert user_defined_functions.json_get_all_parameters_types(
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


def test_optional_date_time_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_date_time="str value"
    ) == [
        "query_date_time value \"str value\" (<class 'str'> type) must be a date time."
    ]


def test_mandatory_array_date_time_parameter_not_provided(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_date_time is required."]


def test_mandatory_array_date_time_parameter_provided_as_empty_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_date_time is required."]


def test_mandatory_array_date_time_parameter_provided_as_none_filled_array(
    json_service,
):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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
    ) == ["query_array_date_time is required."]


def test_mandatory_array_date_time_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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


def test_mandatory_array_date_time_parameter_with_wrong_type_in_array(json_service):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    today_datetime = datetime.datetime.today()
    assert user_defined_functions.json_get_all_parameters_types(
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


def test_valid_mandatory_parameters(json_service, responses):
    from pyxelrest import user_defined_functions

    today_date = datetime.date.today()
    tomorrow_date = today_date + datetime.timedelta(days=1)
    today_datetime = datetime.datetime.combine(today_date, datetime.datetime.min.time())
    tomorrow_datetime = datetime.datetime.combine(
        tomorrow_date, datetime.datetime.min.time()
    )
    today_date_str = today_date.strftime("%Y-%m-%d")
    tomorrow_date_str = tomorrow_date.strftime("%Y-%m-%d")
    today_datetime_str_T = today_datetime.strftime("%Y-%m-%dT%H:%M:%S")
    tomorrow_datetime_str_T = tomorrow_datetime.strftime("%Y-%m-%dT%H:%M:%S")

    responses.add(
        responses.GET,
        url=f"http://localhost:8954/all_parameters_types?query_array_boolean=True&query_array_boolean=False&query_array_date={today_date_str}&query_array_date={tomorrow_date_str}&query_array_date_time={today_datetime_str_T}&query_array_date_time={tomorrow_datetime_str_T}&query_array_double=1.1&query_array_double=2.1&query_array_float=1.01&query_array_float=2.01&query_array_integer=1&query_array_integer=2&query_array_integer32=10&query_array_integer32=20&query_array_integer64=100&query_array_integer64=200&query_array_number=0.1&query_array_number=0.2&query_array_password=password 1&query_array_password=password 2&query_array_string=string 1&query_array_string=string 2&query_array_string_binary=string binary 1&query_array_string_binary=string binary 2&query_array_string_byte=string bytes 1&query_array_string_byte=string bytes 2&query_boolean=True&query_date={today_date_str}&query_date_time={today_datetime_str_T}&query_double=1.1&query_float=1.01&query_integer=1&query_integer32=10&query_integer64=100&query_number=0.1&query_password=password&query_string=string&query_string_binary=string binary&query_string_byte=string bytes",
        json={
            "query_array_boolean": "True",
            "query_array_date": today_date_str,
            "query_array_date_time": today_datetime_str_T,
            "query_array_double": "1.1",
            "query_array_float": "1.01",
            "query_array_integer": "1",
            "query_array_integer32": "10",
            "query_array_integer64": "100",
            "query_array_number": "0.1",
            "query_array_password": "password 1",
            "query_array_string": "string 1",
            "query_array_string_binary": "string binary 1",
            "query_array_string_byte": "string bytes 1",
            "query_boolean": "True",
            "query_date": today_date_str,
            "query_date_time": today_datetime_str_T,
            "query_double": "1.1",
            "query_float": "1.01",
            "query_integer": "1",
            "query_integer32": "10",
            "query_integer64": "100",
            "query_number": "0.1",
            "query_password": "password",
            "query_string": "string",
            "query_string_binary": "string binary",
            "query_string_byte": "string bytes",
        },
        match_querystring=True,
    )
    assert user_defined_functions.json_get_all_parameters_types(
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
        query_date=today_date,
        query_date_time=today_datetime,
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
        query_array_date=[today_date, tomorrow_date],
        query_array_date_time=[today_datetime, tomorrow_datetime],
        query_array_password=["password 1", "password 2"],
    ) == {
        "query_array_boolean": "True",
        "query_array_date": today_date_str,
        "query_array_date_time": today_datetime_str_T,
        "query_array_double": "1.1",
        "query_array_float": "1.01",
        "query_array_integer": "1",
        "query_array_integer32": "10",
        "query_array_integer64": "100",
        "query_array_number": "0.1",
        "query_array_password": "password 1",
        "query_array_string": "string 1",
        "query_array_string_binary": "string binary 1",
        "query_array_string_byte": "string bytes 1",
        "query_boolean": "True",
        "query_date": today_date_str,
        "query_date_time": today_datetime_str_T,
        "query_double": "1.1",
        "query_float": "1.01",
        "query_integer": "1",
        "query_integer32": "10",
        "query_integer64": "100",
        "query_number": "0.1",
        "query_password": "password",
        "query_string": "string",
        "query_string_binary": "string binary",
        "query_string_byte": "string bytes",
    }


def test_optional_array_date_time_parameter_with_wrong_type(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_array_date_time="str value"
    ) == [
        "query_array_date_time value \"str value\" (<class 'str'> type) must be a date time."
    ]


def test_optional_array_date_time_parameter_with_wrong_type_in_array(json_service):
    from pyxelrest import user_defined_functions

    assert user_defined_functions.json_get_all_optional_parameters_types(
        query_array_date_time=["str value"]
    ) == [
        "query_array_date_time value \"str value\" (<class 'str'> type) must be a date time."
    ]

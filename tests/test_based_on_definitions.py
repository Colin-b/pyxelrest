import datetime

from dateutil.tz import tzutc
import pytest
from responses import RequestsMock

from testsutils import loader


@pytest.fixture
def services(responses: RequestsMock):
    # filtered tags service
    responses.add(
        responses.GET,
        url="http://localhost:8944/",
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
                "/tags": {
                    "get": {
                        "operationId": "get_tags",
                        "tags": ["tag 0", "tag 1"],
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
                        "operationId": "post_tags",
                        "tags": ["tag 1", "tag 2"],
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
                        "operationId": "put_tags",
                        "tags": ["tag 2", "tag 3"],
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
                        "operationId": "delete_tags",
                        "tags": ["tag 3", "tag 4"],
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
                }
            },
        },
        match_querystring=True,
    )
    # values false service
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
    # output order service
    responses.add(
        responses.GET,
        url="http://localhost:8946/",
        json={
            "swagger": "2.0",
            "definitions": {
                "Price": {
                    "required": ["curve", "date", "mat", "ts"],
                    "type": "object",
                    "properties": {
                        "ts": {
                            "type": "string",
                            "description": "timeslot",
                            "maxLength": 2,
                        },
                        "date": {
                            "type": "string",
                            "description": "date",
                            "format": "date",
                        },
                        "curve": {
                            "type": "string",
                            "description": "curvename",
                            "maxLength": 20,
                        },
                        "mat": {
                            "type": "string",
                            "description": "maturity",
                            "maxLength": 4,
                        },
                    },
                    "title": "RealizedPrice",
                }
            },
            "paths": {
                "/price/unordered": {
                    "get": {
                        "operationId": "get_price_unordered",
                        "description": "Price",
                        "parameters": [
                            {
                                "in": "query",
                                "description": "date",
                                "format": "date",
                                "required": False,
                                "type": "string",
                                "name": "date",
                            },
                            {
                                "name": "curve",
                                "in": "query",
                                "required": False,
                                "type": "string",
                                "description": "curvename",
                            },
                            {
                                "name": "ts",
                                "in": "query",
                                "required": False,
                                "type": "string",
                                "description": "timeslot",
                            },
                            {
                                "name": "mat",
                                "in": "query",
                                "required": False,
                                "type": "string",
                                "description": "maturity",
                            },
                        ],
                        "responses": {
                            "200": {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"$ref": "#/definitions/Price"},
                                    "type": "array",
                                },
                            }
                        },
                    }
                }
            },
        },
        match_querystring=True,
    )
    # without_parameter_service
    responses.add(
        responses.GET,
        url="http://localhost:8950/",
        json={
            "swagger": "2.0",
            "definitions": {"Test": {"properties": {}}},
            "paths": {
                "/without_parameter": {
                    "get": {
                        "operationId": "get_without_parameter",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {"type": "string"},
                            }
                        },
                    },
                    "post": {
                        "operationId": "post_without_parameter",
                        "responses": {
                            "200": {"description": "POST performed properly"}
                        },
                    },
                    "put": {
                        "operationId": "put_without_parameter",
                        "responses": {"200": {"description": "PUT performed properly"}},
                    },
                    "delete": {
                        "operationId": "delete_without_parameter",
                        "responses": {
                            "200": {"description": "DELETE performed properly"}
                        },
                    },
                },
                "/plain_text_without_parameter": {
                    "get": {
                        "operationId": "get_plain_text_without_parameter",
                        "produces": ["text/plain"],
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {"type": "string"},
                            }
                        },
                    },
                    "post": {
                        "operationId": "post_plain_text_without_parameter",
                        "produces": ["text/plain"],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "put": {
                        "operationId": "put_plain_text_without_parameter",
                        "produces": ["text/plain"],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "delete": {
                        "operationId": "delete_plain_text_without_parameter",
                        "produces": ["text/plain"],
                        "responses": {"200": {"description": "return value"}},
                    },
                },
                "/json_without_parameter": {
                    "get": {
                        "operationId": "get_json_without_parameter",
                        "produces": ["application/json"],
                        "responses": {
                            "200": {
                                "description": "return value",
                                "$ref": "#/definitions/Test",
                            }
                        },
                    },
                    "post": {
                        "operationId": "post_json_without_parameter",
                        "produces": ["application/json"],
                        "responses": {
                            "200": {
                                "description": "return value",
                                "$ref": "#/definitions/Test",
                            }
                        },
                    },
                    "put": {
                        "operationId": "put_json_without_parameter",
                        "produces": ["application/json"],
                        "responses": {
                            "200": {
                                "description": "return value",
                                "$ref": "#/definitions/Test",
                            }
                        },
                    },
                    "delete": {
                        "operationId": "delete_json_without_parameter",
                        "produces": ["application/json"],
                        "responses": {
                            "200": {
                                "description": "return value",
                                "$ref": "#/definitions/Test",
                            }
                        },
                    },
                },
                "/octet_without_parameter": {
                    "get": {
                        "operationId": "get_octet_without_parameter",
                        "produces": ["application/octet-stream"],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "post": {
                        "operationId": "post_octet_without_parameter",
                        "produces": ["application/octet-stream"],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "put": {
                        "operationId": "put_octet_without_parameter",
                        "produces": ["application/octet-stream"],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "delete": {
                        "operationId": "delete_octet_without_parameter",
                        "produces": ["application/octet-stream"],
                        "responses": {"200": {"description": "return value"}},
                    },
                },
            },
        },
        match_querystring=True,
    )
    # header_parameter_service
    responses.add(
        responses.GET,
        url="http://localhost:8951/",
        json={
            "swagger": "2.0",
            "definitions": {
                "Header": {
                    "type": "object",
                    "properties": {
                        "Accept": {"type": "string"},
                        "Accept-Encoding": {"type": "string"},
                        "Connection": {"type": "string"},
                        "Content-Length": {"type": "string"},
                        "Content-Type": {"type": "string"},
                        "Header-String": {"type": "string"},
                        "Host": {"type": "string"},
                        "User-Agent": {"type": "string"},
                    },
                    "title": "Test",
                }
            },
            "paths": {
                "/header": {
                    "get": {
                        "operationId": "get_header",
                        "parameters": [
                            {
                                "description": "header parameter",
                                "in": "header",
                                "name": "header_string",
                                "required": True,
                                "type": "string",
                            }
                        ],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {"$ref": "#/definitions/Header"},
                            }
                        },
                    }
                }
            },
        },
        match_querystring=True,
    )
    # form_parameter_service
    responses.add(
        responses.GET,
        url="http://localhost:8952/",
        json={
            "swagger": "2.0",
            "definitions": {
                "Form": {
                    "type": "object",
                    "properties": {"form_string": {"type": "string"}},
                    "title": "Test",
                }
            },
            "paths": {
                "/form": {
                    "post": {
                        "operationId": "post_form",
                        "parameters": [
                            {
                                "description": "form parameter",
                                "in": "formData",
                                "name": "form_string",
                                "required": True,
                                "type": "string",
                            }
                        ],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {"$ref": "#/definitions/Form"},
                            }
                        },
                    }
                }
            },
        },
        match_querystring=True,
    )
    # array_parameter_service
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

    pyxelrestgenerator = loader.load("based_on_definitions_services.yml")


def test_string_multi_array_parameter(services):

    result = "string_array=\"['str1', 'str2']\""
    assert (
        pyxelrestgenerator.array_parameter_get_string_multi_array_parameter(
            ["str1", "str2"]
        )
        == result
    )


def test_string_default_array_parameter(services):

    result = "string_array=\"['str1,str2']\""
    assert (
        pyxelrestgenerator.array_parameter_get_string_default_array_parameter(
            ["str1", "str2"]
        )
        == result
    )


def test_string_csv_array_parameter(services):

    result = "string_array=\"['str1,str2']\""
    assert (
        pyxelrestgenerator.array_parameter_get_string_csv_array_parameter(
            ["str1", "str2"]
        )
        == result
    )


def test_string_ssv_array_parameter(services):

    result = "string_array=\"['str1 str2']\""
    assert (
        pyxelrestgenerator.array_parameter_get_string_ssv_array_parameter(
            ["str1", "str2"]
        )
        == result
    )


def test_string_tsv_array_parameter(services):

    result = "string_array=\"['str1\\tstr2']\""
    assert (
        pyxelrestgenerator.array_parameter_get_string_tsv_array_parameter(
            ["str1", "str2"]
        )
        == result
    )


def test_string_pipes_array_parameter(services):

    result = "string_array=\"['str1|str2']\""
    assert (
        pyxelrestgenerator.array_parameter_get_string_pipes_array_parameter(
            ["str1", "str2"]
        )
        == result
    )


def test_plain_text_without_parameter(services):

    assert (
        pyxelrestgenerator.without_parameter_get_plain_text_without_parameter()
        == "string value returned should be truncated so that the following information cannot be seen by user, because of the fact that Excel does not allow more than 255 characters in a cell. Only the 255 characters will be returned by the user defined functions:  "
    )


def test_post_without_parameter(services):

    assert (
        pyxelrestgenerator.without_parameter_post_without_parameter()
        == "POST performed properly"
    )


def test_put_without_parameter(services):

    assert (
        pyxelrestgenerator.without_parameter_put_without_parameter()
        == "PUT performed properly"
    )


def test_delete_without_parameter(services):

    assert (
        pyxelrestgenerator.without_parameter_delete_without_parameter()
        == "DELETE performed properly"
    )


def test_get_header_parameter(services):

    headers = pyxelrestgenerator.header_parameter_get_header("sent header")
    header_param_index = headers[0].index("Header-String")
    assert headers[1][header_param_index] == "sent header"


def test_post_form_parameter(services):

    assert pyxelrestgenerator.form_parameter_post_form("sent string form data") == [
        ["form_string"],
        ["sent string form data"],
    ]


def test_get_with_tags(services):

    assert (
        "Second tag is one of the accepted tags"
        == pyxelrestgenerator.filtered_tags_get_tags()
    )


def test_post_with_tags(services):

    assert "All tags are accepted" == pyxelrestgenerator.filtered_tags_post_tags()


def test_put_with_tags(services):

    assert (
        "First tag is one of the accepted tags"
        == pyxelrestgenerator.filtered_tags_put_tags()
    )


def test_delete_with_tags(services):

    assert not hasattr(pyxelrestgenerator, "filtered_tags_delete_tags")


def test_get_with_zero_integer(services):

    assert pyxelrestgenerator.values_false_get_with_zero_integer() == [
        ["zero_integer"],
        [0],
    ]


def test_get_with_zero_float(services):

    assert pyxelrestgenerator.values_false_get_with_zero_float() == [
        ["zero_float"],
        [0.0],
    ]


def test_get_with_false_boolean(services):

    assert pyxelrestgenerator.values_false_get_with_false_boolean() == [
        ["false_boolean"],
        [False],
    ]


def test_get_with_empty_string(services):

    assert pyxelrestgenerator.values_false_get_with_empty_string() == [
        ["empty_string"],
        [""],
    ]


def test_get_with_empty_list(services):

    assert pyxelrestgenerator.values_false_get_with_empty_list() == [""]


def test_get_with_empty_dictionary(services):

    assert pyxelrestgenerator.values_false_get_with_empty_dictionary() == [""]


def test_get_compare_output_order(services):

    assert pyxelrestgenerator.output_order_get_price_unordered() == [
        [u"ts", u"date", u"curve", u"mat"],
        [u"", datetime.datetime(2017, 4, 5, 0, 0), u"PW_FR", u"H01"],
        [u"2017-04-05 12:03:15", datetime.datetime(2017, 4, 5, 0, 0), u"PW_FR", u"H02"],
        [u"", datetime.datetime(2017, 4, 5, 0, 0), u"PW_FR", u"H03"],
    ]

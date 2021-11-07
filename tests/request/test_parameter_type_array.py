from responses import RequestsMock

from tests import loader


def test_null_array_parameter(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_array_parameter",
                        "parameters": [
                            {
                                "in": "query",
                                "name": "array",
                                "required": False,
                                "items": {"type": "string"},
                                "type": "array",
                            }
                        ],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "type": "string",
                            }
                        },
                    }
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "array_parameter": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.array_parameter_get_array_parameter(None) == [[""]]


def test_string_multi_array_parameter(
    responses: RequestsMock, tmpdir, clean_generated_functions
):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_array_parameter",
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
                                    "items": {"type": "string"},
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
    generated_functions = loader.load(
        tmpdir,
        {
            "array_parameter": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test?string_array=str1&string_array=str2",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.array_parameter_get_array_parameter(
        ["str1", "str2"]
    ) == [[""]]


def test_string_default_array_parameter(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_array_parameter",
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
                                    "items": {"type": "string"},
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
    generated_functions = loader.load(
        tmpdir,
        {
            "array_parameter": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test?string_array=str1,str2",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.array_parameter_get_array_parameter(
        ["str1", "str2"]
    ) == [[""]]


def test_string_ssv_array_parameter(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_array_parameter",
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
                                    "items": {"type": "string"},
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
    generated_functions = loader.load(
        tmpdir,
        {
            "array_parameter": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test?string_array=str1%20str2",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.array_parameter_get_array_parameter(
        ["str1", "str2"]
    ) == [[""]]


def test_string_tsv_array_parameter(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_array_parameter",
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
                                    "items": {"type": "string"},
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
    generated_functions = loader.load(
        tmpdir,
        {
            "array_parameter": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test?string_array=str1%09str2",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.array_parameter_get_array_parameter(
        ["str1", "str2"]
    ) == [[""]]


def test_string_csv_array_parameter(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_array_parameter",
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
                                    "items": {"type": "string"},
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
    generated_functions = loader.load(
        tmpdir,
        {
            "array_parameter": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test?string_array=str1,str2",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.array_parameter_get_array_parameter(
        ["str1", "str2"]
    ) == [[""]]


def test_string_pipes_array_parameter(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_array_parameter",
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
                                    "items": {"type": "string"},
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
    generated_functions = loader.load(
        tmpdir,
        {
            "array_parameter": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test?string_array=str1|str2",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.array_parameter_get_array_parameter(
        ["str1", "str2"]
    ) == [[""]]


def test_string_unknown_array_parameter(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_array_parameter",
                        "parameters": [
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "string_array",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                                "collectionFormat": "unknown",
                            }
                        ],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"type": "string"},
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
    generated_functions = loader.load(
        tmpdir,
        {
            "array_parameter": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.array_parameter_get_array_parameter(["str1", "str2"])
        == "Collection format unknown is invalid."
    )


def test_array_unique_parameter(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_array_parameter",
                        "parameters": [
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "string_array",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                                "uniqueItems": True,
                            }
                        ],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"type": "string"},
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
    generated_functions = loader.load(
        tmpdir,
        {
            "array_parameter": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        generated_functions.array_parameter_get_array_parameter(["str1", "str1"])
        == "string_array contains duplicated items."
    )


def test_array_maximum_items_parameter(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_array_parameter",
                        "parameters": [
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "string_array",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                                "maxItems": 2,
                            }
                        ],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"type": "string"},
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
    generated_functions = loader.load(
        tmpdir,
        {
            "array_parameter": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test?string_array=str1,str1",
        json=[],
        match_querystring=True,
    )

    assert (
        generated_functions.array_parameter_get_array_parameter(
            ["str1", "str1", "str1"]
        )
        == "string_array cannot contains more than 2 items."
    )

    assert generated_functions.array_parameter_get_array_parameter(
        ["str1", "str1"]
    ) == [[""]]


def test_array_minimum_items_parameter(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_array_parameter",
                        "parameters": [
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "string_array",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                                "minItems": 2,
                            }
                        ],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"type": "string"},
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
    generated_functions = loader.load(
        tmpdir,
        {
            "array_parameter": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test?string_array=str1,str1",
        json=[],
        match_querystring=True,
    )

    assert (
        generated_functions.array_parameter_get_array_parameter(["str1"])
        == "string_array cannot contains less than 2 items."
    )
    assert generated_functions.array_parameter_get_array_parameter(
        ["str1", "str1"]
    ) == [[""]]


def test_file_array_parameter_description(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_array_parameter",
                        "parameters": [
                            {
                                "in": "query",
                                "name": "files",
                                "required": True,
                                "items": {"type": "file"},
                                "type": "array",
                            }
                        ],
                        "responses": {
                            200: {
                                "type": "string",
                            }
                        },
                    }
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "array_parameter": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    assert (
        generated_functions.array_parameter_get_array_parameter.__xlfunc__["args"][0][
            "doc"
        ]
        == """
Value must be an array of cells with files content or files paths."""
    )

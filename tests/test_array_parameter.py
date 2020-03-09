from responses import RequestsMock

from tests import loader


def test_string_multi_array_parameter(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
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
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test?string_array=str1&string_array=str2",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.array_parameter_get_string_multi_array_parameter(
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
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test?string_array=str1,str2",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.array_parameter_get_string_default_array_parameter(
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
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test?string_array=str1,str2",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.array_parameter_get_string_csv_array_parameter(
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
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test?string_array=str1%20str2",
        json=[],
        match_querystring=True,
    )

    assert hasattr(
        generated_functions, "array_parameter_get_string_ssv_array_parameter"
    ), str(generated_functions.__dict__)
    assert generated_functions.array_parameter_get_string_ssv_array_parameter(
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
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test?string_array=str1\tstr2",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.array_parameter_get_string_tsv_array_parameter(
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
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test?string_array=str1|str2",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.array_parameter_get_string_pipes_array_parameter(
        ["str1", "str2"]
    ) == [[""]]

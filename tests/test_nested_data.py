import pytest
from responses import RequestsMock

from tests import loader


@pytest.fixture
def nested_data_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8947/",
        json={
            "swagger": "2.0",
            "definitions": {
                "Column": {
                    "type": "object",
                    "properties": {
                        "Column 1": {"type": "string", "description": "column1"},
                        "Column 2": {
                            "type": "array",
                            "description": "column2",
                            "items": {"$ref": "#/definitions/Column"},
                        },
                        "Column 3": {"type": "string", "description": "column3"},
                    },
                    "title": "Column",
                },
                "Column1": {
                    "type": "object",
                    "properties": {
                        "Column 1": {
                            "type": "array",
                            "items": {"$ref": "#/definitions/Column2And3"},
                        }
                    },
                    "title": "Column1",
                },
                "Column2And3": {
                    "type": "object",
                    "properties": {
                        "Column 2": {"type": "string", "description": "column1"},
                        "Column 3": {"type": "string", "description": "column3"},
                    },
                    "title": "Column2+3",
                },
                "Column1List": {
                    "type": "object",
                    "properties": {
                        "Column 1": {"type": "array", "items": {"type": "string"}}
                    },
                    "title": "Column1",
                },
            },
            "paths": {
                "/dict_with_empty_nested_list": {
                    "get": {
                        "operationId": "get_dict_with_empty_nested_list",
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {"$ref": "#/definitions/Column"},
                            }
                        },
                    }
                },
                "/dict_with_three_imbricated_levels": {
                    "get": {
                        "operationId": "get_dict_with_three_imbricated_levels",
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {"$ref": "#/definitions/Column"},
                            }
                        },
                    }
                },
                "/dict_with_four_imbricated_levels": {
                    "get": {
                        "operationId": "get_dict_with_four_imbricated_levels",
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {"$ref": "#/definitions/Column"},
                            }
                        },
                    }
                },
                "/dict_with_multiple_imbricated_levels_and_duplicate_keys": {
                    "get": {
                        "operationId": "get_dict_with_multiple_imbricated_levels_and_duplicate_keys",
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {"$ref": "#/definitions/Column"},
                            }
                        },
                    }
                },
                "/empty_dict": {
                    "get": {
                        "operationId": "get_empty_dict",
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {"$ref": "#/definitions/Column"},
                            }
                        },
                    }
                },
                "/empty_list": {
                    "get": {
                        "operationId": "get_empty_list",
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"$ref": "#/definitions/Column"},
                                    "type": "array",
                                },
                            }
                        },
                    }
                },
                "/one_level_dict": {
                    "get": {
                        "operationId": "get_one_level_dict",
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {"$ref": "#/definitions/Column2And3"},
                            }
                        },
                    }
                },
                "/one_level_list": {
                    "get": {
                        "operationId": "get_one_level_list",
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
                },
                "/one_dict_entry_with_a_list": {
                    "get": {
                        "operationId": "get_one_dict_entry_with_a_list",
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {"$ref": "#/definitions/Column1List"},
                            }
                        },
                    }
                },
                "/one_dict_entry_with_a_list_of_dict": {
                    "get": {
                        "operationId": "get_one_dict_entry_with_a_list_of_dict",
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {"$ref": "#/definitions/Column1"},
                            }
                        },
                    }
                },
                "/list_of_dict": {
                    "get": {
                        "operationId": "get_list_of_dict",
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"$ref": "#/definitions/Column2And3"},
                                    "type": "array",
                                },
                            }
                        },
                    }
                },
                "/dict_with_list": {
                    "get": {
                        "operationId": "get_dict_with_list",
                        "responses": {200: {"description": "successful operation"}},
                    }
                },
                "/dict_with_list_of_different_size": {
                    "get": {
                        "operationId": "get_dict_with_list_of_different_size",
                        "responses": {200: {"description": "successful operation"}},
                    }
                },
                "/dict_with_various_columns": {
                    "get": {
                        "operationId": "get_dict_with_various_columns",
                        "responses": {200: {"description": "successful operation"}},
                    }
                },
            },
        },
        match_querystring=True,
    )


def test_get_dict_with_empty_nested_list(nested_data_service, responses, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {"definition": "http://localhost:8947/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/dict_with_empty_nested_list",
        json={
            "Column 1": "0-0-1",
            "Column 2": [
                {
                    "Column 1": "0-0-2 / 1-0-1",
                    "Column 2": [],
                    "Column 3": "0-0-2 / 1-0-3",
                },
                {
                    "Column 1": "0-0-2 / 1-1-1",
                    "Column 2": [
                        {
                            "Column 1": "0-0-2 / 1-1-2 / 2-0-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-1-2 / 2-0-3",
                        },
                        {
                            "Column 1": "0-0-2 / 1-1-2 / 2-1-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-1-2 / 2-1-3",
                        },
                    ],
                    "Column 3": "0-0-2 / 1-1-3",
                },
            ],
            "Column 3": "0-0-3",
        },
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_dict_with_empty_nested_list() == [
        [
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 3",
            "Column 3",
            "Column 3",
        ],
        ["0-0-1", "", "0-0-2 / 1-0-1", "", "", "", "", "0-0-2 / 1-0-3", "0-0-3"],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-0-1",
            "",
            "0-0-2 / 1-1-2 / 2-0-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-1-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
    ]


def test_get_dict_with_empty_nested_list_based_on_definitions(
    nested_data_service, responses, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {
                    "definition": "http://localhost:8947/",
                    "rely_on_definitions": True,
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/dict_with_empty_nested_list",
        json={
            "Column 1": "0-0-1",
            "Column 2": [
                {
                    "Column 1": "0-0-2 / 1-0-1",
                    "Column 2": [],
                    "Column 3": "0-0-2 / 1-0-3",
                },
                {
                    "Column 1": "0-0-2 / 1-1-1",
                    "Column 2": [
                        {
                            "Column 1": "0-0-2 / 1-1-2 / 2-0-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-1-2 / 2-0-3",
                        },
                        {
                            "Column 1": "0-0-2 / 1-1-2 / 2-1-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-1-2 / 2-1-3",
                        },
                    ],
                    "Column 3": "0-0-2 / 1-1-3",
                },
            ],
            "Column 3": "0-0-3",
        },
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_dict_with_empty_nested_list() == [
        [
            "Column 1",
            "Column 2 / Column 1",
            "Column 2 / Column 2 / Column 1",
            "Column 2 / Column 2 / Column 3",
            "Column 2 / Column 3",
            "Column 3",
        ],
        ["0-0-1", "0-0-2 / 1-0-1", "", "", "0-0-2 / 1-0-3", "0-0-3"],
        [
            "0-0-1",
            "0-0-2 / 1-1-1",
            "0-0-2 / 1-1-2 / 2-0-1",
            "0-0-2 / 1-1-2 / 2-0-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "0-0-2 / 1-1-1",
            "0-0-2 / 1-1-2 / 2-1-1",
            "0-0-2 / 1-1-2 / 2-1-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
    ]


def test_get_dict_with_three_imbricated_levels(nested_data_service, responses, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {"definition": "http://localhost:8947/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/dict_with_three_imbricated_levels",
        json={
            "Column 1": "0-0-1",
            "Column 2": [
                {
                    "Column 1": "0-0-2 / 1-0-1",
                    "Column 2": [
                        {
                            "Column 1": "0-0-2 / 1-0-2 / 2-0-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-0-2 / 2-0-3",
                        },
                        {
                            "Column 1": "0-0-2 / 1-0-2 / 2-1-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-0-2 / 2-1-3",
                        },
                    ],
                    "Column 3": "0-0-2 / 1-0-3",
                },
                {
                    "Column 1": "0-0-2 / 1-1-1",
                    "Column 2": [
                        {
                            "Column 1": "0-0-2 / 1-1-2 / 2-0-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-1-2 / 2-0-3",
                        },
                        {
                            "Column 1": "0-0-2 / 1-1-2 / 2-1-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-1-2 / 2-1-3",
                        },
                    ],
                    "Column 3": "0-0-2 / 1-1-3",
                },
            ],
            "Column 3": "0-0-3",
        },
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_dict_with_three_imbricated_levels() == [
        [
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 3",
            "Column 3",
            "Column 3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-1-1",
            "",
            "0-0-2 / 1-0-2 / 2-1-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-0-1",
            "",
            "0-0-2 / 1-1-2 / 2-0-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-1-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
    ]


def test_get_dict_with_three_imbricated_levels_based_on_definitions(
    nested_data_service, responses, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {
                    "definition": "http://localhost:8947/",
                    "rely_on_definitions": True,
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/dict_with_three_imbricated_levels",
        json={
            "Column 1": "0-0-1",
            "Column 2": [
                {
                    "Column 1": "0-0-2 / 1-0-1",
                    "Column 2": [
                        {
                            "Column 1": "0-0-2 / 1-0-2 / 2-0-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-0-2 / 2-0-3",
                        },
                        {
                            "Column 1": "0-0-2 / 1-0-2 / 2-1-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-0-2 / 2-1-3",
                        },
                    ],
                    "Column 3": "0-0-2 / 1-0-3",
                },
                {
                    "Column 1": "0-0-2 / 1-1-1",
                    "Column 2": [
                        {
                            "Column 1": "0-0-2 / 1-1-2 / 2-0-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-1-2 / 2-0-3",
                        },
                        {
                            "Column 1": "0-0-2 / 1-1-2 / 2-1-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-1-2 / 2-1-3",
                        },
                    ],
                    "Column 3": "0-0-2 / 1-1-3",
                },
            ],
            "Column 3": "0-0-3",
        },
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_dict_with_three_imbricated_levels() == [
        [
            "Column 1",
            "Column 2 / Column 1",
            "Column 2 / Column 2 / Column 1",
            "Column 2 / Column 2 / Column 3",
            "Column 2 / Column 3",
            "Column 3",
        ],
        [
            "0-0-1",
            "0-0-2 / 1-0-1",
            "0-0-2 / 1-0-2 / 2-0-1",
            "0-0-2 / 1-0-2 / 2-0-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "0-0-2 / 1-0-1",
            "0-0-2 / 1-0-2 / 2-1-1",
            "0-0-2 / 1-0-2 / 2-1-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "0-0-2 / 1-1-1",
            "0-0-2 / 1-1-2 / 2-0-1",
            "0-0-2 / 1-1-2 / 2-0-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "0-0-2 / 1-1-1",
            "0-0-2 / 1-1-2 / 2-1-1",
            "0-0-2 / 1-1-2 / 2-1-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
    ]


def test_get_dict_with_four_imbricated_levels(nested_data_service, responses, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {"definition": "http://localhost:8947/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/dict_with_four_imbricated_levels",
        json={
            "Column 1": "0-0-1",
            "Column 2": [
                {
                    "Column 1": "0-0-2 / 1-0-1",
                    "Column 2": [
                        {
                            "Column 1": "0-0-2 / 1-0-2 / 2-0-1",
                            "Column 2": [
                                {
                                    "Column 1": "0-0-2 / 1-0-2 / 2-0-2 / 3-0-1",
                                    "Column 2": [],
                                    "Column 3": "0-0-2 / 1-0-2 / 2-0-2 / 3-0-3",
                                },
                                {
                                    "Column 1": "0-0-2 / 1-0-2 / 2-0-2 / 3-1-1",
                                    "Column 2": [],
                                    "Column 3": "0-0-2 / 1-0-2 / 2-0-2 / 3-1-3",
                                },
                            ],
                            "Column 3": "0-0-2 / 1-0-2 / 2-0-3",
                        },
                        {
                            "Column 1": "0-0-2 / 1-0-2 / 2-1-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-0-2 / 2-1-3",
                        },
                    ],
                    "Column 3": "0-0-2 / 1-0-3",
                },
                {
                    "Column 1": "0-0-2 / 1-1-1",
                    "Column 2": [
                        {
                            "Column 1": "0-0-2 / 1-1-2 / 2-0-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-1-2 / 2-0-3",
                        },
                        {
                            "Column 1": "0-0-2 / 1-1-2 / 2-1-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-1-2 / 2-1-3",
                        },
                    ],
                    "Column 3": "0-0-2 / 1-1-3",
                },
            ],
            "Column 3": "0-0-3",
        },
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_dict_with_four_imbricated_levels() == [
        [
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 3",
            "Column 3",
            "Column 3",
            "Column 3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-0-3",
            "0-0-2 / 1-0-2 / 2-0-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-1-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-1-3",
            "0-0-2 / 1-0-2 / 2-0-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-1-1",
            "",
            "",
            "",
            "",
            "0-0-2 / 1-0-2 / 2-1-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-0-1",
            "",
            "",
            "",
            "",
            "0-0-2 / 1-1-2 / 2-0-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-1-1",
            "",
            "",
            "",
            "",
            "0-0-2 / 1-1-2 / 2-1-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
    ]


def test_get_dict_with_four_imbricated_levels_based_on_definitions(
    nested_data_service, responses, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {
                    "definition": "http://localhost:8947/",
                    "rely_on_definitions": True,
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/dict_with_four_imbricated_levels",
        json={
            "Column 1": "0-0-1",
            "Column 2": [
                {
                    "Column 1": "0-0-2 / 1-0-1",
                    "Column 2": [
                        {
                            "Column 1": "0-0-2 / 1-0-2 / 2-0-1",
                            "Column 2": [
                                {
                                    "Column 1": "0-0-2 / 1-0-2 / 2-0-2 / 3-0-1",
                                    "Column 2": [],
                                    "Column 3": "0-0-2 / 1-0-2 / 2-0-2 / 3-0-3",
                                },
                                {
                                    "Column 1": "0-0-2 / 1-0-2 / 2-0-2 / 3-1-1",
                                    "Column 2": [],
                                    "Column 3": "0-0-2 / 1-0-2 / 2-0-2 / 3-1-3",
                                },
                            ],
                            "Column 3": "0-0-2 / 1-0-2 / 2-0-3",
                        },
                        {
                            "Column 1": "0-0-2 / 1-0-2 / 2-1-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-0-2 / 2-1-3",
                        },
                    ],
                    "Column 3": "0-0-2 / 1-0-3",
                },
                {
                    "Column 1": "0-0-2 / 1-1-1",
                    "Column 2": [
                        {
                            "Column 1": "0-0-2 / 1-1-2 / 2-0-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-1-2 / 2-0-3",
                        },
                        {
                            "Column 1": "0-0-2 / 1-1-2 / 2-1-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-1-2 / 2-1-3",
                        },
                    ],
                    "Column 3": "0-0-2 / 1-1-3",
                },
            ],
            "Column 3": "0-0-3",
        },
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_dict_with_four_imbricated_levels() == [
        [
            "Column 1",
            "Column 2 / Column 1",
            "Column 2 / Column 2 / Column 1",
            "Column 2 / Column 2 / Column 2 / Column 1",
            "Column 2 / Column 2 / Column 2 / Column 3",
            "Column 2 / Column 2 / Column 3",
            "Column 2 / Column 3",
            "Column 3",
        ],
        [
            "0-0-1",
            "0-0-2 / 1-0-1",
            "0-0-2 / 1-0-2 / 2-0-1",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-0-1",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-0-3",
            "0-0-2 / 1-0-2 / 2-0-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "0-0-2 / 1-0-1",
            "0-0-2 / 1-0-2 / 2-0-1",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-1-1",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-1-3",
            "0-0-2 / 1-0-2 / 2-0-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "0-0-2 / 1-0-1",
            "0-0-2 / 1-0-2 / 2-1-1",
            "",
            "",
            "0-0-2 / 1-0-2 / 2-1-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "0-0-2 / 1-1-1",
            "0-0-2 / 1-1-2 / 2-0-1",
            "",
            "",
            "0-0-2 / 1-1-2 / 2-0-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "0-0-2 / 1-1-1",
            "0-0-2 / 1-1-2 / 2-1-1",
            "",
            "",
            "0-0-2 / 1-1-2 / 2-1-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
    ]


def test_get_dict_with_multiple_imbricated_levels_and_duplicate_keys(
    nested_data_service, responses, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {"definition": "http://localhost:8947/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/dict_with_multiple_imbricated_levels_and_duplicate_keys",
        json={
            "Column 1": "0-0-1",
            "Column 2": [
                {
                    "Column 1": "0-0-2 / 1-0-1",
                    "Column 2": [
                        {
                            "Column 1": "0-0-2 / 1-0-2 / 2-0-1",
                            "Column 2": [
                                {
                                    "Column 1": "0-0-2 / 1-0-2 / 2-0-2 / 3-0-1",
                                    "Column 2": [],
                                    "Column 3": "0-0-2 / 1-0-2 / 2-0-2 / 3-0-3",
                                },
                                {
                                    "Column 1": "0-0-2 / 1-0-2 / 2-0-2 / 3-1-1",
                                    "Column 2": [],
                                    "Column 3": "0-0-2 / 1-0-2 / 2-0-2 / 3-1-3",
                                },
                            ],
                            "Column 3": "0-0-2 / 1-0-2 / 2-0-3",
                        },
                        {
                            "Column 1": "0-0-2 / 1-0-2 / 2-1-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-0-2 / 2-1-3",
                        },
                    ],
                    "Column 3": "0-0-2 / 1-0-3",
                },
                {
                    "Column 1": "0-0-2 / 1-1-1",
                    "Column 2": [
                        {
                            "Column 1": "0-0-2 / 1-1-2 / 2-0-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-1-2 / 2-0-3",
                        },
                        {
                            "Column 1": "0-0-2 / 1-1-2 / 2-1-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-1-2 / 2-1-3",
                        },
                    ],
                    "Column 3": "0-0-2 / 1-1-3",
                },
            ],
            "Column 3": "0-0-3",
        },
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_dict_with_multiple_imbricated_levels_and_duplicate_keys() == [
        [
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 3",
            "Column 3",
            "Column 3",
            "Column 3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-0-3",
            "0-0-2 / 1-0-2 / 2-0-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-1-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-1-3",
            "0-0-2 / 1-0-2 / 2-0-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-1-1",
            "",
            "",
            "",
            "",
            "0-0-2 / 1-0-2 / 2-1-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-0-1",
            "",
            "",
            "",
            "",
            "0-0-2 / 1-1-2 / 2-0-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-1-1",
            "",
            "",
            "",
            "",
            "0-0-2 / 1-1-2 / 2-1-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
    ]


def test_get_dict_with_multiple_imbricated_levels_and_duplicate_keys_based_on_definitions(
    nested_data_service, responses, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {
                    "definition": "http://localhost:8947/",
                    "rely_on_definitions": True,
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/dict_with_multiple_imbricated_levels_and_duplicate_keys",
        json={
            "Column 1": "0-0-1",
            "Column 2": [
                {
                    "Column 1": "0-0-2 / 1-0-1",
                    "Column 2": [
                        {
                            "Column 1": "0-0-2 / 1-0-2 / 2-0-1",
                            "Column 2": [
                                {
                                    "Column 1": "0-0-2 / 1-0-2 / 2-0-2 / 3-0-1",
                                    "Column 2": [],
                                    "Column 3": "0-0-2 / 1-0-2 / 2-0-2 / 3-0-3",
                                },
                                {
                                    "Column 1": "0-0-2 / 1-0-2 / 2-0-2 / 3-1-1",
                                    "Column 2": [],
                                    "Column 3": "0-0-2 / 1-0-2 / 2-0-2 / 3-1-3",
                                },
                            ],
                            "Column 3": "0-0-2 / 1-0-2 / 2-0-3",
                        },
                        {
                            "Column 1": "0-0-2 / 1-0-2 / 2-1-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-0-2 / 2-1-3",
                        },
                    ],
                    "Column 3": "0-0-2 / 1-0-3",
                },
                {
                    "Column 1": "0-0-2 / 1-1-1",
                    "Column 2": [
                        {
                            "Column 1": "0-0-2 / 1-1-2 / 2-0-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-1-2 / 2-0-3",
                        },
                        {
                            "Column 1": "0-0-2 / 1-1-2 / 2-1-1",
                            "Column 2": [],
                            "Column 3": "0-0-2 / 1-1-2 / 2-1-3",
                        },
                    ],
                    "Column 3": "0-0-2 / 1-1-3",
                },
            ],
            "Column 3": "0-0-3",
        },
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_dict_with_multiple_imbricated_levels_and_duplicate_keys() == [
        [
            "Column 1",
            "Column 2 / Column 1",
            "Column 2 / Column 2 / Column 1",
            "Column 2 / Column 2 / Column 2 / Column 1",
            "Column 2 / Column 2 / Column 2 / Column 3",
            "Column 2 / Column 2 / Column 3",
            "Column 2 / Column 3",
            "Column 3",
        ],
        [
            "0-0-1",
            "0-0-2 / 1-0-1",
            "0-0-2 / 1-0-2 / 2-0-1",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-0-1",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-0-3",
            "0-0-2 / 1-0-2 / 2-0-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "0-0-2 / 1-0-1",
            "0-0-2 / 1-0-2 / 2-0-1",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-1-1",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-1-3",
            "0-0-2 / 1-0-2 / 2-0-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "0-0-2 / 1-0-1",
            "0-0-2 / 1-0-2 / 2-1-1",
            "",
            "",
            "0-0-2 / 1-0-2 / 2-1-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "0-0-2 / 1-1-1",
            "0-0-2 / 1-1-2 / 2-0-1",
            "",
            "",
            "0-0-2 / 1-1-2 / 2-0-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "0-0-2 / 1-1-1",
            "0-0-2 / 1-1-2 / 2-1-1",
            "",
            "",
            "0-0-2 / 1-1-2 / 2-1-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
    ]


def test_get_empty_dict(nested_data_service, responses, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {"definition": "http://localhost:8947/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/empty_dict",
        json={},
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_empty_dict() == [[""]]


def test_get_empty_dict_based_on_definitions(nested_data_service, responses, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {
                    "definition": "http://localhost:8947/",
                    "rely_on_definitions": True,
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/empty_dict",
        json={},
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_empty_dict() == [""]


def test_get_empty_list(nested_data_service, responses, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {"definition": "http://localhost:8947/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/empty_list",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_empty_list() == [[""]]


def test_get_empty_list_based_on_definitions(nested_data_service, responses, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {
                    "definition": "http://localhost:8947/",
                    "rely_on_definitions": True,
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/empty_list",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_empty_list() == [""]


def test_get_one_level_dict(nested_data_service, responses, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {"definition": "http://localhost:8947/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/one_level_dict",
        json={"Column 2": "value 1", "Column 3": "value 2"},
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_one_level_dict() == [
        ["Column 2", "Column 3"],
        ["value 1", "value 2"],
    ]


def test_get_one_level_dict_based_on_definitions(
    nested_data_service, responses, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {
                    "definition": "http://localhost:8947/",
                    "rely_on_definitions": True,
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/one_level_dict",
        json={"Column 2": "value 1", "Column 3": "value 2"},
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_one_level_dict() == [
        ["Column 2", "Column 3"],
        ["value 1", "value 2"],
    ]


def test_get_one_level_list(nested_data_service, responses, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {"definition": "http://localhost:8947/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/one_level_list",
        json=["value 1", "value 2"],
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_one_level_list() == [
        ["value 1"],
        ["value 2"],
    ]


def test_get_one_level_list_based_on_definitions(
    nested_data_service, responses, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {
                    "definition": "http://localhost:8947/",
                    "rely_on_definitions": True,
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/one_level_list",
        json=["value 1", "value 2"],
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_one_level_list() == [
        ["value 1"],
        ["value 2"],
    ]


def test_get_one_dict_entry_with_a_list(nested_data_service, responses, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {"definition": "http://localhost:8947/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/one_dict_entry_with_a_list",
        json={"Column 1": ["value 1", "value 2"]},
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_one_dict_entry_with_a_list() == [
        ["Column 1", "Column 1"],
        ["", "value 1"],
        ["", "value 2"],
    ]


def test_get_one_dict_entry_with_a_list_based_on_definitions(
    nested_data_service, responses, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {
                    "definition": "http://localhost:8947/",
                    "rely_on_definitions": True,
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/one_dict_entry_with_a_list",
        json={"Column 1": ["value 1", "value 2"]},
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_one_dict_entry_with_a_list() == [
        ["Column 1"],
        ["value 1"],
        ["value 2"],
    ]


def test_get_one_dict_entry_with_a_list_of_dict(nested_data_service, responses, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {"definition": "http://localhost:8947/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/one_dict_entry_with_a_list_of_dict",
        json={
            "Column 1": [
                {"Column 2": "value 12", "Column 3": "value 13"},
                {"Column 2": "value 22", "Column 3": "value 23"},
            ]
        },
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_one_dict_entry_with_a_list_of_dict() == [
        ["Column 1", "Column 2", "Column 3"],
        ["", "value 12", "value 13"],
        ["", "value 22", "value 23"],
    ]


def test_get_one_dict_entry_with_a_list_of_dict_based_on_definitions(
    nested_data_service, responses, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {
                    "definition": "http://localhost:8947/",
                    "rely_on_definitions": True,
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/one_dict_entry_with_a_list_of_dict",
        json={
            "Column 1": [
                {"Column 2": "value 12", "Column 3": "value 13"},
                {"Column 2": "value 22", "Column 3": "value 23"},
            ]
        },
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_one_dict_entry_with_a_list_of_dict() == [
        ["Column 1 / Column 2", "Column 1 / Column 3"],
        ["value 12", "value 13"],
        ["value 22", "value 23"],
    ]


def test_get_list_of_dict(nested_data_service, responses, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {"definition": "http://localhost:8947/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/list_of_dict",
        json=[
            {"Column 2": "value 11", "Column 3": "value 12"},
            {"Column 2": "value 21", "Column 3": "value 22"},
        ],
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_list_of_dict() == [
        ["Column 2", "Column 3"],
        ["value 11", "value 12"],
        ["value 21", "value 22"],
    ]


def test_get_list_of_dict_based_on_definitions(nested_data_service, responses, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {
                    "definition": "http://localhost:8947/",
                    "rely_on_definitions": True,
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/list_of_dict",
        json=[
            {"Column 2": "value 11", "Column 3": "value 12"},
            {"Column 2": "value 21", "Column 3": "value 22"},
        ],
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_list_of_dict() == [
        ["Column 2", "Column 3"],
        ["value 11", "value 12"],
        ["value 21", "value 22"],
    ]


def test_get_dict_with_list(nested_data_service, responses, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {"definition": "http://localhost:8947/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/dict_with_list",
        json={
            "Column 1": 23,
            "Column 2": True,
            "Column 3": ["this", "is", "a", "test"],
        },
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_dict_with_list() == [
        ["Column 1", "Column 2", "Column 3", "Column 3"],
        [23, True, "this", ""],
        [23, True, "is", ""],
        [23, True, "a", ""],
        [23, True, "test", ""],
    ]


def test_get_dict_with_list_based_on_definitions(
    nested_data_service, responses, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {
                    "definition": "http://localhost:8947/",
                    "rely_on_definitions": True,
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/dict_with_list",
        json={
            "Column 1": 23,
            "Column 2": True,
            "Column 3": ["this", "is", "a", "test"],
        },
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_dict_with_list() == [
        ["Column 1", "Column 2", "Column 3"],
        [23, True, "this"],
        [23, True, "is"],
        [23, True, "a"],
        [23, True, "test"],
    ]


def test_get_dict_with_list_of_different_size(nested_data_service, responses, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {"definition": "http://localhost:8947/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/dict_with_list_of_different_size",
        json={
            "Column 1": [23],
            "Column 2": [24],
            "Column 3": ["value 1", "value 2", "value 3"],
        },
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_dict_with_list_of_different_size() == [
        ["Column 1", "Column 2", "Column 1", "Column 2", "Column 3", "Column 3"],
        ["", "", 23, 24, "value 1", ""],
        ["", "", "value 2", ""],
        ["", "", "value 3", ""],
    ]


def test_get_dict_with_list_of_different_size_based_on_definitions(
    nested_data_service, responses, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "nested_data": {
                "open_api": {
                    "definition": "http://localhost:8947/",
                    "rely_on_definitions": True,
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8947/dict_with_list_of_different_size",
        json={
            "Column 1": [23],
            "Column 2": [24],
            "Column 3": ["value 1", "value 2", "value 3"],
        },
        match_querystring=True,
    )

    assert generated_functions.nested_data_get_dict_with_list_of_different_size() == [
        ["Column 1", "Column 2", "Column 3"],
        [23, 24, "value 1"],
        [23, 24, "value 2"],
        [23, 24, "value 3"],
    ]

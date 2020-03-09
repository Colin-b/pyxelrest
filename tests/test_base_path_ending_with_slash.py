from responses import RequestsMock

from tests import loader


def test_get_base_path_ending_with_slash(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "basePath": "//",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_method",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {"type": "string"},
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
            "base_path_ending_with_slash": {
                "open_api": {"definition": "http://test/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.GET, url="http://test/test", json={}, match_querystring=True
    )

    assert generated_functions.base_path_ending_with_slash_get_method() == [[""]]


def test_post_base_path_ending_with_slash(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "basePath": "//",
            "paths": {
                "/test": {
                    "post": {
                        "operationId": "post_method",
                        "responses": {
                            "200": {"description": "POST performed properly"}
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
            "base_path_ending_with_slash": {
                "open_api": {"definition": "http://test/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.POST, url="http://test/test", json={}, match_querystring=True
    )

    assert generated_functions.base_path_ending_with_slash_post_method() == [[""]]


def test_put_base_path_ending_with_slash(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "basePath": "//",
            "paths": {
                "/test": {
                    "put": {
                        "operationId": "put_method",
                        "responses": {"200": {"description": "PUT performed properly"}},
                    }
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "base_path_ending_with_slash": {
                "open_api": {"definition": "http://test/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.PUT, url="http://test/test", json={}, match_querystring=True
    )

    assert generated_functions.base_path_ending_with_slash_put_method() == [[""]]


def test_delete_base_path_ending_with_slash(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "basePath": "//",
            "paths": {
                "/test": {
                    "delete": {
                        "operationId": "delete_method",
                        "responses": {
                            "200": {"description": "DELETE performed properly"}
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
            "base_path_ending_with_slash": {
                "open_api": {"definition": "http://test/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.DELETE, url="http://test/test", json={}, match_querystring=True
    )

    assert generated_functions.base_path_ending_with_slash_delete_method() == [[""]]

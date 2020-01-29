import datetime

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


def support_pandas():
    try:
        import pandas

        return True
    except:
        return False


@pytest.fixture
def output_order_service(responses: RequestsMock):
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


@pytest.fixture
def open_api_definition_parsing_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8948/swagger_version_not_provided",
        json={
            "paths": {
                "/should_not_be_available": {
                    "get": {
                        "operationId": "get_should_not_be_available",
                        "responses": {200: {"description": "successful operation"}},
                    }
                }
            }
        },
        match_querystring=True,
    )
    responses.add(
        responses.GET,
        url="http://localhost:8948/swagger_version_not_supported",
        json={
            "swagger": "1.0",
            "paths": {
                "/should_not_be_available": {
                    "get": {
                        "operationId": "get_should_not_be_available",
                        "responses": {200: {"description": "successful operation"}},
                    }
                }
            },
        },
        match_querystring=True,
    )
    responses.add(
        responses.GET,
        url="http://localhost:8948/operation_id_not_provided",
        json={
            "swagger": "2.0",
            "paths": {
                "/without_operationId": {
                    "get": {"responses": {200: {"description": "successful operation"}}}
                }
            },
        },
        match_querystring=True,
    )
    responses.add(
        responses.GET,
        url="http://localhost:8948/operation_id_not_always_provided",
        json={
            "swagger": "2.0",
            "paths": {
                "/without_operationId": {
                    "get": {"responses": {200: {"description": "successful operation"}}}
                },
                "/with_operationId": {
                    "get": {
                        # This is obviously misleading but it can happen...
                        "operationId": "get_without_operationId",
                        "responses": {200: {"description": "successful operation"}},
                    }
                },
            },
        },
        match_querystring=True,
    )


@pytest.fixture
def http_methods_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8955/",
        json={
            "swagger": "2.0",
            "paths": {
                "/http_methods": {
                    "get": {
                        "operationId": "get_http_methods",
                        "responses": {200: {"description": "successful operation"}},
                    },
                    "post": {
                        "operationId": "post_http_methods",
                        "responses": {200: {"description": "successful operation"}},
                    },
                    "put": {
                        "operationId": "put_http_methods",
                        "responses": {200: {"description": "successful operation"}},
                    },
                    "delete": {
                        "operationId": "delete_http_methods",
                        "responses": {200: {"description": "successful operation"}},
                    },
                    "patch": {
                        "operationId": "patch_http_methods",
                        "responses": {200: {"description": "successful operation"}},
                    },
                    "options": {
                        "operationId": "options_http_methods",
                        "responses": {200: {"description": "successful operation"}},
                    },
                    "head": {
                        "operationId": "head_http_methods",
                        "responses": {200: {"description": "successful operation"}},
                    },
                }
            },
        },
        match_querystring=True,
    )


@pytest.fixture
def content_type_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8956/",
        json={
            "swagger": "2.0",
            "paths": {
                "/msgpackpandas": {
                    "get": {
                        "operationId": "get_msgpackpandas",
                        "responses": {200: {"description": "successful operation"}},
                        "produces": ["application/msgpackpandas"],
                    }
                },
                "/json": {
                    "get": {
                        "operationId": "get_json",
                        "responses": {200: {"description": "successful operation"}},
                        "produces": ["application/json"],
                    }
                },
            },
        },
        match_querystring=True,
    )


@pytest.fixture
def base_path_ending_with_slash_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8957/",
        json={
            "swagger": "2.0",
            "basePath": "//",
            "paths": {
                "/method": {
                    "get": {
                        "operationId": "get_method",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {"type": "string"},
                            }
                        },
                    },
                    "post": {
                        "operationId": "post_method",
                        "responses": {
                            "200": {"description": "POST performed properly"}
                        },
                    },
                    "put": {
                        "operationId": "put_method",
                        "responses": {"200": {"description": "PUT performed properly"}},
                    },
                    "delete": {
                        "operationId": "delete_method",
                        "responses": {
                            "200": {"description": "DELETE performed properly"}
                        },
                    },
                }
            },
        },
        match_querystring=True,
    )


@pytest.fixture
def async_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8958/",
        json={
            "swagger": "2.0",
            "paths": {
                "/async": {
                    "get": {
                        "operationId": "get_async",
                        "responses": {
                            "202": {
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


@pytest.fixture
def services(
    output_order_service,
    open_api_definition_parsing_service,
    http_methods_service,
    content_type_service,
    base_path_ending_with_slash_service,
    async_service,
):
    # TODO add static_file_call_service mock to the specific test case
    loader.load("services.yml")


def test_get_compare_output_order(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.output_order_get_price_unordered() == [
        [u"curve", u"date", u"mat", u"ts"],
        [u"PW_FR", datetime.datetime(2017, 4, 5, 0, 0), u"H01", u""],
        [u"PW_FR", datetime.datetime(2017, 4, 5, 0, 0), u"H02", u"2017-04-05 12:03:15"],
        [u"PW_FR", datetime.datetime(2017, 4, 5, 0, 0), u"H03", u""],
    ]


def test_get_static_open_api_definition(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.open_api_definition_loaded_from_file_get_static_file_call()
        == "success"
    )


def test_get_http_method(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.http_methods_get_http_methods() == "GET"


def test_post_http_method(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.http_methods_post_http_methods() == "POST"


def test_put_http_method(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.http_methods_put_http_methods() == "PUT"


def test_delete_http_method(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.http_methods_delete_http_methods() == "DELETE"


def test_patch_http_method(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.http_methods_patch_http_methods() == "PATCH"


def test_options_http_method(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.http_methods_options_http_methods() == "OPTIONS"


def test_head_http_method(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    # HEAD is already handled by Flask
    assert pyxelrestgenerator.http_methods_head_http_methods() == ""


def test_msgpackpandas_content_type(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.content_type_get_msgpackpandas()
        == ["application/msgpackpandas"]
        if support_pandas()
        else ["*/*"]
    )


def test_json_content_type(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.content_type_get_json() == ["application/json"]


def test_missing_operation_id(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.operation_id_not_provided_get_without_operationId()
        == "/without_operationId called."
    )


def test_mixed_operation_id(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.operation_id_not_always_provided_get_without_operationId()
        == "/with_operationId called."
    )
    assert (
        pyxelrestgenerator.operation_id_not_always_provided_duplicated_get_without_operationId()
        == "/without_operationId called."
    )


def test_get_base_path_ending_with_slash(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.base_path_ending_with_slash_get_method()
        == "http://localhost:8957/method"
    )


def test_post_base_path_ending_with_slash(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.base_path_ending_with_slash_post_method()
        == "http://localhost:8957/method"
    )


def test_put_base_path_ending_with_slash(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.base_path_ending_with_slash_put_method()
        == "http://localhost:8957/method"
    )


def test_delete_base_path_ending_with_slash(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.base_path_ending_with_slash_delete_method()
        == "http://localhost:8957/method"
    )


def test_get_async_url(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.async_get_async() == [
        ["Status URL"],
        ["http://localhost:8958/async/status"],
    ]


def test_get_custom_url_sync(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.vba_pyxelrest_get_url(
        "http://localhost:8958/async/status",
        extra_headers=[
            ["X-Custom-Header1", "custom1"],
            ["X-Custom-Header2", "custom2"],
        ],
    ) == [["X-Custom-Header1", "X-Custom-Header2"], ["custom1", "custom2"]]


def test_get_custom_url(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.pyxelrest_get_url(
        "http://localhost:8958/async/status",
        extra_headers=[
            ["X-Custom-Header1", "custom1"],
            ["X-Custom-Header2", "custom2"],
        ],
    ) == [["X-Custom-Header1", "X-Custom-Header2"], ["custom1", "custom2"]]


def test_delete_custom_url_sync(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.vba_pyxelrest_delete_url(
        "http://localhost:8958/unlisted",
        extra_headers=[
            ["X-Custom-Header1", "custom1"],
            ["X-Custom-Header2", "custom2"],
        ],
    ) == [["X-Custom-Header1", "X-Custom-Header2"], ["custom1", "custom2"]]


def test_delete_custom_url(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.pyxelrest_delete_url(
        "http://localhost:8958/unlisted",
        extra_headers=[
            ["X-Custom-Header1", "custom1"],
            ["X-Custom-Header2", "custom2"],
        ],
    ) == [["X-Custom-Header1", "X-Custom-Header2"], ["custom1", "custom2"]]


def test_post_custom_url_dict(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.pyxelrest_post_url(
        "http://localhost:8958/dict",
        [["key1", "key2", "key3"], ["value1", 1, "value3"]],
        extra_headers=[["Content-Type", "application/json"]],
        parse_body_as="dict",
    ) == [["key1", "key2", "key3"], ["value1", 1, "value3"]]


def test_post_custom_url_dict_list_sync(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.vba_pyxelrest_post_url(
        "http://localhost:8958/dict",
        [["key1", "key2", "key3"], ["value1", 1, "value3"], ["other1", 2, "other3"]],
        extra_headers=[["Content-Type", "application/json"]],
        parse_body_as="dict_list",
    ) == [["key1", "key2", "key3"], ["value1", 1, "value3"], ["other1", 2, "other3"]]


def test_post_custom_url_dict_list(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.pyxelrest_post_url(
        "http://localhost:8958/dict",
        [["key1", "key2", "key3"], ["value1", 1, "value3"], ["other1", 2, "other3"]],
        extra_headers=[["Content-Type", "application/json"]],
        parse_body_as="dict_list",
    ) == [["key1", "key2", "key3"], ["value1", 1, "value3"], ["other1", 2, "other3"]]


def test_put_custom_url_dict_list(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.pyxelrest_put_url(
        "http://localhost:8958/dict",
        [["key1", "key2", "key3"], ["value1", 1, "value3"], ["other1", 2, "other3"]],
        extra_headers=[["Content-Type", "application/json"]],
        parse_body_as="dict_list",
    ) == [["key1", "key2", "key3"], ["value1", 1, "value3"], ["other1", 2, "other3"]]


def test_put_custom_url_dict(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.pyxelrest_put_url(
        "http://localhost:8958/dict",
        [["key1", "key2", "key3"], ["value1", 1, "value3"]],
        extra_headers=[["Content-Type", "application/json"]],
        parse_body_as="dict",
    ) == [["key1", "key2", "key3"], ["value1", 1, "value3"]]


def test_put_custom_url_dict_sync(responses: RequestsMock, services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.vba_pyxelrest_put_url(
        "http://localhost:8958/dict",
        [["key1", "key2", "key3"], ["value1", 1, "value3"]],
        extra_headers=[["Content-Type", "application/json"]],
        parse_body_as="dict",
    ) == [["key1", "key2", "key3"], ["value1", 1, "value3"]]

import requests_auth
from requests import PreparedRequest
from requests_auth.testing import token_cache_mock
import pytest
from responses import RequestsMock

from tests import loader


def _get_request(responses: RequestsMock, url: str) -> PreparedRequest:
    for call in responses.calls:
        if call.request.url == url:
            # Pop out verified request (to be able to check multiple requests)
            responses.calls._calls.remove(call)
            return call.request


@pytest.fixture
def services(responses: RequestsMock, tmpdir):
    # authenticated_service
    responses.add(
        responses.GET,
        url="http://localhost:8946/",
        json={
            "swagger": "2.0",
            "paths": {
                "/oauth2/authentication/success": {
                    "get": {
                        "operationId": "get_oauth2_authentication_success",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"oauth2_auth_success": ["custom_label"]}],
                    }
                },
                "/oauth2/authentication/success/with/custom/response/type": {
                    "get": {
                        "operationId": "get_oauth2_authentication_success_with_custom_response_type",
                        "responses": {"200": {"description": "return value"}},
                        "security": [
                            {
                                "oauth2_auth_success_with_custom_response_type": [
                                    "custom_label"
                                ]
                            }
                        ],
                    }
                },
                "/oauth2/authentication/success/without/response/type": {
                    "get": {
                        "operationId": "get_oauth2_authentication_success_without_response_type",
                        "responses": {"200": {"description": "return value"}},
                        "security": [
                            {
                                "oauth2_auth_success_without_response_type": [
                                    "custom_label"
                                ]
                            }
                        ],
                    }
                },
                "/oauth2/authentication/failure": {
                    "get": {
                        "operationId": "get_oauth2_authentication_failure",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"oauth2_auth_failure": ["custom_label"]}],
                    }
                },
                "/oauth2/authentication/timeout": {
                    "get": {
                        "operationId": "get_oauth2_authentication_timeout",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"oauth2_auth_timeout": ["custom_label"]}],
                    }
                },
                "/oauth2/authentication/success/quick/expiry": {
                    "get": {
                        "operationId": "get_oauth2_authentication_success_quick_expiry",
                        "responses": {"200": {"description": "return value"}},
                        "security": [
                            {"oauth2_auth_success_quick_expiry": ["custom_label"]}
                        ],
                    }
                },
                "/api/key/header/authentication/success": {
                    "get": {
                        "operationId": "get_api_key_header_authentication_success",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"api_key_header_auth_success": []}],
                    }
                },
                "/api/key/query/authentication/success": {
                    "get": {
                        "operationId": "get_api_key_query_authentication_success",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"api_key_query_auth_success": []}],
                    }
                },
                "/basic/authentication/success": {
                    "get": {
                        "operationId": "get_basic_authentication_success",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"basic_auth_success": []}],
                    }
                },
                "/basic/and/api/key/authentication/success": {
                    "get": {
                        "operationId": "get_basic_and_api_key_authentication_success",
                        "responses": {"200": {"description": "return value"}},
                        "security": [
                            {
                                "basic_auth_success": [],
                                "api_key_header_auth_success": [],
                            }
                        ],
                    }
                },
                "/basic/or/api/key/authentication/success": {
                    "get": {
                        "operationId": "get_basic_or_api_key_authentication_success",
                        "responses": {"200": {"description": "return value"}},
                        "security": [
                            {"basic_auth_success": []},
                            {"api_key_header_auth_success": []},
                        ],
                    }
                },
                "/api/key/or/basic/authentication/success": {
                    "get": {
                        "operationId": "get_api_key_or_basic_authentication_success",
                        "responses": {"200": {"description": "return value"}},
                        "security": [
                            {"api_key_header_auth_success": []},
                            {"basic_auth_success": []},
                        ],
                    }
                },
            },
            "securityDefinitions": {
                "oauth2_auth_success": {
                    "type": "oauth2",
                    "authorizationUrl": "http://localhost:8947/auth_success?response_type=id_token",
                    "flow": "implicit",
                    "scopes": {"custom_label": "custom category"},
                },
                "oauth2_auth_success_with_custom_response_type": {
                    "type": "oauth2",
                    "authorizationUrl": "http://localhost:8947/auth_success_with_custom_token",
                    "flow": "implicit",
                    "scopes": {"custom_label": "custom category"},
                },
                "oauth2_auth_success_without_response_type": {
                    "type": "oauth2",
                    "authorizationUrl": "http://localhost:8947/auth_success_without_response_type",
                    "flow": "implicit",
                    "scopes": {"custom_label": "custom category"},
                },
                "oauth2_auth_failure": {
                    "type": "oauth2",
                    "authorizationUrl": "http://localhost:8947/auth_failure?response_type=id_token",
                    "flow": "implicit",
                    "scopes": {"custom_label": "custom category"},
                },
                "oauth2_auth_timeout": {
                    "type": "oauth2",
                    "authorizationUrl": "http://localhost:8947/auth_timeout?response_type=id_token",
                    "flow": "implicit",
                    "scopes": {"custom_label": "custom category"},
                },
                "oauth2_auth_success_quick_expiry": {
                    "type": "oauth2",
                    "authorizationUrl": "http://localhost:8947/auth_success_quick_expiry?response_type=id_token",
                    "flow": "implicit",
                    "scopes": {"custom_label": "custom category"},
                },
                "api_key_header_auth_success": {
                    "type": "apiKey",
                    "in": "header",
                    "name": "X-API-HEADER-KEY",
                },
                "api_key_query_auth_success": {
                    "type": "apiKey",
                    "in": "query",
                    "name": "X-API-QUERY-KEY",
                },
                "basic_auth_success": {"type": "basic"},
            },
        },
        match_querystring=True,
    )
    # non_authenticated_service
    responses.add(
        responses.GET,
        url="http://localhost:8948/",
        json={
            "swagger": "2.0",
            "paths": {
                "/without_auth": {
                    "get": {
                        "operationId": "get_without_auth",
                        "responses": {"200": {"description": "return value"}},
                    }
                }
            },
        },
        match_querystring=True,
    )
    pyxelrestgenerator = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://localhost:8946/"},
                "api_key": "my_provided_api_key",
                "basic": {"username": "test_user", "password": "test_pwd"},
                "oauth2": {"timeout": 10},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            },
            "oauth_custom_token_name": {
                "open_api": {"definition": "http://localhost:8946/"},
                "oauth2": {"response_type": "my_custom_token"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            },
            "oauth_cutom_response_port": {
                "open_api": {"definition": "http://localhost:8946/"},
                "oauth2": {"redirect_uri_port": 5001},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            },
            "non_authenticated": {
                "open_api": {"definition": "http://localhost:8948/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            },
            "pyxelrest": {
                "api_key": "my_provided_api_key",
                "basic": {"username": "test_user", "password": "test_pwd"},
                "oauth2": {"timeout": 10},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            },
        },
    )


def test_oauth2_authentication_on_custom_server_port(
    services, token_cache_mock, responses: RequestsMock
):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8946/oauth2/authentication/success",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.oauth_cutom_response_port_get_oauth2_authentication_success() == [
        [""]
    ]
    assert (
        _get_request(
            responses, "http://localhost:8946/oauth2/authentication/success"
        ).headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )

    assert pyxelrestgenerator.authenticated_get_oauth2_authentication_success() == [
        [""]
    ]
    assert (
        _get_request(
            responses, "http://localhost:8946/oauth2/authentication/success"
        ).headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_oauth2_authentication_success(
    services, token_cache_mock, responses: RequestsMock
):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8946/oauth2/authentication/success",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.authenticated_get_oauth2_authentication_success() == [
        [""]
    ]
    assert (
        _get_request(
            responses, "http://localhost:8946/oauth2/authentication/success"
        ).headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_pyxelrest_oauth2_authentication_success(
    services, token_cache_mock, responses: RequestsMock
):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8946/oauth2/authentication/success",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.pyxelrest_get_url(
        "http://localhost:8946/oauth2/authentication/success",
        auth=["oauth2_implicit"],
        oauth2_auth_url="http://localhost:8947/auth_success?response_type=id_token",
    ) == [[""]]
    assert (
        _get_request(
            responses, "http://localhost:8946/oauth2/authentication/success"
        ).headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_oauth2_authentication_success_with_custom_response_type(
    services, token_cache_mock, responses: RequestsMock
):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8946/oauth2/authentication/success/with/custom/response/type",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.oauth_custom_token_name_get_oauth2_authentication_success_with_custom_response_type() == [
        [""]
    ]
    assert (
        _get_request(
            responses,
            "http://localhost:8946/oauth2/authentication/success/with/custom/response/type",
        ).headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_oauth2_authentication_success_without_response_type(
    services, token_cache_mock, responses: RequestsMock
):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8946/oauth2/authentication/success/without/response/type",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.authenticated_get_oauth2_authentication_success_without_response_type() == [
        [""]
    ]
    assert (
        _get_request(
            responses,
            "http://localhost:8946/oauth2/authentication/success/without/response/type",
        ).headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_pyxelrest_oauth2_authentication_success_without_response_type(
    services, token_cache_mock, responses: RequestsMock
):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8946/oauth2/authentication/success/without/response/type",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.pyxelrest_get_url(
        "http://localhost:8946/oauth2/authentication/success/without/response/type",
        auth=["oauth2_implicit"],
        oauth2_auth_url="http://localhost:8947/auth_success_without_response_type",
    ) == [[""]]
    assert (
        _get_request(
            responses,
            "http://localhost:8946/oauth2/authentication/success/without/response/type",
        ).headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_oauth2_authentication_token_reuse(
    services, token_cache_mock, responses: RequestsMock
):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8946/oauth2/authentication/success",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.authenticated_get_oauth2_authentication_success() == [
        [""]
    ]
    assert (
        _get_request(
            responses, "http://localhost:8946/oauth2/authentication/success"
        ).headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )

    # As the token should not be expired, this call should use the same token
    assert pyxelrestgenerator.authenticated_get_oauth2_authentication_success() == [
        [""]
    ]
    assert (
        _get_request(
            responses, "http://localhost:8946/oauth2/authentication/success"
        ).headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_pyxelrest_oauth2_authentication_token_reuse(
    services, token_cache_mock, responses: RequestsMock
):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8946/oauth2/authentication/success",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.pyxelrest_get_url(
        "http://localhost:8946/oauth2/authentication/success",
        auth=["oauth2_implicit"],
        oauth2_auth_url="http://localhost:8947/auth_success?response_type=id_token",
    ) == [[""]]
    assert (
        _get_request(
            responses, "http://localhost:8946/oauth2/authentication/success"
        ).headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )

    assert pyxelrestgenerator.pyxelrest_get_url(
        "http://localhost:8946/oauth2/authentication/success",
        auth=["oauth2_implicit"],
        oauth2_auth_url="http://localhost:8947/auth_success?response_type=id_token",
    ) == [[""]]
    assert (
        _get_request(
            responses, "http://localhost:8946/oauth2/authentication/success"
        ).headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_oauth2_authentication_failure(services, monkeypatch):
    from pyxelrest import pyxelrestgenerator

    class TokenCacheMock:
        def get_token(self, *args, **kwargs) -> str:
            raise requests_auth.errors.GrantNotProvided("id_token", {})

    monkeypatch.setattr(requests_auth.OAuth2, "token_cache", TokenCacheMock())
    assert (
        pyxelrestgenerator.authenticated_get_oauth2_authentication_failure()
        == 'An error occurred. Please check logs for full details: "id_token not provided within {}."'
    )


def test_oauth2_authentication_timeout(services, monkeypatch):
    from pyxelrest import pyxelrestgenerator

    class TokenCacheMock:
        def get_token(self, *args, **kwargs) -> str:
            raise requests_auth.errors.TimeoutOccurred(10)

    monkeypatch.setattr(requests_auth.OAuth2, "token_cache", TokenCacheMock())
    assert (
        pyxelrestgenerator.authenticated_get_oauth2_authentication_timeout()
        == 'An error occurred. Please check logs for full details: "User authentication was not received within 10 seconds."'
    )


def test_without_authentication(services, responses: RequestsMock):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8948/without_auth",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.non_authenticated_get_without_auth() == [[""]]


def test_api_key_header_authentication_success(services, responses: RequestsMock):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8946/api/key/header/authentication/success",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.authenticated_get_api_key_header_authentication_success() == [
        [""]
    ]
    request = _get_request(
        responses, "http://localhost:8946/api/key/header/authentication/success"
    )
    assert request.headers["X-API-HEADER-KEY"] == "my_provided_api_key"


def test_pyxelrest_api_key_header_authentication_success(
    services, responses: RequestsMock
):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8946/api/key/header/authentication/success",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.pyxelrest_get_url(
        "http://localhost:8946/api/key/header/authentication/success",
        auth=["api_key_header"],
        api_key_name="X-API-HEADER-KEY",
    ) == [[""]]
    request = _get_request(
        responses, "http://localhost:8946/api/key/header/authentication/success"
    )
    assert request.headers["X-API-HEADER-KEY"] == "my_provided_api_key"


def test_api_key_query_authentication_success(services, responses: RequestsMock):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8946/api/key/query/authentication/success?X-API-QUERY-KEY=my_provided_api_key",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.authenticated_get_api_key_query_authentication_success() == [
        [""]
    ]


def test_pyxelrest_api_key_query_authentication_success(
    services, responses: RequestsMock
):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8946/api/key/query/authentication/success?X-API-QUERY-KEY=my_provided_api_key",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.pyxelrest_get_url(
        "http://localhost:8946/api/key/query/authentication/success",
        auth=["api_key_query"],
        api_key_name="X-API-QUERY-KEY",
    ) == [[""]]


def test_basic_authentication_success(services, responses: RequestsMock):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8946/basic/authentication/success",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.authenticated_get_basic_authentication_success() == [[""]]
    request = _get_request(
        responses, "http://localhost:8946/basic/authentication/success"
    )
    assert request.headers["Authorization"] == "Basic dGVzdF91c2VyOnRlc3RfcHdk"


def test_pyxelrest_basic_authentication_success(services, responses: RequestsMock):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8946/basic/authentication/success",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.pyxelrest_get_url(
        "http://localhost:8946/basic/authentication/success", auth=["basic"]
    ) == [[""]]
    request = _get_request(
        responses, "http://localhost:8946/basic/authentication/success"
    )
    assert request.headers["Authorization"] == "Basic dGVzdF91c2VyOnRlc3RfcHdk"


def test_basic_and_api_key_authentication_success(services, responses: RequestsMock):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8946/basic/and/api/key/authentication/success",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.authenticated_get_basic_and_api_key_authentication_success() == [
        [""]
    ]
    request = _get_request(
        responses, "http://localhost:8946/basic/and/api/key/authentication/success"
    )
    assert request.headers["Authorization"] == "Basic dGVzdF91c2VyOnRlc3RfcHdk"
    assert request.headers["X-API-HEADER-KEY"] == "my_provided_api_key"


def test_pyxelrest_basic_and_api_key_authentication_success(
    services, responses: RequestsMock
):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8946/basic/and/api/key/authentication/success",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.pyxelrest_get_url(
        "http://localhost:8946/basic/and/api/key/authentication/success",
        auth=["basic", "api_key_header"],
        api_key_name="X-API-HEADER-KEY",
    ) == [[""]]
    request = _get_request(
        responses, "http://localhost:8946/basic/and/api/key/authentication/success"
    )
    assert request.headers["Authorization"] == "Basic dGVzdF91c2VyOnRlc3RfcHdk"
    assert request.headers["X-API-HEADER-KEY"] == "my_provided_api_key"


def test_basic_or_api_key_authentication_success(services, responses: RequestsMock):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8946/basic/or/api/key/authentication/success",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.authenticated_get_basic_or_api_key_authentication_success() == [
        [""]
    ]
    request = _get_request(
        responses, "http://localhost:8946/basic/or/api/key/authentication/success"
    )
    assert "X-API-HEADER-KEY" not in request.headers
    assert request.headers["Authorization"] == "Basic dGVzdF91c2VyOnRlc3RfcHdk"


def test_api_key_or_basic_authentication_success(services, responses: RequestsMock):
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        "http://localhost:8946/api/key/or/basic/authentication/success",
        json=[],
        match_querystring=True,
    )
    assert pyxelrestgenerator.authenticated_get_api_key_or_basic_authentication_success() == [
        [""]
    ]
    request = _get_request(
        responses, "http://localhost:8946/api/key/or/basic/authentication/success"
    )
    assert "Authorization" not in request.headers
    assert request.headers["X-API-HEADER-KEY"] == "my_provided_api_key"

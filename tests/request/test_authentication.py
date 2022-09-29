import os
from importlib import import_module, reload

import requests_auth
from requests_auth.testing import token_cache_mock, token_mock
from responses import RequestsMock

from tests import loader
from tests.request._request import _get_request


def test_unknown_authentication(
    tmpdir, monkeypatch, token_cache_mock, responses: RequestsMock
):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"oauth2_auth_success": ["custom_label"]}],
                    }
                }
            },
            "securityDefinitions": {
                "oauth2_auth_success": {
                    "type": "unknown",
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)

    assert generated_functions.authenticated_get_authenticated() == [[""]]
    assert "Authorization" not in _get_request(responses, "http://test/test").headers


def test_oauth2_unknown_flow_authentication_success(
    tmpdir, monkeypatch, token_cache_mock, responses: RequestsMock
):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"oauth2_auth_success": ["custom_label"]}],
                    }
                }
            },
            "securityDefinitions": {
                "oauth2_auth_success": {
                    "type": "oauth2",
                    "authorizationUrl": "http://localhost:8947/auth_success?response_type=id_token",
                    "flow": "unknown",
                    "scopes": {"custom_label": "custom category"},
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {"oauth2": {"timeout": 10}},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)

    assert generated_functions.authenticated_get_authenticated() == [[""]]
    assert "Authorization" not in _get_request(responses, "http://test/test").headers


def test_oauth2_implicit_flow_authentication_success(
    tmpdir, monkeypatch, token_cache_mock, responses: RequestsMock
):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"oauth2_auth_success": ["custom_label"]}],
                    }
                }
            },
            "securityDefinitions": {
                "oauth2_auth_success": {
                    "type": "oauth2",
                    "authorizationUrl": "http://localhost:8947/auth_success?response_type=id_token",
                    "flow": "implicit",
                    "scopes": {"custom_label": "custom category"},
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {"oauth2": {"timeout": 10}},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)

    assert generated_functions.authenticated_get_authenticated() == [[""]]
    assert (
        _get_request(responses, "http://test/test").headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_oauth2_implicit_flow_relative_authorization_url_authentication_success(
    tmpdir, monkeypatch, token_cache_mock, responses: RequestsMock
):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"oauth2_auth_success": ["custom_label"]}],
                    }
                }
            },
            "securityDefinitions": {
                "oauth2_auth_success": {
                    "type": "oauth2",
                    "authorizationUrl": "/auth_success?response_type=id_token",
                    "flow": "implicit",
                    "scopes": {"custom_label": "custom category"},
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {"oauth2": {"timeout": 10}},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)

    assert generated_functions.authenticated_get_authenticated() == [[""]]
    assert (
        _get_request(responses, "http://test/test").headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_oauth2_access_code_flow_authentication_success(
    tmpdir, monkeypatch, token_cache_mock, responses: RequestsMock
):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"oauth2_auth_success": ["custom_label"]}],
                    }
                }
            },
            "securityDefinitions": {
                "oauth2_auth_success": {
                    "type": "oauth2",
                    "authorizationUrl": "http://localhost:8947/auth_success?response_type=id_token",
                    "tokenUrl": "http://localhost:8947/auth_success?response_type=id_token",
                    "flow": "accessCode",
                    "scopes": {"custom_label": "custom category"},
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {"oauth2": {"timeout": 10}},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)

    assert generated_functions.authenticated_get_authenticated() == [[""]]
    assert (
        _get_request(responses, "http://test/test").headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_oauth2_access_code_flow_relative_authorization_url_authentication_success(
    tmpdir, monkeypatch, token_cache_mock, responses: RequestsMock
):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"oauth2_auth_success": ["custom_label"]}],
                    }
                }
            },
            "securityDefinitions": {
                "oauth2_auth_success": {
                    "type": "oauth2",
                    "authorizationUrl": "/auth_success?response_type=id_token",
                    "tokenUrl": "http://localhost:8947/auth_success?response_type=id_token",
                    "flow": "accessCode",
                    "scopes": {"custom_label": "custom category"},
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {"oauth2": {"timeout": 10}},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)

    assert generated_functions.authenticated_get_authenticated() == [[""]]
    assert (
        _get_request(responses, "http://test/test").headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_oauth2_access_code_flow_relative_token_url_authentication_success(
    tmpdir, monkeypatch, token_cache_mock, responses: RequestsMock
):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"oauth2_auth_success": ["custom_label"]}],
                    }
                }
            },
            "securityDefinitions": {
                "oauth2_auth_success": {
                    "type": "oauth2",
                    "authorizationUrl": "http://localhost:8947/auth_success?response_type=id_token",
                    "tokenUrl": "/auth_success?response_type=id_token",
                    "flow": "accessCode",
                    "scopes": {"custom_label": "custom category"},
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {"oauth2": {"timeout": 10}},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)

    assert generated_functions.authenticated_get_authenticated() == [[""]]
    assert (
        _get_request(responses, "http://test/test").headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_oauth2_access_code_flow_relative_authorization_and_token_url_authentication_success(
    tmpdir, monkeypatch, token_cache_mock, responses: RequestsMock
):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"oauth2_auth_success": ["custom_label"]}],
                    }
                }
            },
            "securityDefinitions": {
                "oauth2_auth_success": {
                    "type": "oauth2",
                    "authorizationUrl": "/auth_success?response_type=id_token",
                    "tokenUrl": "/auth_success?response_type=id_token",
                    "flow": "accessCode",
                    "scopes": {"custom_label": "custom category"},
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {"oauth2": {"timeout": 10}},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)

    assert generated_functions.authenticated_get_authenticated() == [[""]]
    assert (
        _get_request(responses, "http://test/test").headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_oauth2_password_flow_authentication_success(
    tmpdir, monkeypatch, token_cache_mock, responses: RequestsMock
):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"oauth2_auth_success": ["custom_label"]}],
                    }
                }
            },
            "securityDefinitions": {
                "oauth2_auth_success": {
                    "type": "oauth2",
                    "tokenUrl": "http://localhost:8947/auth_success?response_type=id_token",
                    "flow": "password",
                    "scopes": {"custom_label": "custom category"},
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {
                    "oauth2": {"timeout": 10, "username": "user", "password": "pwd"}
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)

    assert generated_functions.authenticated_get_authenticated() == [[""]]
    assert (
        _get_request(responses, "http://test/test").headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_oauth2_password_flow_relative_token_url_authentication_success(
    tmpdir, monkeypatch, token_cache_mock, responses: RequestsMock
):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"oauth2_auth_success": ["custom_label"]}],
                    }
                }
            },
            "securityDefinitions": {
                "oauth2_auth_success": {
                    "type": "oauth2",
                    "tokenUrl": "/auth_success?response_type=id_token",
                    "flow": "password",
                    "scopes": {"custom_label": "custom category"},
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {
                    "oauth2": {"timeout": 10, "username": "user", "password": "pwd"}
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)

    assert generated_functions.authenticated_get_authenticated() == [[""]]
    assert (
        _get_request(responses, "http://test/test").headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_oauth2_application_flow_authentication_success(
    tmpdir, monkeypatch, token_cache_mock, responses: RequestsMock
):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"oauth2_auth_success": ["custom_label"]}],
                    }
                }
            },
            "securityDefinitions": {
                "oauth2_auth_success": {
                    "type": "oauth2",
                    "tokenUrl": "http://localhost:8947/auth_success?response_type=id_token",
                    "flow": "application",
                    "scopes": {"custom_label": "custom category"},
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {
                    "oauth2": {
                        "timeout": 10,
                        "client_id": "user",
                        "client_secret": "pwd",
                    }
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)

    assert generated_functions.authenticated_get_authenticated() == [[""]]
    assert (
        _get_request(responses, "http://test/test").headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_oauth2_application_flow_relative_token_url_authentication_success(
    tmpdir, monkeypatch, token_cache_mock, responses: RequestsMock
):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"oauth2_auth_success": ["custom_label"]}],
                    }
                }
            },
            "securityDefinitions": {
                "oauth2_auth_success": {
                    "type": "oauth2",
                    "tokenUrl": "/auth_success?response_type=id_token",
                    "flow": "application",
                    "scopes": {"custom_label": "custom category"},
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {
                    "oauth2": {
                        "timeout": 10,
                        "client_id": "user",
                        "client_secret": "pwd",
                    }
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)

    assert generated_functions.authenticated_get_authenticated() == [[""]]
    assert (
        _get_request(responses, "http://test/test").headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_pyxelrest_oauth2_implicit_flow_authentication_success(
    tmpdir, monkeypatch, token_cache_mock, responses: RequestsMock
):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "auth": {"oauth2": {"timeout": 10}},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)

    assert generated_functions.pyxelrest_get_url(
        "http://test/test",
        security_definitions=[
            ["type", "flow", "authorizationUrl"],
            [
                "oauth2",
                "implicit",
                "http://localhost:8947/auth_success?response_type=id_token",
            ],
        ],
    ) == [[""]]
    assert (
        _get_request(responses, "http://test/test").headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


def test_oauth2_implicit_flow_authentication_failure(
    tmpdir, monkeypatch, responses: RequestsMock
):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"oauth2_auth_failure": ["custom_label"]}],
                    }
                }
            },
            "securityDefinitions": {
                "oauth2_auth_failure": {
                    "type": "oauth2",
                    "authorizationUrl": "http://localhost:8947/auth_failure?response_type=id_token",
                    "flow": "implicit",
                    "scopes": {"custom_label": "custom category"},
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {"oauth2": {"timeout": 10}},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    class TokenCacheMock:
        def get_token(self, *args, **kwargs) -> str:
            raise requests_auth.errors.GrantNotProvided("id_token", {})

    monkeypatch.setattr(requests_auth.OAuth2, "token_cache", TokenCacheMock())
    assert (
        generated_functions.authenticated_get_authenticated()
        == 'An error occurred. Please check logs for full details: "id_token not provided within {}."'
    )


def test_oauth2_implicit_flow_authentication_timeout(
    tmpdir, monkeypatch, responses: RequestsMock
):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"oauth2_auth_timeout": ["custom_label"]}],
                    }
                }
            },
            "securityDefinitions": {
                "oauth2_auth_timeout": {
                    "type": "oauth2",
                    "authorizationUrl": "http://localhost:8947/auth_timeout?response_type=id_token",
                    "flow": "implicit",
                    "scopes": {"custom_label": "custom category"},
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {"oauth2": {"timeout": 10}},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    class TokenCacheMock:
        def get_token(self, *args, **kwargs) -> str:
            raise requests_auth.errors.TimeoutOccurred(10)

    monkeypatch.setattr(requests_auth.OAuth2, "token_cache", TokenCacheMock())
    assert (
        generated_functions.authenticated_get_authenticated()
        == 'An error occurred. Please check logs for full details: "User authentication was not received within 10 seconds."'
    )


def test_without_authentication(tmpdir, responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_without_auth",
                        "responses": {"200": {"description": "return value"}},
                    }
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "non_authenticated": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)
    assert generated_functions.non_authenticated_get_without_auth() == [[""]]


def test_api_key_header_authentication_success(tmpdir, responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"api_key_header_auth_success": []}],
                    }
                }
            },
            "securityDefinitions": {
                "api_key_header_auth_success": {
                    "type": "apiKey",
                    "in": "header",
                    "name": "X-API-HEADER-KEY",
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {"api_key": "my_provided_api_key"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)
    assert generated_functions.authenticated_get_authenticated() == [[""]]
    request = _get_request(responses, "http://test/test")
    assert request.headers["X-API-HEADER-KEY"] == "my_provided_api_key"


def test_pyxelrest_api_key_header_authentication_success(
    tmpdir, responses: RequestsMock
):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "auth": {"api_key": "my_provided_api_key"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)
    assert generated_functions.pyxelrest_get_url(
        "http://test/test",
        security_definitions=[
            ["type", "in", "name"],
            ["apiKey", "header", "X-API-HEADER-KEY"],
        ],
    ) == [[""]]
    request = _get_request(responses, "http://test/test")
    assert request.headers["X-API-HEADER-KEY"] == "my_provided_api_key"


def test_api_key_query_authentication_success(tmpdir, responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"api_key_query_auth_success": []}],
                    }
                }
            },
            "securityDefinitions": {
                "api_key_query_auth_success": {
                    "type": "apiKey",
                    "in": "query",
                    "name": "X-API-QUERY-KEY",
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {"api_key": "my_provided_api_key"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(
        responses.GET,
        "http://test/test?X-API-QUERY-KEY=my_provided_api_key",
        json=[],
        match_querystring=True,
    )
    assert generated_functions.authenticated_get_authenticated() == [[""]]


def test_pyxelrest_api_key_query_authentication_success(
    tmpdir, responses: RequestsMock
):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "auth": {"api_key": "my_provided_api_key"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(
        responses.GET,
        "http://test/test?X-API-QUERY-KEY=my_provided_api_key",
        json=[],
        match_querystring=True,
    )
    assert generated_functions.pyxelrest_get_url(
        "http://test/test",
        security_definitions=[
            ["type", "in", "name"],
            ["apiKey", "query", "X-API-QUERY-KEY"],
        ],
    ) == [[""]]


def test_basic_authentication_success(tmpdir, responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [{"basic_auth_success": []}],
                    }
                }
            },
            "securityDefinitions": {"basic_auth_success": {"type": "basic"}},
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {"basic": {"username": "test_user", "password": "test_pwd"}},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)
    assert generated_functions.authenticated_get_authenticated() == [[""]]
    request = _get_request(responses, "http://test/test")
    assert request.headers["Authorization"] == "Basic dGVzdF91c2VyOnRlc3RfcHdk"


def test_pyxelrest_basic_authentication_success(tmpdir, responses: RequestsMock):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "auth": {"basic": {"username": "test_user", "password": "test_pwd"}},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)
    assert generated_functions.pyxelrest_get_url(
        "http://test/test",
        security_definitions=[["type"], ["basic"]],
    ) == [[""]]
    request = _get_request(responses, "http://test/test")
    assert request.headers["Authorization"] == "Basic dGVzdF91c2VyOnRlc3RfcHdk"


def test_basic_and_api_key_authentication_success(tmpdir, responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [
                            {
                                "basic_auth_success": [],
                                "api_key_header_auth_success": [],
                            }
                        ],
                    }
                }
            },
            "securityDefinitions": {
                "api_key_header_auth_success": {
                    "type": "apiKey",
                    "in": "header",
                    "name": "X-API-HEADER-KEY",
                },
                "basic_auth_success": {"type": "basic"},
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {
                    "api_key": "my_provided_api_key",
                    "basic": {"username": "test_user", "password": "test_pwd"},
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)
    assert generated_functions.authenticated_get_authenticated() == [[""]]
    request = _get_request(responses, "http://test/test")
    assert request.headers["Authorization"] == "Basic dGVzdF91c2VyOnRlc3RfcHdk"
    assert request.headers["X-API-HEADER-KEY"] == "my_provided_api_key"


def test_pyxelrest_basic_and_api_key_authentication_success(
    tmpdir, responses: RequestsMock
):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "auth": {
                    "api_key": "my_provided_api_key",
                    "basic": {"username": "test_user", "password": "test_pwd"},
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)
    assert generated_functions.pyxelrest_get_url(
        "http://test/test",
        security_definitions=[
            ["type", "in", "name"],
            ["basic", "", ""],
            ["apiKey", "header", "X-API-HEADER-KEY"],
        ],
    ) == [[""]]
    request = _get_request(responses, "http://test/test")
    assert request.headers["Authorization"] == "Basic dGVzdF91c2VyOnRlc3RfcHdk"
    assert request.headers["X-API-HEADER-KEY"] == "my_provided_api_key"


def test_basic_or_api_key_authentication_success(tmpdir, responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [
                            {"basic_auth_success": []},
                            {"api_key_header_auth_success": []},
                        ],
                    }
                }
            },
            "securityDefinitions": {
                "api_key_header_auth_success": {
                    "type": "apiKey",
                    "in": "header",
                    "name": "X-API-HEADER-KEY",
                },
                "basic_auth_success": {"type": "basic"},
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {
                    "api_key": "my_provided_api_key",
                    "basic": {"username": "test_user", "password": "test_pwd"},
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)
    assert generated_functions.authenticated_get_authenticated() == [[""]]
    request = _get_request(responses, "http://test/test")
    assert "X-API-HEADER-KEY" not in request.headers
    assert request.headers["Authorization"] == "Basic dGVzdF91c2VyOnRlc3RfcHdk"


def test_api_key_or_basic_authentication_success(tmpdir, responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                        "security": [
                            {"api_key_header_auth_success": []},
                            {"basic_auth_success": []},
                        ],
                    }
                }
            },
            "securityDefinitions": {
                "api_key_header_auth_success": {
                    "type": "apiKey",
                    "in": "header",
                    "name": "X-API-HEADER-KEY",
                },
                "basic_auth_success": {"type": "basic"},
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {"definition": "http://test/"},
                "auth": {
                    "api_key": "my_provided_api_key",
                    "basic": {"username": "test_user", "password": "test_pwd"},
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(responses.GET, "http://test/test", json=[], match_querystring=True)
    assert generated_functions.authenticated_get_authenticated() == [[""]]
    request = _get_request(responses, "http://test/test")
    assert "Authorization" not in request.headers
    assert request.headers["X-API-HEADER-KEY"] == "my_provided_api_key"


def test_token_cache_location(fake_install_location):
    reload(import_module("pyxelrest._generator_config"))
    reload(import_module("pyxelrest._authentication"))
    assert requests_auth.OAuth2.token_cache.tokens_path == os.path.join(
        fake_install_location, "tokens.json"
    )

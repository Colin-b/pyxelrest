import requests_auth
from requests import PreparedRequest
from requests_auth.testing import token_cache_mock, token_mock
from responses import RequestsMock

from tests import loader


def _get_request(responses: RequestsMock, url: str) -> PreparedRequest:
    for call in responses.calls:
        if call.request.url == url:
            # Pop out verified request (to be able to check multiple requests)
            responses.calls._calls.remove(call)
            return call.request


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
                    }
                }
            },
        },
        match_querystring=True,
    )
    loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {
                    "definition": "http://test/",
                    "definition_retrieval_auths": {"unknown": {}},
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    assert "Authorization" not in _get_request(responses, "http://test/").headers


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
                    }
                }
            },
        },
        match_querystring=True,
    )
    loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {
                    "definition": "http://test/",
                    "definition_retrieval_auths": {"oauth2": {"unknown": {}}},
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert "Authorization" not in _get_request(responses, "http://test/").headers


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
                    }
                }
            },
        },
        match_querystring=True,
    )
    loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {
                    "definition": "http://test/",
                    "definition_retrieval_auths": {
                        "oauth2": {
                            "implicit": {
                                "authorization_url": "http://localhost:8947/auth_success?response_type=id_token",
                            }
                        }
                    },
                },
                "auth": {"oauth2": {"timeout": 10}},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        _get_request(responses, "http://test/").headers["Authorization"]
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
                    }
                }
            },
        },
        match_querystring=True,
    )
    loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {
                    "definition": "http://test/",
                    "definition_retrieval_auths": {
                        "oauth2": {
                            "access_code": {
                                "authorization_url": "http://localhost:8947/auth_success?response_type=id_token",
                                "token_url": "http://localhost:8947/auth_success?response_type=id_token",
                            }
                        }
                    },
                },
                "auth": {"oauth2": {"timeout": 10}},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        _get_request(responses, "http://test/").headers["Authorization"]
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
                    }
                }
            },
        },
        match_querystring=True,
    )
    loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {
                    "definition": "http://test/",
                    "definition_retrieval_auths": {
                        "oauth2": {
                            "password": {
                                "token_url": "http://localhost:8947/auth_success?response_type=id_token",
                            }
                        }
                    },
                },
                "auth": {
                    "oauth2": {"timeout": 10, "username": "user", "password": "pwd"}
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        _get_request(responses, "http://test/").headers["Authorization"]
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
                    }
                }
            },
        },
        match_querystring=True,
    )
    loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {
                    "definition": "http://test/",
                    "definition_retrieval_auths": {
                        "oauth2": {
                            "application": {
                                "token_url": "http://localhost:8947/auth_success?response_type=id_token",
                            }
                        }
                    },
                },
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

    assert (
        _get_request(responses, "http://test/").headers["Authorization"]
        == "Bearer 2YotnFZFEjr1zCsicMWpAA"
    )


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
                    }
                }
            },
        },
        match_querystring=True,
    )
    loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {
                    "definition": "http://test/",
                    "definition_retrieval_auths": {
                        "api_key": {"header_name": "X-API-HEADER-KEY"}
                    },
                },
                "auth": {"api_key": "my_provided_api_key"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        _get_request(responses, "http://test/").headers["X-API-HEADER-KEY"]
        == "my_provided_api_key"
    )


def test_api_key_query_authentication_success(tmpdir, responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://test/?X-API-QUERY-KEY=my_provided_api_key",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_authenticated",
                        "responses": {"200": {"description": "return value"}},
                    }
                }
            },
        },
        match_querystring=True,
    )
    loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {
                    "definition": "http://test/",
                    "definition_retrieval_auths": {
                        "api_key": {"query_parameter_name": "X-API-QUERY-KEY"}
                    },
                },
                "auth": {"api_key": "my_provided_api_key"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )


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
                    }
                }
            },
        },
        match_querystring=True,
    )
    loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {
                    "definition": "http://test/",
                    "definition_retrieval_auths": {
                        "basic": {},
                        "api_key": {"header_name": "X-API-HEADER-KEY"},
                    },
                },
                "auth": {"basic": {"username": "test_user", "password": "test_pwd"}},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert (
        _get_request(responses, "http://test/").headers["Authorization"]
        == "Basic dGVzdF91c2VyOnRlc3RfcHdk"
    )


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
                    }
                }
            },
        },
        match_querystring=True,
    )
    loader.load(
        tmpdir,
        {
            "authenticated": {
                "open_api": {
                    "definition": "http://test/",
                    "definition_retrieval_auths": {"basic": {}},
                },
                "auth": {
                    "api_key": "my_provided_api_key",
                    "basic": {"username": "test_user", "password": "test_pwd"},
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    request = _get_request(responses, "http://test/")
    assert request.headers["Authorization"] == "Basic dGVzdF91c2VyOnRlc3RfcHdk"
    assert request.headers["X-API-HEADER-KEY"] == "my_provided_api_key"

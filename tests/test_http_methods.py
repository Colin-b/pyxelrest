import pytest
from responses import RequestsMock

from tests import loader


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


def test_get_http_method(responses: RequestsMock, http_methods_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "http_methods": {
                "open_api": {"definition": "http://localhost:8955/"},
                "methods": ["get", "post", "put", "delete", "patch", "options", "head"],
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8955/http_methods",
        json={},
        match_querystring=True,
    )

    assert generated_functions.http_methods_get_http_methods() == [[""]]


def test_post_http_method(responses: RequestsMock, http_methods_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "http_methods": {
                "open_api": {"definition": "http://localhost:8955/"},
                "methods": ["get", "post", "put", "delete", "patch", "options", "head"],
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.POST,
        url="http://localhost:8955/http_methods",
        json={},
        match_querystring=True,
    )

    assert generated_functions.http_methods_post_http_methods() == [[""]]


def test_put_http_method(responses: RequestsMock, http_methods_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "http_methods": {
                "open_api": {"definition": "http://localhost:8955/"},
                "methods": ["get", "post", "put", "delete", "patch", "options", "head"],
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.PUT,
        url="http://localhost:8955/http_methods",
        json={},
        match_querystring=True,
    )

    assert generated_functions.http_methods_put_http_methods() == [[""]]


def test_delete_http_method(responses: RequestsMock, http_methods_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "http_methods": {
                "open_api": {"definition": "http://localhost:8955/"},
                "methods": ["get", "post", "put", "delete", "patch", "options", "head"],
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.DELETE,
        url="http://localhost:8955/http_methods",
        json={},
        match_querystring=True,
    )

    assert generated_functions.http_methods_delete_http_methods() == [[""]]


def test_patch_http_method(responses: RequestsMock, http_methods_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "http_methods": {
                "open_api": {"definition": "http://localhost:8955/"},
                "methods": ["get", "post", "put", "delete", "patch", "options", "head"],
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.PATCH,
        url="http://localhost:8955/http_methods",
        json={},
        match_querystring=True,
    )

    assert generated_functions.http_methods_patch_http_methods() == [[""]]


def test_options_http_method(responses: RequestsMock, http_methods_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "http_methods": {
                "open_api": {"definition": "http://localhost:8955/"},
                "methods": ["get", "post", "put", "delete", "patch", "options", "head"],
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.OPTIONS,
        url="http://localhost:8955/http_methods",
        json={},
        match_querystring=True,
    )

    assert generated_functions.http_methods_options_http_methods() == [[""]]


def test_head_http_method(responses: RequestsMock, http_methods_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "http_methods": {
                "open_api": {"definition": "http://localhost:8955/"},
                "methods": ["get", "post", "put", "delete", "patch", "options", "head"],
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.HEAD,
        url="http://localhost:8955/http_methods",
        json={},
        match_querystring=True,
    )

    assert generated_functions.http_methods_head_http_methods() == [[""]]

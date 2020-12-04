import pytest
from responses import RequestsMock

from tests import loader


def test_plain_without_parameter(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_plain_text_without_parameter",
                        "produces": ["text/plain"],
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
            "without_parameter": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test",
        body="string value returned should be truncated so that the following information cannot be seen by user, "
        "because of the fact that Excel does not allow more than 255 characters in a cell. "
        "Only the 255 characters will be returned by the user defined functions:  YOU CANNOT RECEIVE THIS!!!!!!",
        match_querystring=True,
    )

    assert (
        generated_functions.without_parameter_get_plain_text_without_parameter()
        == "string value returned should be truncated so that the following information cannot be seen by user, because of the fact that Excel does not allow more than 255 characters in a cell. Only the 255 characters will be returned by the user defined functions:  "
    )


def test_post_without_parameter(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "post": {
                        "operationId": "post_without_parameter",
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
            "without_parameter": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.POST, url="http://test/test", json={}, match_querystring=True
    )

    assert generated_functions.without_parameter_post_without_parameter() == [[""]]


def test_put_without_parameter(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "put": {
                        "operationId": "put_without_parameter",
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
            "without_parameter": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.PUT, url="http://test/test", json={}, match_querystring=True
    )

    assert generated_functions.without_parameter_put_without_parameter() == [[""]]


def test_delete_without_parameter(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "delete": {
                        "operationId": "delete_without_parameter",
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
            "without_parameter": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.DELETE, url="http://test/test", json={}, match_querystring=True
    )

    assert generated_functions.without_parameter_delete_without_parameter() == [[""]]


def test_service_without_sync_does_not_have_sync(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "delete": {
                        "operationId": "delete_without_parameter",
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
            "without_parameter": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    assert not hasattr(
        generated_functions, "vba_without_parameter_delete_without_parameter"
    )

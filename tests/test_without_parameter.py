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


@pytest.fixture
def without_parameter_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8950/",
        json={
            "swagger": "2.0",
            "definitions": {"Test": {"properties": {}}},
            "paths": {
                "/without_parameter": {
                    "get": {
                        "operationId": "get_without_parameter",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {"type": "string"},
                            }
                        },
                    },
                    "post": {
                        "operationId": "post_without_parameter",
                        "responses": {
                            "200": {"description": "POST performed properly"}
                        },
                    },
                    "put": {
                        "operationId": "put_without_parameter",
                        "responses": {"200": {"description": "PUT performed properly"}},
                    },
                    "delete": {
                        "operationId": "delete_without_parameter",
                        "responses": {
                            "200": {"description": "DELETE performed properly"}
                        },
                    },
                },
                "/plain_text_without_parameter": {
                    "get": {
                        "operationId": "get_plain_text_without_parameter",
                        "produces": ["text/plain"],
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {"type": "string"},
                            }
                        },
                    },
                    "post": {
                        "operationId": "post_plain_text_without_parameter",
                        "produces": ["text/plain"],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "put": {
                        "operationId": "put_plain_text_without_parameter",
                        "produces": ["text/plain"],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "delete": {
                        "operationId": "delete_plain_text_without_parameter",
                        "produces": ["text/plain"],
                        "responses": {"200": {"description": "return value"}},
                    },
                },
                "/json_without_parameter": {
                    "get": {
                        "operationId": "get_json_without_parameter",
                        "produces": ["application/json"],
                        "responses": {
                            "200": {
                                "description": "return value",
                                "$ref": "#/definitions/Test",
                            }
                        },
                    },
                    "post": {
                        "operationId": "post_json_without_parameter",
                        "produces": ["application/json"],
                        "responses": {
                            "200": {
                                "description": "return value",
                                "$ref": "#/definitions/Test",
                            }
                        },
                    },
                    "put": {
                        "operationId": "put_json_without_parameter",
                        "produces": ["application/json"],
                        "responses": {
                            "200": {
                                "description": "return value",
                                "$ref": "#/definitions/Test",
                            }
                        },
                    },
                    "delete": {
                        "operationId": "delete_json_without_parameter",
                        "produces": ["application/json"],
                        "responses": {
                            "200": {
                                "description": "return value",
                                "$ref": "#/definitions/Test",
                            }
                        },
                    },
                },
                "/octet_without_parameter": {
                    "get": {
                        "operationId": "get_octet_without_parameter",
                        "produces": ["application/octet-stream"],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "post": {
                        "operationId": "post_octet_without_parameter",
                        "produces": ["application/octet-stream"],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "put": {
                        "operationId": "put_octet_without_parameter",
                        "produces": ["application/octet-stream"],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "delete": {
                        "operationId": "delete_octet_without_parameter",
                        "produces": ["application/octet-stream"],
                        "responses": {"200": {"description": "return value"}},
                    },
                },
            },
        },
        match_querystring=True,
    )


@pytest.mark.parametrize(
    "service_config",
    [
        {
            "without_parameter": {
                "open_api": {"definition": "http://localhost:8950/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
        {
            "without_parameter": {
                "open_api": {
                    "definition": "http://localhost:8950/",
                    "rely_on_definitions": True,
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    ],
)
def test_plain_without_parameter(
    responses: RequestsMock, without_parameter_service, tmpdir, service_config: dict
):
    pyxelrestgenerator = loader.load2(tmpdir, service_config)
    responses.add(
        responses.GET,
        url="http://localhost:8950/plain_text_without_parameter",
        body="string value returned should be truncated so that the following information cannot be seen by user, "
        "because of the fact that Excel does not allow more than 255 characters in a cell. "
        "Only the 255 characters will be returned by the user defined functions:  YOU CANNOT RECEIVE THIS!!!!!!",
        match_querystring=True,
    )

    assert (
        pyxelrestgenerator.without_parameter_get_plain_text_without_parameter()
        == "string value returned should be truncated so that the following information cannot be seen by user, because of the fact that Excel does not allow more than 255 characters in a cell. Only the 255 characters will be returned by the user defined functions:  "
    )


def test_post_without_parameter(
    responses: RequestsMock, without_parameter_service, tmpdir
):
    pyxelrestgenerator = loader.load2(
        tmpdir,
        {
            "without_parameter": {
                "open_api": {"definition": "http://localhost:8950/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.POST,
        url="http://localhost:8950/without_parameter",
        json={},
        match_querystring=True,
    )

    assert pyxelrestgenerator.without_parameter_post_without_parameter() == [[""]]


def test_put_without_parameter(
    responses: RequestsMock, without_parameter_service, tmpdir
):
    pyxelrestgenerator = loader.load2(
        tmpdir,
        {
            "without_parameter": {
                "open_api": {"definition": "http://localhost:8950/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.PUT,
        url="http://localhost:8950/without_parameter",
        json={},
        match_querystring=True,
    )

    assert pyxelrestgenerator.without_parameter_put_without_parameter() == [[""]]


def test_delete_without_parameter(
    responses: RequestsMock, without_parameter_service, tmpdir
):
    pyxelrestgenerator = loader.load2(
        tmpdir,
        {
            "without_parameter": {
                "open_api": {"definition": "http://localhost:8950/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )
    responses.add(
        responses.DELETE,
        url="http://localhost:8950/without_parameter",
        json={},
        match_querystring=True,
    )

    assert pyxelrestgenerator.without_parameter_delete_without_parameter() == [[""]]


def test_service_without_sync_does_not_have_sync(without_parameter_service, tmpdir):
    pyxelrestgenerator = loader.load2(
        tmpdir,
        {
            "without_parameter": {
                "open_api": {"definition": "http://localhost:8950/"},
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    with pytest.raises(AttributeError) as exception_info:
        pyxelrestgenerator.vba_without_parameter_delete_without_parameter()
    assert (
        str(exception_info.value)
        == "module 'pyxelrest.pyxelrestgenerator' has no attribute 'vba_without_parameter_delete_without_parameter'"
    )

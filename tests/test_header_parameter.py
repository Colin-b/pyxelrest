import os

import pytest
from requests import PreparedRequest
from responses import RequestsMock

from tests import loader


def _get_request(responses: RequestsMock, url: str) -> PreparedRequest:
    for call in responses.calls:
        if call.request.url == url:
            # Pop out verified request (to be able to check multiple requests)
            responses.calls._calls.remove(call)
            return call.request


@pytest.fixture
def header_parameter_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8951/",
        json={
            "swagger": "2.0",
            "definitions": {
                "Header": {
                    "type": "object",
                    "properties": {
                        "Accept": {"type": "string"},
                        "Accept-Encoding": {"type": "string"},
                        "Connection": {"type": "string"},
                        "Content-Length": {"type": "string"},
                        "Content-Type": {"type": "string"},
                        "Header-String": {"type": "string"},
                        "Host": {"type": "string"},
                        "User-Agent": {"type": "string"},
                    },
                    "title": "Test",
                }
            },
            "paths": {
                "/header": {
                    "get": {
                        "operationId": "get_header",
                        "parameters": [
                            {
                                "description": "header parameter",
                                "in": "header",
                                "name": "header_string",
                                "required": True,
                                "type": "string",
                            }
                        ],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {"$ref": "#/definitions/Header"},
                            }
                        },
                    }
                }
            },
        },
        match_querystring=True,
    )


def test_get_header_parameter(
    responses: RequestsMock, header_parameter_service, tmpdir
):
    pyxelrestgenerator = loader.load(
        tmpdir,
        {
            "header_parameter": {
                "open_api": {"definition": "http://localhost:8951/"},
                "udf": {
                    "return_types": ["vba_compatible", "sync_auto_expand"],
                    "shift_result": False,
                },
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8951/header",
        json={},
        match_querystring=True,
    )

    assert pyxelrestgenerator.header_parameter_get_header("sent header") == [[""]]
    assert (
        _get_request(responses, "http://localhost:8951/header").headers["header_string"]
        == "sent header"
    )


def test_get_header_parameter_sync(
    responses: RequestsMock, header_parameter_service, tmpdir
):
    pyxelrestgenerator = loader.load(
        tmpdir,
        {
            "header_parameter": {
                "open_api": {"definition": "http://localhost:8951/"},
                "udf": {
                    "return_types": ["vba_compatible", "sync_auto_expand"],
                    "shift_result": False,
                },
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8951/header",
        json={},
        match_querystring=True,
    )

    assert pyxelrestgenerator.vba_header_parameter_get_header("sent header") == [[""]]
    assert (
        _get_request(responses, "http://localhost:8951/header").headers["header_string"]
        == "sent header"
    )


def test_service_only_sync_does_not_have_vba_prefix(header_parameter_service, tmpdir):
    pyxelrestgenerator = loader.load(
        tmpdir,
        {
            "header_advanced_configuration": {
                "open_api": {"definition": "http://localhost:8951/"},
                "udf": {"return_types": ["vba_compatible"], "shift_result": False},
                "headers": {
                    "X-PXL-CUSTOM": "MyCustomValue",
                    "X-PXL-OTHER": "MyOtherValue",
                    "X-PXL-ENVVAR": "%USERNAME%",
                },
            }
        },
    )

    with pytest.raises(AttributeError) as exception_info:
        pyxelrestgenerator.vba_header_advanced_configuration_get_header("sent header")
    assert (
        str(exception_info.value)
        == "module 'pyxelrest.pyxelrestgenerator' has no attribute 'vba_header_advanced_configuration_get_header'"
    )


class DateTimeMock:
    @staticmethod
    def today():
        class UTCDateTimeMock:
            @staticmethod
            def isoformat():
                return "2018-10-11T15:05:05.663979"

        return UTCDateTimeMock


class DateTimeModuleMock:
    datetime = DateTimeMock


def test_get_header_advanced_configuration(
    responses: RequestsMock, header_parameter_service, monkeypatch, tmpdir
):
    pyxelrestgenerator = loader.load(
        tmpdir,
        {
            "header_advanced_configuration": {
                "open_api": {"definition": "http://localhost:8951/"},
                "udf": {"return_types": ["vba_compatible"], "shift_result": False},
                "headers": {
                    "X-PXL-CUSTOM": "MyCustomValue",
                    "X-PXL-OTHER": "MyOtherValue",
                    "X-PXL-ENVVAR": "%USERNAME%",
                },
            }
        },
    )
    import pyxelrest.session

    monkeypatch.setattr(pyxelrest.session, "datetime", DateTimeModuleMock)
    responses.add(
        responses.GET,
        url="http://localhost:8951/header",
        json={},
        match_querystring=True,
    )

    assert pyxelrestgenerator.header_advanced_configuration_get_header(
        "sent header"
    ) == [[""]]
    headers = _get_request(responses, "http://localhost:8951/header").headers

    assert headers["X-Pxl-Custom"] == "MyCustomValue"
    assert headers["X-Pxl-Other"] == "MyOtherValue"
    assert headers["X-Pxl-Envvar"] == os.environ["USERNAME"]
    assert headers["X-Pxl-Request"]
    assert headers["User-Agent"] == "PyxelRest v0.69.1.dev1"
    assert headers["X-Pxl-Cell"] == "Python"
    assert headers["X-Pxl-Session"] == "2018-10-11T15:05:05.663979"

import os

import pytest
from responses import RequestsMock

from tests import loader
from tests.request._request import _get_request


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
    generated_functions = loader.load(
        tmpdir,
        {
            "header_parameter": {
                "open_api": {"definition": "http://localhost:8951/"},
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                    "vba_compatible": {},
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

    assert generated_functions.header_parameter_get_header("sent header") == [[""]]
    assert (
        _get_request(responses, "http://localhost:8951/header").headers["header_string"]
        == "sent header"
    )


def test_get_header_parameter_sync(
    responses: RequestsMock, header_parameter_service, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "header_parameter": {
                "open_api": {"definition": "http://localhost:8951/"},
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                    "vba_compatible": {},
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

    assert generated_functions.vba_header_parameter_get_header("sent header") == [[""]]
    assert (
        _get_request(responses, "http://localhost:8951/header").headers["header_string"]
        == "sent header"
    )


def test_get_header_advanced_configuration(
    responses: RequestsMock, header_parameter_service, tmpdir
):
    import pyxelrest._session
    from pyxelrest import __version__

    pyxelrest._session._sessions.clear()
    generated_functions = loader.load(
        tmpdir,
        {
            "header_advanced_configuration": {
                "open_api": {"definition": "http://localhost:8951/"},
                "formulas": {"vba_compatible": {}},
                "network": {
                    "headers": {
                        "X-PXL-CUSTOM": "MyCustomValue",
                        "X-PXL-OTHER": "MyOtherValue",
                        "X-PXL-ENVVAR": "%USERNAME%",
                    },
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

    assert generated_functions.vba_header_advanced_configuration_get_header(
        "sent header"
    ) == [[""]]
    headers = _get_request(responses, "http://localhost:8951/header").headers

    assert headers["X-Pxl-Custom"] == "MyCustomValue"
    assert headers["X-Pxl-Other"] == "MyOtherValue"
    assert headers["X-Pxl-Envvar"] == os.environ["USERNAME"]
    assert headers["User-Agent"] == f"pyxelrest/{__version__}"
    assert headers["X-Pxl-Caller"] == ""


def test_get_vba_caller(responses: RequestsMock, header_parameter_service, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "header_advanced_configuration": {
                "open_api": {"definition": "http://localhost:8951/"},
                "formulas": {"vba_compatible": {}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8951/header",
        json={},
        match_querystring=True,
    )

    class FakeApplication:
        class FakeVBE:
            class FakeCodePane:
                CodeModule = "FakeModule"

            ActiveCodePane = FakeCodePane

        VBE = FakeVBE

    assert generated_functions.vba_header_advanced_configuration_get_header(
        header_string="", caller="fake", excel_application=FakeApplication
    ) == [[""]]
    headers = _get_request(responses, "http://localhost:8951/header").headers
    assert headers["X-Pxl-Caller"] == "VBA:FakeModule"


def test_get_caller_exception(
    responses: RequestsMock, header_parameter_service, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "header_advanced_configuration": {
                "open_api": {"definition": "http://localhost:8951/"},
                "formulas": {"vba_compatible": {}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8951/header",
        json={},
        match_querystring=True,
    )

    class FakeCaller:
        Rows = "FakeRows"

        @staticmethod
        def get_address():
            raise Exception("Failure to retrieve address")

    assert generated_functions.vba_header_advanced_configuration_get_header(
        header_string="", caller=FakeCaller
    ) == [[""]]
    headers = _get_request(responses, "http://localhost:8951/header").headers
    assert headers["X-Pxl-Caller"] == ""


def test_get_excel_caller_address(
    responses: RequestsMock, header_parameter_service, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "header_advanced_configuration": {
                "open_api": {"definition": "http://localhost:8951/"},
                "formulas": {"vba_compatible": {}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8951/header",
        json={},
        match_querystring=True,
    )

    class FakeCaller:
        Rows = "FakeRows"

        @staticmethod
        def get_address():
            return "Excel address"

    assert generated_functions.vba_header_advanced_configuration_get_header(
        header_string="", caller=FakeCaller
    ) == [[""]]
    headers = _get_request(responses, "http://localhost:8951/header").headers
    assert headers["X-Pxl-Caller"] == "Excel address"

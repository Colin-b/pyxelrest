import datetime

from dateutil.tz import tzutc
import pytest
from responses import RequestsMock

from testsutils import loader


@pytest.fixture
def services(responses: RequestsMock):
    # output order service
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
    # header_parameter_service
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
    # form_parameter_service
    responses.add(
        responses.GET,
        url="http://localhost:8952/",
        json={
            "swagger": "2.0",
            "definitions": {
                "Form": {
                    "type": "object",
                    "properties": {"form_string": {"type": "string"}},
                    "title": "Test",
                }
            },
            "paths": {
                "/form": {
                    "post": {
                        "operationId": "post_form",
                        "parameters": [
                            {
                                "description": "form parameter",
                                "in": "formData",
                                "name": "form_string",
                                "required": True,
                                "type": "string",
                            }
                        ],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {"$ref": "#/definitions/Form"},
                            }
                        },
                    }
                }
            },
        },
        match_querystring=True,
    )

    pyxelrestgenerator = loader.load("based_on_definitions_services.yml")


def test_get_header_parameter(services):

    headers = pyxelrestgenerator.header_parameter_get_header("sent header")
    header_param_index = headers[0].index("Header-String")
    assert headers[1][header_param_index] == "sent header"


def test_post_form_parameter(services):

    assert pyxelrestgenerator.form_parameter_post_form("sent string form data") == [
        ["form_string"],
        ["sent string form data"],
    ]


def test_get_compare_output_order(services):

    assert pyxelrestgenerator.output_order_get_price_unordered() == [
        [u"ts", u"date", u"curve", u"mat"],
        [u"", datetime.datetime(2017, 4, 5, 0, 0), u"PW_FR", u"H01"],
        [u"2017-04-05 12:03:15", datetime.datetime(2017, 4, 5, 0, 0), u"PW_FR", u"H02"],
        [u"", datetime.datetime(2017, 4, 5, 0, 0), u"PW_FR", u"H03"],
    ]

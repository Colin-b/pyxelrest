import datetime

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


def test_get_compare_output_order(
    responses: RequestsMock, output_order_service, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "output_order": {
                "open_api": {"definition": "http://localhost:8946/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8946/price/unordered",
        json=[
            {"ts": None, "curve": "PW_FR", "date": "2017-04-05", "mat": "H01"},
            {
                "ts": "2017-04-05 12:03:15",
                "curve": "PW_FR",
                "date": "2017-04-05",
                "mat": "H02",
            },
            {"ts": None, "curve": "PW_FR", "date": "2017-04-05", "mat": "H03"},
        ],
        match_querystring=True,
    )

    assert generated_functions.output_order_get_price_unordered() == [
        ["ts", "curve", "date", "mat"],
        ["", "PW_FR", datetime.datetime(2017, 4, 5, 0, 0), "H01"],
        ["2017-04-05 12:03:15", "PW_FR", datetime.datetime(2017, 4, 5, 0, 0), "H02"],
        ["", "PW_FR", datetime.datetime(2017, 4, 5, 0, 0), "H03"],
    ]


def test_get_compare_output_order_based_on_definition(
    responses: RequestsMock, output_order_service, tmpdir
):
    generated_functions = loader.load(
        tmpdir,
        {
            "output_order": {
                "open_api": {
                    "definition": "http://localhost:8946/",
                    "rely_on_definitions": True,
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://localhost:8946/price/unordered",
        json=[
            {"ts": None, "curve": "PW_FR", "date": "2017-04-05", "mat": "H01"},
            {
                "ts": "2017-04-05 12:03:15",
                "curve": "PW_FR",
                "date": "2017-04-05",
                "mat": "H02",
            },
            {"ts": None, "curve": "PW_FR", "date": "2017-04-05", "mat": "H03"},
        ],
        match_querystring=True,
    )

    assert generated_functions.output_order_get_price_unordered() == [
        ["ts", "date", "curve", "mat"],
        ["", datetime.datetime(2017, 4, 5, 0, 0), "PW_FR", "H01"],
        ["2017-04-05 12:03:15", datetime.datetime(2017, 4, 5, 0, 0), "PW_FR", "H02"],
        ["", datetime.datetime(2017, 4, 5, 0, 0), "PW_FR", "H03"],
    ]

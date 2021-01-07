import datetime

from dateutil.tz import tzutc
from responses import RequestsMock

from tests import loader


def test_maximum_length(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/max": {
                    "get": {
                        "parameters": [
                            {
                                "in": "query",
                                "name": "str",
                                "type": "string",
                                "maxLength": 2,
                            },
                        ],
                        "responses": {
                            "200": {
                                "type": "string",
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
            "string": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/max?str=te",
        json=[],
        match_querystring=True,
    )

    assert (
        generated_functions.string_get_max("tes")
        == 'str_visual_basic value "tes" cannot contains more than 2 characters.'
    )
    assert generated_functions.string_get_max("te") == [[""]]


def test_minimum_length(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/min": {
                    "get": {
                        "parameters": [
                            {
                                "in": "query",
                                "name": "str",
                                "type": "string",
                                "minLength": 2,
                            },
                        ],
                        "responses": {
                            "200": {
                                "type": "string",
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
            "string": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/min?str=te",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.string_get_min("te") == [[""]]
    assert (
        generated_functions.string_get_min("t")
        == 'str_visual_basic value "t" cannot contains less than 2 characters.'
    )

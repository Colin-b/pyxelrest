import datetime

from dateutil.tz import tzutc
from responses import RequestsMock

from tests import loader


def test_exclusive_maximum(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/exclusive_max": {
                    "get": {
                        "parameters": [
                            {
                                "in": "query",
                                "name": "int",
                                "type": "integer",
                                "maximum": 10,
                                "exclusiveMaximum": True,
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
            "number": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/exclusive_max?int=9",
        json=[],
        match_querystring=True,
    )

    assert (
        generated_functions.number_get_exclusive_max(11)
        == 'int value "11" must be strictly inferior to 10.'
    )
    assert (
        generated_functions.number_get_exclusive_max(10)
        == 'int value "10" must be strictly inferior to 10.'
    )
    assert generated_functions.number_get_exclusive_max(9) == [[""]]


def test_maximum(responses: RequestsMock, tmpdir):
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
                                "name": "int",
                                "type": "integer",
                                "maximum": 10,
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
            "number": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/max?int=10",
        json=[],
        match_querystring=True,
    )
    responses.add(
        responses.GET,
        url="http://test/max?int=9",
        json=[],
        match_querystring=True,
    )

    assert (
        generated_functions.number_get_max(11)
        == 'int value "11" must be inferior or equals to 10.'
    )
    assert generated_functions.number_get_max(10) == [[""]]
    assert generated_functions.number_get_max(9) == [[""]]


def test_exclusive_minimum(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/exclusive_min": {
                    "get": {
                        "parameters": [
                            {
                                "in": "query",
                                "name": "int",
                                "type": "integer",
                                "minimum": 10,
                                "exclusiveMinimum": True,
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
            "number": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/exclusive_min?int=11",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.number_get_exclusive_min(11) == [[""]]
    assert (
        generated_functions.number_get_exclusive_min(10)
        == 'int value "10" must be strictly superior to 10.'
    )
    assert (
        generated_functions.number_get_exclusive_min(9)
        == 'int value "9" must be strictly superior to 10.'
    )


def test_minimum(responses: RequestsMock, tmpdir):
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
                                "name": "int",
                                "type": "integer",
                                "minimum": 10,
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
            "number": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/min?int=11",
        json=[],
        match_querystring=True,
    )
    responses.add(
        responses.GET,
        url="http://test/min?int=10",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.number_get_min(11) == [[""]]
    assert generated_functions.number_get_min(10) == [[""]]
    assert (
        generated_functions.number_get_min(9)
        == 'int value "9" must be superior or equals to 10.'
    )


def test_multiple_of(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/multiple": {
                    "get": {
                        "parameters": [
                            {
                                "in": "query",
                                "name": "int",
                                "type": "integer",
                                "multipleOf": 2,
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
            "number": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/multiple?int=4",
        json=[],
        match_querystring=True,
    )
    responses.add(
        responses.GET,
        url="http://test/multiple?int=2",
        json=[],
        match_querystring=True,
    )

    assert generated_functions.number_get_multiple(4) == [[""]]
    assert (
        generated_functions.number_get_multiple(3)
        == 'int value "3" must be a multiple of 2.'
    )
    assert generated_functions.number_get_multiple(2) == [[""]]
    assert (
        generated_functions.number_get_multiple(1)
        == 'int value "1" must be a multiple of 2.'
    )

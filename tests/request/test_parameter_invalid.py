import pytest
from responses import RequestsMock

from tests import loader


def test_parameter_cannot_be_parsed(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "parameters": [
                            {
                                "in": "query",
                                "name": "param",
                                "schema": {},
                            }
                        ],
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
    with pytest.raises(Exception) as exception_info:
        loader.load(
            tmpdir,
            {
                "invalid": {
                    "open_api": {"definition": "http://test/"},
                    "formulas": {"dynamic_array": {"lock_excel": True}},
                }
            },
        )
    assert (
        str(exception_info.value)
        == "Unable to extract parameters from {'in': 'query', 'name': 'param', 'schema': {}, 'server_param_name': 'param'}"
    )


def test_parameter_with_more_than_one_field_type(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "parameters": [
                            {
                                "in": "query",
                                "name": "param",
                                "type": ["string", "integer"],
                            }
                        ],
                        "responses": {
                            "200": {
                                "description": "return value",
                            }
                        },
                    }
                }
            },
        },
        match_querystring=True,
    )
    with pytest.raises(Exception) as exception_info:
        loader.load(
            tmpdir,
            {
                "invalid": {
                    "open_api": {"definition": "http://test/"},
                    "formulas": {"dynamic_array": {"lock_excel": True}},
                }
            },
        )
    assert (
        str(exception_info.value)
        == "Unable to guess field type amongst ['string', 'integer']"
    )

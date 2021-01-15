import logging

from responses import RequestsMock

from tests import loader


def test_duplicated_parameters(responses: RequestsMock, tmpdir, caplog):
    caplog.set_level(logging.ERROR, logger="pyxelrest")
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
                                "name": "name1",
                                "type": "string",
                            },
                            {
                                "in": "query",
                                "name": "name1",
                                "type": "string",
                            },
                        ],
                        "responses": {
                            "200": {
                                "type": "string",
                            }
                        },
                    }
                },
            },
        },
        match_querystring=True,
    )
    loader.load(
        tmpdir,
        {
            "duplicated": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    assert caplog.messages == [
        """"duplicated" will not be available: get /test parameters are not unique: [{'in': 'query', 'name': 'name1', 'type': 'string', 'server_param_name': 'name1'}, {'in': 'query', 'name': 'name1', 'type': 'string', 'server_param_name': 'name1'}]."""
    ]

import time

import pytest
from responses import RequestsMock

from testsutils import loader


@pytest.fixture
def caching_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8949/",
        json={
            "swagger": "2.0",
            "produces": ["application/json"],
            "paths": {
                "/cached": {
                    "parameters": [
                        {
                            "description": "",
                            "in": "query",
                            "name": "test1",
                            "required": True,
                            "type": "string",
                        },
                        {
                            "description": "",
                            "in": "query",
                            "name": "test2",
                            "required": True,
                            "type": "string",
                        },
                    ],
                    "get": {
                        "operationId": "get_cached",
                        "responses": {"200": {"description": "return value"}},
                    },
                    "post": {
                        "operationId": "post_cached",
                        "responses": {"200": {"description": "return value"}},
                    },
                    "put": {
                        "operationId": "put_cached",
                        "responses": {"200": {"description": "return value"}},
                    },
                    "delete": {
                        "operationId": "delete_cached",
                        "responses": {"200": {"description": "return value"}},
                    },
                }
            },
        },
        match_querystring=True,
    )
    loader.load("caching_services.yml")


def test_get_cached(caching_service, responses: RequestsMock):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.caching_get_cached(test1="1", test2="2") == [
        ["request_nb", "test1", "test2"],
        [1, "1", "2"],
    ]
    assert pyxelrestgenerator.caching_get_cached(test1="1", test2="3") == [
        ["request_nb", "test1", "test2"],
        [2, "1", "3"],
    ]
    assert pyxelrestgenerator.caching_get_cached(test1="1", test2="2") == [
        ["request_nb", "test1", "test2"],
        [1, "1", "2"],
    ]
    time.sleep(5)
    assert pyxelrestgenerator.caching_get_cached(test1="1", test2="2") == [
        ["request_nb", "test1", "test2"],
        [3, "1", "2"],
    ]
    assert pyxelrestgenerator.caching_get_cached(test1="1", test2="2") == [
        ["request_nb", "test1", "test2"],
        [3, "1", "2"],
    ]


def test_post_cached(caching_service, responses: RequestsMock):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.caching_post_cached(test1="1", test2="2") == [
        ["request_nb", "test1", "test2"],
        [1, "1", "2"],
    ]
    assert pyxelrestgenerator.caching_post_cached(test1="1", test2="3") == [
        ["request_nb", "test1", "test2"],
        [2, "1", "3"],
    ]
    assert pyxelrestgenerator.caching_post_cached(test1="1", test2="2") == [
        ["request_nb", "test1", "test2"],
        [3, "1", "2"],
    ]
    time.sleep(5)
    assert pyxelrestgenerator.caching_post_cached(test1="1", test2="2") == [
        ["request_nb", "test1", "test2"],
        [4, "1", "2"],
    ]
    assert pyxelrestgenerator.caching_post_cached(test1="1", test2="2") == [
        ["request_nb", "test1", "test2"],
        [5, "1", "2"],
    ]


def test_put_cached(caching_service, responses: RequestsMock):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.caching_put_cached(test1="1", test2="2") == [
        ["request_nb", "test1", "test2"],
        [1, "1", "2"],
    ]
    assert pyxelrestgenerator.caching_put_cached(test1="1", test2="3") == [
        ["request_nb", "test1", "test2"],
        [2, "1", "3"],
    ]
    assert pyxelrestgenerator.caching_put_cached(test1="1", test2="2") == [
        ["request_nb", "test1", "test2"],
        [3, "1", "2"],
    ]
    time.sleep(5)
    assert pyxelrestgenerator.caching_put_cached(test1="1", test2="2") == [
        ["request_nb", "test1", "test2"],
        [4, "1", "2"],
    ]
    assert pyxelrestgenerator.caching_put_cached(test1="1", test2="2") == [
        ["request_nb", "test1", "test2"],
        [5, "1", "2"],
    ]


def test_delete_cached(caching_service, responses: RequestsMock):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.caching_delete_cached(test1="1", test2="2") == [
        ["request_nb", "test1", "test2"],
        [1, "1", "2"],
    ]
    assert pyxelrestgenerator.caching_delete_cached(test1="1", test2="3") == [
        ["request_nb", "test1", "test2"],
        [2, "1", "3"],
    ]
    assert pyxelrestgenerator.caching_delete_cached(test1="1", test2="2") == [
        ["request_nb", "test1", "test2"],
        [3, "1", "2"],
    ]
    time.sleep(5)
    assert pyxelrestgenerator.caching_delete_cached(test1="1", test2="2") == [
        ["request_nb", "test1", "test2"],
        [4, "1", "2"],
    ]
    assert pyxelrestgenerator.caching_delete_cached(test1="1", test2="2") == [
        ["request_nb", "test1", "test2"],
        [5, "1", "2"],
    ]

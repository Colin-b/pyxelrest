import time

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


def test_get_cached(caching_service, responses: RequestsMock):
    loader.load("caching_services.yml")
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.GET,
        url="http://localhost:8949/cached?test1=1&test2=2",
        json={},
        match_querystring=True,
    )

    assert pyxelrestgenerator.caching_get_cached(test1="1", test2="2") == [[""]]
    assert _get_request(responses, "http://localhost:8949/cached?test1=1&test2=2")

    responses.add(
        responses.GET,
        url="http://localhost:8949/cached?test1=1&test2=3",
        json={},
        match_querystring=True,
    )
    assert pyxelrestgenerator.caching_get_cached(test1="1", test2="3") == [[""]]
    assert _get_request(responses, "http://localhost:8949/cached?test1=1&test2=3")

    assert pyxelrestgenerator.caching_get_cached(test1="1", test2="2") == [[""]]
    assert not _get_request(responses, "http://localhost:8949/cached?test1=1&test2=2")

    # Wait for cache to be out of date
    time.sleep(5)

    assert pyxelrestgenerator.caching_get_cached(test1="1", test2="2") == [[""]]
    assert _get_request(responses, "http://localhost:8949/cached?test1=1&test2=2")

    assert pyxelrestgenerator.caching_get_cached(test1="1", test2="2") == [[""]]
    assert not _get_request(responses, "http://localhost:8949/cached?test1=1&test2=2")


def test_post_cached(caching_service, responses: RequestsMock):
    loader.load("caching_services.yml")
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.POST,
        url="http://localhost:8949/cached?test1=1&test2=2",
        json={},
        match_querystring=True,
    )

    assert pyxelrestgenerator.caching_post_cached(test1="1", test2="2") == [[""]]
    assert _get_request(responses, "http://localhost:8949/cached?test1=1&test2=2")

    responses.add(
        responses.POST,
        url="http://localhost:8949/cached?test1=1&test2=3",
        json={},
        match_querystring=True,
    )
    assert pyxelrestgenerator.caching_post_cached(test1="1", test2="3") == [[""]]
    assert _get_request(responses, "http://localhost:8949/cached?test1=1&test2=3")
    assert pyxelrestgenerator.caching_post_cached(test1="1", test2="2") == [[""]]
    assert _get_request(responses, "http://localhost:8949/cached?test1=1&test2=2")
    time.sleep(5)
    assert pyxelrestgenerator.caching_post_cached(test1="1", test2="2") == [[""]]
    assert _get_request(responses, "http://localhost:8949/cached?test1=1&test2=2")
    assert pyxelrestgenerator.caching_post_cached(test1="1", test2="2") == [[""]]
    assert _get_request(responses, "http://localhost:8949/cached?test1=1&test2=2")


def test_put_cached(caching_service, responses: RequestsMock):
    loader.load("caching_services.yml")
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.PUT,
        url="http://localhost:8949/cached?test1=1&test2=2",
        json={},
        match_querystring=True,
    )

    assert pyxelrestgenerator.caching_put_cached(test1="1", test2="2") == [[""]]
    assert _get_request(responses, "http://localhost:8949/cached?test1=1&test2=2")

    responses.add(
        responses.PUT,
        url="http://localhost:8949/cached?test1=1&test2=3",
        json={},
        match_querystring=True,
    )
    assert pyxelrestgenerator.caching_put_cached(test1="1", test2="3") == [[""]]
    assert _get_request(responses, "http://localhost:8949/cached?test1=1&test2=3")
    assert pyxelrestgenerator.caching_put_cached(test1="1", test2="2") == [[""]]
    assert _get_request(responses, "http://localhost:8949/cached?test1=1&test2=2")
    time.sleep(5)
    assert pyxelrestgenerator.caching_put_cached(test1="1", test2="2") == [[""]]
    assert _get_request(responses, "http://localhost:8949/cached?test1=1&test2=2")
    assert pyxelrestgenerator.caching_put_cached(test1="1", test2="2") == [[""]]
    assert _get_request(responses, "http://localhost:8949/cached?test1=1&test2=2")


def test_delete_cached(caching_service, responses: RequestsMock):
    loader.load("caching_services.yml")
    from pyxelrest import pyxelrestgenerator

    responses.add(
        responses.DELETE,
        url="http://localhost:8949/cached?test1=1&test2=2",
        json={},
        match_querystring=True,
    )
    assert pyxelrestgenerator.caching_delete_cached(test1="1", test2="2") == [[""]]
    assert _get_request(responses, "http://localhost:8949/cached?test1=1&test2=2")

    responses.add(
        responses.DELETE,
        url="http://localhost:8949/cached?test1=1&test2=3",
        json={},
        match_querystring=True,
    )
    assert pyxelrestgenerator.caching_delete_cached(test1="1", test2="3") == [[""]]
    assert _get_request(responses, "http://localhost:8949/cached?test1=1&test2=3")
    assert pyxelrestgenerator.caching_delete_cached(test1="1", test2="2") == [[""]]
    assert _get_request(responses, "http://localhost:8949/cached?test1=1&test2=2")
    time.sleep(5)
    assert pyxelrestgenerator.caching_delete_cached(test1="1", test2="2") == [[""]]
    assert _get_request(responses, "http://localhost:8949/cached?test1=1&test2=2")
    assert pyxelrestgenerator.caching_delete_cached(test1="1", test2="2") == [[""]]
    assert _get_request(responses, "http://localhost:8949/cached?test1=1&test2=2")

import time

import pytest
from responses import RequestsMock

from testsutils import serviceshandler, loader


@pytest.fixture
def caching_service(responses: RequestsMock):
    from testsutils import caching_service

    serviceshandler.start_services((caching_service, 8949))
    loader.load("caching_services.yml")
    yield 1
    serviceshandler.stop_services()


def test_get_cached(caching_service):
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


def test_post_cached(caching_service):
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


def test_put_cached(caching_service):
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


def test_delete_cached(caching_service):
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

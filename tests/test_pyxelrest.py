from requests import PreparedRequest
from responses import RequestsMock

from tests import loader


def _get_request(responses: RequestsMock, url: str) -> PreparedRequest:
    for call in responses.calls:
        if call.request.url == url:
            # Pop out verified request (to be able to check multiple requests)
            responses.calls._calls.remove(call)
            return call.request


def test_get_custom_url_sync(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                    "vba_compatible": {},
                }
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8958/async/status",
        json={},
        match_querystring=True,
    )

    assert generated_functions.vba_pyxelrest_get_url(
        "http://localhost:8958/async/status",
        extra_headers=[
            ["X-Custom-Header1", "custom1"],
            ["X-Custom-Header2", "custom2"],
        ],
    ) == [[""]]
    headers = _get_request(responses, "http://localhost:8958/async/status").headers
    assert headers["X-Custom-Header1"] == "custom1"
    assert headers["X-Custom-Header2"] == "custom2"


def test_get_custom_url(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                    "vba_compatible": {},
                }
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8958/async/status",
        json={},
        match_querystring=True,
    )

    assert generated_functions.pyxelrest_get_url(
        "http://localhost:8958/async/status",
        extra_headers=[
            ["X-Custom-Header1", "custom1"],
            ["X-Custom-Header2", "custom2"],
        ],
    ) == [[""]]
    headers = _get_request(responses, "http://localhost:8958/async/status").headers
    assert headers["X-Custom-Header1"] == "custom1"
    assert headers["X-Custom-Header2"] == "custom2"


def test_delete_custom_url_sync(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                    "vba_compatible": {},
                }
            }
        },
    )

    responses.add(
        responses.DELETE,
        url="http://localhost:8958/unlisted",
        json={},
        match_querystring=True,
    )

    assert generated_functions.vba_pyxelrest_delete_url(
        "http://localhost:8958/unlisted",
        extra_headers=[
            ["X-Custom-Header1", "custom1"],
            ["X-Custom-Header2", "custom2"],
        ],
    ) == [[""]]
    headers = _get_request(responses, "http://localhost:8958/unlisted").headers
    assert headers["X-Custom-Header1"] == "custom1"
    assert headers["X-Custom-Header2"] == "custom2"


def test_delete_custom_url(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                    "vba_compatible": {},
                }
            }
        },
    )

    responses.add(
        responses.DELETE,
        url="http://localhost:8958/unlisted",
        json={},
        match_querystring=True,
    )

    assert generated_functions.pyxelrest_delete_url(
        "http://localhost:8958/unlisted",
        extra_headers=[
            ["X-Custom-Header1", "custom1"],
            ["X-Custom-Header2", "custom2"],
        ],
    ) == [[""]]
    headers = _get_request(responses, "http://localhost:8958/unlisted").headers
    assert headers["X-Custom-Header1"] == "custom1"
    assert headers["X-Custom-Header2"] == "custom2"


def test_post_custom_url_dict(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                    "vba_compatible": {},
                }
            }
        },
    )

    responses.add(
        responses.POST,
        url="http://localhost:8958/dict",
        json={},
        match_querystring=True,
    )

    assert generated_functions.pyxelrest_post_url(
        "http://localhost:8958/dict",
        [["key1", "key2", "key3"], ["value1", 1, "value3"]],
        extra_headers=[["Content-Type", "application/json"]],
        parse_body_as="dict",
    ) == [[""]]
    request = _get_request(responses, "http://localhost:8958/dict")
    assert request.headers["Content-Type"] == "application/json"
    assert request.body == b'{"key1": "value1", "key2": 1, "key3": "value3"}'


def test_post_custom_url_dict_list_sync(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                    "vba_compatible": {},
                }
            }
        },
    )

    responses.add(
        responses.POST,
        url="http://localhost:8958/dict",
        json={},
        match_querystring=True,
    )

    assert generated_functions.vba_pyxelrest_post_url(
        "http://localhost:8958/dict",
        [["key1", "key2", "key3"], ["value1", 1, "value3"], ["other1", 2, "other3"]],
        extra_headers=[["Content-Type", "application/json"]],
        parse_body_as="dict_list",
    ) == [[""]]
    request = _get_request(responses, "http://localhost:8958/dict")
    assert request.headers["Content-Type"] == "application/json"
    assert (
        request.body
        == b'[{"key1": "value1", "key2": 1, "key3": "value3"}, {"key1": "other1", "key2": 2, "key3": "other3"}]'
    )


def test_post_custom_url_dict_list(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                    "vba_compatible": {},
                }
            }
        },
    )

    responses.add(
        responses.POST,
        url="http://localhost:8958/dict",
        json={},
        match_querystring=True,
    )

    assert generated_functions.pyxelrest_post_url(
        "http://localhost:8958/dict",
        [["key1", "key2", "key3"], ["value1", 1, "value3"], ["other1", 2, "other3"]],
        extra_headers=[["Content-Type", "application/json"]],
        parse_body_as="dict_list",
    ) == [[""]]
    request = _get_request(responses, "http://localhost:8958/dict")
    assert request.headers["Content-Type"] == "application/json"
    assert (
        request.body
        == b'[{"key1": "value1", "key2": 1, "key3": "value3"}, {"key1": "other1", "key2": 2, "key3": "other3"}]'
    )


def test_put_custom_url_dict_list(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                    "vba_compatible": {},
                }
            }
        },
    )

    responses.add(
        responses.PUT, url="http://localhost:8958/dict", json={}, match_querystring=True
    )

    assert generated_functions.pyxelrest_put_url(
        "http://localhost:8958/dict",
        [["key1", "key2", "key3"], ["value1", 1, "value3"], ["other1", 2, "other3"]],
        extra_headers=[["Content-Type", "application/json"]],
        parse_body_as="dict_list",
    ) == [[""]]
    request = _get_request(responses, "http://localhost:8958/dict")
    assert request.headers["Content-Type"] == "application/json"
    assert (
        request.body
        == b'[{"key1": "value1", "key2": 1, "key3": "value3"}, {"key1": "other1", "key2": 2, "key3": "other3"}]'
    )


def test_put_custom_url_dict(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                    "vba_compatible": {},
                }
            }
        },
    )

    responses.add(
        responses.PUT, url="http://localhost:8958/dict", json={}, match_querystring=True
    )

    assert generated_functions.pyxelrest_put_url(
        "http://localhost:8958/dict",
        [["key1", "key2", "key3"], ["value1", 1, "value3"]],
        extra_headers=[["Content-Type", "application/json"]],
        parse_body_as="dict",
    ) == [[""]]
    request = _get_request(responses, "http://localhost:8958/dict")
    assert request.headers["Content-Type"] == "application/json"
    assert request.body == b'{"key1": "value1", "key2": 1, "key3": "value3"}'


def test_put_custom_url_dict_sync(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                    "vba_compatible": {},
                }
            }
        },
    )

    responses.add(
        responses.PUT, url="http://localhost:8958/dict", json={}, match_querystring=True
    )

    assert generated_functions.vba_pyxelrest_put_url(
        "http://localhost:8958/dict",
        [["key1", "key2", "key3"], ["value1", 1, "value3"]],
        extra_headers=[["Content-Type", "application/json"]],
        parse_body_as="dict",
    ) == [[""]]
    request = _get_request(responses, "http://localhost:8958/dict")
    assert request.headers["Content-Type"] == "application/json"
    assert request.body == b'{"key1": "value1", "key2": 1, "key3": "value3"}'

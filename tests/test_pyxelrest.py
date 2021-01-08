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

    assert (
        generated_functions.vba_pyxelrest_get_url(
            "http://localhost:8958/async/status",
            extra_headers=[
                ["X-Custom-Header1", "custom1"],
                ["X-Custom-Header2", "custom2"],
            ],
        )
        == [[""]]
    )
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

    assert (
        generated_functions.pyxelrest_get_url(
            "http://localhost:8958/async/status",
            extra_headers=[
                ["X-Custom-Header1", "custom1"],
                ["X-Custom-Header2", "custom2"],
            ],
        )
        == [[""]]
    )
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

    assert (
        generated_functions.vba_pyxelrest_delete_url(
            "http://localhost:8958/unlisted",
            extra_headers=[
                ["X-Custom-Header1", "custom1"],
                ["X-Custom-Header2", "custom2"],
            ],
        )
        == [[""]]
    )
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

    assert (
        generated_functions.pyxelrest_delete_url(
            "http://localhost:8958/unlisted",
            extra_headers=[
                ["X-Custom-Header1", "custom1"],
                ["X-Custom-Header2", "custom2"],
            ],
        )
        == [[""]]
    )
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

    assert (
        generated_functions.pyxelrest_post_url(
            "http://localhost:8958/dict",
            [["key1", "key2", "key3"], ["value1", 1, "value3"]],
            extra_headers=[["Content-Type", "application/json"]],
            parse_body_as="dict",
        )
        == [[""]]
    )
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

    assert (
        generated_functions.vba_pyxelrest_post_url(
            "http://localhost:8958/dict",
            [
                ["key1", "key2", "key3"],
                ["value1", 1, "value3"],
                ["other1", 2, "other3"],
            ],
            extra_headers=[["Content-Type", "application/json"]],
            parse_body_as="dict_list",
        )
        == [[""]]
    )
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

    assert (
        generated_functions.pyxelrest_post_url(
            "http://localhost:8958/dict",
            [
                ["key1", "key2", "key3"],
                ["value1", 1, "value3"],
                ["other1", 2, "other3"],
            ],
            extra_headers=[["Content-Type", "application/json"]],
            parse_body_as="dict_list",
        )
        == [[""]]
    )
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

    assert (
        generated_functions.pyxelrest_put_url(
            "http://localhost:8958/dict",
            [
                ["key1", "key2", "key3"],
                ["value1", 1, "value3"],
                ["other1", 2, "other3"],
            ],
            extra_headers=[["Content-Type", "application/json"]],
            parse_body_as="dict_list",
        )
        == [[""]]
    )
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

    assert (
        generated_functions.pyxelrest_put_url(
            "http://localhost:8958/dict",
            [["key1", "key2", "key3"], ["value1", 1, "value3"]],
            extra_headers=[["Content-Type", "application/json"]],
            parse_body_as="dict",
        )
        == [[""]]
    )
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

    assert (
        generated_functions.vba_pyxelrest_put_url(
            "http://localhost:8958/dict",
            [["key1", "key2", "key3"], ["value1", 1, "value3"]],
            extra_headers=[["Content-Type", "application/json"]],
            parse_body_as="dict",
        )
        == [[""]]
    )
    request = _get_request(responses, "http://localhost:8958/dict")
    assert request.headers["Content-Type"] == "application/json"
    assert request.body == b'{"key1": "value1", "key2": 1, "key3": "value3"}'


def test_post_invalid_parse_body_as_date(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                }
            }
        },
    )

    assert (
        generated_functions.pyxelrest_post_url(
            "http://localhost:8958/dict",
            [["key1", "key2", "key3"], ["value1", 1, "value3"]],
            parse_body_as="invalid",
        )
        == ['parse_body_as value "invalid" should be dict or dict_list.']
    )


def test_post_invalid_wait_for_status(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                }
            }
        },
    )

    assert (
        generated_functions.pyxelrest_post_url(
            "http://localhost:8958/dict",
            [["key1", "key2", "key3"], ["value1", 1, "value3"]],
            wait_for_status="invalid",
        )
        == ['wait_for_status value "invalid" must be an integer.']
    )


def test_post_negative_wait_for_status(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                }
            }
        },
    )

    assert (
        generated_functions.pyxelrest_post_url(
            "http://localhost:8958/dict",
            [["key1", "key2", "key3"], ["value1", 1, "value3"]],
            wait_for_status=-1,
        )
        == ['wait_for_status value "-1" must be superior or equals to 0.']
    )


def test_post_invalid_check_interval(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                }
            }
        },
    )

    assert (
        generated_functions.pyxelrest_post_url(
            "http://localhost:8958/dict",
            [["key1", "key2", "key3"], ["value1", 1, "value3"]],
            check_interval="invalid",
        )
        == ['check_interval value "invalid" must be an integer.']
    )


def test_post_negative_check_interval(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                }
            }
        },
    )

    assert (
        generated_functions.pyxelrest_post_url(
            "http://localhost:8958/dict",
            [["key1", "key2", "key3"], ["value1", 1, "value3"]],
            check_interval=-1,
        )
        == ['check_interval value "-1" must be superior or equals to 0.']
    )


def test_post_invalid_url(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                }
            }
        },
    )

    assert (
        generated_functions.pyxelrest_post_url(
            -1,
            [["key1", "key2", "key3"], ["value1", 1, "value3"]],
        )
        == ['url value "-1" must be formatted as text.']
    )


def test_get_invalid_auth(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                }
            }
        },
    )

    assert generated_functions.pyxelrest_get_url(
        "http://localhost:8958/dict",
        auth="invalid",
    ) == [
        'auth value "invalid" should be oauth2_implicit or api_key_header or api_key_query or basic.'
    ]


def test_get_invalid_oauth2_auth_url(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                }
            }
        },
    )

    assert (
        generated_functions.pyxelrest_get_url(
            "http://localhost:8958/dict",
            auth="oauth2_implicit",
            oauth2_auth_url=-1,
        )
        == ['oauth2_auth_url value "-1" must be formatted as text.']
    )


def test_get_invalid_oauth2_token_url(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                }
            }
        },
    )

    assert (
        generated_functions.pyxelrest_get_url(
            "http://localhost:8958/dict",
            auth="oauth2_implicit",
            oauth2_token_url=-1,
        )
        == ['oauth2_token_url value "-1" must be formatted as text.']
    )


def test_get_invalid_api_key_name(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                }
            }
        },
    )

    assert (
        generated_functions.pyxelrest_get_url(
            "http://localhost:8958/dict",
            auth="api_key_header",
            api_key_name=-1,
        )
        == ['api_key_name value "-1" must be formatted as text.']
    )


def test_get_wait_for_status(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                }
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8958/test",
        status=303,
        adding_headers={"location": "http://localhost:8958/test2"},
        match_querystring=True,
    )

    responses.add(
        responses.GET,
        url="http://localhost:8958/test2",
        json={},
        status=200,
        match_querystring=True,
    )

    assert (
        generated_functions.pyxelrest_get_url(
            "http://localhost:8958/test",
            wait_for_status=303,
        )
        == [[""]]
    )


def test_get_check_interval(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                }
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8958/test",
        status=303,
        adding_headers={"location": "http://localhost:8958/test2"},
        match_querystring=True,
    )

    responses.add(
        responses.GET,
        url="http://localhost:8958/test2",
        json={},
        status=200,
        match_querystring=True,
    )

    assert (
        generated_functions.pyxelrest_get_url(
            "http://localhost:8958/test",
            wait_for_status=303,
            check_interval=1,
        )
        == [[""]]
    )


def test_post_invalid_dict_only_header(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                }
            }
        },
    )

    assert (
        generated_functions.pyxelrest_post_url(
            "http://localhost:8958/dict",
            [["key1", "key2", "key3"]],
            parse_body_as="dict",
        )
        == ["There should be only two rows. Header and values."]
    )


def test_post_invalid_dict_too_many_rows(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                }
            }
        },
    )

    assert (
        generated_functions.pyxelrest_post_url(
            "http://localhost:8958/dict",
            [["key1", "key2"], ["value1", "value2"], ["value10", "value20"]],
            parse_body_as="dict",
        )
        == ["There should be only two rows. Header and values."]
    )


def test_post_invalid_dict_list_only_header(responses: RequestsMock, tmpdir):
    generated_functions = loader.load(
        tmpdir,
        {
            "pyxelrest": {
                "formulas": {
                    "dynamic_array": {"lock_excel": True},
                }
            }
        },
    )

    assert (
        generated_functions.pyxelrest_post_url(
            "http://localhost:8958/dict",
            [["key1", "key2", "key3"]],
            parse_body_as="dict_list",
        )
        == ["There should be at least two rows. Header and first dictionary values."]
    )

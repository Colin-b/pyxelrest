import time

from requests_auth import authentication
import pytest
from responses import RequestsMock

from testsutils import serviceshandler, loader


@pytest.fixture
def services(responses: RequestsMock):
    from testsutils import (
        authenticated_service,
        oauth2_authentication_service,
        non_authenticated_service,
    )

    serviceshandler.start_services(
        (authenticated_service, 8946),
        (oauth2_authentication_service, 8947),
        (non_authenticated_service, 8948),
    )
    loader.load("authentication_services.yml")
    authentication.OAuth2.token_cache.clear()
    yield 1
    serviceshandler.stop_services()


def test_oauth2_authentication_on_custom_server_port(services):
    from pyxelrest import pyxelrestgenerator

    first_token = (
        pyxelrestgenerator.oauth_cutom_response_port_get_oauth2_authentication_success()
    )
    assert first_token[0] == ["Authorization"]
    # Wait for 1 second and send a second request from another server to the same auth server
    # (should not request another token)
    time.sleep(1)
    second_token = pyxelrestgenerator.authenticated_get_oauth2_authentication_success()
    assert second_token[0] == ["Authorization"]
    assert first_token[1] == second_token[1]


def test_oauth2_authentication_success(services):
    from pyxelrest import pyxelrestgenerator

    token = pyxelrestgenerator.authenticated_get_oauth2_authentication_success()
    assert token[0] == ["Authorization"]
    assert token[1]


def test_pyxelrest_oauth2_authentication_success(services):
    from pyxelrest import pyxelrestgenerator

    token = pyxelrestgenerator.pyxelrest_get_url(
        "http://localhost:8946/oauth2/authentication/success",
        auth=["oauth2_implicit"],
        oauth2_auth_url="http://localhost:8947/auth_success?response_type=id_token",
    )
    assert token[0] == ["Authorization"]
    assert token[1]


def test_oauth2_authentication_success_with_custom_response_type(services):
    from pyxelrest import pyxelrestgenerator

    token = (
        pyxelrestgenerator.oauth_custom_token_name_get_oauth2_authentication_success_with_custom_response_type()
    )
    assert token[0] == ["Authorization"]
    assert token[1]


def test_oauth2_authentication_success_without_response_type(services):
    from pyxelrest import pyxelrestgenerator

    token = (
        pyxelrestgenerator.authenticated_get_oauth2_authentication_success_without_response_type()
    )
    assert token[0] == ["Authorization"]
    assert token[1]


def test_pyxelrest_oauth2_authentication_success_without_response_type(services):
    from pyxelrest import pyxelrestgenerator

    token = pyxelrestgenerator.pyxelrest_get_url(
        "http://localhost:8946/oauth2/authentication/success/without/response/type",
        auth=["oauth2_implicit"],
        oauth2_auth_url="http://localhost:8947/auth_success_without_response_type",
    )
    assert token[0] == ["Authorization"]
    assert token[1]


def test_oauth2_authentication_token_reuse(services):
    from pyxelrest import pyxelrestgenerator

    first_token = pyxelrestgenerator.authenticated_get_oauth2_authentication_success()
    assert first_token[0] == ["Authorization"]
    # As the token should not be expired, this call should use the same token
    second_token = pyxelrestgenerator.authenticated_get_oauth2_authentication_success()
    assert first_token == second_token


def test_pyxelrest_oauth2_authentication_token_reuse(services):
    from pyxelrest import pyxelrestgenerator

    first_token = pyxelrestgenerator.pyxelrest_get_url(
        "http://localhost:8946/oauth2/authentication/success",
        auth=["oauth2_implicit"],
        oauth2_auth_url="http://localhost:8947/auth_success?response_type=id_token",
    )
    assert first_token[0] == ["Authorization"]
    second_token = pyxelrestgenerator.pyxelrest_get_url(
        "http://localhost:8946/oauth2/authentication/success",
        auth=["oauth2_implicit"],
        oauth2_auth_url="http://localhost:8947/auth_success?response_type=id_token",
    )
    assert first_token == second_token


def test_oauth2_authentication_failure(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        'An error occurred. Please check logs for full details: "id_token not provided within {}."'
        == pyxelrestgenerator.authenticated_get_oauth2_authentication_failure()
    )


def test_oauth2_authentication_timeout(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        'An error occurred. Please check logs for full details: "User authentication was not received within 10 seconds."'
        == pyxelrestgenerator.authenticated_get_oauth2_authentication_timeout()
    )


def test_without_authentication(services):
    from pyxelrest import pyxelrestgenerator

    assert [
        ["received token"],
        [False],
    ] == pyxelrestgenerator.non_authenticated_get_without_auth()


def test_oauth2_authentication_expiry(services):
    from pyxelrest import pyxelrestgenerator

    # This token will expires in 1 seconds
    first_token = (
        pyxelrestgenerator.authenticated_get_oauth2_authentication_success_quick_expiry()
    )
    assert first_token[0] == ["Authorization"], str(first_token)
    time.sleep(2)
    # Token should now be expired, a new one should be requested
    second_token = (
        pyxelrestgenerator.authenticated_get_oauth2_authentication_success_quick_expiry()
    )
    assert second_token[0] == ["Authorization"]
    assert first_token[1] != second_token[1]


def test_api_key_header_authentication_success(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.authenticated_get_api_key_header_authentication_success() == [
        ["X-API-HEADER-KEY"],
        ["my_provided_api_key"],
    ]


def test_pyxelrest_api_key_header_authentication_success(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.pyxelrest_get_url(
        "http://localhost:8946/api/key/header/authentication/success",
        auth=["api_key_header"],
        api_key_name="X-API-HEADER-KEY",
    ) == [["X-API-HEADER-KEY"], ["my_provided_api_key"]]


def test_api_key_query_authentication_success(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.authenticated_get_api_key_query_authentication_success() == [
        ["X-API-QUERY-KEY"],
        ["my_provided_api_key"],
    ]


def test_pyxelrest_api_key_query_authentication_success(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.pyxelrest_get_url(
        "http://localhost:8946/api/key/query/authentication/success",
        auth=["api_key_query"],
        api_key_name="X-API-QUERY-KEY",
    ) == [["X-API-QUERY-KEY"], ["my_provided_api_key"]]


def test_basic_authentication_success(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.authenticated_get_basic_authentication_success() == [
        ["Authorization"],
        ["Basic dGVzdF91c2VyOnRlc3RfcHdk"],
    ]


def test_pyxelrest_basic_authentication_success(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.pyxelrest_get_url(
        "http://localhost:8946/basic/authentication/success", auth=["basic"]
    ) == [["Authorization"], ["Basic dGVzdF91c2VyOnRlc3RfcHdk"]]


def test_basic_and_api_key_authentication_success(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.authenticated_get_basic_and_api_key_authentication_success() == [
        ["Authorization", "X-API-HEADER-KEY"],
        ["Basic dGVzdF91c2VyOnRlc3RfcHdk", "my_provided_api_key"],
    ]


def test_pyxelrest_basic_and_api_key_authentication_success(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.pyxelrest_get_url(
        "http://localhost:8946/basic/and/api/key/authentication/success",
        auth=["basic", "api_key_header"],
        api_key_name="X-API-HEADER-KEY",
    ) == [
        ["Authorization", "X-API-HEADER-KEY"],
        ["Basic dGVzdF91c2VyOnRlc3RfcHdk", "my_provided_api_key"],
    ]


def test_basic_or_api_key_authentication_success(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.authenticated_get_basic_or_api_key_authentication_success() == [
        ["Authorization", "X-API-HEADER-KEY"],
        ["Basic dGVzdF91c2VyOnRlc3RfcHdk", ""],
    ]


def test_api_key_or_basic_authentication_success(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.authenticated_get_api_key_or_basic_authentication_success() == [
        ["Authorization", "X-API-HEADER-KEY"],
        ["", "my_provided_api_key"],
    ]

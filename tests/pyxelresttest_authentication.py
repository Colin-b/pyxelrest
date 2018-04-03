from requests_auth import authentication
import time
import unittest

from testsutils import (serviceshandler, loader)


class PyxelRestAuthenticationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.start_services()
        loader.load('authentication_services.yml')

    @classmethod
    def tearDownClass(cls):
        serviceshandler.stop_services()

    def setUp(self):
        authentication.OAuth2.token_cache.clear()

    @classmethod
    def start_services(cls):
        from testsutils import (
            authenticated_service,
            oauth2_authentication_service,
            non_authenticated_service
        )
        serviceshandler.start_services(
            (authenticated_service, 8946),
            (oauth2_authentication_service, 8947),
            (non_authenticated_service, 8948)
        )

    def test_oauth2_authentication_on_custom_server_port(self):
        from pyxelrest import pyxelrestgenerator
        first_token = pyxelrestgenerator.oauth_cutom_response_port_get_oauth2_authentication_success()
        self.assertEqual(first_token[0], ['Bearer'])
        # Wait for 1 second and send a second request from another server to the same auth server
        # (should not request another token)
        time.sleep(1)
        second_token = pyxelrestgenerator.authenticated_get_oauth2_authentication_success()
        self.assertEqual(second_token[0], ['Bearer'])
        self.assertEqual(first_token[1], second_token[1])

    def test_oauth2_authentication_success(self):
        from pyxelrest import pyxelrestgenerator
        token = pyxelrestgenerator.authenticated_get_oauth2_authentication_success()
        self.assertEqual(token[0], ['Bearer'])
        self.assertIsNotNone(token[1])

    def test_oauth2_authentication_success_with_custom_response_type(self):
        from pyxelrest import pyxelrestgenerator
        token = pyxelrestgenerator.oauth_custom_token_name_get_oauth2_authentication_success_with_custom_response_type()
        self.assertEqual(token[0], ['Bearer'])
        self.assertIsNotNone(token[1])

    def test_oauth2_authentication_success_without_response_type(self):
        from pyxelrest import pyxelrestgenerator
        token = pyxelrestgenerator.authenticated_get_oauth2_authentication_success_without_response_type()
        self.assertEqual(token[0], ['Bearer'])
        self.assertIsNotNone(token[1])

    def test_oauth2_authentication_token_reuse(self):
        from pyxelrest import pyxelrestgenerator
        first_token = pyxelrestgenerator.authenticated_get_oauth2_authentication_success()
        self.assertEqual(first_token[0], ['Bearer'])
        # As the token should not be expired, this call should use the same token
        second_token = pyxelrestgenerator.authenticated_get_oauth2_authentication_success()
        self.assertEqual(first_token, second_token)

    def test_oauth2_authentication_failure(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual('An error occurred. Please check logs for full details: "id_token not provided within {}."',
                         pyxelrestgenerator.authenticated_get_oauth2_authentication_failure())

    def test_oauth2_authentication_timeout(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual('An error occurred. Please check logs for full details: "User authentication was not received within 10 seconds."',
                         pyxelrestgenerator.authenticated_get_oauth2_authentication_timeout())

    def test_without_authentication(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual([
            ['received token'],
            [False]
        ],
            pyxelrestgenerator.non_authenticated_get_without_auth())

    def test_oauth2_authentication_expiry(self):
        from pyxelrest import pyxelrestgenerator
        # This token will expires in 1 seconds
        first_token = pyxelrestgenerator.authenticated_get_oauth2_authentication_success_quick_expiry()
        self.assertEqual(first_token[0], ['Bearer'], str(first_token))
        time.sleep(2)
        # Token should now be expired, a new one should be requested
        second_token = pyxelrestgenerator.authenticated_get_oauth2_authentication_success_quick_expiry()
        self.assertEqual(second_token[0], ['Bearer'])
        self.assertNotEqual(first_token[1], second_token[1])

    def test_api_key_header_authentication_success(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.authenticated_get_api_key_header_authentication_success(),
                         [
                             ['X-API-HEADER-KEY'],
                             ['my_provided_api_key']
                         ])

    def test_api_key_query_authentication_success(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.authenticated_get_api_key_query_authentication_success(),
                         [
                             ['X-API-QUERY-KEY'],
                             ['my_provided_api_key']
                         ])

    def test_basic_authentication_success(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.authenticated_get_basic_authentication_success(),
                         [
                             ['Authorization'],
                             ['Basic dGVzdF91c2VyOnRlc3RfcHdk']
                         ])

    def test_basic_and_api_key_authentication_success(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.authenticated_get_basic_and_api_key_authentication_success(),
                         [
                             ['Authorization', 'X-API-HEADER-KEY'],
                             ['Basic dGVzdF91c2VyOnRlc3RfcHdk', 'my_provided_api_key']
                         ])

    def test_basic_or_api_key_authentication_success(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.authenticated_get_basic_or_api_key_authentication_success(),
                         [
                             ['Authorization', 'X-API-HEADER-KEY'],
                             ['Basic dGVzdF91c2VyOnRlc3RfcHdk', '']
                         ])

    def test_api_key_or_basic_authentication_success(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(pyxelrestgenerator.authenticated_get_api_key_or_basic_authentication_success(),
                         [
                             ['Authorization', 'X-API-HEADER-KEY'],
                             ['', 'my_provided_api_key']
                         ])


if __name__ == '__main__':
    unittest.main()

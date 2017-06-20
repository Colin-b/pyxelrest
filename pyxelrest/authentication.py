import logging
import sys
import requests
import requests.auth

import oauth2_authentication_responses_server

if sys.version_info.major > 2:
    # Python 3
    from urllib.parse import parse_qs, urlsplit, urlunsplit, urlencode
else:
    # Python 2
    from urllib import urlencode
    from urlparse import parse_qs, urlsplit, urlunsplit


# Key is a tuple 'service name, security key'
security_definitions = {}
# Key is service name
custom_authentications = {}


def get_detail(detail_key, details_string):
    """
    Retrieve authentication detail from configuration.
    
    :param detail_key: Authentication detail to be retrieved
    :param details_string: Authentication details string
    :return: Authentication detail as a string, or None if not found
    """
    if details_string:
        # TODO Use regex instead of this split mechanism
        for detail_entry in details_string.split(','):
            detail_entry = detail_entry.split('=')
            if detail_key == detail_entry[0]:
                return detail_entry[1] if len(detail_entry) == 2 else None


def get_detail_int(detail_key, details_string, default_value):
    value = get_detail(detail_key, details_string)
    return int(value) if value else default_value


class OAuth2Auth(requests.auth.AuthBase):
    """Describes an OAuth 2 security definition."""
    def __init__(self, service_name, security_definition, security_details):
        self.service_name = service_name
        self.security_definition = security_definition
        self.security_details = security_details
        authorization_url = security_definition['authorizationUrl']
        self.key = '{0}/{1}'.format(service_name, security_definition['security_definition_key'])
        self.port = get_detail_int('port', security_details,
                                   oauth2_authentication_responses_server.DEFAULT_SERVER_PORT)
        self.redirect_uri = 'http://localhost:{0}/{1}'.format(self.port, self.key)
        self.full_url = OAuth2Auth.create_auth_url(authorization_url, self.redirect_uri)
        self.token_name = OAuth2Auth.get_query_parameter(authorization_url, 'response_type') or \
                          get_detail('response_type', security_details) or \
                          oauth2_authentication_responses_server.DEFAULT_TOKEN_NAME
        self.timeout = get_detail_int('timeout', security_details,
                                      oauth2_authentication_responses_server.DEFAULT_AUTHENTICATION_TIMEOUT)
        self.success_display_time = get_detail_int('success_display_time', security_details,
                                                   oauth2_authentication_responses_server.DEFAULT_SUCCESS_DISPLAY_TIME)
        self.failure_display_time = get_detail_int('failure_display_time', security_details,
                                                   oauth2_authentication_responses_server.DEFAULT_FAILURE_DISPLAY_TIME)

    def __call__(self, r):
        r.headers['Bearer'] = oauth2_authentication_responses_server.get_bearer(self)
        return r

    @staticmethod
    def get_query_parameter(url, param_name):
        scheme, netloc, path, query_string, fragment = urlsplit(url)
        query_params = parse_qs(query_string)
        all_values = query_params.get(param_name)
        return all_values[0] if all_values else None

    @staticmethod
    def create_auth_url(url, redirect_url):
        scheme, netloc, path, query_string, fragment = urlsplit(url)
        query_params = parse_qs(query_string)

        query_params['redirect_uri'] = [redirect_url]
        # Force Form Post as get is only providing token in anchor and anchor is not provided to server
        # (interpreted on client side only)
        query_params['response_mode'] = ['form_post']
        new_query_string = urlencode(query_params, doseq=True)

        return urlunsplit((scheme, netloc, path, new_query_string, fragment))

    def __str__(self):
        return "authentication.OAuth2Auth('{0}', {1}, '{2}')".format(self.service_name,
                                                                     self.security_definition,
                                                                     self.security_details)


class ApiKeyAuth(requests.auth.AuthBase):
    """Describes an API Key security definition."""
    def __init__(self, security_definition, security_details):
        self.security_definition = security_definition
        self.security_details = security_details
        self.field_name = security_definition['name']
        self.value_in = security_definition['in']
        self.api_key = get_detail('api_key', security_details)

    def __call__(self, r):
        if not self.api_key:
            logging.error('api_key is not defined. Call might be rejected by server.')
        else:
            if self.value_in == 'header':
                r.headers[self.field_name] = self.api_key
            elif self.value_in == 'query':
                r.url = ApiKeyAuth.add_query_parameter(r.url, self.field_name, self.api_key)
            else:
                logging.warning('api_key "{0}" destination is not supported.'.format(self.value_in))
        return r

    @staticmethod
    def add_query_parameter(url, parameter_name, parameter_value):
        scheme, netloc, path, query_string, fragment = urlsplit(url)
        query_params = parse_qs(query_string)

        query_params[parameter_name] = [parameter_value]
        new_query_string = urlencode(query_params, doseq=True)

        return urlunsplit((scheme, netloc, path, new_query_string, fragment))

    def __str__(self):
        return "authentication.ApiKeyAuth({0},'{1}')".format(self.security_definition, self.security_details)


class BasicAuth(requests.auth.HTTPBasicAuth):
    """Describes a basic security definition."""
    def __init__(self, security_details):
        self.security_details = security_details
        username = get_detail('username', security_details)
        password = get_detail('password', security_details)
        requests.auth.HTTPBasicAuth.__init__(self, username, password)

    def __str__(self):
        return "authentication.BasicAuth('{0}')".format(self.security_details)


class NTLMAuth:
    """Describes a NTLM authentication."""
    def __init__(self, security_details):
        self.security_details = security_details
        username = get_detail('username', security_details)
        password = get_detail('password', security_details)
        if not username and not password:
            try:
                import requests_negotiate_sspi
                self.auth = requests_negotiate_sspi.HttpNegotiateAuth()
            except ImportError:
                raise Exception('NTLM authentication requires requests_negotiate_sspi module.')
        else:
            if not username:
                raise Exception('NTLM authentication requires "username" to be provided in security_details.')
            if not password:
                raise Exception('NTLM authentication requires "password" to be provided in security_details.')
            try:
                import requests_ntlm
                self.auth = requests_ntlm.HttpNtlmAuth(username, password)
            except ImportError:
                raise Exception('NTLM authentication requires requests_ntlm module.')

    def __call__(self, r):
        self.auth.__call__(r)
        return r

    def __str__(self):
        return "authentication.NTLMAuth('{0}')".format(self.security_details)


class MultipleAuth(requests.auth.AuthBase):
    """Authentication using multiple authentication methods."""
    def __init__(self, authentication_modes):
        self.authentication_modes = authentication_modes

    def __call__(self, r):
        for authentication_mode in self.authentication_modes:
            authentication_mode.__call__(r)
        return r

    def __str__(self):
        return "authentication.MultipleAuth([" + ", ".join(map(str, self.authentication_modes)) + "])"


def add_service_custom_authentication(service_name, security_details):
    auth = get_detail('auth', security_details)
    if 'ntlm' == auth:
        custom_authentications[service_name] = NTLMAuth(security_details)
        return auth


def add_service_security(service_name, swagger, security_details):
    json_security_definitions = swagger.get('securityDefinitions', {})
    for security_definition_key in json_security_definitions.keys():
        security_definition = json_security_definitions[security_definition_key]
        security_definition['security_definition_key'] = security_definition_key
        authentication = create_authentication(security_definition, service_name, security_details)
        if authentication:
            security_definitions[service_name, security_definition_key] = authentication


def create_authentication(security_definition, service_name, security_details):
    if 'oauth2' == security_definition.get('type'):
        if security_definition.get('flow') == 'implicit':
            return OAuth2Auth(service_name, security_definition, security_details)
        # TODO Handle all OAuth2 flows
        logging.warning('OAuth2 flow is not supported: {0}'.format(security_definition))
    elif 'apiKey' == security_definition.get('type'):
        return ApiKeyAuth(security_definition, security_details)
    elif 'basic' == security_definition.get('type'):
        return BasicAuth(security_details)
    else:
        logging.error('Unexpected security definition type: {0}'.format(security_definition))


def get_auth(service_name, securities):
    custom_authentication = custom_authentications.get(service_name)

    # Run through all available securities
    for security in securities:
        authentication_modes = [custom_authentication] if custom_authentication else []
        for security_definition_key in security.keys():
            auth = security_definitions.get((service_name, security_definition_key))
            if auth:
                authentication_modes.append(auth)
        # A single authentication method is required and PyxelRest support it
        if len(authentication_modes) == 1:
            return authentication_modes[0]
        # Multiple authentication methods are required and PyxelRest support it
        if len(authentication_modes) > 1:
            return MultipleAuth(authentication_modes)
        # Otherwise check if there is another security available

    # Default to custom authentication if no security is supported
    return custom_authentication

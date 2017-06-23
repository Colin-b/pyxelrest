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


def add_parameters(initial_url, extra_parameters):
    """
    Add parameters to an URL and return the new URL.

    :param initial_url:
    :param extra_parameters: dictionary of parameters name and value.
    :return: the new URL containing parameters.
    """
    scheme, netloc, path, query_string, fragment = urlsplit(initial_url)
    query_params = parse_qs(query_string)

    for parameter_name in extra_parameters.keys():
        # TODO Handle parameters with a list as a value and submit PR to requests or Python
        query_params[parameter_name] = [extra_parameters[parameter_name]]

    new_query_string = urlencode(query_params, doseq=True)

    return urlunsplit((scheme, netloc, path, new_query_string, fragment))


def get_query_parameter(url, param_name):
    scheme, netloc, path, query_string, fragment = urlsplit(url)
    query_params = parse_qs(query_string)
    all_values = query_params.get(param_name)
    return all_values[0] if all_values else None


class OAuth2Auth(requests.auth.AuthBase):
    """Describes an OAuth 2 security definition."""
    def __init__(self, service_name, security_definition, security_details):
        from oauth2_authentication_responses_server import (
            DEFAULT_SERVER_PORT,
            DEFAULT_TOKEN_NAME,
            DEFAULT_AUTHENTICATION_TIMEOUT,
            DEFAULT_SUCCESS_DISPLAY_TIME,
            DEFAULT_FAILURE_DISPLAY_TIME
        )
        self.service_name = service_name
        self.security_definition = security_definition
        self.security_details = security_details
        self.key = '{0}/{1}'.format(service_name, security_definition['security_definition_key'])
        self.port = int(security_details.get('port', DEFAULT_SERVER_PORT))
        self.redirect_uri = 'http://localhost:{0}/{1}'.format(self.port, self.key)
        self.full_url = add_parameters(security_definition['authorizationUrl'], self.get_oauth2_parameters())
        self.token_name = get_query_parameter(self.full_url, 'response_type') or DEFAULT_TOKEN_NAME
        self.timeout = int(security_details.get('timeout', DEFAULT_AUTHENTICATION_TIMEOUT))
        self.success_display_time = int(security_details.get('success_display_time', DEFAULT_SUCCESS_DISPLAY_TIME))
        self.failure_display_time = int(security_details.get('failure_display_time', DEFAULT_FAILURE_DISPLAY_TIME))

    def __call__(self, r):
        r.headers['Bearer'] = oauth2_authentication_responses_server.get_bearer(self)
        return r

    def get_oauth2_parameters(self):
        extra_parameters = {
            'redirect_uri': self.redirect_uri,

            # TODO Handle GET to be able to get rid of this HACK (not working with every OAUTH2 provider anyway)
            # Force Form Post as get is only providing token in anchor and anchor is not provided to server
            # (interpreted on client side only)
            'response_mode': 'form_post'
        }
        # Return all parameters specified in configuration (prefixed with oauth2.)
        extra_parameters.update({
            security_detail_key[7:]: self.security_details[security_detail_key]
            for security_detail_key in self.security_details.keys() if security_detail_key.startswith('oauth2.')
        })

        return extra_parameters

    def __str__(self):
        return "authentication.OAuth2Auth('{0}', {1}, {2})".format(self.service_name,
                                                                   self.security_definition,
                                                                   self.security_details)


class ApiKeyAuth(requests.auth.AuthBase):
    """Describes an API Key security definition."""
    def __init__(self, security_definition, security_details):
        self.security_definition = security_definition
        self.security_details = security_details
        self.field_name = security_definition['name']
        self.value_in = security_definition['in']
        self.api_key = security_details.get('api_key')

    def __call__(self, r):
        if not self.api_key:
            logging.error('api_key is not defined. Call might be rejected by server.')
        else:
            if self.value_in == 'header':
                r.headers[self.field_name] = self.api_key
            elif self.value_in == 'query':
                r.url = add_parameters(r.url, {self.field_name: self.api_key})
            else:
                logging.warning('api_key "{0}" destination is not supported.'.format(self.value_in))
        return r

    def __str__(self):
        return "authentication.ApiKeyAuth({0}, {1})".format(self.security_definition, self.security_details)


class BasicAuth(requests.auth.HTTPBasicAuth):
    """Describes a basic security definition."""
    def __init__(self, security_details):
        self.security_details = security_details
        username = security_details.get('username')
        password = security_details.get('password')
        requests.auth.HTTPBasicAuth.__init__(self, username, password)

    def __str__(self):
        return "authentication.BasicAuth({0})".format(self.security_details)


class NTLMAuth:
    """Describes a NTLM authentication."""
    def __init__(self, security_details):
        self.security_details = security_details
        username = security_details.get('username')
        password = security_details.get('password')
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
        return "authentication.NTLMAuth({0})".format(self.security_details)


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
    auth = security_details.get('auth')
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

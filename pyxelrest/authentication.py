import logging
import os
import jinja2
import datetime
import sys
import requests
import requests.auth
from importlib import import_module
try:
    # Python 3
    from importlib import reload
    from urllib.parse import parse_qs, urlsplit, urlunsplit, urlencode
except ImportError:
    # Python 2
    from imp import reload
    from urllib import urlencode
    from urlparse import parse_qs, urlsplit, urlunsplit


# Key is a tuple 'service name, security key'
security_definitions = {}
# Key is port
oauth2_security_definitions_by_port = {}
# Key is service_name
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

    DEFAULT_OAUTH2_SERVER_PORT = 5000
    DEFAULT_OAUTH2_AUTHENTICATION_TIMEOUT = 20  # Time is expressed in seconds
    DEFAULT_SUCCESS_DISPLAY_TIME = 1  # Time is expressed in milliseconds
    DEFAULT_FAILURE_DISPLAY_TIME = 5000  # Time is expressed in milliseconds

    def __init__(self, security_definition_key, security_definition, service_name, security_details):
        self.port = get_detail_int('port', security_details, OAuth2Auth.DEFAULT_OAUTH2_SERVER_PORT)
        self.key = service_name, security_definition_key
        self.service_name = service_name
        self.security_definition_key = security_definition_key
        self.redirect_uri = 'http://localhost:{0}/{1}/{2}'.format(self.port, service_name, security_definition_key)
        authorization_url = security_definition['authorizationUrl']
        self.full_url = OAuth2Auth.create_auth_url(authorization_url, self.redirect_uri)
        self.token_name = OAuth2Auth.get_query_parameter(authorization_url, 'response_type') or 'token'
        self.timeout = get_detail_int('timeout', security_details, OAuth2Auth.DEFAULT_OAUTH2_AUTHENTICATION_TIMEOUT)
        self.success_display_time = get_detail_int('success_display_time', security_details, OAuth2Auth.DEFAULT_SUCCESS_DISPLAY_TIME)
        self.failure_display_time = get_detail_int('failure_display_time', security_details, OAuth2Auth.DEFAULT_FAILURE_DISPLAY_TIME)

    def __call__(self, r):
        import oauth2_authentication_responses_servers
        server = oauth2_authentication_responses_servers.servers[self.port]
        r.headers['Bearer'] = server.get_bearer(self)
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


class ApiKeyAuth(requests.auth.AuthBase):
    """Describes an API Key security definition."""
    def __init__(self, security_definition, security_details):
        self.field_name = security_definition['name']
        self.value_in = security_definition['in']
        self.api_key = get_detail('api_key', security_details)

    def __call__(self, r):
        if not self.api_key:
            logging.warning('api_key is not defined. Call might be rejected by server.')
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


class BasicAuth(requests.auth.HTTPBasicAuth):
    """Describes a basic security definition."""
    def __init__(self, security_details):
        username = get_detail('username', security_details)
        password = get_detail('password', security_details)
        requests.auth.HTTPBasicAuth.__init__(self, username, password)


class NTLMAuth:
    """Describes a NTLM authentication."""
    def __init__(self, security_details):
        username = get_detail('username', security_details)
        if not username:
            raise Exception('NTLM authentication requires username to be provided in security_details.')
        password = get_detail('password', security_details)
        if not password:
            raise Exception('NTLM authentication requires password to be provided in security_details.')
        try:
            import requests_ntlm
            self.auth = requests_ntlm.HttpNtlmAuth(username, password)
        except ImportError:
            raise Exception('NTLM Authentication requires requests_ntlm module.')

    def __call__(self, r):
        self.auth.__call__(r)
        return r


class MultipleAuth(requests.auth.AuthBase):
    """Authentication using multiple authentication methods."""
    def __init__(self, authentication_modes):
        self.authentication_modes = authentication_modes

    def __call__(self, r):
        for authentication_mode in self.authentication_modes:
            authentication_mode.__call__(r)
        return r


def add_service_custom_authentication(service_name, security_details):
    auth = get_detail('auth', security_details)
    if 'ntlm' == auth:
        custom_authentications[service_name] = NTLMAuth(security_details)
        return auth


def add_service_security(service_name, swagger, security_details):
    json_security_definitions = swagger.get('securityDefinitions', {})
    for security_definition_key in json_security_definitions.keys():
        security_definition = json_security_definitions[security_definition_key]
        add_service_security_definition(security_definition, service_name, security_details, security_definition_key)


def add_service_security_definition(security_definition, service_name, security_details, security_definition_key):
    if 'oauth2' == security_definition.get('type'):
        add_oauth2_security_definition(security_definition, service_name, security_details, security_definition_key)
    elif 'apiKey' == security_definition.get('type'):
        add_api_key_security_definition(security_definition, service_name, security_details, security_definition_key)
    elif 'basic' == security_definition.get('type'):
        add_basic_security_definition(security_definition, service_name, security_details, security_definition_key)
    else:
        logging.error('Unexpected security definition type: {0}'.format(security_definition))


def add_oauth2_security_definition(security_definition, service_name, security_details, security_definition_key):
    if security_definition.get('flow') == 'implicit':
        authentication_definition = OAuth2Auth(security_definition_key, security_definition, service_name, security_details)
        if authentication_definition.port not in oauth2_security_definitions_by_port:
            oauth2_security_definitions_by_port[authentication_definition.port] = []
        oauth2_security_definitions_by_port[authentication_definition.port].append(authentication_definition)
        security_definitions[service_name, security_definition_key] = authentication_definition
    else:
        # TODO Handle all OAuth2 flows
        logging.warning('OAuth2 flow is not supported: {0}'.format(security_definition))


def add_api_key_security_definition(security_definition, service_name, security_details, security_definition_key):
    security_definitions[service_name, security_definition_key] = ApiKeyAuth(security_definition, security_details)


def add_basic_security_definition(security_definition, service_name, security_details, security_definition_key):
    security_definitions[service_name, security_definition_key] = BasicAuth(security_details)


def start_servers():
    if oauth2_security_definitions_by_port:
        logging.debug('Generating OAuth 2 authentication responses servers.')
        for port in oauth2_security_definitions_by_port.keys():
            create_server_module(port)
        reload_server_modules()


def create_server_module(port):
    with open(os.path.join(os.path.dirname(__file__), 'oauth2_authentication_responses_server_{0}.py'.format(port)), 'w') as generated_file:
        renderer = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), trim_blocks=True)
        generated_file.write(
            renderer.get_template('oauth2_authentication_responses_server.jinja2').render(
                current_utc_time=datetime.datetime.utcnow().isoformat(),
                run_with_python_3=sys.version_info[0] == 3,
                security_definitions=oauth2_security_definitions_by_port[port],
                port=port
            )
        )


def reload_server_modules():
    with open(os.path.join(os.path.dirname(__file__), 'oauth2_authentication_responses_servers.py'), 'w') as generated_file:
        renderer = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), trim_blocks=True)
        generated_file.write(
            renderer.get_template('oauth2_authentication_responses_servers.jinja2').render(
                current_utc_time=datetime.datetime.utcnow().isoformat(),
                run_with_python_3=sys.version_info[0] == 3,
                ports=oauth2_security_definitions_by_port.keys()
            )
        )

    reload(import_module('oauth2_authentication_responses_servers'))
    import oauth2_authentication_responses_servers
    oauth2_authentication_responses_servers.start_servers()


def stop_servers():
    if oauth2_security_definitions_by_port:
        logging.debug('Stopping OAuth 2 authentication responses servers...')
        for port in oauth2_security_definitions_by_port.keys():
            # Shutdown authentication server thread if needed (in case module is reloaded)
            try:
                requests.post('http://localhost:{0}/shutdown'.format(port))
            except:
                pass


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

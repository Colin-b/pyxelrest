import logging
import os
import jinja2
import datetime
import sys
import requests
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


class OAuth2:
    """Describes an OAuth 2 security definition."""

    DEFAULT_OAUTH2_SERVER_PORT = 5000
    DEFAULT_OAUTH2_AUTHENTICATION_TIMEOUT = 20

    def __init__(self, security_definition_key, security_definition, service_name, security_details):
        port = get_detail('port', security_details)
        self.port = int(port) if port else OAuth2.DEFAULT_OAUTH2_SERVER_PORT
        self.key = service_name, security_definition_key
        self.service_name = service_name
        self.security_definition_key = security_definition_key
        self.redirect_uri = 'http://localhost:{0}/{1}/{2}'.format(self.port, service_name, security_definition_key)
        authorization_url = security_definition['authorizationUrl']
        self.full_url = OAuth2.create_auth_url(authorization_url, self.redirect_uri)
        self.token_name = OAuth2.get_query_parameter(authorization_url, 'response_type') or 'token'
        timeout = get_detail('timeout', security_details)
        self.timeout = int(timeout) if timeout else OAuth2.DEFAULT_OAUTH2_AUTHENTICATION_TIMEOUT

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


class ApiKey:
    """Describes an API Key security definition."""
    def __init__(self, security_definition, security_details):
        self.header_field_name = security_definition['name']
        self.api_key = get_detail('api_key', security_details)
        if not self.api_key:
            logging.warning('api_key is not defined. Calls requiring an API Key authentication might fail.')


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
        authentication_definition = OAuth2(security_definition_key, security_definition, service_name, security_details)
        if authentication_definition.port not in oauth2_security_definitions_by_port:
            oauth2_security_definitions_by_port[authentication_definition.port] = []
        oauth2_security_definitions_by_port[authentication_definition.port].append(authentication_definition)
        security_definitions[service_name, security_definition_key] = authentication_definition
    else:
        # TODO Handle all OAuth2 flows
        logging.warning('OAuth2 flow is not supported: {0}'.format(security_definition))


def add_api_key_security_definition(security_definition, service_name, security_details, security_definition_key):
    if security_definition.get('in') == 'header':
        security_definitions[service_name, security_definition_key] = ApiKey(security_definition, security_details)
    else:
        # TODO Handle all API Key destination
        logging.warning('API Key destination is not supported: {0}'.format(security_definition))


def add_basic_security_definition(security_definition, service_name, security_details, security_definition_key):
    # TODO Handle basic authentication
    logging.warning('Basic security definition is not supported: {0}'.format(security_definition))


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


def add_auth(service_name, securities, header):
    for security in securities:
        for security_definition_key in security.keys():
            security_definition = security_definitions.get((service_name, security_definition_key))
            if isinstance(security_definition, OAuth2):
                import oauth2_authentication_responses_servers
                server = oauth2_authentication_responses_servers.servers[security_definition.port]
                server.add_auth(security_definition, header)
                return
            if isinstance(security_definition, ApiKey):
                if security_definition.api_key:
                    header[security_definition.header_field_name] = security_definition.api_key
                return

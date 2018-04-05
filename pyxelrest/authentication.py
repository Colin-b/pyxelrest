import logging
import os
from requests_auth.authentication import NTLM, OAuth2, HeaderApiKey, QueryApiKey, Basic, Auths
from requests_auth.oauth2_tokens import JsonTokenFileCache

logger = logging.getLogger(__name__)
# Key is a tuple 'service name, security key'
security_definitions = {}
# Key is service name
custom_authentications = {}

oauth2_tokens_cache_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'tokens.json')
OAuth2.token_cache = JsonTokenFileCache(oauth2_tokens_cache_path)


def add_service_custom_authentication(service_name, service_config):
    ntlm_config = service_config.get('ntlm')
    if ntlm_config:
        custom_authentications[service_name] = NTLM(ntlm_config.get('username'), ntlm_config.get('password'))
        return 'ntlm'


def add_service_security(service_name, open_api_definition, service_config):
    json_security_definitions = open_api_definition.get('securityDefinitions', {})
    for security_definition_key in json_security_definitions.keys():
        security_definition = json_security_definitions[security_definition_key]
        try:
            authentication = _create_authentication(security_definition, service_config)
            if authentication:
                security_definitions[service_name, security_definition_key] = authentication
        except Exception as e:
            logger.error('Authentication cannot be handled ({}) for {}'.format(e, security_definition))


def _create_authentication(security_definition, service_config):
    if 'oauth2' == security_definition.get('type'):
        oauth2_config = dict(service_config.get('oauth2', {}))
        if security_definition.get('flow') == 'implicit':
            return OAuth2(authorization_url=security_definition['authorizationUrl'],
                          redirect_uri_port=oauth2_config.pop('port', None),
                          token_reception_timeout=oauth2_config.pop('timeout', None),
                          token_reception_success_display_time=oauth2_config.pop('success_display_time', None),
                          token_reception_failure_display_time=oauth2_config.pop('failure_display_time', None),
                          **oauth2_config)
        # TODO Handle all OAuth2 flows
        logger.warning('OAuth2 flow is not supported: {0}'.format(security_definition))
    elif 'apiKey' == security_definition.get('type'):
        if security_definition['in'] == 'query':
            return QueryApiKey(service_config.get('api_key'), security_definition['name'])
        return HeaderApiKey(service_config.get('api_key'), security_definition['name'])
    elif 'basic' == security_definition.get('type'):
        basic_config = service_config.get('basic', {})
        return Basic(basic_config.get('username'), basic_config.get('password'))
    else:
        logger.error('Unexpected security definition type: {0}'.format(security_definition))


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
            return Auths(authentication_modes)
        # Otherwise check if there is another security available

    # Default to custom authentication if no security is supported
    return custom_authentication

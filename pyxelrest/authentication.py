import logging
import os
from requests_auth.authentication import NTLM, OAuth2, HeaderApiKey, QueryApiKey, Basic, Auths
from requests_auth.oauth2_tokens import JsonTokenFileCache
import requests_auth.oauth2_authentication_responses_server as oauth2_authentication_responses_server

logger = logging.getLogger(__name__)
# Key is a tuple 'service name, security key'
security_definitions = {}
# Key is service name
custom_authentications = {}

oauth2_tokens_cache_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'tokens.json')
oauth2_authentication_responses_server.oauth2_tokens = JsonTokenFileCache(oauth2_tokens_cache_path)


def add_service_custom_authentication(service_name, security_details):
    auth = security_details.get('auth')
    if 'ntlm' == auth:
        custom_authentications[service_name] = NTLM(security_details.get('username'), security_details.get('password'))
        return auth


def add_service_security(service_name, swagger, security_details):
    json_security_definitions = swagger.get('securityDefinitions', {})
    for security_definition_key in json_security_definitions.keys():
        security_definition = json_security_definitions[security_definition_key]
        security_definition['security_definition_key'] = security_definition_key
        try:
            authentication = _create_authentication(security_definition, service_name, security_details)
            if authentication:
                security_definitions[service_name, security_definition_key] = authentication
        except Exception as e:
            logger.error('Authentication cannot be handled ({}) for {}'.format(e, security_definition))


def _create_authentication(security_definition, service_name, security_details):
    if 'oauth2' == security_definition.get('type'):
        if security_definition.get('flow') == 'implicit':
            additional_authorization_parameters = {
                security_detail_key[7:]: security_details[security_detail_key]
                for security_detail_key in security_details.keys() if security_detail_key.startswith('oauth2.')
            }
            return OAuth2(security_definition['authorizationUrl'],
                          key='service_{0}__security_definition_key_{1}'.format(service_name,
                                                                                security_definition['security_definition_key']),
                          additional_authorization_parameters=additional_authorization_parameters,
                          port=security_details.get('port'),
                          timeout=security_details.get('timeout'),
                          success_display_time=security_details.get('success_display_time'),
                          failure_display_time=security_details.get('failure_display_time'))
        # TODO Handle all OAuth2 flows
        logger.warning('OAuth2 flow is not supported: {0}'.format(security_definition))
    elif 'apiKey' == security_definition.get('type'):
        if security_definition['in'] == 'query':
            return QueryApiKey(security_details.get('api_key'), security_definition['name'])
        return HeaderApiKey(security_details.get('api_key'), security_definition['name'])
    elif 'basic' == security_definition.get('type'):
        return Basic(security_details.get('username'), security_details.get('password'))
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

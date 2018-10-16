import logging
import os
from requests_auth import NTLM, OAuth2, HeaderApiKey, QueryApiKey, Basic, Auths
from requests_auth.oauth2_tokens import JsonTokenFileCache

logger = logging.getLogger(__name__)

oauth2_tokens_cache_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'tokens.json')
OAuth2.token_cache = JsonTokenFileCache(oauth2_tokens_cache_path)


def _create_authentication(service_config, open_api_security_definition, request_content):
    if 'oauth2' == open_api_security_definition.get('type'):
        oauth2_config = dict(service_config.oauth2)
        if open_api_security_definition.get('flow') == 'implicit':
            return OAuth2(authorization_url=open_api_security_definition.get('authorizationUrl', request_content.extra_parameters.get('oauth2_auth_url')),
                          **oauth2_config)
        # TODO Handle all OAuth2 flows
        logger.warning('OAuth2 flow is not supported: {0}'.format(open_api_security_definition))
    elif 'apiKey' == open_api_security_definition.get('type'):
        if open_api_security_definition['in'] == 'query':
            return QueryApiKey(service_config.api_key, open_api_security_definition.get('name', request_content.extra_parameters.get('api_key_name')))
        return HeaderApiKey(service_config.api_key, open_api_security_definition.get('name', request_content.extra_parameters.get('api_key_name')))
    elif 'basic' == open_api_security_definition.get('type'):
        return Basic(service_config.basic.get('username'), service_config.basic.get('password'))
    else:
        logger.error('Unexpected security definition type: {0}'.format(open_api_security_definition))


def _create_authentication_from_config(service_config, authentication_mode, authentication):
    if 'oauth2' == authentication_mode:
        oauth2_config = dict(service_config.oauth2)
        return OAuth2(authorization_url=authentication.get('oauth2_auth_url'), **oauth2_config)
    elif 'api_key' == authentication_mode:
        if authentication.get('in') == 'query':
            return QueryApiKey(service_config.api_key, authentication.get('name'))
        return HeaderApiKey(service_config.api_key, authentication.get('name'))
    elif 'basic' == authentication_mode:
        return Basic(service_config.basic.get('username'), service_config.basic.get('password'))
    else:
        logger.error('Unexpected security definition type: {0}'.format(authentication_mode))


def get_auth(udf_method, request_content):
    if not udf_method.requires_authentication(request_content):
        return None

    security_definitions = udf_method.service.open_api_definition.get('securityDefinitions', {})

    securities = udf_method.security(request_content)
    ntlm_config = udf_method.service.config.ntlm_auth
    ntlm_authentication = NTLM(ntlm_config.get('username'), ntlm_config.get('password')) if ntlm_config else None

    # Run through all available securities
    for security in securities:
        authentication_modes = [ntlm_authentication] if ntlm_authentication else []
        for security_definition_key in security.keys():
            try:
                auth = _create_authentication(udf_method.service.config, security_definitions.get(security_definition_key, {}), request_content)
                if auth:
                    authentication_modes.append(auth)
            except:
                logger.exception('{0} authentication cannot be handled.'.format(security_definition_key))
        # A single authentication method is required and PyxelRest support it
        if len(authentication_modes) == 1:
            return authentication_modes[0]
        # Multiple authentication methods are required and PyxelRest support it
        if len(authentication_modes) > 1:
            return Auths(*authentication_modes)
        # Otherwise check if there is another security available

    # Default to custom authentication if no security is supported
    return ntlm_authentication


def get_definition_retrieval_auth(service_config):
    if not service_config.definition_retrieval_auths:
        return None

    ntlm_config = service_config.ntlm_auth if service_config.definition_retrieval_auths.pop('ntlm', None) else None
    ntlm_authentication = NTLM(ntlm_config.get('username'), ntlm_config.get('password')) if ntlm_config else None

    for authentication_mode, authentication in service_config.definition_retrieval_auths.items():
        authentication_modes = [ntlm_authentication] if ntlm_authentication else []
        try:
            auth = _create_authentication_from_config(service_config, authentication_mode, authentication)
            if auth:
                authentication_modes.append(auth)
        except:
            logger.exception('{0} authentication cannot be handled.'.format(authentication_mode))
        # A single authentication method is required and PyxelRest support it
        if len(authentication_modes) == 1:
            return authentication_modes[0]
        # Multiple authentication methods are required and PyxelRest support it
        if len(authentication_modes) > 1:
            return Auths(*authentication_modes)
        # Otherwise check if there is another security available

    # Default to custom authentication if no security is supported
    return ntlm_authentication

import logging
import os
from typing import Optional

import requests.auth
from requests_auth import (
    NTLM,
    OAuth2Implicit,
    OAuth2AuthorizationCode,
    OAuth2ClientCredentials,
    OAuth2ResourceOwnerPasswordCredentials,
    HeaderApiKey,
    QueryApiKey,
    Basic,
    OAuth2,
)
from requests_auth.oauth2_tokens import JsonTokenFileCache

logger = logging.getLogger(__name__)

oauth2_tokens_cache_path = os.path.join(
    os.getenv("APPDATA"), "pyxelrest", "configuration", "tokens.json"
)
OAuth2.token_cache = JsonTokenFileCache(oauth2_tokens_cache_path)


def _create_authentication(
    service_config: "pyxelrest.open_api.ServiceConfigSection",
    open_api_security_definition: dict,
    request_content: "pyxelrest.open_api.RequestContent",
):
    if "oauth2" == open_api_security_definition.get("type"):
        flow = open_api_security_definition.get("flow")
        oauth2_config = dict(service_config.oauth2)
        if flow == "implicit":
            return OAuth2Implicit(
                authorization_url=open_api_security_definition.get(
                    "authorizationUrl",
                    request_content.extra_parameters.get("oauth2_auth_url"),
                ),
                **oauth2_config,
            )
        elif flow == "accessCode":
            return OAuth2AuthorizationCode(
                authorization_url=open_api_security_definition.get(
                    "authorizationUrl",
                    request_content.extra_parameters.get("oauth2_auth_url"),
                ),
                token_url=open_api_security_definition.get(
                    "tokenUrl", request_content.extra_parameters.get("oauth2_token_url")
                ),
                **oauth2_config,
            )
        elif flow == "password":
            return OAuth2ResourceOwnerPasswordCredentials(
                token_url=open_api_security_definition.get(
                    "tokenUrl", request_content.extra_parameters.get("oauth2_token_url")
                ),
                **oauth2_config,
            )
        elif flow == "application":
            return OAuth2ClientCredentials(
                token_url=open_api_security_definition.get(
                    "tokenUrl", request_content.extra_parameters.get("oauth2_token_url")
                ),
                **oauth2_config,
            )
        logger.warning(f"Unexpected OAuth2 flow: {open_api_security_definition}")
    elif "apiKey" == open_api_security_definition.get("type"):
        if open_api_security_definition["in"] == "query":
            return QueryApiKey(
                service_config.api_key,
                open_api_security_definition.get(
                    "name", request_content.extra_parameters.get("api_key_name")
                ),
            )
        return HeaderApiKey(
            service_config.api_key,
            open_api_security_definition.get(
                "name", request_content.extra_parameters.get("api_key_name")
            ),
        )
    elif "basic" == open_api_security_definition.get("type"):
        return Basic(
            service_config.basic.get("username"), service_config.basic.get("password")
        )
    else:
        logger.error(
            f"Unexpected security definition type: {open_api_security_definition}"
        )


def _create_authentication_from_config(
    service_config: "pyxelrest.open_api.ServiceConfigSection",
    authentication_mode: str,
    authentication: dict,
):
    if "oauth2_implicit" == authentication_mode:
        oauth2_config = dict(service_config.oauth2)
        return OAuth2Implicit(
            authorization_url=authentication.get("oauth2_auth_url"), **oauth2_config
        )
    elif "oauth2_access_code" == authentication_mode:
        oauth2_config = dict(service_config.oauth2)
        return OAuth2AuthorizationCode(
            authorization_url=authentication.get("oauth2_auth_url"),
            token_url=authentication.get("oauth2_token_url"),
            **oauth2_config,
        )
    elif "oauth2_password" == authentication_mode:
        oauth2_config = dict(service_config.oauth2)
        return OAuth2ResourceOwnerPasswordCredentials(
            token_url=authentication.get("oauth2_token_url"), **oauth2_config
        )
    elif "oauth2_application" == authentication_mode:
        oauth2_config = dict(service_config.oauth2)
        return OAuth2ClientCredentials(
            token_url=authentication.get("oauth2_token_url"), **oauth2_config
        )
    elif "api_key" == authentication_mode:
        if authentication.get("in") == "query":
            return QueryApiKey(service_config.api_key, authentication.get("name"))
        return HeaderApiKey(service_config.api_key, authentication.get("name"))
    elif "basic" == authentication_mode:
        return Basic(
            service_config.basic.get("username"), service_config.basic.get("password")
        )
    else:
        logger.error(f"Unexpected security definition type: {authentication_mode}")


def get_auth(
    udf_method: "pyxelrest.open_api.UDFMethod",
    request_content: "pyxelrest.open_api.RequestContent",
) -> Optional[requests.auth.AuthBase]:
    if not udf_method.requires_authentication(request_content):
        return None

    security_definitions = udf_method.service.open_api_definition.get(
        "securityDefinitions", {}
    )

    securities = udf_method.security(request_content)
    ntlm_config = udf_method.service.config.ntlm_auth
    authentication = (
        NTLM(ntlm_config.get("username"), ntlm_config.get("password"))
        if ntlm_config
        else None
    )

    # Run through all available securities
    for security in securities:
        for security_definition_key in security.keys():
            try:
                auth = _create_authentication(
                    udf_method.service.config,
                    security_definitions.get(security_definition_key, {}),
                    request_content,
                )
                if auth:
                    if authentication:
                        authentication += auth
                    else:
                        authentication = auth
            except:
                logger.exception(
                    f"{security_definition_key} authentication cannot be handled."
                )
        # If a supported authentication is found, return it
        if authentication:
            return authentication
        # Otherwise check if there is another security available

    # Default to custom authentication if no security is supported
    return authentication


def get_definition_retrieval_auth(
    service_config: "pyxelrest.open_api.ServiceConfigSection",
) -> Optional[requests.auth.AuthBase]:
    if not service_config.definition_retrieval_auths:
        return None

    ntlm_config = (
        service_config.ntlm_auth
        if service_config.definition_retrieval_auths.pop("ntlm", None)
        else None
    )
    authentication = (
        NTLM(ntlm_config.get("username"), ntlm_config.get("password"))
        if ntlm_config
        else None
    )

    for (
        authentication_mode,
        authentication_config,
    ) in service_config.definition_retrieval_auths.items():
        try:
            auth = _create_authentication_from_config(
                service_config, authentication_mode, authentication_config
            )
            if auth:
                if authentication:
                    authentication += auth
                else:
                    authentication = auth
        except:
            logger.exception(
                "{0} authentication cannot be handled.".format(authentication_mode)
            )
        # If a supported authentication is found, return it
        if authentication:
            return authentication
        # Otherwise check if there is another security available

    # Default to custom authentication if no security is supported
    return authentication
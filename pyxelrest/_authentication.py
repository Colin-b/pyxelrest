import logging

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

from pyxelrest._generator_config import TOKEN_CACHE_FILE_PATH

if TOKEN_CACHE_FILE_PATH:
    OAuth2.token_cache = JsonTokenFileCache(TOKEN_CACHE_FILE_PATH)

logger = logging.getLogger(__name__)


def _create_authentication(
    service: "pyxelrest._common.Service",
    open_api_security_definition: dict,
):
    service_config = service.config.auth
    if "oauth2" == open_api_security_definition.get("type"):
        flow = open_api_security_definition.get("flow")
        oauth2_config = dict(service_config.get("oauth2", {}))
        if flow == "implicit":
            authorization_url = open_api_security_definition["authorizationUrl"]
            # Handle relative authentication URI
            if authorization_url.startswith("/"):
                authorization_url = f"{service.uri}{authorization_url}"

            return OAuth2Implicit(authorization_url=authorization_url, **oauth2_config)
        elif flow == "accessCode":
            authorization_url = open_api_security_definition["authorizationUrl"]
            # Handle relative authentication URI
            if authorization_url.startswith("/"):
                authorization_url = f"{service.uri}{authorization_url}"

            token_url = open_api_security_definition["tokenUrl"]
            # Handle relative authentication URI
            if token_url.startswith("/"):
                token_url = f"{service.uri}{token_url}"

            return OAuth2AuthorizationCode(
                authorization_url=authorization_url,
                token_url=token_url,
                **oauth2_config,
            )
        elif flow == "password":
            token_url = open_api_security_definition["tokenUrl"]
            # Handle relative authentication URI
            if token_url.startswith("/"):
                token_url = f"{service.uri}{token_url}"

            return OAuth2ResourceOwnerPasswordCredentials(
                token_url=token_url, **oauth2_config
            )
        elif flow == "application":
            token_url = open_api_security_definition["tokenUrl"]
            # Handle relative authentication URI
            if token_url.startswith("/"):
                token_url = f"{service.uri}{token_url}"

            return OAuth2ClientCredentials(token_url=token_url, **oauth2_config)
        raise Exception(f"Unexpected OAuth2 flow: {open_api_security_definition}")
    elif "apiKey" == open_api_security_definition.get("type"):
        if open_api_security_definition["in"] == "query":
            return QueryApiKey(
                service_config.get("api_key"),
                open_api_security_definition["name"],
            )
        return HeaderApiKey(
            service_config.get("api_key"),
            open_api_security_definition["name"],
        )
    elif "basic" == open_api_security_definition.get("type"):
        return Basic(
            service_config.get("basic", {}).get("username"),
            service_config.get("basic", {}).get("password"),
        )
    raise Exception(
        f"Unexpected security definition type: {open_api_security_definition}"
    )


def _create_authentication_from_config(
    service_config: dict, authentication_mode: str, authentication: dict
):
    if "oauth2" == authentication_mode:
        oauth2_config = dict(service_config.get("oauth2", {}))
        for flow, authentication in authentication.items():
            if "implicit" == flow:
                return OAuth2Implicit(
                    authorization_url=authentication.get("authorization_url"),
                    **oauth2_config,
                )
            elif "access_code" == flow:
                return OAuth2AuthorizationCode(
                    authorization_url=authentication.get("authorization_url"),
                    token_url=authentication.get("token_url"),
                    **oauth2_config,
                )
            elif "password" == flow:
                return OAuth2ResourceOwnerPasswordCredentials(
                    token_url=authentication.get("token_url"), **oauth2_config
                )
            elif "application" == flow:
                return OAuth2ClientCredentials(
                    token_url=authentication.get("token_url"), **oauth2_config
                )
            raise Exception(f"Unexpected OAuth2 flow: {flow}")
    elif "api_key" == authentication_mode:
        if "query_parameter_name" in authentication:
            return QueryApiKey(
                service_config.get("api_key"), authentication["query_parameter_name"]
            )
        return HeaderApiKey(
            service_config.get("api_key"), authentication.get("header_name")
        )
    elif "basic" == authentication_mode:
        return Basic(
            service_config.get("basic", {}).get("username"),
            service_config.get("basic", {}).get("password"),
        )

    raise Exception(f"Unexpected security definition type: {authentication_mode}")


def get_auth(
    udf_method: "pyxelrest.open_api.UDFMethod",
    request_content: "pyxelrest.open_api.RequestContent",
) -> requests.auth.AuthBase | None:
    if not udf_method.requires_authentication(request_content):
        return None

    securities = udf_method.security(request_content)
    ntlm_config = udf_method.service.config.auth.get("ntlm", {})
    authentication = (
        NTLM(ntlm_config.get("username"), ntlm_config.get("password"))
        if ntlm_config
        else None
    )

    security_definitions = udf_method.service.open_api_definition.get(
        "securityDefinitions", {}
    )

    # Run through all available securities
    for security in securities:
        for security_definition_key in security.keys():
            try:
                auth = _create_authentication(
                    udf_method.service,
                    security_definitions.get(security_definition_key, {}),
                )
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
    service_config: "pyxelrest.open_api.RESTAPIConfigSection",
) -> requests.auth.AuthBase | None:
    if not service_config.definition_retrieval_auths:
        return None

    ntlm_config = (
        service_config.auth.get("ntlm", {})
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
                service_config.auth, authentication_mode, authentication_config
            )
            if authentication:
                authentication += auth
            else:
                authentication = auth
        except:
            logger.exception(f"{authentication_mode} authentication cannot be handled.")

    return authentication

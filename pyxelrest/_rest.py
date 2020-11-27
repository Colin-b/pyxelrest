import datetime
from typing import Any, List, Union

from pyxelrest._common import (
    ConfigSection,
    UDFMethod,
    UDFParameter,
    RequestContent,
    Service,
    list_to_dict,
    list_to_dict_list,
)
from pyxelrest._fast_deserializer import Flattenizer


class PyxelRestConfigSection(ConfigSection):
    def __init__(self, service_name: str, service_config: dict):
        """
        Load service information from configuration.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param service_config: Dictionary containing service details.
        """
        ConfigSection.__init__(self, service_name, service_config)
        self.rely_on_definitions = False


class ParseBodyAsParameter(UDFParameter):
    def __init__(self):
        UDFParameter.__init__(
            self, "parse_body_as", "parse_body_as", "", False, "string"
        )
        self.choices = ["dict", "dict_list"]
        self.description = f"How the body should be sent ({self.choices})."

    def _convert_to_str(self, value: Any) -> str:
        if isinstance(value, datetime.date):
            raise Exception(f'{self.name} value "{value}" must be formatted as text.')
        if isinstance(value, int) or isinstance(value, float):
            value = str(value)
        if value and value not in self.choices:
            raise Exception(
                f'{self.name} value "{value}" should be {" or ".join(self.choices)}.'
            )
        return value

    def validate_optional(self, value: Any, request_content: RequestContent):
        if value is not None:
            value = self._convert_to_str(value)
        request_content.add_value(self, value)


class WaitForStatusParameter(UDFParameter):
    def __init__(self):
        UDFParameter.__init__(
            self, "wait_for_status", "wait_for_status", "", False, "integer"
        )
        self.description = (
            "HTTP status code to wait for before returning response. "
            "303 means that result is now provided in another URL."
        )

    def _convert_to_int(self, value: Any) -> int:
        if not isinstance(value, int):
            raise Exception(f'{self.name} value "{value}" must be an integer.')
        if value < 0:
            raise Exception(
                f'{self.name} value "{value}" must be superior or equals to 0.'
            )
        return value

    def validate_optional(self, value: Any, request_content: RequestContent):
        if value is not None:
            value = self._convert_to_int(value)
        request_content.add_value(self, value)


class CheckIntervalParameter(UDFParameter):
    def __init__(self):
        UDFParameter.__init__(
            self, "check_interval", "check_interval", "", False, "integer"
        )
        self.description = "Number of seconds to wait before sending a new request. Wait for 30 seconds by default."

    def _convert_to_int(self, value: Any):
        if not isinstance(value, int):
            raise Exception(f'{self.name} value "{value}" must be an integer.')
        if value < 0:
            raise Exception(
                f'{self.name} value "{value}" must be superior or equals to 0.'
            )
        return value

    def validate_optional(self, value: Any, request_content: RequestContent):
        if value is not None:
            value = self._convert_to_int(value)
        else:
            value = 30
        request_content.add_value(self, value)


class UrlParameter(UDFParameter):
    def __init__(self):
        UDFParameter.__init__(self, "url", "url", "path", True, "string")
        self.description = "URL to query."

    def _convert_to_str(self, value: Any) -> str:
        if isinstance(value, datetime.date):
            raise Exception(f'{self.name} value "{value}" must be formatted as text.')
        if isinstance(value, int) or isinstance(value, float):
            value = str(value)
        return value

    def validate_optional(self, value: Any, request_content: RequestContent):
        if value is not None:
            value = self._convert_to_str(value)
        request_content.add_value(self, value)


class BodyParameter(UDFParameter):
    def __init__(self):
        UDFParameter.__init__(self, "body", "body", "body", True, "object")
        self.description = "Content of the body."

    def validate_optional(self, value: Any, request_content: RequestContent):
        self.received_value = (
            value  # Save value as is to serialize it properly afterwards
        )

    def validate(self, request_content: RequestContent):
        request_content.payload = BodyParameter.list_as_json(
            self.received_value, request_content.extra_parameters.get("parse_body_as")
        )

    @staticmethod
    def list_as_json(lists: list, parse_as: str) -> Union[list, dict]:
        if "dict" == parse_as:
            if len(lists) != 2:
                return ["There should be only two rows. Header and values."]
            return list_to_dict(lists[0], lists[1])

        if "dict_list" == parse_as:
            if len(lists) < 2:
                return [
                    "There should be at least two rows. Header and first dictionary values."
                ]
            return list_to_dict_list(lists[0], lists[1:])

        return lists


class ExtraHeadersParameter(UDFParameter):
    def __init__(self):
        UDFParameter.__init__(
            self, "extra_headers", "extra_headers", "headers", False, "object"
        )
        self.description = "Extra headers to send in the query."

    def validate_optional(self, value: Any, request_content: RequestContent):
        self.received_value = value  # TODO Validate dict

    def validate(self, request_content: RequestContent):
        if self.received_value:
            request_content.header.update(self.received_value)


class AuthenticationParameter(UDFParameter):
    def __init__(self):
        UDFParameter.__init__(self, "auth", "auth", "", False, "array")
        self.choices = ["oauth2_implicit", "api_key_header", "api_key_query", "basic"]
        self.description = f"Authentication methods to use. ({self.choices})"

    def _convert_to_str(self, value: Any) -> str:
        if value and value not in self.choices:
            raise Exception(
                f'{self.name} value "{value}" should be {" or ".join(self.choices)}.'
            )
        return value

    def _convert_to_array(self, value: Any) -> List[str]:
        if isinstance(value, list):
            return [self._convert_to_str(item) for item in value if item is not None]
        return [self._convert_to_str(value)]

    def validate_optional(self, value, request_content: RequestContent):
        if value is not None:
            value = self._convert_to_array(value)
        request_content.add_value(self, value)


class OAuth2AuthorizationUrlParameter(UDFParameter):
    def __init__(self):
        UDFParameter.__init__(
            self, "oauth2_auth_url", "oauth2_auth_url", "", False, "string"
        )
        self.description = "OAuth2 authorization URL."

    def _convert_to_str(self, value: Any) -> str:
        if isinstance(value, datetime.date):
            raise Exception(f'{self.name} value "{value}" must be formatted as text.')
        if isinstance(value, int) or isinstance(value, float):
            value = str(value)
        return value

    def validate_optional(self, value: Any, request_content: RequestContent):
        if value is not None:
            value = self._convert_to_str(value)
        request_content.add_value(self, value)


class OAuth2TokenUrlParameter(UDFParameter):
    def __init__(self):
        UDFParameter.__init__(
            self, "oauth2_token_url", "oauth2_token_url", "", False, "string"
        )
        self.description = "OAuth2 token URL."

    def _convert_to_str(self, value: Any) -> str:
        if isinstance(value, datetime.date):
            raise Exception(f'{self.name} value "{value}" must be formatted as text.')
        if isinstance(value, int) or isinstance(value, float):
            value = str(value)
        return value

    def validate_optional(self, value: Any, request_content: RequestContent):
        if value is not None:
            value = self._convert_to_str(value)
        request_content.add_value(self, value)


class ApiKeyNameParameter(UDFParameter):
    def __init__(self):
        UDFParameter.__init__(self, "api_key_name", "api_key_name", "", False, "string")
        self.description = "Name of the field containing API key."

    def _convert_to_str(self, value: Any) -> str:
        if isinstance(value, datetime.date):
            raise Exception(f'{self.name} value "{value}" must be formatted as text.')
        if isinstance(value, int) or isinstance(value, float):
            value = str(value)
        return value

    def validate_optional(self, value: Any, request_content: RequestContent):
        if value is not None:
            value = self._convert_to_str(value)
        request_content.add_value(self, value)


class PyxelRestUDFMethod(UDFMethod):
    def __init__(
        self,
        service: "PyxelRestService",
        http_method: str,
        formula_type: str,
        formula_options: dict,
    ):
        udf_name = f"{service.config.udf_prefix(formula_options)}_{http_method}_url"
        UDFMethod.__init__(
            self,
            service=service,
            http_method=http_method,
            path="{url}",
            formula_type=formula_type,
            formula_options=formula_options,
            udf_name=udf_name,
        )

    def _create_udf_parameters(self) -> List[UDFParameter]:
        parameters = [
            UrlParameter(),
            ExtraHeadersParameter(),
            WaitForStatusParameter(),
            CheckIntervalParameter(),
            AuthenticationParameter(),
            OAuth2AuthorizationUrlParameter(),
            OAuth2TokenUrlParameter(),
            ApiKeyNameParameter(),
        ]

        if self.requests_method in ["post", "put"]:
            parameters.append(BodyParameter())
            parameters.append(ParseBodyAsParameter())

        return parameters

    def summary(self) -> str:
        return f"Send a HTTP {self.requests_method} request to specified URL."

    def return_a_list(self) -> bool:
        return True

    def security(self, request_content: RequestContent) -> List[dict]:
        auths = request_content.extra_parameters.get("auth")
        return [{auth: "" for auth in auths}] if auths else []

    def json_to_list(self, status_code: int, json_data: Any) -> list:
        return Flattenizer({}, status_code, {}).to_list(json_data)


class PyxelRestService(Service):
    def __init__(self, service_name: str, service_config: dict):
        """
        Load service information from configuration.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param service_config: Dictionary containing service details.
        """
        self.methods = {}
        config = PyxelRestConfigSection(service_name, service_config)
        self.open_api_definition = {
            "securityDefinitions": {
                "oauth2_implicit": {"type": "oauth2", "flow": "implicit"},
                "api_key_header": {"type": "apiKey", "in": "header"},
                "api_key_query": {"type": "apiKey", "in": "query"},
                "basic": {"type": "basic"},
            }
        }
        Service.__init__(self, config, "")

    def create_method(
        self, http_method: str, formula_type: str, formula_options: dict
    ) -> PyxelRestUDFMethod:
        udf = PyxelRestUDFMethod(self, http_method, formula_type, formula_options)
        self.methods[udf.udf_name] = udf
        return udf

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
from pyxelrest._json_deserializer import Flattenizer


class ParseBodyAsParameter(UDFParameter):
    def __init__(self):
        UDFParameter.__init__(
            self,
            name="parse_body_as",
            server_param_name="parse_body_as",
            location="",
            required=False,
            field_type="string",
        )
        self.choices = ["dict", "dict_list"]
        self.description = f"How the body should be sent ({self.choices})."

    def _convert_to_str(self, value: Any) -> str:
        # No need to convert value as it's impossible to get a valid value if not a string anyway
        if value not in self.choices:
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
            self,
            name="wait_for_status",
            server_param_name="wait_for_status",
            location="",
            required=False,
            field_type="integer",
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
            self,
            name="check_interval",
            server_param_name="check_interval",
            location="",
            required=False,
            field_type="integer",
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
        UDFParameter.__init__(
            self,
            name="url",
            server_param_name="url",
            location="path",
            required=True,
            field_type="string",
        )
        self.description = "URL to query."

    def _convert_to_str(self, value: Any) -> str:
        if not isinstance(value, str):
            raise Exception(f'{self.name} value "{value}" must be formatted as text.')
        return value

    def validate_optional(self, value: Any, request_content: RequestContent):
        if value is not None:
            value = self._convert_to_str(value)
        request_content.add_value(self, value)


class BodyParameter(UDFParameter):
    def __init__(self):
        UDFParameter.__init__(
            self,
            name="body",
            server_param_name="body",
            location="body",
            required=True,
            field_type="object",
        )
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
                raise Exception("There should be only two rows. Header and values.")
            return list_to_dict(lists[0], lists[1])

        if "dict_list" == parse_as:
            if len(lists) < 2:
                raise Exception(
                    "There should be at least two rows. Header and first dictionary values."
                )
            return list_to_dict_list(lists[0], lists[1:])

        return lists


class ExtraHeadersParameter(UDFParameter):
    def __init__(self):
        UDFParameter.__init__(
            self,
            name="extra_headers",
            server_param_name="extra_headers",
            location="headers",
            required=False,
            field_type="object",
        )
        self.description = "Extra headers to send in the query."

    def validate_optional(self, value: Any, request_content: RequestContent):
        self.received_value = value  # TODO Validate dict

    def validate(self, request_content: RequestContent):
        if self.received_value:
            request_content.header.update(self.received_value)


class SecurityDefinitionsParameter(UDFParameter):
    def __init__(self):
        UDFParameter.__init__(
            self,
            name="security_definitions",
            server_param_name="security_definitions",
            location="",
            required=False,
            field_type="array",
        )
        self.description = f"Authentication mechanisms to use."

    def _convert_to_array(self, value: Any) -> List[dict]:
        if not isinstance(value, list):
            raise Exception(
                f'{self.name} value "{value}" ({type(value)} type) must be a list.'
            )
        if len(value) < 2:
            raise Exception(
                f"{self.name} value should contains at least two rows. Header and values."
            )

        return list_to_dict_list(value[0], value[1:])

    def validate_optional(self, value, request_content: RequestContent):
        if value is not None:
            value = self._convert_to_array(value)
        request_content.add_value(self, value)


class PyxelRestUDFMethod(UDFMethod):
    def __init__(
        self,
        service: "PyxelRest",
        http_method: str,
        formula_type: str,
        formula_options: dict,
    ):
        udf_name = f"{service.config.udf_prefix(formula_options)}{http_method}_url"
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
            SecurityDefinitionsParameter(),
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
        security_definitions = request_content.extra_parameters.get(
            "security_definitions"
        )
        if not security_definitions:
            return []

        # Create a fake securityDefinition matching provided auths
        self.service.open_api_definition["securityDefinitions"] = {
            str(index): security_definition
            for index, security_definition in enumerate(security_definitions)
        }
        return [{str(index): "" for index in range(len(security_definitions))}]

    def json_to_list(self, status_code: int, json_data: Any) -> list:
        return Flattenizer({}, status_code, {}).to_list(json_data)


class PyxelRest(Service):
    def __init__(self, settings: dict):
        """
        Load service information from configuration.
        :param settings: Section configuration settings.
        """
        self.methods = {}
        config = ConfigSection("pyxelrest", settings)
        self.open_api_definition = {}
        Service.__init__(self, config, "")

    def create_method(
        self, http_method: str, formula_type: str, formula_options: dict
    ) -> PyxelRestUDFMethod:
        udf = PyxelRestUDFMethod(self, http_method, formula_type, formula_options)
        self.methods[udf.udf_name] = udf
        return udf

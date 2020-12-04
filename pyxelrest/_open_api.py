import datetime
import logging
import os
import re
from typing import List, Union, Optional, Any, Dict
from urllib.parse import urlsplit

from pyxelrest import _authentication, _session, _vba, _definition_deserializer
from pyxelrest._common import (
    ConfigSection,
    UDFMethod,
    UDFParameter,
    RequestContent,
    list_to_dict,
    list_to_dict_list,
    Service,
)
from pyxelrest._definition_deserializer import Response
from pyxelrest._exceptions import (
    MandatoryPropertyNotProvided,
    DuplicatedParameters,
    OpenAPIVersionNotProvided,
    UnsupportedOpenAPIVersion,
    EmptyResponses,
    InvalidOpenAPIDefinition,
)
from pyxelrest._fast_deserializer import Flattenizer

logger = logging.getLogger(__name__)


def to_valid_regex(user_friendly_regex: str) -> str:
    if "*" in user_friendly_regex and ".*" not in user_friendly_regex:
        return f'^{user_friendly_regex.replace("*", ".*")}$'
    return f"^{user_friendly_regex}$"


def to_vba_valid_name(open_api_name: str) -> str:
    """
    Return name as non VBA or python restricted keyword
    """
    # replace vba restricted keywords
    if open_api_name.lower() in _vba.vba_restricted_keywords:
        open_api_name = _vba.vba_restricted_keywords[open_api_name.lower()]
    # replace forbidden VBA or Python characters (carets, dots and leading underscores)
    return open_api_name.replace("-", "_").replace(".", "_").lstrip("_")


def return_type_can_be_handled(method_produces: List[str]) -> bool:
    return "application/octet-stream" not in method_produces


class ServiceConfigSection(ConfigSection):
    def __init__(self, service_name: str, service_config: dict):
        """
        Load service information from configuration.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param service_config: Dictionary containing service details.
        """
        ConfigSection.__init__(self, service_name, service_config)
        open_api = service_config.get("open_api")
        if not open_api:
            raise MandatoryPropertyNotProvided(service_name, "open_api")

        self.open_api_definition = open_api.get("definition")
        if not self.open_api_definition:
            raise MandatoryPropertyNotProvided(service_name, "open_api/definition")

        self.definition_read_timeout = open_api.get("definition_read_timeout", 5)
        self.rely_on_definitions = open_api.get("rely_on_definitions")
        self.selected_methods = open_api.get(
            "selected_methods",
            ["get", "post", "put", "delete", "patch", "options", "head"],
        )
        self.selected_tags = open_api.get("selected_tags", [])
        self.excluded_tags = open_api.get("excluded_tags", [])
        self.excluded_operation_ids = open_api.get("excluded_operation_ids", [])
        self.selected_operation_ids = open_api.get("selected_operation_ids", [])
        self.excluded_parameters = open_api.get("excluded_parameters", [])
        self.selected_parameters = open_api.get("selected_parameters", [])
        self.definition_retrieval_auths = open_api.get("definition_retrieval_auths", {})

    def _allow_tags(self, method_tags: Optional[List[str]]) -> bool:
        if not method_tags:
            return True

        # Search excluded first
        if self.excluded_tags:
            for method_tag in method_tags:
                if method_tag in self.excluded_tags:
                    return False

        if self.selected_tags:
            for method_tag in method_tags:
                if method_tag in self.selected_tags:
                    return True
            return False

        return True

    def _allow_operation_id(self, method_operation_id: Optional[str]) -> bool:
        if not method_operation_id:
            return True

        if self.excluded_operation_ids:
            for excluded_operation_id in self.excluded_operation_ids:
                try:
                    if re.match(
                        to_valid_regex(excluded_operation_id), method_operation_id
                    ):
                        return False
                except:  # Handle non regex values
                    pass

        if self.selected_operation_ids:
            for selected_operation_id in self.selected_operation_ids:
                try:
                    if re.match(
                        to_valid_regex(selected_operation_id), method_operation_id
                    ):
                        return True
                except:  # Handle non regex values
                    pass
            return False

        return True

    def allow_parameter(self, parameter_name: str) -> bool:
        if self.excluded_parameters:
            for excluded_parameter in self.excluded_parameters:
                try:
                    if re.match(to_valid_regex(excluded_parameter), parameter_name):
                        return False
                except:  # Handle non regex values
                    pass

        if self.selected_parameters:
            for selected_parameter in self.selected_parameters:
                try:
                    if re.match(to_valid_regex(selected_parameter), parameter_name):
                        return True
                except:  # Handle non regex values
                    pass
            return False

        return True

    def should_provide_method(self, http_verb: str, open_api_method: dict) -> bool:
        if http_verb not in self.selected_methods:
            return False
        return (
            self._allow_tags(open_api_method.get("tags"))
            and self._allow_operation_id(open_api_method.get("operationId"))
            and return_type_can_be_handled(open_api_method.get("produces", []))
        )


class APIUDFParameter(UDFParameter):
    def __init__(self, open_api_parameter: dict, schema: dict):
        UDFParameter.__init__(
            self,
            open_api_parameter["name"],
            open_api_parameter["server_param_name"],
            # path, body, formData, query, header
            open_api_parameter["in"],
            open_api_parameter.get("required"),
            # file (formData location), integer, number, string, boolean, array
            open_api_parameter.get("type"),
        )
        self.schema = schema
        # Apply to integer, number, string
        self.choices = open_api_parameter.get("enum")
        self.default_value = open_api_parameter.get("default")
        # date (string type), date-time (string type)
        self.format = open_api_parameter.get("format")
        self.maximum = open_api_parameter.get("maximum")  # Apply to integer and number
        # Apply to integer and number
        self.exclusive_maximum = open_api_parameter.get("exclusiveMaximum")
        self.minimum = open_api_parameter.get("minimum")  # Apply to integer and number
        # Apply to integer and number
        self.exclusive_minimum = open_api_parameter.get("exclusiveMinimum")
        self.max_length = open_api_parameter.get("maxLength")  # Apply to string
        self.min_length = open_api_parameter.get("minLength")  # Apply to string
        self.max_items = open_api_parameter.get("maxItems")  # Apply to array
        self.min_items = open_api_parameter.get("minItems")  # Apply to array
        self.unique_items = open_api_parameter.get("uniqueItems")  # Apply to array
        # Apply to integer and number
        self.multiple_of = open_api_parameter.get("multipleOf")
        # Apply to arrays
        self.collection_format = open_api_parameter.get("collectionFormat")

        open_api_array_parameter = self._get_open_api_array_parameter(
            open_api_parameter
        )
        if open_api_array_parameter:
            if open_api_array_parameter.get("type") == "object" or (
                "$ref" in open_api_array_parameter
            ):
                self.array_parameter = None
                self._convert_to_type = self._convert_to_dict_list
                self.description = self._get_dict_list_documentation(open_api_parameter)
            else:
                self.array_parameter = APIUDFParameter(open_api_array_parameter, {})
                self.array_dimension = 1 + self.array_parameter.array_dimension
                self._convert_to_type = self._convert_to_array
                self.description = self._get_list_documentation(open_api_parameter)
        else:
            self.array_parameter = None
            self._convert_to_type = self._get_convert_method()
            self.description = self._get_documentation(open_api_parameter)

    def validate_optional(self, value: Any, request_content: RequestContent):
        if value is not None:
            value = self._convert_to_type(value)
        request_content.add_value(self, value)

    def _get_open_api_array_parameter(self, open_api_parameter: dict) -> Optional[dict]:
        if self.type == "array":
            open_api_array_parameter = dict(open_api_parameter)
            open_api_array_parameter.update(open_api_parameter["items"])
            return open_api_array_parameter
        elif self.schema.get("type") == "array":
            open_api_array_parameter = dict(open_api_parameter)
            self.collection_format = self.schema.get("collectionFormat")
            return open_api_array_parameter

    def _convert_to_int(self, value: Any) -> int:
        if not isinstance(value, int):
            raise Exception(
                f'{self.name} value "{value}" ({type(value)} type) must be an integer.'
            )
        self._check_number(value)
        return value

    def _convert_to_float(self, value: Any) -> float:
        if not isinstance(value, float):
            raise Exception(
                f'{self.name} value "{value}" ({type(value)} type) must be a number.'
            )
        self._check_number(value)
        return value

    def _check_number(self, value: Union[int, float]):
        if self.maximum is not None:
            if self.exclusive_maximum:
                if value >= self.maximum:
                    raise Exception(
                        f'{self.name} value "{value}" must be strictly inferior to {self.maximum}.'
                    )
            else:
                if value > self.maximum:
                    raise Exception(
                        f'{self.name} value "{value}" must be inferior or equals to {self.maximum}.'
                    )

        if self.minimum is not None:
            if self.exclusive_minimum:
                if value <= self.minimum:
                    raise Exception(
                        f'{self.name} value "{value}" must be strictly superior to {self.minimum}.'
                    )
            else:
                if value < self.minimum:
                    raise Exception(
                        f'{self.name} value "{value}" must be superior or equals to {self.minimum}.'
                    )

        if self.multiple_of and (value % self.multiple_of) == 0:
            raise Exception(
                f'{self.name} value "{value}" must be a multiple of {self.multiple_of}.'
            )

        self._check_choices(value)

    def _convert_to_date(self, value: Any) -> str:
        if not isinstance(value, datetime.date):
            raise Exception(
                f'{self.name} value "{value}" ({type(value)} type) must be a date.'
            )
        return value.isoformat()

    def _convert_to_date_time(self, value: Any) -> str:
        if not isinstance(value, datetime.datetime):
            raise Exception(
                f'{self.name} value "{value}" ({type(value)} type) must be a date time.'
            )
        return value.isoformat()

    def _convert_to_str(self, value: Any) -> str:
        if isinstance(value, datetime.date):
            raise Exception(
                f'{self.name} value "{value}" ({type(value)} type) must be formatted as text.'
            )
        if isinstance(value, int):
            value = str(value)
        if isinstance(value, float):
            # Send float values without decimal as int string values
            if value == float(int(value)):
                value = str(int(value))
            else:
                value = str(value)
        self._check_choices(value)
        if self.max_length is not None and len(value) > self.max_length:
            raise Exception(
                f'{self.name} value "{value}" cannot contains more than {self.max_length} characters.'
            )
        if self.min_length is not None and len(value) < self.min_length:
            raise Exception(
                f'{self.name} value "{value}" cannot contains less than {self.min_length} characters.'
            )
        return value

    def _check_choices(self, value: Any):
        if self.choices and value not in self.choices:
            raise Exception(
                f'{self.name} value "{value}" should be {" or ".join([str(choice) for choice in self.choices])}.'
            )

    def _convert_to_bool(self, value: Any) -> bool:
        if not isinstance(value, bool):
            raise Exception(
                f'{self.name} value "{value}" ({type(value)} type) must be a boolean.'
            )
        return value

    def _convert_to_dict(self, value: Any) -> dict:
        if not isinstance(value, list):
            raise Exception(
                f'{self.name} value "{value}" ({type(value)} type) must be a list.'
            )
        if len(value) != 2:
            raise Exception(
                f"{self.name} value should contains only two rows. Header and values."
            )
        return list_to_dict(value[0], value[1])

    def _convert_to_dict_list(self, value: Any) -> List[dict]:
        if not isinstance(value, list):
            raise Exception(
                f'{self.name} value "{value}" ({type(value)} type) must be a list.'
            )
        if len(value) < 2:
            raise Exception(
                f"{self.name} value should contains at least two rows. Header and values."
            )
        list_value = list_to_dict_list(value[0], value[1:])
        self._check_array(list_value)
        return list_value

    def _convert_to_file(self, value: Any):
        if os.path.isfile(value):  # Can be a path to a file
            return open(value, "rb")
        return self.server_param_name, value  # Or the content of the file

    def _convert_to_array(self, value: Any) -> Union[str, list]:
        if isinstance(value, list):
            list_value = self._convert_list_to_array(value)
        else:
            if value is not None or self.allow_null:
                list_value = [self.array_parameter._convert_to_type(value)]
            else:
                list_value = []
        self._check_array(list_value)
        return self._apply_collection_format(list_value)

    def _convert_list_to_array(self, list_value: list) -> list:
        return [
            self.array_parameter._convert_to_type(list_item)
            if list_item is not None
            else None
            for list_item in list_value
            if list_item is not None or self.allow_null
        ]

    def _apply_collection_format(self, list_value: list) -> Union[str, list]:
        if not self.collection_format or "csv" == self.collection_format:
            return ",".join([str(value) for value in list_value])
        if "multi" == self.collection_format:
            return (
                list_value  # requests module will send one parameter per item in list
            )
        if "ssv" == self.collection_format:
            return " ".join([str(value) for value in list_value])
        if "tsv" == self.collection_format:
            return "\t".join([str(value) for value in list_value])
        if "pipes" == self.collection_format:
            return "|".join([str(value) for value in list_value])
        raise Exception(f"Collection format {self.collection_format} is invalid.")

    def _check_array(self, value: list):
        if self.unique_items and len(set(value)) != len(value):
            raise Exception(f"{self.name} contains duplicated items.")

        if self.max_items is not None and len(value) > self.max_items:
            raise Exception(
                f"{self.name} cannot contains more than {self.max_items} items."
            )

        if self.min_items is not None and len(value) < self.min_items:
            raise Exception(
                f"{self.name} cannot contains less than {self.min_items} items."
            )

    def _get_convert_method(self) -> callable:
        if self.type == "integer":
            return self._convert_to_int
        elif self.type == "number":
            return self._convert_to_float
        elif self.type == "string":
            if self.format == "date":
                return self._convert_to_date
            elif self.format == "date-time":
                return self._convert_to_date_time
            return self._convert_to_str
        elif self.type == "boolean":
            return self._convert_to_bool
        elif self.type == "object":
            return self._convert_to_dict
        elif self.type == "file":
            return self._convert_to_file
        return lambda value: value  # Unhandled type, best effort

    def _common_documentation(self, open_api_parameter: dict) -> str:
        description = open_api_parameter.get("description", "") or ""
        if self.choices:
            description += f" Valid values are: {', '.join([str(choice) for choice in self.choices])}."
        if self.default_value:
            description += f" Default value is: {self.default_value}."
        return description

    def _get_documentation(self, open_api_parameter: dict) -> str:
        description = self._common_documentation(open_api_parameter)
        if self.type == "integer":
            description += "\nValue must be an integer."
        elif self.type == "number":
            description += "\nValue must be a number."
        elif self.type == "string":
            if self.format == "date":
                description += "\nValue must be formatted as date."
            elif self.format == "date-time":
                description += "\nValue must be formatted as date-time."
            else:
                description += "\nValue must be formatted as text."
        elif self.type == "boolean":
            description += "\nValue must be formatted as boolean."
        elif self.type == "object":
            description += "\nValue must be an array of two rows (field names, values)."
        elif self.type == "file":
            description += "\nValue must be the content of the file or the file path."
        return description.replace("'", "")

    def _get_dict_list_documentation(self, open_api_parameter: dict) -> str:
        description = self._common_documentation(open_api_parameter)
        description += (
            "\nValue must be an array of at least two rows (field names, values)."
        )
        return description.replace("'", "")

    def _get_list_documentation(self, open_api_parameter: dict) -> str:
        description = self._common_documentation(open_api_parameter)
        if self.array_parameter.type == "integer":
            description += "\nValue must be an array of integers."
        elif self.array_parameter.type == "number":
            description += "\nValue must be an array of numbers."
        elif self.array_parameter.type == "string":
            if self.array_parameter.format == "date":
                description += "\nValue must be an array of date formatted cells."
            elif self.array_parameter.format == "date-time":
                description += "\nValue must be an array of date-time formatted cells."
            else:
                description += "\nValue must be an array of text formatted cells."
        elif self.array_parameter.type == "boolean":
            description += "\nValue must be an array of boolean formatted cells."
        elif self.array_parameter.type == "file":
            description += (
                "\nValue must be an array of cells with files content or files paths."
            )
        return description.replace("'", "")


class OpenAPIUDFMethod(UDFMethod):
    def __init__(
        self,
        service: "OpenAPI",
        http_method: str,
        open_api_method: dict,
        path: str,
        formula_type: str,
        formula_options: dict,
    ):
        # Uses "or" in case OpenAPI definition contains None in description (explicitly set by service)
        self.help_url = OpenAPIUDFMethod.extract_url(
            open_api_method.get("description") or ""
        )
        operation_id = open_api_method.get(
            "operationId"
        ) or OpenAPIUDFMethod._compute_operation_id(http_method, path)
        # Ensure that there is no duplicate (in case a computed operationId matches a provided operationId)
        open_api_method["operationId"] = service.get_unique_operation_id(
            formula_type, operation_id
        )
        prefix = service.config.udf_prefix(formula_options)
        udf_name = f"{prefix}{open_api_method['operationId']}"
        self.responses = open_api_method.get("responses")
        if not self.responses:
            raise EmptyResponses(udf_name)
        self.open_api_method = open_api_method
        UDFMethod.__init__(
            self,
            service=service,
            http_method=http_method,
            path=path,
            formula_type=formula_type,
            formula_options=formula_options,
            udf_name=udf_name,
        )

    def _create_udf_parameters(self) -> List[UDFParameter]:
        udf_parameters = []
        for open_api_parameter in self.open_api_method.get("parameters", []):
            udf_parameters.extend(self._to_parameters(open_api_parameter))
        self._avoid_duplicated_names(udf_parameters)
        return udf_parameters

    @staticmethod
    def _compute_operation_id(http_method: str, path: str) -> str:
        """
        Compute the operationId OpenAPI field.

        :param path: path provided in OpenAPI definition for this method
        """
        return f"{http_method}{path.replace('/', '_')}"

    def return_a_list(self) -> bool:
        return "application/json" in self.open_api_method["produces"]

    def security(self, request_content: RequestContent) -> Optional[List[dict]]:
        return self.open_api_method.get("security")

    def summary(self) -> Optional[str]:
        return self.open_api_method.get("summary")

    def initial_header(self) -> Dict[str, str]:
        """
        Initial header content
        For more details refer to https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
        """
        header = {}

        if self.contains_body_parameters:
            consumes = self.open_api_method.get("consumes")
            if not consumes or "application/json" in consumes:
                header["Content-Type"] = "application/json"
            else:
                logger.warning(
                    f"{self.uri} is expecting {self.open_api_method['consumes']} encoded body. "
                    "For now PyxelRest only send JSON body so request might fail."
                )

        if "application/json" in self.open_api_method["produces"]:
            header["Accept"] = "application/json"

        header.update(self.service.config.custom_headers)

        return header

    @staticmethod
    def extract_url(text: str) -> Optional[str]:
        """
        OpenAPI URLs are interpreted thanks to the following format:
        [description of the url](url)
        :return: URL or None if no URL can be found.
        """
        urls = re.findall(r"^.*\[.*\]\((.*)\).*$", text)
        if urls:
            return urls[0]

    def _to_parameters(self, open_api_parameter: dict) -> List[APIUDFParameter]:
        if (
            "type" in open_api_parameter
        ):  # Type usually means that this is not a complex type
            return [APIUDFParameter(open_api_parameter, {})]

        schema = open_api_parameter["schema"]
        parameters = []
        open_api_definition = self._get_definition(schema)
        if open_api_definition:
            for inner_parameter_name, inner_parameter in open_api_definition[
                "properties"
            ].items():
                if not inner_parameter.get("readOnly", False):
                    inner_parameter["server_param_name"] = inner_parameter_name
                    inner_parameter["name"] = to_vba_valid_name(inner_parameter_name)
                    inner_parameter["in"] = open_api_parameter["in"]
                    inner_parameter[
                        "required"
                    ] = inner_parameter_name in open_api_definition.get("required", [])
                    parameters.append(APIUDFParameter(inner_parameter, schema))
        elif "items" in schema:
            inner_parameter = dict(open_api_parameter)
            inner_parameter.update(schema["items"])
            inner_parameter[
                "server_param_name"
            ] = None  # Indicate that this is the whole body
            parameters.append(APIUDFParameter(inner_parameter, schema))
        else:
            raise Exception(f"Unable to extract parameters from {open_api_parameter}")
        return parameters

    def _get_definition(self, schema: dict) -> dict:
        if "$ref" in schema:
            ref = schema["$ref"][len("#/definitions/") :]
            return self.service.open_api_definitions.get(ref, {})
        if "items" in schema:
            return self._get_definition(schema["items"])
        if "properties" in schema:
            return schema
        return {}

    def _avoid_duplicated_names(self, udf_parameters: List[UDFParameter]):
        parameters_by_name = {}
        for udf_parameter in udf_parameters:
            parameters_by_name.setdefault(udf_parameter.name, []).append(udf_parameter)
        for parameters in parameters_by_name.values():
            if len(parameters) > 1:
                for parameter in parameters:
                    # Keep original name for body and form as they make the more sense for those location
                    if (
                        parameter.location != "body"
                        and parameter.location != "formData"
                    ):
                        parameter.name = f"{parameter.location}_{parameter.name}"
        # Ensure that names are not duplicated anymore
        if len(parameters_by_name) != len(udf_parameters):
            self._avoid_duplicated_names(udf_parameters)

    def json_to_list(self, status_code: int, json_data: Any) -> list:
        all_definitions = self.service.open_api_definitions

        if self.service.config.rely_on_definitions:
            # TODO This is buggy, we need to allow concurrent deserialization
            _definition_deserializer.all_definitions = {}
            return Response(self.responses, status_code, all_definitions).rows(
                json_data
            )

        return Flattenizer(self.responses, status_code, all_definitions).to_list(
            json_data
        )


class OpenAPI(Service):
    def __init__(self, service_name: str, service_config: dict):
        """
        Load service information from configuration and OpenAPI definition.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param service_config: Dictionary containing service details.
        """
        self.methods = {}
        config = ServiceConfigSection(service_name, service_config)
        self.existing_operation_ids = {
            formula_type: [] for formula_type in config.formulas
        }
        self.open_api_definition = OpenAPI._retrieve_open_api_definition(config)
        self.validate_open_api_version()
        self.open_api_definitions = self.open_api_definition.get("definitions") or {}
        # Remove trailing slashes (as paths must starts with a slash)
        uri = self._extract_uri(config).rstrip("/")
        Service.__init__(self, config, uri)

    def _extract_uri(self, config: ServiceConfigSection) -> str:
        open_api_definition_url = (
            urlsplit(config.open_api_definition)
            if isinstance(config.open_api_definition, str)
            else None
        )

        schemes = self.open_api_definition.get("schemes")
        if not schemes:
            # The default scheme to be used is the one used to access the OpenAPI definition itself.
            if open_api_definition_url:
                schemes = [open_api_definition_url.scheme]
            else:
                raise InvalidOpenAPIDefinition("At least one scheme must be provided.")

        scheme = "https" if "https" in schemes else schemes[0]

        # host property is here to handle REST API behind a reverse proxy
        # (otherwise host will be the reverse proxy one when retrieving it from the URL)
        host = self.open_api_definition.get("host", config.network.get("host"))
        if not host:
            # The default host to be used is the host serving the documentation (including the port).
            if open_api_definition_url:
                host = open_api_definition_url.netloc
            else:
                raise InvalidOpenAPIDefinition("host must be provided.")

        # Allow user to provide host starting with scheme (removing it)
        host_parsed = urlsplit(host)
        if host_parsed.netloc:
            host = host_parsed.netloc + host_parsed.path
        # If it is not included, the API is served directly under the host.
        base_path = self.open_api_definition.get("basePath", None) or ""

        return f"{scheme}://{host}{base_path}"

    def create_method(
        self,
        http_method: str,
        open_api_method: dict,
        method_path: str,
        formula_type: str,
        formula_options: dict,
    ) -> OpenAPIUDFMethod:
        udf = OpenAPIUDFMethod(
            self,
            http_method,
            open_api_method,
            method_path,
            formula_type,
            formula_options,
        )
        self.methods[udf.udf_name] = udf
        return udf

    @classmethod
    def _retrieve_open_api_definition(cls, config: ServiceConfigSection) -> dict:
        """
        Retrieve OpenAPI JSON definition from service.
        :return: Dictionary representation of the retrieved Open API JSON definition.
        """
        if isinstance(config.open_api_definition, str):
            requests_session = _session.get(0)
            response = requests_session.get(
                config.open_api_definition,
                proxies=config.network.get("proxies", {}),
                verify=config.network.get("verify", True),
                headers=config.custom_headers,
                timeout=(
                    config.network.get("connect_timeout", 1),
                    config.definition_read_timeout,
                ),
                auth=_authentication.get_definition_retrieval_auth(config),
            )
            response.raise_for_status()
            open_api_definition = response.json()
        else:
            open_api_definition = config.open_api_definition
        cls._normalize_methods(open_api_definition)
        return open_api_definition

    # TODO Clean this method as it is too big and a smart refactoring might be needed
    @classmethod
    def _normalize_methods(cls, open_api_definition: dict):
        """
        Normalize method parameters from dict representing the OpenAPI definition to:
        - rename parameters name that are VBA restricted keywords
        - rename parameters name that uses '-' (to '_')
        - cascade parameters defined at path level to operation level

        Normalize method produces from dict representing the OpenAPI definition to:
        - cascade produces defined at root level to operation level

        :param open_api_definition: Dictionary representing the OpenAPI definition.
        :return: None
        """

        def _normalise_names(parameters):
            for parameter in parameters:
                parameter["server_param_name"] = parameter["name"]
                parameter["name"] = to_vba_valid_name(parameter["name"])
            return parameters

        def _update_method_parameters():
            method["parameters"] = (
                root_parameters
                + methods_parameters
                + _normalise_names(method.get("parameters", []))
            )

            method_parameters_names_per_location = {}
            for parameter in method["parameters"]:
                method_parameters_names_per_location.setdefault(
                    parameter["in"], []
                ).append(parameter["name"])

            for (
                location,
                parameters_names,
            ) in method_parameters_names_per_location.items():
                if len(set(parameters_names)) != len(parameters_names):
                    raise DuplicatedParameters(method)

        def _update_method_produces():
            method["produces"] = (
                root_produces + methods_produces + method.get("produces", [])
            )

        def _update_method_security():
            method["security"] = (
                root_security + methods_security + method.get("security", [])
            )

        def _update_method_consumes():
            method["consumes"] = (
                root_consumes + methods_consumes + method.get("consumes", [])
            )

        root_parameters = _normalise_names(open_api_definition.get("parameters", []))
        root_produces = open_api_definition.get("produces", [])
        root_security = open_api_definition.get("security", [])
        root_consumes = open_api_definition.get("consumes", [])

        for methods in open_api_definition["paths"].values():
            # retrieve parameters listed at the path level
            methods_parameters = _normalise_names(methods.pop("parameters", []))
            methods_produces = methods.pop("produces", [])
            methods_security = methods.pop("security", [])
            methods_consumes = methods.pop("consumes", [])

            for mode, method in methods.items():
                _update_method_parameters()
                _update_method_produces()
                _update_method_security()
                _update_method_consumes()

    def get_unique_operation_id(
        self, formula_type: str, potential_duplicated_operation_id: str
    ) -> str:
        unique_operation_id = (
            potential_duplicated_operation_id  # At this time, this might not be unique
        )
        if (
            potential_duplicated_operation_id
            in self.existing_operation_ids[formula_type]
        ):
            logger.warning(
                f"Duplicated operationId found: {potential_duplicated_operation_id}."
            )
            unique_operation_id = f"duplicated_{potential_duplicated_operation_id}"

        self.existing_operation_ids[formula_type].append(unique_operation_id)
        return unique_operation_id

    def validate_open_api_version(self):
        if "swagger" not in self.open_api_definition:
            raise OpenAPIVersionNotProvided()
        if self.open_api_definition["swagger"] != "2.0":
            raise UnsupportedOpenAPIVersion(self.open_api_definition["swagger"])

    def __str__(self) -> str:
        if "ntlm" in self.config.auth:
            return (
                f"[{self.config.name}] service. {self.uri} ({self.config.auth['ntlm']})"
            )
        return f"[{self.config.name}] service. {self.uri}"


def load_service(service_name: str, service_config: dict) -> OpenAPI:
    logger.debug(f'Loading "{service_name}" service...')
    try:
        service = OpenAPI(service_name, service_config)
        logger.info(f'"{service_name}" service will be available.')
        logger.debug(str(service))
        return service
    except Exception as e:
        logger.error(f'"{service_name}" service will not be available: {e}')

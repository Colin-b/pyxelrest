from collections import OrderedDict
import datetime
import logging
import os
import re
from typing import List, Union, Optional, Any, Dict

import requests
import requests.exceptions
import time
import xlwings
import xlwings.conversion
import xlwings.server
import yaml

from urllib.parse import urlsplit


from pyxelrest import authentication, session, definition_deserializer, vba
from pyxelrest.fast_deserializer import Flattenizer
from pyxelrest.pyxelresterrors import *
from pyxelrest.definition_deserializer import Response


logger = logging.getLogger(__name__)


def to_valid_regex(user_friendly_regex: str) -> str:
    if "*" in user_friendly_regex and ".*" not in user_friendly_regex:
        return f'^{user_friendly_regex.replace("*", ".*")}$'
    return f"^{user_friendly_regex}$"


def to_valid_python_vba(str_value: str) -> str:
    return re.sub("[^a-zA-Z_]+[^a-zA-Z_0-9]*", "", str_value)


def to_vba_valid_name(open_api_name: str) -> str:
    """
    Return name as non VBA or python restricted keyword
    """
    # replace vba restricted keywords
    if open_api_name.lower() in vba.vba_restricted_keywords:
        open_api_name = vba.vba_restricted_keywords[open_api_name.lower()]
    # replace forbidden VBA or Python characters (carets, dots and leading underscores)
    return open_api_name.replace("-", "_").replace(".", "_").lstrip("_")


def return_type_can_be_handled(method_produces: List[str]) -> bool:
    return "application/octet-stream" not in method_produces


def list_to_dict(header: Any, values: Any) -> dict:
    if not isinstance(header, list):
        header = [header]
    if not isinstance(values, list):
        values = [values]
    return {header[index]: value for index, value in enumerate(values)}


def list_to_dict_list(header: Any, values_list: Any) -> List[dict]:
    return [list_to_dict(header, values) for values in values_list]


def convert_environment_variable(value: str) -> str:
    """
    Value can be an environment variable formatted as %MY_ENV_VARIABLE%
    """
    environment_variables_match = re.match("^%(.*)%$", value)
    if environment_variables_match:
        environment_variable = environment_variables_match.group(1)
        return os.environ[environment_variable]
    return value


class ConfigSection:
    def __init__(self, service_name: str, service_config: dict):
        """
        Load service information from configuration.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param service_config: Dictionary containing service details.
        """
        self.name = service_name
        self.requested_methods = service_config.get(
            "methods", ["get", "post", "put", "delete", "patch", "options", "head"]
        )
        self.connect_timeout = service_config.get("connect_timeout", 1)
        self.read_timeout = service_config.get("read_timeout")
        udf = service_config.get("udf", {})
        # UDFs will be auto expanded by default (if required, ie: result does not fit in a single cell)
        self.udf_return_types = udf.get("return_types", ["async_auto_expand"])
        self.shift_result = udf.get("shift_result", True)
        self.max_retries = service_config.get("max_retries", 5)
        self.custom_headers = {
            key: convert_environment_variable(value)
            for key, value in service_config.get("headers", {}).items()
        }
        self.proxies = service_config.get("proxies", {})
        self.oauth2 = service_config.get("oauth2", {})
        self.basic = service_config.get("basic", {})
        self.api_key = service_config.get("api_key")
        if self.api_key:
            self.api_key = convert_environment_variable(self.api_key)
        self.ntlm_auth = service_config.get("ntlm", {})
        caching_conf = service_config.get("caching", {})
        max_nb_results = (
            self._to_positive_int(caching_conf.get("max_nb_results")) or 100
        )
        result_caching_time = self._to_positive_int(
            caching_conf.get("result_caching_time")
        )
        self.cache = (
            self._create_cache(max_nb_results, result_caching_time)
            if result_caching_time
            else None
        )
        results = service_config.get("result", {})
        self.flatten_results = bool(results.get("flatten", True))
        self.raise_exception = bool(results.get("raise_exception", False))
        self.udf_name_prefix = service_config.get("udf_name_prefix", "{service_name}_")

    @staticmethod
    def _create_cache(max_nb_results: int, ttl: int) -> Optional["cachetools.TTLCache"]:
        """
        Create a new in-memory cache.

        :param max_nb_results: Maximum number of results that can be stored.
        :param ttl: max time to live for items in seconds
        :return The newly created memory cache or None if not created.
        """
        try:
            import cachetools

            return cachetools.TTLCache(max_nb_results, ttl)
        except ImportError:
            logger.warning(
                "cachetools module is required to initialize a memory cache."
            )

    @staticmethod
    def _to_positive_int(value: Union[str, int]) -> Optional[int]:
        if value:
            try:
                value = int(value)
                return value if value else None
            except ValueError:
                logger.warning(
                    f"Invalid positive value provided: {value}. Considering as not set."
                )

    @staticmethod
    def is_asynchronous(udf_return_type: str) -> bool:
        return "async_auto_expand" == udf_return_type

    @staticmethod
    def auto_expand_result(udf_return_type: str) -> bool:
        return udf_return_type.endswith("_auto_expand")

    def udf_prefix(self, udf_return_type: str) -> str:
        service_name_prefix = to_valid_python_vba(self.name)
        if (len(self.udf_return_types) == 1) or self.auto_expand_result(
            udf_return_type
        ):
            return service_name_prefix
        return f"vba_{service_name_prefix}"


class ServiceConfigSection(ConfigSection):
    def __init__(self, service_name: str, service_config: dict):
        """
        Load service information from configuration.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param service_config: Dictionary containing service details.
        """
        ConfigSection.__init__(self, service_name, service_config)
        open_api = service_config.get("open_api", None)
        if not open_api:
            raise MandatoryPropertyNotProvided(service_name, "open_api")

        self.open_api_definition = open_api.get("definition", None)
        if not self.open_api_definition:
            raise MandatoryPropertyNotProvided(service_name, "open_api/definition")

        self.open_api_definition_url_parsed = urlsplit(self.open_api_definition)
        self.definition_read_timeout = open_api.get("definition_read_timeout", 5)
        self.service_host = open_api.get(
            "service_host", self.open_api_definition_url_parsed.netloc
        )
        self.rely_on_definitions = open_api.get("rely_on_definitions")
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
        if http_verb not in self.requested_methods:
            return False
        return (
            self._allow_tags(open_api_method.get("tags"))
            and self._allow_operation_id(open_api_method.get("operationId"))
            and return_type_can_be_handled(open_api_method.get("produces", []))
        )


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

    def should_provide_method(self, http_verb: str) -> bool:
        return http_verb in self.requested_methods

    def allow_parameter(self, parameter_name: str) -> bool:
        return True


class PyxelRestService:
    def __init__(self, service_name: str, service_config: dict):
        """
        Load service information from configuration.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param service_config: Dictionary containing service details.
        """
        self.methods = {}
        self.uri = ""
        self.config = PyxelRestConfigSection(service_name, service_config)
        self.existing_operation_ids = {
            udf_return_type: [] for udf_return_type in self.config.udf_return_types
        }
        self.open_api_definitions = {}
        self.open_api_definition = {
            "securityDefinitions": {
                "oauth2_implicit": {"type": "oauth2", "flow": "implicit"},
                "api_key_header": {"type": "apiKey", "in": "header"},
                "api_key_query": {"type": "apiKey", "in": "query"},
                "basic": {"type": "basic"},
            }
        }

    def create_method(
        self, http_method: str, udf_return_type: str
    ) -> "PyxelRestUDFMethod":
        udf = PyxelRestUDFMethod(self, http_method, udf_return_type)
        self.methods[udf.udf_name] = udf
        return udf


class UDFMethod:
    def __init__(
        self,
        service: Union[PyxelRestService, "OpenAPI"],
        http_method: str,
        path: str,
        udf_return_type: str,
    ):
        self.service = service
        self.requests_method = http_method
        self.uri = f"{service.uri}{path}"
        self.help_url = ""
        self.auto_expand_result = service.config.auto_expand_result(udf_return_type)
        self.is_asynchronous = service.config.is_asynchronous(udf_return_type)
        self.path_parameters = []
        self.required_parameters = []
        self.optional_parameters = []
        self.contains_body_parameters = False
        self.contains_file_parameters = False
        self.contains_query_parameters = False
        udf_parameters = self._create_udf_parameters()
        self.parameters = {}
        for udf_parameter in udf_parameters:
            if udf_parameter.location == "path":
                self.path_parameters.append(udf_parameter)
            # Required but not in path
            elif udf_parameter.required:
                self.update_information_on_parameter_type(udf_parameter)
                self.required_parameters.append(udf_parameter)
            else:
                if not self.service.config.allow_parameter(udf_parameter.name):
                    continue
                self.update_information_on_parameter_type(udf_parameter)
                self.optional_parameters.append(udf_parameter)

            self.parameters[udf_parameter.name] = udf_parameter

    def _create_udf_parameters(self) -> List["UDFParameter"]:
        return []

    def get_cached_result(self, request_content: "RequestContent") -> Optional[Any]:
        if self.service.config.cache is None:
            return
        # Caching is only effective on GET requests
        if "get" != self.requests_method:
            return

        request_id = request_content.unique_id()
        if request_id in self.service.config.cache:
            logger.debug(f"Retrieving cached result for {request_id}")
            return self.service.config.cache[request_id]
        else:
            logger.debug(f"No result yet cached for {request_id}")

    def cache_result(self, request_content: "RequestContent", result: Any):
        if self.service.config.cache is None:
            return

        request_id = request_content.unique_id()
        logger.debug(f"Cache result for {request_id}")
        self.service.config.cache[request_id] = result

    def update_information_on_parameter_type(self, parameter: "UDFParameter"):
        if parameter.location == "body":
            self.contains_body_parameters = True
        elif parameter.location == "formData":
            if parameter.type == "file":
                self.contains_file_parameters = True
            else:
                self.contains_body_parameters = True
        elif parameter.location == "query":
            self.contains_query_parameters = True

    def has_path_parameters(self) -> bool:
        return len(self.path_parameters) > 0

    def has_required_parameters(self) -> bool:
        return len(self.required_parameters) > 0

    def has_optional_parameters(self) -> bool:
        return len(self.optional_parameters) > 0

    def initial_header(self) -> Dict[str, str]:
        """
        Initial header content
        For more details refer to https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
        """
        return self.service.config.custom_headers

    def requires_authentication(
        self, request_content: "RequestContent"
    ) -> Union[List[dict], dict]:
        return self.security(request_content) or self.service.config.ntlm_auth

    def security(self, request_content: "RequestContent") -> Optional[List[dict]]:
        pass


class UDFParameter:
    def __init__(
        self,
        name: str,
        server_param_name: str,
        location: str,
        required: Optional[bool],
        field_type: Union[List[str], str],
    ):
        self.name = name
        self.server_param_name = server_param_name
        self.location = location
        self.required = required
        self.allow_null = False
        if isinstance(field_type, list):
            field_type = list(field_type)  # Copy to avoid propagate changes
            if "null" in field_type:
                field_type.remove("null")
                self.allow_null = True
            if len(field_type) != 1:
                raise Exception(f"Unable to guess field type amongst {field_type}")
            field_type = field_type[0]
        self.type = field_type
        self.array_dimension = 0

    def validate(self, request_content: "RequestContent"):
        pass

    def validate_required(self, value: Any, request_content: "RequestContent"):
        if value is None or isinstance(value, list) and all(x is None for x in value):
            raise self._not_provided()
        self.validate_optional(value, request_content)

    def validate_optional(self, value: Any, request_content: "RequestContent"):
        pass

    def _not_provided(self) -> Exception:
        return Exception(f"{self.name} is required.")


class PyxelRestUDFMethod(UDFMethod):
    class ParseBodyAsParameter(UDFParameter):
        def __init__(self):
            UDFParameter.__init__(
                self, "parse_body_as", "parse_body_as", "", False, "string"
            )
            self.choices = ["dict", "dict_list"]
            self.description = f"How the body should be sent ({self.choices})."

        def _convert_to_str(self, value: Any) -> str:
            if isinstance(value, datetime.date):
                raise Exception(
                    f'{self.name} value "{value}" must be formatted as text.'
                )
            if isinstance(value, int) or isinstance(value, float):
                value = str(value)
            if value and value not in self.choices:
                raise Exception(
                    f'{self.name} value "{value}" should be {" or ".join(self.choices)}.'
                )
            return value

        def validate_optional(self, value: Any, request_content: "RequestContent"):
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

        def validate_optional(self, value: Any, request_content: "RequestContent"):
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

        def validate_optional(self, value: Any, request_content: "RequestContent"):
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
                raise Exception(
                    f'{self.name} value "{value}" must be formatted as text.'
                )
            if isinstance(value, int) or isinstance(value, float):
                value = str(value)
            return value

        def validate_optional(self, value: Any, request_content: "RequestContent"):
            if value is not None:
                value = self._convert_to_str(value)
            request_content.add_value(self, value)

    class BodyParameter(UDFParameter):
        def __init__(self):
            UDFParameter.__init__(self, "body", "body", "body", True, "object")
            self.description = "Content of the body."

        def validate_optional(self, value: Any, request_content: "RequestContent"):
            self.received_value = (
                value  # Save value as is to serialize it properly afterwards
            )

        def validate(self, request_content: "RequestContent"):
            request_content.payload = list_as_json(
                self.received_value,
                request_content.extra_parameters.get("parse_body_as"),
            )

    class ExtraHeadersParameter(UDFParameter):
        def __init__(self):
            UDFParameter.__init__(
                self, "extra_headers", "extra_headers", "headers", False, "object"
            )
            self.description = "Extra headers to send in the query."

        def validate_optional(self, value: Any, request_content: "RequestContent"):
            self.received_value = value  # TODO Validate dict

        def validate(self, request_content: "RequestContent"):
            if self.received_value:
                request_content.header.update(self.received_value)

    class AuthenticationParameter(UDFParameter):
        def __init__(self):
            UDFParameter.__init__(self, "auth", "auth", "", False, "array")
            self.choices = [
                "oauth2_implicit",
                "api_key_header",
                "api_key_query",
                "basic",
            ]
            self.description = f"Authentication methods to use. ({self.choices})"

        def _convert_to_str(self, value: Any) -> str:
            if value and value not in self.choices:
                raise Exception(
                    f'{self.name} value "{value}" should be {" or ".join(self.choices)}.'
                )
            return value

        def _convert_to_array(self, value: Any) -> List[str]:
            if isinstance(value, list):
                return [
                    self._convert_to_str(item) for item in value if item is not None
                ]
            return [self._convert_to_str(value)]

        def validate_optional(self, value, request_content: "RequestContent"):
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
                raise Exception(
                    f'{self.name} value "{value}" must be formatted as text.'
                )
            if isinstance(value, int) or isinstance(value, float):
                value = str(value)
            return value

        def validate_optional(self, value: Any, request_content: "RequestContent"):
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
                raise Exception(
                    f'{self.name} value "{value}" must be formatted as text.'
                )
            if isinstance(value, int) or isinstance(value, float):
                value = str(value)
            return value

        def validate_optional(self, value: Any, request_content: "RequestContent"):
            if value is not None:
                value = self._convert_to_str(value)
            request_content.add_value(self, value)

    class ApiKeyNameParameter(UDFParameter):
        def __init__(self):
            UDFParameter.__init__(
                self, "api_key_name", "api_key_name", "", False, "string"
            )
            self.description = "Name of the field containing API key."

        def _convert_to_str(self, value: Any) -> str:
            if isinstance(value, datetime.date):
                raise Exception(
                    f'{self.name} value "{value}" must be formatted as text.'
                )
            if isinstance(value, int) or isinstance(value, float):
                value = str(value)
            return value

        def validate_optional(self, value: Any, request_content: "RequestContent"):
            if value is not None:
                value = self._convert_to_str(value)
            request_content.add_value(self, value)

    def __init__(
        self, service: PyxelRestService, http_method: str, udf_return_type: str
    ):
        UDFMethod.__init__(self, service, http_method, "{url}", udf_return_type)
        self.udf_name = (
            f"{service.config.udf_prefix(udf_return_type)}_{http_method}_url"
        )
        self.responses = {}

    def _create_udf_parameters(self) -> List[UDFParameter]:
        parameters = [
            self.UrlParameter(),
            self.ExtraHeadersParameter(),
            self.WaitForStatusParameter(),
            self.CheckIntervalParameter(),
            self.AuthenticationParameter(),
            self.OAuth2AuthorizationUrlParameter(),
            self.OAuth2TokenUrlParameter(),
            self.ApiKeyNameParameter(),
        ]

        if self.requests_method in ["post", "put"]:
            parameters.append(self.BodyParameter())
            parameters.append(self.ParseBodyAsParameter())

        return parameters

    def summary(self) -> str:
        return f"Send a HTTP {self.requests_method} request to specified URL."

    def return_a_list(self) -> bool:
        return True

    def security(self, request_content: "RequestContent") -> List[dict]:
        auths = request_content.extra_parameters.get("auth")
        return [{auth: "" for auth in auths}] if auths else []


class OpenAPI:
    def __init__(self, service_name: str, service_config: dict):
        """
        Load service information from configuration and OpenAPI definition.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param service_config: Dictionary containing service details.
        """
        self.methods = {}
        self.config = ServiceConfigSection(service_name, service_config)
        self.existing_operation_ids = {
            udf_return_type: [] for udf_return_type in self.config.udf_return_types
        }
        self.open_api_definition = self._retrieve_open_api_definition()
        self.validate_open_api_version()
        self.open_api_definitions = self.open_api_definition.get("definitions") or {}
        # Remove trailing slashes (as paths must starts with a slash)
        self.uri = self._extract_uri().rstrip("/")

    def _extract_uri(self) -> str:
        # The default scheme to be used is the one used to access the OpenAPI definition itself.
        schemes = self.open_api_definition.get(
            "schemes", [self.config.open_api_definition_url_parsed.scheme]
        )
        scheme = "https" if "https" in schemes else schemes[0]

        # If the host is not included, the host serving the documentation is to be used (including the port).
        # service_host property is here to handle services behind a reverse proxy
        # (otherwise host will be the reverse proxy one)
        host = self.open_api_definition.get("host", self.config.service_host)
        # Allow user to provide service_host starting with scheme (removing it)
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
        udf_return_type: str,
    ) -> "OpenAPIUDFMethod":
        udf = OpenAPIUDFMethod(
            self, http_method, open_api_method, method_path, udf_return_type
        )
        self.methods[udf.udf_name] = udf
        return udf

    def _retrieve_open_api_definition(self) -> dict:
        """
        Retrieve OpenAPI JSON definition from service.
        :return: Dictionary representation of the retrieved Open API JSON definition.
        """
        requests_session = session.get(0)
        response = requests_session.get(
            self.config.open_api_definition,
            proxies=self.config.proxies,
            verify=False,
            headers=self.config.custom_headers,
            timeout=(self.config.connect_timeout, self.config.definition_read_timeout),
            auth=authentication.get_definition_retrieval_auth(self.config),
        )
        response.raise_for_status()
        # TODO Check if we still need to explicitely use OrderedDict since python 3.6
        # Always keep the order provided by server (for definitions)
        open_api_definition = response.json(object_pairs_hook=OrderedDict)
        self._normalize_methods(open_api_definition)
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
        self, udf_return_type: str, potential_duplicated_operation_id: str
    ) -> str:
        unique_operation_id = (
            potential_duplicated_operation_id  # At this time, this might not be unique
        )
        if (
            potential_duplicated_operation_id
            in self.existing_operation_ids[udf_return_type]
        ):
            logger.warning(
                f"Duplicated operationId found: {potential_duplicated_operation_id}."
            )
            unique_operation_id = f"duplicated_{potential_duplicated_operation_id}"

        self.existing_operation_ids[udf_return_type].append(unique_operation_id)
        return unique_operation_id

    def validate_open_api_version(self):
        if "swagger" not in self.open_api_definition:
            raise OpenAPIVersionNotProvided()
        if self.open_api_definition["swagger"] != "2.0":
            raise UnsupportedOpenAPIVersion(self.open_api_definition["swagger"])

    def __str__(self) -> str:
        if self.config.ntlm_auth:
            return f"[{self.config.name}] service. {self.uri} ({self.config.ntlm_auth})"
        return f"[{self.config.name}] service. {self.uri}"


class OpenAPIUDFMethod(UDFMethod):
    def __init__(
        self,
        service: OpenAPI,
        http_method: str,
        open_api_method: dict,
        path: str,
        udf_return_type: str,
    ):
        self.open_api_method = open_api_method
        UDFMethod.__init__(self, service, http_method, path, udf_return_type)
        # Uses "or" in case OpenAPI definition contains None in description (explicitly set by service)
        self.help_url = self.extract_url(open_api_method.get("description") or "")
        self._compute_operation_id(udf_return_type, path)
        prefix = service.config.udf_name_prefix.format(
            service_name=service.config.udf_prefix(udf_return_type)
        )
        self.udf_name = f"{prefix}{self.open_api_method['operationId']}"
        self.responses = open_api_method.get("responses")
        if not self.responses:
            raise EmptyResponses(self.udf_name)

    def _create_udf_parameters(self) -> List[UDFParameter]:
        udf_parameters = []
        for open_api_parameter in self.open_api_method.get("parameters", []):
            udf_parameters.extend(self._to_parameters(open_api_parameter))
        self._avoid_duplicated_names(udf_parameters)
        return udf_parameters

    def _compute_operation_id(self, udf_return_type: str, path: str):
        """
        Compute the operationId OpenAPI field (as it may not be provided).
        Also ensure that there is no duplicate (in case a computed one matches a provided one)

        :param path: path provided in OpenAPI definition for this method
        """
        operation_id = (
            self.open_api_method.get("operationId")
            or f"{self.requests_method}{path.replace('/', '_')}"
        )
        self.open_api_method["operationId"] = self.service.get_unique_operation_id(
            udf_return_type, operation_id
        )

    def return_a_list(self) -> bool:
        return "application/json" in self.open_api_method["produces"]

    def security(self, request_content: "RequestContent") -> Optional[List[dict]]:
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

    def _to_parameters(self, open_api_parameter):
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

    def _get_definition(self, schema: dict):
        if "$ref" in schema:
            ref = schema["$ref"][len("#/definitions/") :]
            return self.service.open_api_definitions.get(ref, {})
        if "items" in schema:
            return self._get_definition(schema["items"])
        if "properties" in schema:
            return schema
        return {}

    def _avoid_duplicated_names(self, udf_parameters):
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

    def validate_optional(self, value: Any, request_content: "RequestContent"):
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


class RequestContent:
    def __init__(self, udf_method: UDFMethod, excel_caller_address):
        self.udf_method = udf_method
        self.header = udf_method.initial_header()
        self.header["X-Pxl-Cell"] = excel_caller_address
        self.header_parameters = {}
        self.payload = {}
        self.files = {}
        self.parameters = {}
        self.path_values = {}
        # Contains parameters that were not provided but may still need to be sent with None value
        self._none_parameters = []
        # Parameters that should not be sent but interpreted by pyxelrest
        self.extra_parameters = {}

    def validate(self):
        for udf_parameter in self.udf_method.parameters.values():
            udf_parameter.validate(self)

    def unique_id(self) -> str:
        return f"method={self.udf_method.requests_method},payload={self.payload},files={self.files},parameters={self.parameters},path={self.path_values},headers={self.header_parameters}"

    def add_value(self, parameter, value):
        if parameter.location == "query":
            self._add_query_parameter(parameter, value)
        elif parameter.location == "body":
            self._add_body_parameter(parameter, value)
        elif parameter.location == "formData":
            self._add_form_parameter(parameter, value)
        elif parameter.location == "header":
            self._add_header_parameter(parameter, value)
        elif parameter.location == "path":
            self._add_path_parameter(parameter, value)
        elif parameter.location == "":
            self._add_extra_parameter(parameter, value)

    def _add_query_parameter(self, parameter, value):
        if value is not None:
            self.parameters[parameter.server_param_name] = value

    def _add_extra_parameter(self, parameter, value):
        self.extra_parameters[parameter.server_param_name] = value

    def _add_path_parameter(self, parameter, value):
        self.path_values[parameter.server_param_name] = value

    def _add_body_parameter(self, parameter, value):
        if parameter.schema.get("type") == "array":
            self._add_body_list_parameter(parameter, value)
        else:
            if parameter.server_param_name:
                self.payload[parameter.server_param_name] = value
            else:
                self.payload = value

    def _add_body_list_parameter(self, parameter, value):
        # Change the default payload to list
        if self.payload == {}:
            self.payload = []

        if value is None:
            if len(self.payload) == 0:
                self._none_parameters.append(parameter)

            for list_item in self.payload:
                list_item[parameter.server_param_name] = None
        else:
            nb_values = len(value)
            nb_list_items = len(self.payload)

            # All items will be updated with a new provided value
            if nb_values == nb_list_items:
                for index, parameter_list_item in enumerate(value):
                    self.payload[index][
                        parameter.server_param_name
                    ] = parameter_list_item

            # All items will be updated with a new provided value and new items will be added
            elif nb_values > nb_list_items:
                # Add empty items to current payload so that length fits the new one
                empty_item = (
                    {field_name: None for field_name in self.payload[0]}
                    if nb_list_items > 0
                    else {
                        none_parameter.server_param_name: None
                        for none_parameter in self._none_parameters
                    }
                )
                self._none_parameters.clear()
                for new_index in range(nb_list_items, nb_values):
                    self.payload.append(dict(empty_item))

                for index, parameter_list_item in enumerate(value):
                    if parameter.server_param_name:
                        self.payload[index][
                            parameter.server_param_name
                        ] = parameter_list_item
                    else:
                        self.payload[index] = parameter_list_item

            # Some items will be updated with a new provided value and remaining will contains None
            else:
                for index, parameter_list_item in enumerate(value):
                    self.payload[index][
                        parameter.server_param_name
                    ] = parameter_list_item

                for non_provided_index in range(nb_values, nb_list_items):
                    self.payload[non_provided_index][parameter.server_param_name] = None

    def _add_form_parameter(self, parameter, value):
        if parameter.type == "file":
            if value is not None:
                self.files[parameter.server_param_name] = value
        else:
            self.payload[parameter.server_param_name] = value

    def _add_header_parameter(self, parameter, value):
        if value is not None:
            self.header[parameter.server_param_name] = value
            self.header_parameters[parameter.server_param_name] = value


def load_services_from_yaml(
    services_configuration_file_path: str,
) -> List[Union[PyxelRestService, OpenAPI]]:
    """
    Retrieve OpenAPI JSON definition for each service defined in configuration file.
    :return: List of OpenAPI and PyxelRestService instances, size is the same one as the number of sections within
    configuration file
    """
    if not os.path.isfile(services_configuration_file_path):
        raise ConfigurationFileNotFound(services_configuration_file_path)

    with open(services_configuration_file_path, "r") as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)

    logging.debug(f'Loading services from "{services_configuration_file_path}"...')
    return load_services(config)


def load_services(config: dict) -> List[Union[PyxelRestService, OpenAPI]]:
    """
    Retrieve OpenAPI JSON definition for each service defined in configuration.
    :return: List of OpenAPI and PyxelRestService instances, size is the same one as the number of sections within
    configuration.
    """
    if not isinstance(config, dict):
        raise Exception("Configuration must be a dictionary.")

    loaded_services = []
    for service_name, service_config in config.items():
        if "pyxelrest" == service_name:
            pyxelrest_service = PyxelRestService(service_name, service_config)
            loaded_services.append(pyxelrest_service)
        else:
            service = load_service(service_name, service_config)
            if service:
                loaded_services.append(service)

    check_for_duplicates(loaded_services)
    return loaded_services


def load_service(service_name: str, service_config: dict) -> OpenAPI:
    logger.debug(f'Loading "{service_name}" service...')
    try:
        service = OpenAPI(service_name, service_config)
        logger.info(f'"{service_name}" service will be available.')
        logger.debug(str(service))
        return service
    except Exception as e:
        logger.error(f'"{service_name}" service will not be available: {e}')


def check_for_duplicates(loaded_services: List[Union[PyxelRestService, OpenAPI]]):
    services_by_prefix = {}
    for service in loaded_services:
        for udf_return_type in service.config.udf_return_types:
            services_by_prefix.setdefault(
                service.config.udf_prefix(udf_return_type), []
            ).append(service.config.name)
    for udf_prefix in services_by_prefix:
        service_names = services_by_prefix[udf_prefix]
        if len(service_names) > 1:
            logger.warning(
                f'{service_names} services will use the same "{udf_prefix}" prefix, in case there is the same call available, '
                "only the last declared one will be available."
            )


def get_result(
    udf_method: Union[PyxelRestUDFMethod, OpenAPIUDFMethod],
    request_content: RequestContent,
    excel_application,
):
    cached_result = udf_method.get_cached_result(request_content)
    if cached_result is not None:
        return shift_result(cached_result, udf_method)

    response = None
    try:
        response = session.get(udf_method.service.config.max_retries).request(
            udf_method.requests_method,
            udf_method.uri.format(**request_content.path_values),
            json=request_content.payload
            if udf_method.contains_body_parameters
            else None,
            params=request_content.parameters
            if udf_method.contains_query_parameters
            else None,
            files=request_content.files
            if udf_method.contains_file_parameters
            else None,
            auth=authentication.get_auth(udf_method, request_content),
            verify=False,
            headers=request_content.header,
            proxies=udf_method.service.config.proxies,
            timeout=(
                udf_method.service.config.connect_timeout,
                udf_method.service.config.read_timeout,
            ),
        )
        response.raise_for_status()

        # Wait for a specific status if needed
        wait_for_status = request_content.extra_parameters.get("wait_for_status")
        if wait_for_status:
            if not response.history or (
                response.history[0].status_code != wait_for_status
            ):
                check_interval = request_content.extra_parameters["check_interval"]
                logger.info(
                    f"Waiting for {wait_for_status} status. Sending a new request in {check_interval} seconds."
                )
                time.sleep(check_interval)
                return get_result(udf_method, request_content, excel_application)

        logger.info(
            f"{get_caller_address(excel_application)} [status=Valid] response received for [function={udf_method.udf_name}] [url={response.request.url}]."
        )
        if 202 == response.status_code:
            result = [["Status URL"], [response.headers["location"]]]
        elif response.headers["content-type"] == "application/json":
            result = json_as_list(response, udf_method)
        else:
            result = convert_to_return_type(response.text[:255], udf_method)
        udf_method.cache_result(request_content, result)
        return shift_result(result, udf_method)
    except requests.exceptions.ConnectionError as e:
        logger.exception(
            f"{get_caller_address(excel_application)} Connection [status=error] occurred while calling [function={udf_method.udf_name}] [url={udf_method.uri}]."
        )
        return handle_exception(
            udf_method,
            "Cannot connect to service. Please retry once connection is re-established.",
            e,
        )
    except Exception as error:
        # Check "is not None" because response.ok is overridden according to HTTP status code.
        if response is not None:
            logger.exception(
                f"{get_caller_address(excel_application)} [status=Error] occurred while handling "
                f"[function={udf_method.udf_name}] [url={response.request.url}] response: [response={response.text}]."
            )
        else:
            logger.exception(
                f"{get_caller_address(excel_application)} [status=Error] occurred while calling [function={udf_method.udf_name}] [url={udf_method.uri}]."
            )
        return handle_exception(udf_method, describe_error(response, error), error)
    finally:
        # Check "is not None" because response.ok is overridden according to HTTP status code.
        if response is not None:
            response.close()


def get_caller_address(excel_application) -> str:
    try:
        if not excel_application:
            return "Python"  # TODO Return details on caller of UDF?
        excel_caller = excel_application.Caller
        if not hasattr(excel_caller, "Rows"):
            return f"VBA:{excel_application.VBE.ActiveCodePane.CodeModule}"
        return str(
            xlwings.xlplatform.Range(xl=excel_caller).get_address(True, True, True)
        )
    except:
        logger.exception("Unable to retrieve caller address.")
        return ""


def convert_to_return_type(
    str_value: str, udf_method: Union[PyxelRestUDFMethod, OpenAPIUDFMethod]
) -> Union[List[str], str]:
    return [str_value] if udf_method.return_a_list() else str_value


def describe_error(response: requests.Response, error: Exception) -> str:
    # Check "is not None" because response.ok is overridden according to HTTP status code.
    if response is not None:
        return f'An error occurred. Please check logs for full details: "{response.text[:198]}"'
    return (
        f'An error occurred. Please check logs for full details: "{str(error)[:198]}"'
    )


def handle_exception(
    udf_method: Union[PyxelRestUDFMethod, OpenAPIUDFMethod],
    exception_message: str,
    exception: Exception,
):
    if udf_method.service.config.raise_exception:
        raise exception

    return shift_result(
        convert_to_return_type(exception_message, udf_method), udf_method
    )


def json_as_list(
    response: requests.Response, udf_method: Union[PyxelRestUDFMethod, OpenAPIUDFMethod]
) -> list:
    if udf_method.service.config.rely_on_definitions:
        definition_deserializer.all_definitions = {}
        logger.debug(
            "Converting JSON string to corresponding python structure (relying on definitions)..."
        )
        json_data = (
            response.json(object_pairs_hook=OrderedDict)
            if len(response.content)
            else ""
        )
        all_definitions = udf_method.service.open_api_definitions
        return Response(
            udf_method.responses, response.status_code, all_definitions
        ).rows(json_data)

    logger.debug("Converting JSON string to corresponding python structure...")
    json_data = (
        response.json(object_pairs_hook=OrderedDict) if len(response.content) else ""
    )
    if udf_method.service.config.flatten_results:
        all_definitions = udf_method.service.open_api_definitions
        return Flattenizer(
            udf_method.responses, response.status_code, all_definitions
        ).to_list(json_data)
    else:
        return json_data


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


def shift_result(result: list, udf_method: Union[PyxelRestUDFMethod, OpenAPIUDFMethod]):
    # First result cell is stuck to "computing..." in such case
    # If result is a single cell, force the shift to make sure client knows the computation is over
    if (
        udf_method.is_asynchronous
        and not udf_method.service.config.shift_result
        and result
        and len(result) == 1
    ):
        if isinstance(result[0], list) and len(result[0]) == 1:
            result[0].insert(0, "Formula")
        elif isinstance(result, list):
            result = [["Formula", value] for value in result]

    if (
        udf_method.service.config.shift_result
        and udf_method.auto_expand_result
        and result
    ):
        if isinstance(result[0], list):
            for row in result:
                row.insert(0, "")
        elif isinstance(result, list):
            result = [["", value] for value in result]
    return result

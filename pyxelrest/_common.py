import logging
import re
import os
import time
from collections import OrderedDict
from typing import Optional, Union, List, Any, Dict


import requests
import xlwings
import xlwings.conversion
import xlwings.server

from pyxelrest import _session, _authentication


logger = logging.getLogger(__name__)


def list_to_dict(header: Any, values: Any) -> dict:
    if not isinstance(header, list):
        header = [header]
    if not isinstance(values, list):
        values = [values]
    return {header[index]: value for index, value in enumerate(values)}


def list_to_dict_list(header: Any, values_list: Any) -> List[dict]:
    return [list_to_dict(header, values) for values in values_list]


def to_valid_python_vba(str_value: str) -> str:
    return re.sub("[^a-zA-Z_]+[^a-zA-Z_0-9]*", "", str_value)


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
        self.formulas = service_config.get(
            "formulas", {"dynamic_array": {"lock_excel": False, "shift_result": False}}
        )
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

    def udf_prefix(self, formula_type: str) -> str:
        service_name_prefix = to_valid_python_vba(self.name)

        if "vba_compatible" == formula_type:
            return f"vba_{service_name_prefix}"

        # TODO Drop the behavior where there is no prefix for non dynamic arrays (when there is no more users using it?)
        if len(self.formulas) == 1 or "dynamic_array" == formula_type:
            return service_name_prefix

        # Legacy array and there is more than one formula per operation
        return f"legacy_{service_name_prefix}"

    def allow_parameter(self, parameter_name: str) -> bool:
        return True


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


class UDFMethod:
    def __init__(
        self,
        *,
        service: "Service",
        http_method: str,
        path: str,
        formula_type: str,
        formula_options: dict,
        udf_name: str,
    ):
        self.service = service
        self.shift_result = formula_options.get("shift_result", False)
        self.requests_method = http_method
        self.uri = f"{service.uri}{path}"
        self.udf_name = udf_name
        self.help_url = ""
        self.auto_expand_result = "legacy_array" == formula_type
        self.is_asynchronous = "vba_compatible" != formula_type and not formula_options.get(
            "lock_excel", False
        )
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

    def update_information_on_parameter_type(self, parameter: UDFParameter):
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

    def json_result(self, response: requests.Response) -> list:
        logger.debug("Converting JSON string to corresponding python structure...")
        # TODO Check if we still need to use an OrderedDict here
        json_data = (
            response.json(object_pairs_hook=OrderedDict)
            if len(response.content)
            else ""
        )

        return (
            self.json_to_list(response.status_code, json_data)
            if self.service.config.flatten_results
            else json_data
        )

    def _create_udf_parameters(self) -> List[UDFParameter]:
        raise NotImplementedError  # pragma: no cover

    def security(self, request_content: "RequestContent") -> Optional[List[dict]]:
        raise NotImplementedError  # pragma: no cover

    def json_to_list(self, status_code: int, json_data: Any) -> list:
        raise NotImplementedError  # pragma: no cover


class Service:
    def __init__(self, config: ConfigSection, uri: str):
        self.uri = uri
        self.config = config


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
                for _ in range(nb_list_items, nb_values):
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


def check_for_duplicates(loaded_services: List[Service]):
    services_by_prefix = {}
    for service in loaded_services:
        for formula_type in service.config.formulas:
            services_by_prefix.setdefault(
                service.config.udf_prefix(formula_type), []
            ).append(service.config.name)
    for udf_prefix in services_by_prefix:
        service_names = services_by_prefix[udf_prefix]
        if len(service_names) > 1:
            logger.warning(
                f'{service_names} services will use the same "{udf_prefix}" prefix, in case there is the same call available, '
                "only the last declared one will be available."
            )


def get_result(
    udf_method: UDFMethod, request_content: RequestContent, excel_application
):
    cached_result = udf_method.get_cached_result(request_content)
    if cached_result is not None:
        return shift_result(cached_result, udf_method)

    response = None
    try:
        # TODO Use a context manager ?
        response = _session.get(udf_method.service.config.max_retries).request(
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
            auth=_authentication.get_auth(udf_method, request_content),
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
            result = udf_method.json_result(response)
        else:
            result = convert_to_return_type(response.text[:255], udf_method)
        udf_method.cache_result(request_content, result)
        return shift_result(result, udf_method)
    except requests.ConnectionError as e:
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


def describe_error(response: requests.Response, error: Exception) -> str:
    # Check "is not None" because response.ok is overridden according to HTTP status code.
    if response is not None:
        return f'An error occurred. Please check logs for full details: "{response.text[:198]}"'
    return (
        f'An error occurred. Please check logs for full details: "{str(error)[:198]}"'
    )


def handle_exception(
    udf_method: UDFMethod, exception_message: str, exception: Exception
):
    if udf_method.service.config.raise_exception:
        raise exception

    return shift_result(
        convert_to_return_type(exception_message, udf_method), udf_method
    )


def convert_to_return_type(
    str_value: str, udf_method: UDFMethod
) -> Union[List[str], str]:
    return [str_value] if udf_method.return_a_list() else str_value


def shift_result(result: list, udf_method: UDFMethod) -> list:
    """
    In case Microsoft Excel should not be locked (computation performed in another thread)
    The first cell is stuck to "computing..." (this is a known xlwings issue)

    This function provides the ability to shift the actual result to make sure it is always displayed.
    """
    # If result is a single cell, force the shift to make sure client knows the computation is over
    if (
        udf_method.is_asynchronous
        and not udf_method.shift_result
        and result
        and len(result) == 1
    ):
        if isinstance(result[0], list) and len(result[0]) == 1:
            result[0].insert(0, "Formula")
        elif isinstance(result, list):
            result = [["Formula", value] for value in result]

    # If client explicitly asked for shifted results, update them
    if udf_method.shift_result and result:
        if isinstance(result[0], list):
            for row in result:
                row.insert(0, "")
        elif isinstance(result, list):
            result = [["", value] for value in result]

    return result
from collections import OrderedDict
import datetime
import logging
import os
from pip.commands.install import InstallCommand
import re
import requests
import requests.exceptions
import sys
import threading
import time
import xlwings
import xlwings.conversion
import xlwings.server
import yaml

try:
    # Python 3
    from urllib.parse import urlsplit
except ImportError:
    # Python 2
    from urlparse import urlsplit


from pyxelrest import (
    authentication,
    custom_logging,
    session,
    fileadapter,
    definition_deserializer,
    vba,
    SERVICES_CONFIGURATION_FILE_PATH
)
from pyxelrest.fast_deserializer import Flattenizer
from pyxelrest.pyxelresterrors import *
from pyxelrest.definition_deserializer import Response


def support_ujson():
    try:
        import ujson
        return True
    except:
        return False


def support_pandas():
    try:
        import pandas
        return True
    except:
        return False


if support_ujson():
    import ujson

if support_pandas():
    import pandas


logger = logging.getLogger(__name__)


def to_valid_regex(user_friendly_regex):
    if '*' in user_friendly_regex and '.*' not in user_friendly_regex:
        return '^{0}$'.format(user_friendly_regex.replace('*', '.*'))
    return '^{0}$'.format(user_friendly_regex)


def to_valid_python_vba(str_value):
    return re.sub('[^a-zA-Z_]+[^a-zA-Z_0-9]*', '', str_value)


def to_vba_valid_name(open_api_name):
    """
    Return name as non VBA or python restricted keyword
    """
    # replace vba restricted keywords
    if open_api_name.lower() in vba.vba_restricted_keywords:
        open_api_name = vba.vba_restricted_keywords[open_api_name.lower()]
    # replace '-'
    if "-" in open_api_name:
        open_api_name = open_api_name.replace("-", "_")
    if open_api_name.startswith("_"):  # TODO Handle more than one
        open_api_name = open_api_name[1:]
    return open_api_name


def return_type_can_be_handled(method_produces):
    return 'application/octet-stream' not in method_produces


def list_to_dict(header, values):
    if not isinstance(header, list):
        header = [header]
    if not isinstance(values, list):
        values = [values]
    return {
        header[index]: value
        for index, value in enumerate(values)
    }


def list_to_dict_list(header, values_list):
    return [
        list_to_dict(header, values)
        for values in values_list
    ]


def convert_environment_variable(value):
    """
    Value can be an environment variable formatted as %MY_ENV_VARIABLE%
    """
    environment_variables_match = re.match('^%(.*)%$', value)
    if environment_variables_match:
        environment_variable = environment_variables_match.group(1)
        return os.environ[environment_variable]
    return value


class ConfigSection:
    def __init__(self, service_name, service_config):
        """
        Load service information from configuration.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param service_config: Dictionary containing service details.
        """
        self.name = service_name
        self.requested_methods = service_config.get('methods', ['get', 'post', 'put', 'delete', 'patch', 'options', 'head'])
        self.connect_timeout = service_config.get('connect_timeout', 1)
        self.read_timeout = service_config.get('read_timeout')
        udf = service_config.get('udf', {})
        # UDFs will be auto expanded by default (if required, ie: result does not fit in a single cell)
        self.udf_return_types = udf.get('return_types', ['async_auto_expand'])
        self.shift_result = udf.get('shift_result', True)
        self.max_retries = service_config.get('max_retries', 5)
        self.custom_headers = {key: convert_environment_variable(value) for key, value in service_config.get('headers', {}).items()}
        self.proxies = service_config.get('proxies', {})
        self.oauth2 = service_config.get('oauth2', {})
        self.basic = service_config.get('basic', {})
        self.api_key = service_config.get('api_key')
        if self.api_key:
            self.api_key = convert_environment_variable(self.api_key)
        self.ntlm_auth = service_config.get('ntlm', {})

    def is_asynchronous(self, udf_return_type):
        return 'async_auto_expand' == udf_return_type

    def auto_expand_result(self, udf_return_type):
        return udf_return_type.endswith('_auto_expand')

    def udf_prefix(self, udf_return_type):
        service_name_prefix = to_valid_python_vba(self.name)
        if (len(self.udf_return_types) == 1) or self.auto_expand_result(udf_return_type):
            return service_name_prefix
        return 'vba_{0}'.format(service_name_prefix)


class ServiceConfigSection(ConfigSection):
    def __init__(self, service_name, service_config):
        """
        Load service information from configuration.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param service_config: Dictionary containing service details.
        """
        ConfigSection.__init__(self, service_name, service_config)
        open_api = service_config.get('open_api', None)
        if not open_api:
            raise MandatoryPropertyNotProvided(service_name, 'open_api')

        self.open_api_definition = open_api.get('definition', None)
        if not self.open_api_definition:
            raise MandatoryPropertyNotProvided(service_name, 'open_api/definition')

        self.open_api_definition_url_parsed = urlsplit(self.open_api_definition)
        self.definition_read_timeout = open_api.get('definition_read_timeout', 5)
        self.service_host = open_api.get('service_host', self.open_api_definition_url_parsed.netloc)
        self.rely_on_definitions = open_api.get('rely_on_definitions')
        self.selected_tags = open_api.get('selected_tags', [])
        self.excluded_tags = open_api.get('excluded_tags', [])
        self.excluded_operation_ids = open_api.get('excluded_operation_ids', [])
        self.selected_operation_ids = open_api.get('selected_operation_ids', [])
        self.excluded_parameters = open_api.get('excluded_parameters', [])
        self.selected_parameters = open_api.get('selected_parameters', [])

    def _allow_tags(self, method_tags):
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

    def _allow_operation_id(self, method_operation_id):
        if not method_operation_id:
            return True

        if self.excluded_operation_ids:
            for excluded_operation_id in self.excluded_operation_ids:
                try:
                    if re.match(to_valid_regex(excluded_operation_id), method_operation_id):
                        return False
                except:  # Handle non regex values
                    pass

        if self.selected_operation_ids:
            for selected_operation_id in self.selected_operation_ids:
                try:
                    if re.match(to_valid_regex(selected_operation_id), method_operation_id):
                        return True
                except:  # Handle non regex values
                    pass
            return False

        return True

    def allow_parameter(self, parameter_name):
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

    def should_provide_method(self, http_verb, open_api_method):
        if http_verb not in self.requested_methods:
            return False
        return self._allow_tags(open_api_method.get('tags')) \
               and self._allow_operation_id(open_api_method.get('operationId')) \
               and return_type_can_be_handled(open_api_method.get('produces', []))


class PyxelRestConfigSection(ConfigSection):
    def __init__(self, service_name, service_config):
        """
        Load service information from configuration.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param service_config: Dictionary containing service details.
        """
        ConfigSection.__init__(self, service_name, service_config)
        self.rely_on_definitions = False

    def should_provide_method(self, http_verb):
        return http_verb in self.requested_methods

    def allow_parameter(self, parameter_name):
        return True


class PyxelRestService:
    def __init__(self, service_name, service_config, flattenize):
        """
        Load service information from configuration.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param service_config: Dictionary containing service details.
        :param flattenize: Flatten results so that it can be consumed by Microsoft Excel.
        """
        self.flattenize = flattenize
        self.methods = {}
        self.uri = ''
        self.config = PyxelRestConfigSection(service_name, service_config)
        self.existing_operation_ids = {udf_return_type: [] for udf_return_type in self.config.udf_return_types}
        self.open_api_definitions = {}
        self.open_api_definition = {
            'securityDefinitions': {
                'oauth2_implicit': {
                    'type': 'oauth2',
                    'flow': 'implicit',
                },
                'api_key_header': {
                    'type': 'apiKey',
                    'in': 'header',
                },
                'api_key_query': {
                    'type': 'apiKey',
                    'in': 'query',
                },
                'basic': {
                    'type': 'basic',
                },
            }
        }

    def create_method(self, http_method, udf_return_type):
        udf = PyxelRestUDFMethod(self, http_method, udf_return_type)
        self.methods[udf.udf_name] = udf
        return udf


class UDFMethod:
    def __init__(self, service, http_method, path, udf_return_type):
        self.service = service
        self.requests_method = http_method
        self.uri = '{0}{1}'.format(service.uri, path)
        self.help_url = ''
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
            if udf_parameter.location == 'path':
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

    def _create_udf_parameters(self):
        return []

    def update_information_on_parameter_type(self, parameter):
        if parameter.location == 'body':
            self.contains_body_parameters = True
        elif parameter.location == 'formData':
            if parameter.type == 'file':
                self.contains_file_parameters = True
            else:
                self.contains_body_parameters = True
        elif parameter.location == 'query':
            self.contains_query_parameters = True

    def has_path_parameters(self):
        return len(self.path_parameters) > 0

    def has_required_parameters(self):
        return len(self.required_parameters) > 0

    def has_optional_parameters(self):
        return len(self.optional_parameters) > 0

    def initial_header(self):
        """
        Initial header content
        For more details refer to https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
        """
        return self.service.config.custom_headers

    def requires_authentication(self, request_content):
        return self.security(request_content) or self.service.config.ntlm_auth

    def security(self, request_content):
        pass


class UDFParameter:
    def __init__(self, name, server_param_name, location, required, field_type):
        self.name = name
        self.server_param_name = server_param_name
        self.location = location
        self.required = required
        self.type = field_type
        self.array_dimension = 0

    def validate(self, request_content):
        pass

    def validate_required(self, value, request_content):
        if value is None or isinstance(value, list) and all(x is None for x in value):
            raise self._not_provided()
        self.validate_optional(value, request_content)

    def validate_optional(self, value, request_content):
        pass

    def _not_provided(self):
        return Exception('{0} is required.'.format(self.name))


class PyxelRestUDFMethod(UDFMethod):
    class ParseBodyAsParameter(UDFParameter):
        def __init__(self):
            UDFParameter.__init__(
                self,
                'parse_body_as',
                'parse_body_as',
                '',
                False,
                'string'
            )
            self.choices = ['dict', 'dict_list']
            self.description = 'How the body should be sent ({0}).'.format(self.choices)

        def _convert_to_str(self, value):
            if isinstance(value, datetime.date):
                raise Exception('{0} value "{1}" must be formatted as text.'.format(self.name, value))
            if isinstance(value, int) or isinstance(value, float):
                value = str(value)
            if value and value not in self.choices:
                raise Exception('{0} value "{1}" should be {2}.'.format(self.name, value, ' or '.join(self.choices)))
            return value

        def validate_optional(self, value, request_content):
            if value is not None:
                value = self._convert_to_str(value)
            request_content.add_value(self, value)

    class WaitForStatusParameter(UDFParameter):
        def __init__(self):
            UDFParameter.__init__(
                self,
                'wait_for_status',
                'wait_for_status',
                '',
                False,
                'integer'
            )
            self.description = 'HTTP status code to wait for before returning response.'

        def _convert_to_int(self, value):
            if not isinstance(value, int):
                raise Exception('{0} value "{1}" must be an integer.'.format(self.name, value))
            if value < 0:
                raise Exception('{0} value "{1}" must be superior or equals to 0.'.format(self.name, value))
            return value

        def validate_optional(self, value, request_content):
            if value is not None:
                value = self._convert_to_int(value)
            request_content.add_value(self, value)

    class CheckIntervalParameter(UDFParameter):
        def __init__(self):
            UDFParameter.__init__(
                self,
                'check_interval',
                'check_interval',
                '',
                False,
                'integer'
            )
            self.description = 'Number of seconds to wait before sending a new request. Wait for 30 seconds by default.'

        def _convert_to_int(self, value):
            if not isinstance(value, int):
                raise Exception('{0} value "{1}" must be an integer.'.format(self.name, value))
            if value < 0:
                raise Exception('{0} value "{1}" must be superior or equals to 0.'.format(self.name, value))
            return value

        def validate_optional(self, value, request_content):
            if value is not None:
                value = self._convert_to_int(value)
            else:
                value = 30
            request_content.add_value(self, value)

    class UrlParameter(UDFParameter):
        def __init__(self):
            UDFParameter.__init__(
                self,
                'url',
                'url',
                'path',
                True,
                'string'
            )
            self.description = 'URL to query.'

        def _convert_to_str(self, value):
            if isinstance(value, datetime.date):
                raise Exception('{0} value "{1}" must be formatted as text.'.format(self.name, value))
            if isinstance(value, int) or isinstance(value, float):
                value = str(value)
            return value

        def validate_optional(self, value, request_content):
            if value is not None:
                value = self._convert_to_str(value)
            request_content.add_value(self, value)

    class BodyParameter(UDFParameter):
        def __init__(self):
            UDFParameter.__init__(
                self,
                'body',
                'body',
                'body',
                True,
                'object'
            )
            self.description = 'Content of the body.'

        def validate_optional(self, value, request_content):
            self.received_value = value  # Save value as is to serialize it properly afterwards

        def validate(self, request_content):
            request_content.payload = list_as_json(self.received_value, request_content.extra_parameters.get('parse_body_as'))

    class ExtraHeadersParameter(UDFParameter):
        def __init__(self):
            UDFParameter.__init__(
                self,
                'extra_headers',
                'extra_headers',
                'headers',
                False,
                'object'
            )
            self.description = 'Extra headers to send in the query.'

        def validate_optional(self, value, request_content):
            self.received_value = value  # TODO Validate dict

        def validate(self, request_content):
            if self.received_value:
                request_content.header.update(self.received_value)

    class AuthenticationParameter(UDFParameter):
        def __init__(self):
            UDFParameter.__init__(
                self,
                'auth',
                'auth',
                '',
                False,
                'array'
            )
            self.choices = ['oauth2_implicit', 'api_key_header', 'api_key_query', 'basic']
            self.description = 'Authentication methods to use. ({0})'.format(self.choices)

        def _convert_to_str(self, value):
            if value and value not in self.choices:
                raise Exception('{0} value "{1}" should be {2}.'.format(self.name, value, ' or '.join(self.choices)))
            return value

        def _convert_to_array(self, value):
            if isinstance(value, list):
                return [
                    self._convert_to_str(item)
                    for item in value if item is not None
                ]
            return [self._convert_to_str(value)]

        def validate_optional(self, value, request_content):
            if value is not None:
                value = self._convert_to_array(value)
            request_content.add_value(self, value)

    class OAuth2AuthorizationUrlParameter(UDFParameter):
        def __init__(self):
            UDFParameter.__init__(
                self,
                'oauth2_auth_url',
                'oauth2_auth_url',
                '',
                False,
                'string'
            )
            self.description = 'OAuth2 authorization URL.'

        def _convert_to_str(self, value):
            if isinstance(value, datetime.date):
                raise Exception('{0} value "{1}" must be formatted as text.'.format(self.name, value))
            if isinstance(value, int) or isinstance(value, float):
                value = str(value)
            return value

        def validate_optional(self, value, request_content):
            if value is not None:
                value = self._convert_to_str(value)
            request_content.add_value(self, value)

    class ApiKeyNameParameter(UDFParameter):
        def __init__(self):
            UDFParameter.__init__(
                self,
                'api_key_name',
                'api_key_name',
                '',
                False,
                'string'
            )
            self.description = 'Name of the field containing API key.'

        def _convert_to_str(self, value):
            if isinstance(value, datetime.date):
                raise Exception('{0} value "{1}" must be formatted as text.'.format(self.name, value))
            if isinstance(value, int) or isinstance(value, float):
                value = str(value)
            return value

        def validate_optional(self, value, request_content):
            if value is not None:
                value = self._convert_to_str(value)
            request_content.add_value(self, value)

    def __init__(self, service, http_method, udf_return_type):
        UDFMethod.__init__(self, service, http_method, '{url}', udf_return_type)
        self.udf_name = '{0}_{1}_url'.format(service.config.udf_prefix(udf_return_type), http_method)
        self.responses = {}

    def _create_udf_parameters(self):
        parameters = [
            self.UrlParameter(),
            self.ExtraHeadersParameter(),
            self.WaitForStatusParameter(),
            self.CheckIntervalParameter(),
            self.AuthenticationParameter(),
            self.OAuth2AuthorizationUrlParameter(),
            self.ApiKeyNameParameter(),
        ]

        if self.requests_method in ['post', 'put']:
            parameters.append(self.BodyParameter())
            parameters.append(self.ParseBodyAsParameter())

        return parameters

    def summary(self):
        return 'Send a HTTP {0} request to specified URL.'.format(self.requests_method)

    def return_a_list(self):
        return True

    def security(self, request_content):
        auths = request_content.extra_parameters.get('auth')
        return [{auth: '' for auth in auths}] if auths else []


class OpenAPI:
    def __init__(self, service_name, service_config, flattenize):
        """
        Load service information from configuration and OpenAPI definition.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param service_config: Dictionary containing service details.
        :param flattenize: Flatten results so that it can be consumed by Microsoft Excel.
        """
        self.flattenize = flattenize
        self.methods = {}
        self.config = ServiceConfigSection(service_name, service_config)
        self.existing_operation_ids = {udf_return_type: [] for udf_return_type in self.config.udf_return_types}
        self.open_api_definition = self._retrieve_open_api_definition()
        self.validate_open_api_version()
        self.open_api_definitions = self.open_api_definition.get('definitions') or {}
        # Remove trailing slashes (as paths must starts with a slash)
        self.uri = self._extract_uri().rstrip('/')

    def _extract_uri(self):
        # The default scheme to be used is the one used to access the OpenAPI definition itself.
        scheme = self.open_api_definition.get('schemes', [self.config.open_api_definition_url_parsed.scheme])[0]
        # If the host is not included, the host serving the documentation is to be used (including the port).
        # service_host property is here to handle services behind a reverse proxy
        # (otherwise host will be the reverse proxy one)
        host = self.open_api_definition.get('host', self.config.service_host)
        # Allow user to provide service_host starting with scheme (removing it)
        host_parsed = urlsplit(host)
        if host_parsed.netloc:
            host = host_parsed.netloc + host_parsed.path
        # If it is not included, the API is served directly under the host.
        base_path = self.open_api_definition.get('basePath', None)

        return scheme + '://' + host + base_path if base_path else scheme + '://' + host

    def create_method(self, http_method, open_api_method, method_path, udf_return_type):
        udf = OpenAPIUDFMethod(self, http_method, open_api_method, method_path, udf_return_type)
        self.methods[udf.udf_name] = udf
        return udf

    def _retrieve_open_api_definition(self):
        """
        Retrieve OpenAPI JSON definition from service.
        :return: Dictionary representation of the retrieved Open API JSON definition.
        """
        requests_session = session.get(0)
        requests_session.mount('file://', fileadapter.LocalFileAdapter())
        response = requests_session.get(self.config.open_api_definition, proxies=self.config.proxies, verify=False,
                                        headers=self.config.custom_headers,
                                        timeout=(self.config.connect_timeout, self.config.definition_read_timeout))
        response.raise_for_status()
        # Always keep the order provided by server (for definitions)
        open_api_definition = response.json(object_pairs_hook=OrderedDict)
        self._normalize_methods(open_api_definition)
        return open_api_definition

    # TODO Clean this method as it is too big and a smart refactoring might be needed
    @classmethod
    def _normalize_methods(cls, open_api_definition):
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
                parameter['server_param_name'] = parameter['name']
                parameter['name'] = to_vba_valid_name(parameter['name'])
            return parameters

        def _update_method_parameters():
            method['parameters'] = root_parameters + methods_parameters + _normalise_names(method.get('parameters', []))

            method_parameters_names_per_location = {}
            for parameter in method['parameters']:
                method_parameters_names_per_location.setdefault(parameter['in'], []).append(parameter['name'])

            for location, parameters_names in method_parameters_names_per_location.items():
                if len(set(parameters_names)) != len(parameters_names):
                    raise DuplicatedParameters(method)

        def _update_method_produces():
            method['produces'] = root_produces + methods_produces + method.get('produces', [])

        def _update_method_security():
            method['security'] = root_security + methods_security + method.get('security', [])

        def _update_method_consumes():
            method['consumes'] = root_consumes + methods_consumes + method.get('consumes', [])

        root_parameters = _normalise_names(open_api_definition.get('parameters', []))
        root_produces = open_api_definition.get('produces', [])
        root_security = open_api_definition.get('security', [])
        root_consumes = open_api_definition.get('consumes', [])

        for methods in open_api_definition['paths'].values():
            # retrieve parameters listed at the path level
            methods_parameters = _normalise_names(methods.pop('parameters', []))
            methods_produces = methods.pop('produces', [])
            methods_security = methods.pop('security', [])
            methods_consumes = methods.pop('consumes', [])

            for mode, method in methods.items():
                _update_method_parameters()
                _update_method_produces()
                _update_method_security()
                _update_method_consumes()

    def get_unique_operation_id(self, udf_return_type, potential_duplicated_operation_id):
        unique_operation_id = potential_duplicated_operation_id  # At this time, this might not be unique
        if potential_duplicated_operation_id in self.existing_operation_ids[udf_return_type]:
            logger.warning('Duplicated operationId found: {0}.'.format(potential_duplicated_operation_id))
            unique_operation_id = 'duplicated_{0}'.format(potential_duplicated_operation_id)

        self.existing_operation_ids[udf_return_type].append(unique_operation_id)
        return unique_operation_id

    def validate_open_api_version(self):
        if 'swagger' not in self.open_api_definition:
            raise OpenAPIVersionNotProvided()
        if self.open_api_definition['swagger'] != '2.0':
            raise UnsupportedOpenAPIVersion(self.open_api_definition['swagger'])

    def __str__(self):
        if self.config.ntlm_auth:
            return '[{0}] service. {1} ({2})'.format(self.config.name, self.uri, self.config.ntlm_auth)
        return '[{0}] service. {1}'.format(self.config.name, self.uri)


class OpenAPIUDFMethod(UDFMethod):
    def __init__(self, service, http_method, open_api_method, path, udf_return_type):
        self.open_api_method = open_api_method
        UDFMethod.__init__(self, service, http_method, path, udf_return_type)
        # Uses "or" in case OpenAPI definition contains None in description (explicitly set by service)
        self.help_url = self.extract_url(open_api_method.get('description') or '')
        self._compute_operation_id(udf_return_type, path)
        self.udf_name = '{0}_{1}'.format(service.config.udf_prefix(udf_return_type), self.open_api_method['operationId'])
        self.responses = open_api_method.get('responses')
        if not self.responses:
            raise EmptyResponses(self.udf_name)

    def _create_udf_parameters(self):
        udf_parameters = []
        for open_api_parameter in self.open_api_method.get('parameters', []):
            udf_parameters.extend(self._to_parameters(open_api_parameter))
        self._avoid_duplicated_names(udf_parameters)
        return udf_parameters

    def _compute_operation_id(self, udf_return_type, path):
        """
        Compute the operationId OpenAPI field (as it may not be provided).
        Also ensure that there is no duplicate (in case a computed one matches a provided one)

        :param path: path provided in OpenAPI definition for this method
        """
        operation_id = self.open_api_method.get('operationId') or \
                       '{0}{1}'.format(self.requests_method, path.replace('/', '_'))
        self.open_api_method['operationId'] = self.service.get_unique_operation_id(udf_return_type, operation_id)

    def return_a_list(self):
        return ('application/json' in self.open_api_method['produces']) or \
               ('application/msgpackpandas' in self.open_api_method['produces'])

    def security(self, request_content):
        return self.open_api_method.get('security')

    def summary(self):
        return self.open_api_method.get('summary')

    def initial_header(self):
        """
        Initial header content
        For more details refer to https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
        """
        header = {}

        if self.contains_body_parameters:
            consumes = self.open_api_method.get('consumes')
            if not consumes or 'application/json' in consumes:
                header['Content-Type'] = 'application/json'
            else:
                logger.warning('{0} is expecting {0} encoded body. '
                               'For now PyxelRest only send JSON body so request might fail.'.format(
                    self.uri,
                    self.open_api_method['consumes']
                ))

        if 'application/msgpackpandas' in self.open_api_method['produces'] and support_pandas():
            header['Accept'] = 'application/msgpackpandas'
        elif 'application/json' in self.open_api_method['produces']:
            header['Accept'] = 'application/json'

        header.update(self.service.config.custom_headers)

        return header

    @staticmethod
    def extract_url(text):
        """
        OpenAPI URLs are interpreted thanks to the following format:
        [description of the url](url)
        :return: URL or None if no URL can be found.
        """
        urls = re.findall('^.*\[.*\]\((.*)\).*$', text)
        if urls:
            return urls[0]

    def _to_parameters(self, open_api_parameter):
        if 'type' in open_api_parameter:  # Type usually means that this is not a complex type
            return [APIUDFParameter(open_api_parameter, {})]

        schema = open_api_parameter['schema']
        ref = schema['$ref'] if '$ref' in schema else schema['items'].get('$ref', '')
        ref = ref[len('#/definitions/'):]
        parameters = []
        open_api_definition = self.service.open_api_definitions.get(ref, {})
        if open_api_definition:
            for inner_parameter_name, inner_parameter in open_api_definition['properties'].items():
                if not inner_parameter.get('readOnly', False):
                    inner_parameter['server_param_name'] = inner_parameter_name
                    inner_parameter['name'] = to_vba_valid_name(inner_parameter_name)
                    inner_parameter['in'] = open_api_parameter['in']
                    inner_parameter['required'] = inner_parameter_name in open_api_definition.get('required', [])
                    parameters.append(APIUDFParameter(inner_parameter, schema))
        else:
            inner_parameter = dict(open_api_parameter)
            inner_parameter.update(schema['items'])
            inner_parameter['server_param_name'] = None  # Indicate that this is the whole body
            parameters.append(APIUDFParameter(inner_parameter, schema))
        return parameters

    def _avoid_duplicated_names(self, udf_parameters):
        parameters_by_name = {}
        for udf_parameter in udf_parameters:
            parameters_by_name.setdefault(udf_parameter.name, []).append(udf_parameter)
        for parameters in parameters_by_name.values():
            if len(parameters) > 1:
                for parameter in parameters:
                    # Keep original name for body and form as they make the more sense for those location
                    if parameter.location != 'body' and parameter.location != 'formData':
                        parameter.name = '{0}_{1}'.format(parameter.location, parameter.name)
        # Ensure that names are not duplicated anymore
        if len(parameters_by_name) != len(udf_parameters):
            self._avoid_duplicated_names(udf_parameters)


class APIUDFParameter(UDFParameter):
    def __init__(self, open_api_parameter, schema):
        UDFParameter.__init__(
            self,
            open_api_parameter['name'],
            open_api_parameter['server_param_name'],
            open_api_parameter['in'],  # path, body, formData, query, header
            open_api_parameter.get('required'),
            open_api_parameter.get('type')  # file (formData location), integer, number, string, boolean, array
        )
        self.schema = schema
        self.choices = open_api_parameter.get('enum')  # string type
        self.default_value = open_api_parameter.get('default')
        self.format = open_api_parameter.get('format')  # date (string type), date-time (string type)
        self.maximum = open_api_parameter.get('maximum')  # Apply to integer and number
        self.exclusive_maximum = open_api_parameter.get('exclusiveMaximum')  # Apply to integer and number
        self.minimum = open_api_parameter.get('minimum')  # Apply to integer and number
        self.exclusive_minimum = open_api_parameter.get('exclusiveMinimum')  # Apply to integer and number
        self.max_length = open_api_parameter.get('maxLength')  # Apply to string
        self.min_length = open_api_parameter.get('minLength')  # Apply to string
        self.max_items = open_api_parameter.get('maxItems')  # Apply to array
        self.min_items = open_api_parameter.get('minItems')  # Apply to array
        self.unique_items = open_api_parameter.get('uniqueItems')  # Apply to array
        self.multiple_of = open_api_parameter.get('multipleOf')  # Apply to integer and number
        self.collection_format = open_api_parameter.get('collectionFormat')  # Apply to arrays

        open_api_array_parameter = self._get_open_api_array_parameter(open_api_parameter)
        if open_api_array_parameter:
            if open_api_array_parameter.get('type') == 'object' or ('$ref' in open_api_array_parameter):
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

    def validate_optional(self, value, request_content):
        if value is not None:
            value = self._convert_to_type(value)
        request_content.add_value(self, value)

    def _get_open_api_array_parameter(self, open_api_parameter):
        if self.type == 'array':
            open_api_array_parameter = dict(open_api_parameter)
            open_api_array_parameter.update(open_api_parameter['items'])
            return open_api_array_parameter
        elif self.schema.get('type') == 'array':
            open_api_array_parameter = dict(open_api_parameter)
            self.collection_format = self.schema.get('collectionFormat')
            return open_api_array_parameter

    def _convert_to_int(self, value):
        if not isinstance(value, int):
            raise Exception('{0} value "{1}" ({2} type) must be an integer.'.format(self.name, value, type(value)))
        self._check_number(value)
        return value

    def _check_number(self, value):
        if self.maximum is not None:
            if self.exclusive_maximum:
                if value >= self.maximum:
                    raise Exception('{0} value "{1}" must be strictly inferior to {2}.'.format(self.name, value, self.maximum))
            else:
                if value > self.maximum:
                    raise Exception('{0} value "{1}" must be inferior or equals to {2}.'.format(self.name, value, self.maximum))

        if self.minimum is not None:
            if self.exclusive_minimum:
                if value <= self.minimum:
                    raise Exception('{0} value "{1}" must be strictly superior to {2}.'.format(self.name, value, self.minimum))
            else:
                if value < self.minimum:
                    raise Exception('{0} value "{1}" must be superior or equals to {2}.'.format(self.name, value, self.minimum))

        if self.multiple_of:
            if (value % self.multiple_of) == 0:
                raise Exception('{0} value "{1}" must be a multiple of {2}.'.format(self.name, value, self.multiple_of))

    def _convert_to_float(self, value):
        if not isinstance(value, float):
            raise Exception('{0} value "{1}" ({2} type) must be a number.'.format(self.name, value, type(value)))
        self._check_number(value)
        return value

    def _convert_to_date(self, value):
        if not isinstance(value, datetime.date):
            raise Exception('{0} value "{1}" ({2} type) must be a date.'.format(self.name, value, type(value)))
        return value

    def _convert_to_date_time(self, value):
        if not isinstance(value, datetime.datetime):
            raise Exception('{0} value "{1}" ({2} type) must be a date time.'.format(self.name, value, type(value)))
        return value.isoformat()

    def _convert_to_str(self, value):
        if isinstance(value, datetime.date):
            raise Exception('{0} value "{1}" ({2} type) must be formatted as text.'.format(self.name, value, type(value)))
        if isinstance(value, int):
            value = str(value)
        if isinstance(value, float):
            # Send float values without decimal as int string values
            if value == float(int(value)):
                value = str(int(value))
            else:
                value = str(value)
        if self.choices and value not in self.choices:
            raise Exception('{0} value "{1}" should be {2}.'.format(self.name, value, ' or '.join(self.choices)))
        if self.max_length is not None:
            if len(value) > self.max_length:
                raise Exception('{0} value "{1}" cannot contains more than {2} characters.'.format(self.name, value, self.max_length))
        if self.min_length is not None:
            if len(value) < self.min_length:
                raise Exception('{0} value "{1}" cannot contains less than {2} characters.'.format(self.name, value, self.min_length))
        return value

    def _convert_to_bool(self, value):
        if not isinstance(value, bool):
            raise Exception('{0} value "{1}" ({2} type) must be a boolean.'.format(self.name, value, type(value)))
        return value

    def _convert_to_dict(self, value):
        if not isinstance(value, list):
            raise Exception('{0} value "{1}" ({2} type) must be a list.'.format(self.name, value, type(value)))
        if len(value) != 2:
            raise Exception('{0} value should contains only two rows. Header and values.'.format(self.name))
        return list_to_dict(value[0], value[1])

    def _convert_to_dict_list(self, value):
        if not isinstance(value, list):
            raise Exception('{0} value "{1}" ({2} type) must be a list.'.format(self.name, value, type(value)))
        if len(value) < 2:
            raise Exception('{0} value should contains at least two rows. Header and values.'.format(self.name))
        list_value = list_to_dict_list(value[0], value[1:])
        self._check_array(list_value)
        return list_value

    def _convert_to_file(self, value):
        if os.path.isfile(value):  # Can be a path to a file
            return open(value, 'rb')
        return self.server_param_name, value  # Or the content of the file

    def _convert_to_array(self, value):
        if isinstance(value, list):
            list_value = self._convert_list_to_array(value)
        else:
            list_value = [
                self.array_parameter._convert_to_type(value)
            ]
        self._check_array(list_value)
        return self._apply_collection_format(list_value)

    def _convert_list_to_array(self, list_value):
        return [
            self.array_parameter._convert_to_type(list_item) if list_item is not None else None
            for list_item in list_value
        ]

    def _apply_collection_format(self, list_value):
        if not self.collection_format or 'csv' == self.collection_format:
            return ','.join([str(value) for value in list_value])
        if 'multi' == self.collection_format:
            return list_value  # requests module will send one parameter per item in list
        if 'ssv' == self.collection_format:
            return ' '.join([str(value) for value in list_value])
        if 'tsv' == self.collection_format:
            return '\t'.join([str(value) for value in list_value])
        if 'pipes' == self.collection_format:
            return '|'.join([str(value) for value in list_value])
        raise Exception('Collection format {0} is invalid.'.format(self.collection_format))

    def _check_array(self, value):
        if self.unique_items:
            if len(set(value)) != len(value):
                raise Exception('{0} contains duplicated items.'.format(self.name))

        if self.max_items is not None:
            if len(value) > self.max_items:
                raise Exception('{0} cannot contains more than {1} items.'.format(self.name, self.max_items))

        if self.min_items is not None:
            if len(value) < self.min_items:
                raise Exception('{0} cannot contains less than {1} items.'.format(self.name, self.min_items))

    def _get_convert_method(self):
        if self.type == 'integer':
            return self._convert_to_int
        elif self.type == 'number':
            return self._convert_to_float
        elif self.type == 'string':
            if self.format == 'date':
                return self._convert_to_date
            elif self.format == 'date-time':
                return self._convert_to_date_time
            return self._convert_to_str
        elif self.type == 'boolean':
            return self._convert_to_bool
        elif self.type == 'object':
            return self._convert_to_dict
        elif self.type == 'file':
            return self._convert_to_file
        return lambda value: value  # Unhandled type, best effort

    def _common_documentation(self, open_api_parameter):
        description = open_api_parameter.get('description', '') or ''
        if self.choices:
            description += ' Valid values are: {0}.'.format(', '.join(self.choices))
        if self.default_value:
            description += ' Default value is: {0}.'.format(self.default_value)
        return description

    def _get_documentation(self, open_api_parameter):
        description = self._common_documentation(open_api_parameter)
        if self.type == 'integer':
            description += '\nValue must be an integer.'
        elif self.type == 'number':
            description += '\nValue must be a number.'
        elif self.type == 'string':
            if self.format == 'date':
                description += '\nValue must be formatted as date.'
            elif self.format == 'date-time':
                description += '\nValue must be formatted as date-time.'
            else:
                description += '\nValue must be formatted as text.'
        elif self.type == 'boolean':
            description += '\nValue must be formatted as boolean.'
        elif self.type == 'object':
            description += '\nValue must be an array of two rows (field names, values).'
        elif self.type == 'file':
            description += '\nValue must be the content of the file or the file path.'
        return description.replace('\'', '')

    def _get_dict_list_documentation(self, open_api_parameter):
        description = self._common_documentation(open_api_parameter)
        description += '\nValue must be an array of at least two rows (field names, values).'
        return description.replace('\'', '')

    def _get_list_documentation(self, open_api_parameter):
        description = self._common_documentation(open_api_parameter)
        if self.array_parameter.type == 'integer':
            description += '\nValue must be an array of integers.'
        elif self.array_parameter.type == 'number':
            description += '\nValue must be an array of numbers.'
        elif self.array_parameter.type == 'string':
            if self.array_parameter.format == 'date':
                description += '\nValue must be an array of date formatted cells.'
            elif self.array_parameter.format == 'date-time':
                description += '\nValue must be an array of date-time formatted cells.'
            else:
                description += '\nValue must be an array of text formatted cells.'
        elif self.array_parameter.type == 'boolean':
            description += '\nValue must be an array of boolean formatted cells.'
        elif self.array_parameter.type == 'file':
            description += '\nValue must be an array of cells with files content or files paths.'
        return description.replace('\'', '')


class RequestContent:
    def __init__(self, udf_method):
        self.udf_method = udf_method
        self.header = udf_method.initial_header()
        self.payload = {}
        self.files = {}
        self.parameters = {}
        self.path_values = {}
        # Contains parameters that were not provided but may still need to be sent with None value
        self._none_parameters = []
        # Parameters that should not be sent by interpreted by pyxelrest
        self.extra_parameters = {}

    def validate(self):
        for udf_parameter in self.udf_method.parameters.values():
            udf_parameter.validate(self)

    def add_value(self, parameter, value):
        if parameter.location == 'query':
            self._add_query_parameter(parameter, value)
        elif parameter.location == 'body':
            self._add_body_parameter(parameter, value)
        elif parameter.location == 'formData':
            self._add_form_parameter(parameter, value)
        elif parameter.location == 'header':
            self._add_header_parameter(parameter, value)
        elif parameter.location == 'path':
            self._add_path_parameter(parameter, value)
        elif parameter.location == '':
            self._add_extra_parameter(parameter, value)

    def _add_query_parameter(self, parameter, value):
        if value is not None:
            self.parameters[parameter.server_param_name] = value

    def _add_extra_parameter(self, parameter, value):
        self.extra_parameters[parameter.server_param_name] = value

    def _add_path_parameter(self, parameter, value):
        self.path_values[parameter.server_param_name] = value

    def _add_body_parameter(self, parameter, value):
        if parameter.schema.get('type') == 'array':
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
                    self.payload[index][parameter.server_param_name] = parameter_list_item

            # All items will be updated with a new provided value and new items will be added
            elif nb_values > nb_list_items:
                # Add empty items to current payload so that length fits the new one
                empty_item = {
                    field_name: None
                    for field_name in self.payload[0]
                } if nb_list_items > 0 else {
                    none_parameter.server_param_name: None
                    for none_parameter in self._none_parameters
                }
                self._none_parameters.clear()
                for new_index in range(nb_list_items, nb_values):
                    self.payload.append(dict(empty_item))

                for index, parameter_list_item in enumerate(value):
                    if parameter.server_param_name:
                        self.payload[index][parameter.server_param_name] = parameter_list_item
                    else:
                        self.payload[index] = parameter_list_item

            # Some items will be updated with a new provided value and remaining will contains None
            else:
                for index, parameter_list_item in enumerate(value):
                    self.payload[index][parameter.server_param_name] = parameter_list_item

                for non_provided_index in range(nb_values, nb_list_items):
                    self.payload[non_provided_index][parameter.server_param_name] = None

    def _add_form_parameter(self, parameter, value):
        if parameter.type == 'file':
            if value is not None:
                self.files[parameter.server_param_name] = value
        else:
            self.payload[parameter.server_param_name] = value

    def _add_header_parameter(self, parameter, value):
        if value is not None:
            self.header[parameter.server_param_name] = value


def load_services(flattenize=True):
    """
    Retrieve OpenAPI JSON definition for each service defined in configuration file.
    :return: List of OpenAPI and PyxelRestService instances, size is the same one as the number of sections within configuration file
    """
    if not os.path.isfile(SERVICES_CONFIGURATION_FILE_PATH):
        raise ConfigurationFileNotFound(SERVICES_CONFIGURATION_FILE_PATH)

    with open(SERVICES_CONFIGURATION_FILE_PATH, 'r') as config_file:
        config = yaml.load(config_file)

    logging.debug('Loading services from "{0}"...'.format(SERVICES_CONFIGURATION_FILE_PATH))
    loaded_services = []
    for service_name, service_config in config.items():
        if 'pyxelrest' == service_name:
            pyxelrest_service = PyxelRestService(service_name, service_config, flattenize)
            loaded_services.append(pyxelrest_service)
        else:
            service = load_service(service_name, service_config, flattenize)
            if service:
                loaded_services.append(service)

    check_for_duplicates(loaded_services)
    return loaded_services


def load_service(service_name, service_config, flattenize):
    logger.debug('Loading "{0}" service...'.format(service_name))
    try:
        service = OpenAPI(service_name, service_config, flattenize)
        logger.info('"{0}" service will be available.'.format(service_name))
        logger.debug(str(service))
        return service
    except Exception as e:
        logger.error('"{0}" service will not be available: {1}'.format(service_name, e))


def check_for_duplicates(loaded_services):
    services_by_prefix = {}
    for service in loaded_services:
        for udf_return_type in service.config.udf_return_types:
            services_by_prefix.setdefault(service.config.udf_prefix(udf_return_type), []).append(service.config.name)
    for udf_prefix in services_by_prefix:
        service_names = services_by_prefix[udf_prefix]
        if len(service_names) > 1:
            logger.warning('{0} services will use the same "{1}" prefix, in case there is the same call available, '
                           'only the last declared one will be available.'.format(service_names, udf_prefix))


def get_result(udf_method, request_content):
    response = None
    try:
        response = session.get(udf_method.service.config.max_retries).request(
            udf_method.requests_method,
            udf_method.uri.format(**request_content.path_values),
            json=request_content.payload if udf_method.contains_body_parameters else None,
            params=request_content.parameters if udf_method.contains_query_parameters else None,
            files=request_content.files if udf_method.contains_file_parameters else None,
            auth=authentication.get_auth(udf_method, request_content),
            verify=False,
            headers=request_content.header,
            proxies=udf_method.service.config.proxies,
            timeout=(udf_method.service.config.connect_timeout, udf_method.service.config.read_timeout)
        )
        response.raise_for_status()

        # Wait for a specific status if needed
        wait_for_status = request_content.extra_parameters.get('wait_for_status')
        if wait_for_status:
            if not response.history or (response.history[0].status_code != wait_for_status):
                check_interval = request_content.extra_parameters['check_interval']
                logger.info('Waiting for {0} status. Sending a new request in {1} seconds.'.format(wait_for_status, check_interval))
                time.sleep(check_interval)
                return get_result(udf_method, request_content)

        logger.info('[status=Valid] response received for [function={1}] [url={0}].'.format(response.request.url, udf_method.udf_name))
        if 202 == response.status_code:
            return shift_result([['Status URL'], [response.headers['location']]], udf_method)
        if response.headers['content-type'] == 'application/json':
            return shift_result(json_as_list(response, udf_method), udf_method)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return shift_result(msgpackpandas_as_list(response.content), udf_method)
        else:
            return shift_result(convert_to_return_type(response.text[:255], udf_method), udf_method)
    except requests.exceptions.ConnectionError:
        logger.exception('Connection [status=error] occurred while calling [function={0}] [url={1}].'.format(udf_method.udf_name, udf_method.uri))
        return shift_result(convert_to_return_type('Cannot connect to service. Please retry once connection is re-established.', udf_method), udf_method)
    except Exception as error:
        # Check "is not None" because response.ok is overridden according to HTTP status code.
        if response is not None:
            logger.exception('[status=Error] occurred while handling [function={0}] [url={1}] response: [response={2}].'.format(udf_method.udf_name, response.request.url, response.text[:64]))
        else:
            logger.exception('[status=Error] occurred while calling [function={0}] [url={1}].'.format(udf_method.udf_name, udf_method.uri))
        return shift_result(convert_to_return_type(describe_error(response, error), udf_method), udf_method)
    finally:
        # Check "is not None" because response.ok is overridden according to HTTP status code.
        if response is not None:
            response.close()


class DelayWrite(object):
    def __init__(self, rng, options, value, skip):
        self.range = rng
        self.options = options
        self.value = value
        self.skip = skip

    def __call__(self, *args, **kwargs):
        xlwings.conversion.write(
            self.value,
            self.range,
            xlwings.conversion.Options(self.options)
            .override(_skip_tl_cells=self.skip)
        )


def get_result_async(udf_method, request_content, excel_caller):
    def get_and_send_result(excel_range, nb_rows, nb_columns):
        try:
            result = get_result(udf_method, request_content)
            xlwings.server.add_idle_task(DelayWrite(excel_range, {'expand': 'table'}, result, (nb_rows, nb_columns)))
        except:
            logger.exception('[status=Error] occurred while calling [function={0}] [url={1}].'.format(udf_method.udf_name, udf_method.uri))
    try:
        if not hasattr(excel_caller, 'Rows'):
            return convert_to_return_type('Asynchronous UDF called from VBA.', udf_method)
        excel_range = xlwings.Range(impl=xlwings.xlplatform.Range(xl=excel_caller))
        threading.Thread(
            target=get_and_send_result,
            args=(excel_range, excel_caller.Rows.Count, excel_caller.Columns.Count)
        ).start()
        return shift_result(['Processing request...'], udf_method)
    except Exception as error:
        logger.exception('[status=Error] occurred while calling [function={0}] [url={1}].'.format(udf_method.udf_name, udf_method.uri))
        return convert_to_return_type(describe_error(None, error), udf_method)


def convert_to_return_type(str_value, udf_method):
    return [str_value] if udf_method.return_a_list() else str_value


def describe_error(response, error):
    # Check "is not None" because response.ok is overridden according to HTTP status code.
    if response is not None:
        return 'An error occurred. Please check logs for full details: "{0}"'.format(response.text[:198])
    return 'An error occurred. Please check logs for full details: "{0}"'.format(str(error)[:198])


def json_as_list(response, udf_method):
    if udf_method.service.config.rely_on_definitions:
        definition_deserializer.all_definitions = {}
        if support_ujson():
            response_text = response.text
            logger.debug('Converting JSON string to corresponding python structure using ujson (relying on definitions)...')
            json_data = ujson.loads(response_text) if response_text != '' else response_text
        else:
            logger.debug('Converting JSON string to corresponding python structure (relying on definitions)...')
            json_data = response.json(object_pairs_hook=OrderedDict) if len(response.content) else ''
        all_definitions = udf_method.service.open_api_definitions
        return Response(udf_method.responses, response.status_code, all_definitions).rows(json_data)

    logger.debug('Converting JSON string to corresponding python structure...')
    json_data = response.json(object_pairs_hook=OrderedDict) if len(response.content) else ''
    if udf_method.service.flattenize:
        all_definitions = udf_method.service.open_api_definitions
        return Flattenizer(udf_method.responses, response.status_code, all_definitions).to_list(json_data)
    else:
        return json_data


def msgpackpandas_as_list(msgpack_pandas):
    if support_pandas():
        logger.debug('Converting message pack pandas to list...')
        data = pandas.read_msgpack(msgpack_pandas)
        logger.debug('Converting dictionary to list...')
        if sys.version_info[0] < 3:
            header = [header_name.decode() for header_name in data.columns.values.tolist()]
        else:
            header = data.columns.tolist()
        values = data.values.tolist()
        flatten_data = [header] + values if values else [header]
        logger.debug('Data converted to list.')
        return flatten_data
    else:
        logger.warning('Pandas module is required to decode response.')
        return ['Please install pandas module to be able to decode result.']


def list_as_json(lists, parse_as):
    if 'dict' == parse_as:
        if len(lists) != 2:
            return ['There should be only two rows. Header and values.']
        return list_to_dict(lists[0], lists[1])

    if 'dict_list' == parse_as:
        if len(lists) < 2:
            return ['There should be at least two rows. Header and first dictionary values.']
        return list_to_dict_list(lists[0], lists[1:])

    return lists


def shift_result(result, udf_method):
    if udf_method.service.config.shift_result and udf_method.auto_expand_result:
        if result:
            if isinstance(result[0], list):
                for row in result:
                    row.insert(0, '')
            elif isinstance(result, list):
                result = [['', value] for value in result]
    return result

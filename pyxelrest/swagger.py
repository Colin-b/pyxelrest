from collections import OrderedDict
import datetime
import logging
import os
import re
import requests
import yaml

try:
    # Python 3
    from urllib.parse import urlsplit
except ImportError:
    # Python 2
    from urlparse import urlsplit

from pyxelrest import vba, SERVICES_CONFIGURATION_FILE_PATH
from pyxelrest.pyxelresterrors import *
from pyxelrest import authentication
from pyxelrest import fileadapter


logger = logging.getLogger(__name__)


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


def convert_environment_variable(loader, node):
    """
    Value can be an environment variable formatted as %MY_ENV_VARIABLE%
    """
    value = loader.construct_scalar(node)
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
        self.auth = authentication.add_service_custom_authentication(self.name, service_config)
        # UDFs will be Asynchronous by default (if required, ie: result does not fit in a single cell)
        self.udf_return_types = service_config.get('udf_return_types', ['asynchronous'])
        self.max_retries = service_config.get('max_retries', 5)
        self.custom_headers = service_config.get('headers', {})
        self.proxies = service_config.get('proxies', {})

    def is_asynchronous(self, udf_return_type):
        return udf_return_type == 'asynchronous'

    def udf_prefix(self, udf_return_type):
        service_name_prefix = to_valid_python_vba(self.name)
        if (len(self.udf_return_types) == 1) or self.is_asynchronous(udf_return_type):
            return service_name_prefix
        return 'sync_{0}'.format(service_name_prefix)


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
        self.tags = open_api.get('tags', [])

    def _allow_tags(self, method_tags):
        if not self.tags or not method_tags:
            return True
        for method_tag in method_tags:
            if method_tag in self.tags:
                return True
        return False

    def should_provide_method(self, http_verb, open_api_method):
        if http_verb not in self.requested_methods:
            return False
        return self._allow_tags(open_api_method.get('tags')) and return_type_can_be_handled(
            open_api_method.get('produces', []))


class PyxelRestConfigSection(ConfigSection):
    def __init__(self, service_name, service_config):
        """
        Load service information from configuration.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param service_config: Dictionary containing service details.
        """
        ConfigSection.__init__(self, service_name, service_config)

    def should_provide_method(self, http_verb):
        return http_verb in self.requested_methods


class OpenAPI:
    def __init__(self, service_name, service_config):
        """
        Load service information from configuration and OpenAPI definition.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param service_config: Dictionary containing service details.
        """
        self.methods = {}
        self.config = ServiceConfigSection(service_name, service_config)
        self.existing_operation_ids = {udf_return_type: [] for udf_return_type in self.config.udf_return_types}
        self.open_api_definition = self._retrieve_open_api_definition()
        self.validate_open_api_version()
        self.open_api_definitions = self.open_api_definition.get('definitions')
        # Remove trailing slashes (as paths must starts with a slash)
        self.uri = self._extract_uri().rstrip('/')
        authentication.add_service_security(self.config.name, self.open_api_definition, service_config)

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
        udf = UDFMethod(self, http_method, open_api_method, method_path, udf_return_type)
        self.methods[udf.udf_name] = udf
        return udf

    def _retrieve_open_api_definition(self):
        """
        Retrieve OpenAPI JSON definition from service.
        :return: Dictionary representation of the retrieved Open API JSON definition.
        """
        requests_session = requests.session()
        requests_session.mount('file://', fileadapter.LocalFileAdapter())
        response = requests_session.get(self.config.open_api_definition, proxies=self.config.proxies, verify=False,
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
        if self.config.auth:
            return '[{0}] service. {1} (custom {2} authentication)'.format(self.config.name, self.uri, self.config.auth)
        return '[{0}] service. {1}'.format(self.config.name, self.uri)


class UDFMethod:
    def __init__(self, service, http_method, open_api_method, path, udf_return_type):
        self.uri = '{0}{1}'.format(service.uri, path)
        self.service = service
        self.requests_method = http_method
        self.open_api_method = open_api_method
        self.is_asynchronous = service.config.is_asynchronous(udf_return_type)
        self.path_parameters = []
        self.required_parameters = []
        self.optional_parameters = []
        self.contains_body_parameters = False
        self.contains_file_parameters = False
        self.contains_query_parameters = False
        udf_parameters = []
        for open_api_parameter in open_api_method.get('parameters', []):
            udf_parameters.extend(self._to_parameters(open_api_parameter))
        self._avoid_duplicated_names(udf_parameters)
        self.parameters = {}
        for udf_parameter in udf_parameters:
            self.parameters[udf_parameter.name] = udf_parameter
            if udf_parameter.location == 'path':
                self.path_parameters.append(udf_parameter)
            # Required but not in path
            elif udf_parameter.required:
                self.update_information_on_parameter_type(udf_parameter)
                self.required_parameters.append(udf_parameter)
            else:
                self.update_information_on_parameter_type(udf_parameter)
                self.optional_parameters.append(udf_parameter)
        # Uses "or" in case OpenAPI definition contains None in description (explicitly set by service)
        self.help_url = UDFMethod.extract_url(open_api_method.get('description') or '')
        self._compute_operation_id(udf_return_type, path)
        self.udf_name = '{0}_{1}'.format(service.config.udf_prefix(udf_return_type), self.open_api_method['operationId'])
        self.responses = open_api_method.get('responses')
        if not self.responses:
            raise EmptyResponses(self.udf_name)

    def _compute_operation_id(self, udf_return_type, path):
        """
        Compute the operationId OpenAPI field (as it may not be provided).
        Also ensure that there is no duplicate (in case a computed one matches a provided one)

        :param path: path provided in OpenAPI definition for this method
        """
        operation_id = self.open_api_method.get('operationId') or \
                       '{0}{1}'.format(self.requests_method, path.replace('/', '_'))
        self.open_api_method['operationId'] = self.service.get_unique_operation_id(udf_return_type, operation_id)

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

    def return_a_list(self):
        return ('application/json' in self.open_api_method['produces']) or \
               ('application/msgpackpandas' in self.open_api_method['produces'])

    def requires_authentication(self):
        return self.security() or self.service.config.auth

    def security(self):
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

    def has_path_parameters(self):
        return len(self.path_parameters) > 0

    def has_required_parameters(self):
        return len(self.required_parameters) > 0

    def has_optional_parameters(self):
        return len(self.optional_parameters) > 0

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
            return [UDFParameter(open_api_parameter, {})]

        schema = open_api_parameter['schema']
        ref = schema['$ref'] if '$ref' in schema else schema['items']['$ref']
        ref = ref[len('#/definitions/'):]
        parameters = []
        open_api_definition = self.service.open_api_definitions[ref]
        for inner_parameter_name, inner_parameter in open_api_definition['properties'].items():
            if not inner_parameter.get('readOnly', False):
                inner_parameter['server_param_name'] = inner_parameter_name
                inner_parameter['name'] = to_vba_valid_name(inner_parameter_name)
                inner_parameter['in'] = open_api_parameter['in']
                inner_parameter['required'] = inner_parameter_name in open_api_definition.get('required', [])
                parameters.append(UDFParameter(inner_parameter, schema))
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


class UDFParameter:
    def __init__(self, open_api_parameter, schema):
        self.name = open_api_parameter['name']
        self.server_param_name = open_api_parameter['server_param_name']
        self.schema = schema
        self.location = open_api_parameter['in']  # path, body, formData, query, header
        self.required = open_api_parameter.get('required')
        self.type = open_api_parameter.get('type')  # file (formData location), integer, number, string, boolean, array
        self.format = open_api_parameter.get('format')  # date (string type), date-time (string type)
        self.choices = open_api_parameter.get('enum')  # string type
        self.default_value = open_api_parameter.get('default')

        open_api_array_parameter = self._get_open_api_array_parameter(open_api_parameter)
        if open_api_array_parameter:
            if open_api_array_parameter.get('type') == 'object' or ('$ref' in open_api_array_parameter):
                self._convert_to_type = self._convert_to_dict_list
                self.description = self._get_dict_list_documentation(open_api_parameter)
            else:
                inner_parameter = UDFParameter(open_api_array_parameter, {})
                self._convert_to_type = self._get_convert_array_method(inner_parameter)
                self.description = self._get_list_documentation(open_api_parameter, inner_parameter)
        else:
            self._convert_to_type = self._get_convert_method()
            self.description = self._get_documentation(open_api_parameter)

    def _get_open_api_array_parameter(self, open_api_parameter):
        if self.type == 'array':
            open_api_array_parameter = dict(open_api_parameter)
            open_api_array_parameter.update(open_api_parameter['items'])
            return open_api_array_parameter
        elif self.schema.get('type') == 'array':
            return dict(open_api_parameter)

    def validate_path(self, value):
        if value is None or isinstance(value, list) and all(x is None for x in value):
            raise self._not_provided()

    def validate_required(self, value, request_content):
        if value is None or isinstance(value, list) and all(x is None for x in value):
            raise self._not_provided()
        self.validate_optional(value, request_content)

    def validate_optional(self, value, request_content):
        if value is not None:
            value = self._convert_to_type(value)
        request_content.add_value(self, value)

    def _not_provided(self):
        return Exception('{0} is required.'.format(self.name))

    def _convert_to_int(self, value):
        if not isinstance(value, int):
            raise Exception('{0} value "{1}" must be an integer.'.format(self.name, value))
        return value

    def _convert_to_float(self, value):
        if not isinstance(value, float):
            raise Exception('{0} value "{1}" must be a number.'.format(self.name, value))
        return value

    def _convert_to_date(self, value):
        if not isinstance(value, datetime.date):
            raise Exception('{0} value "{1}" must be a date.'.format(self.name, value))
        return value

    def _convert_to_date_time(self, value):
        if not isinstance(value, datetime.datetime):
            raise Exception('{0} value "{1}" must be a date time.'.format(self.name, value))
        return value.isoformat()

    def _convert_to_str(self, value):
        if isinstance(value, datetime.date):
            raise Exception('{0} value "{1}" must be formatted as text.'.format(self.name, value))
        if isinstance(value, int) or isinstance(value, float):
            value = str(value)
        if self.choices and value not in self.choices:
            raise Exception('{0} value "{1}" should be {2}.'.format(self.name, value, self.choices.join(' or ')))
        return value

    def _convert_to_bool(self, value):
        if not isinstance(value, bool):
            raise Exception('{0} value "{1}" must be a boolean.'.format(self.name, value))
        return value

    def _convert_to_dict(self, value):
        if not isinstance(value, list):
            raise Exception('{0} value "{1}" must be a list.'.format(self.name, value))
        if len(value) != 2:
            raise Exception('{0} value should contains only two rows. Header and values.'.format(self.name))
        return list_to_dict(value[0], value[1])

    def _convert_to_dict_list(self, value):
        if not isinstance(value, list):
            raise Exception('{0} value "{1}" must be a list.'.format(self.name, value))
        if len(value) < 2:
            raise Exception('{0} value should contains at least two rows. Header and values.'.format(self.name))
        return list_to_dict_list(value[0], value[1:])

    def _convert_to_file(self, value):
        if os.path.isfile(value):  # Can be a path to a file
            return open(value, 'rb')
        return self.server_param_name, value  # Or the content of the file

    def _get_convert_array_method(self, array_parameter):
        return lambda value: [
            array_parameter._convert_to_type(item) if item is not None else None
            for item in value
        ] if isinstance(value, list) else [
            array_parameter._convert_to_type(value)
        ]

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

    def _get_list_documentation(self, open_api_parameter, inner_parameter):
        description = self._common_documentation(open_api_parameter)
        if inner_parameter.type == 'integer':
            description += '\nValue must be an array of integers.'
        elif inner_parameter.type == 'number':
            description += '\nValue must be an array of numbers.'
        elif inner_parameter.type == 'string':
            if inner_parameter.format == 'date':
                description += '\nValue must be an array of date formatted cells.'
            elif inner_parameter.format == 'date-time':
                description += '\nValue must be an array of date-time formatted cells.'
            else:
                description += '\nValue must be an array of text formatted cells.'
        elif inner_parameter.type == 'boolean':
            description += '\nValue must be an array of boolean formatted cells.'
        elif inner_parameter.type == 'file':
            description += '\nValue must be an array of cells with files content or files paths.'
        return description.replace('\'', '')


class RequestContent:
    def __init__(self, open_api_method):
        self.header = open_api_method.initial_header()
        self.payload = {}
        self.files = {}
        self.parameters = {}
        # Contains parameters that were not provided but may still need to be sent with None value
        self._none_parameters = []

    def add_value(self, parameter, value):
        if parameter.location == 'query':
            self._add_query_parameter(parameter, value)
        elif parameter.location == 'body':
            self._add_body_parameter(parameter, value)
        elif parameter.location == 'formData':
            self._add_form_parameter(parameter, value)
        elif parameter.location == 'header':
            self._add_header_parameter(parameter, value)

    def _add_query_parameter(self, parameter, value):
        if value is not None:
            self.parameters[parameter.server_param_name] = value

    def _add_body_parameter(self, parameter, value):
        if parameter.schema.get('type') == 'array':
            self._add_body_list_parameter(parameter, value)
        else:
            self.payload[parameter.server_param_name] = value

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
                    self.payload[index][parameter.server_param_name] = parameter_list_item

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


def support_pandas():
    try:
        import pandas
        return True
    except:
        return False


def load_services():
    """
    Retrieve OpenAPI JSON definition for each service defined in configuration file.
    :return: List of OpenAPI instances, size is the same one as the number of sections within configuration file
    and the loaded pyxelrest configuration if provided
    """
    if not os.path.isfile(SERVICES_CONFIGURATION_FILE_PATH):
        raise ConfigurationFileNotFound(SERVICES_CONFIGURATION_FILE_PATH)

    yaml.add_constructor(u'!environment_variable', convert_environment_variable)
    yaml.add_implicit_resolver(u'!environment_variable', re.compile('^%(.*)%$'))
    with open(SERVICES_CONFIGURATION_FILE_PATH, 'r') as config_file:
        config = yaml.load(config_file)

    logging.debug('Loading services from "{0}"...'.format(SERVICES_CONFIGURATION_FILE_PATH))
    loaded_services = []
    pyxelrest_config = None
    for service_name, service_config in config.items():
        if 'pyxelrest' == service_name:
            pyxelrest_config = PyxelRestConfigSection(service_name, service_config)
        else:
            service = load_service(service_name, service_config)
            if service:
                loaded_services.append(service)

    check_for_duplicates(loaded_services)
    return loaded_services, pyxelrest_config


def load_service(service_name, service_config):
    logger.debug('Loading "{0}" service...'.format(service_name))
    try:
        service = OpenAPI(service_name, service_config)
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

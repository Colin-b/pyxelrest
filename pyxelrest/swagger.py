import datetime
import os
import re
import requests
import logging
from collections import OrderedDict

try:
    # Python 3
    from configparser import ConfigParser
    from urllib.parse import urlsplit
except ImportError:
    # Python 2
    from ConfigParser import RawConfigParser
    from urlparse import urlsplit

from pyxelrest import vba
from pyxelrest.pyxelresterrors import *
from pyxelrest import authentication
from pyxelrest import fileadapter


logger = logging.getLogger(__name__)


def to_valid_python_vba(str_value):
    return re.sub('[^a-zA-Z_]+[^a-zA-Z_0-9]*', '', str_value)


def to_vba_valid_name(swagger_name):
    """
    Return name as non VBA or python restricted keyword
    """
    # replace vba restricted keywords
    if swagger_name.lower() in vba.vba_restricted_keywords:
        swagger_name = vba.vba_restricted_keywords[swagger_name.lower()]
    # replace '-'
    if "-" in swagger_name:
        swagger_name = swagger_name.replace("-", "_")
    if swagger_name.startswith("_"):  # TODO Handle more than one
        swagger_name = swagger_name[1:]
    return swagger_name


def return_type_can_be_handled(method_produces):
    return 'application/octet-stream' not in method_produces


class ConfigSection:
    def __init__(self, service_name, config):
        """
        Load service information from configuration.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param config: ConfigParser instance from where service details are retrieved.
        """
        self.name = service_name
        self.udf_prefix = to_valid_python_vba(service_name)
        self.requested_methods = [method.strip() for method in self.get_item_default(config, 'methods', '').split(',') if method.strip()]
        if not self.requested_methods:
            self.requested_methods = ['get', 'post', 'put', 'delete', 'patch', 'options', 'head']
        self.advanced_configuration = self._get_advanced_configuration(config)
        self.connect_timeout = float(self.advanced_configuration.get('connect_timeout', 1))
        self.read_timeout = self.advanced_configuration.get('read_timeout')
        if self.read_timeout:
            self.read_timeout = float(self.read_timeout)
        self.security_details = self._get_security_details(config)
        self.auth = authentication.add_service_custom_authentication(self.name, self.security_details)
        # UDFs will be Asynchronous by default (if required, ie: result does not fit in a single cell)
        self.udf_return_type = self.advanced_configuration.get('udf_return_type', 'asynchronous')
        self.max_retries = self.advanced_configuration.get('max_retries', 5)
        self.custom_headers = {key[7:]: value for key, value in self.advanced_configuration.items()
                               if key.startswith('header.')}

    def get_item(self, config, key):
        try:
            # Python 3
            section = config[self.name]
            if key not in section:
                raise MandatoryPropertyNotProvided(self.name, key)
            return section[key]
        except AttributeError:
            # Python 2
            if not config.has_option(self.name, key):
                raise MandatoryPropertyNotProvided(self.name, key)
            return config.get(self.name, key)

    def get_item_default(self, config, key, default_value):
        try:
            # Python 3
            section = config[self.name]
            return section[key] if key in section else default_value
        except AttributeError:
            # Python 2
            return config.get(self.name, key) if config.has_option(self.name, key) else default_value

    def _get_proxies(self, config, default_scheme):
        proxy_url_str = self.get_item_default(config, 'proxy_url', None)
        if proxy_url_str and '=' not in proxy_url_str:
            proxy_url_str = '{0}={1}'.format(default_scheme, proxy_url_str)
        proxies = self._str_to_dict(proxy_url_str)
        logger.debug("Proxies: {0}".format(proxies))
        return proxies

    def _get_advanced_configuration(self, config):
        advanced_configuration_str = self.get_item_default(config, 'advanced_configuration', None)
        details = self._str_to_dict(advanced_configuration_str)
        for key, value in details.items():
            details[key] = self._convert(value)
        logger.debug("Advanced configuration: {0}".format(details))
        return details

    def _get_security_details(self, config):
        security_details_str = self.get_item_default(config, 'security_details', None)
        details = self._str_to_dict(security_details_str)
        for key, value in details.items():
            details[key] = self._convert(value)
        logger.debug("Security details: {0}".format(details))
        return details

    def _convert(self, value):
        """
        Value can be an environment variable formatted as %MY_ENV_VARIABLE%
        """
        environment_variables_match = re.match('^%(.*)%$', value)
        if environment_variables_match:
            environment_variable = environment_variables_match.group(1)
            return os.environ[environment_variable]
        return value

    def _str_to_dict(self, str_value):
        items = {}
        if str_value:
            for item in str_value.split(','):
                item_entry = item.split('=')
                if len(item_entry) == 2:
                    items[item_entry[0]] = item_entry[1]
                else:
                    logger.warning("'{0}' does not respect the key=value rule. Property will be skipped.".format(item_entry))
        return items

    def should_return_asynchronously(self):
        return self.udf_return_type == 'asynchronous'


class ServiceConfigSection(ConfigSection):
    def __init__(self, service_name, config):
        """
        Load service information from configuration.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param config: ConfigParser instance from where service details are retrieved.
        """
        ConfigSection.__init__(self, service_name, config)
        self.tags = [tag.strip() for tag in self.advanced_configuration.get('tags', '').split(';') if tag.strip()]
        self.swagger_url = self.get_item(config, 'swagger_url')
        self.swagger_url_parsed = urlsplit(self.swagger_url)
        self.proxies = self._get_proxies(config, self.swagger_url_parsed.scheme)
        self.swagger_read_timeout = float(self.advanced_configuration.get('swagger_read_timeout', 5))
        self.service_host = self.get_item_default(config, 'service_host', self.swagger_url_parsed.netloc)
        self.rely_on_definitions = self.advanced_configuration.get('rely_on_definitions') == 'True'

    def _allow_tags(self, method_tags):
        if not self.tags or not method_tags:
            return True
        for method_tag in method_tags:
            if method_tag in self.tags:
                return True
        return False

    def should_provide_method(self, http_verb, swagger_method):
        if http_verb not in self.requested_methods:
            return False
        return self._allow_tags(swagger_method.get('tags')) and return_type_can_be_handled(
            swagger_method.get('produces', []))


class PyxelRestConfigSection(ConfigSection):
    def __init__(self, service_name, config):
        """
        Load service information from configuration.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param config: ConfigParser instance from where service details are retrieved.
        """
        ConfigSection.__init__(self, service_name, config)
        self.proxies = self._get_proxies(config, 'http')

    def should_provide_method(self, http_verb):
        return http_verb in self.requested_methods


class SwaggerService:
    def __init__(self, service_name, config):
        """
        Load service information from configuration and swagger JSON.
        :param service_name: Will be used as prefix to use in front of services UDFs
        to avoid duplicate between services.
        :param config: ConfigParser instance from where service details are retrieved.
        """
        self.methods = {}
        self.config = ServiceConfigSection(service_name, config)
        self.existing_operation_ids = []
        self.swagger = self._retrieve_swagger()
        self.validate_swagger_version()
        self.swagger_definitions = self.swagger.get('definitions')
        # Remove trailing slashes (as paths must starts with a slash)
        self.uri = self._extract_uri().rstrip('/')
        authentication.add_service_security(self.config.name, self.swagger, self.config.security_details)

    def _extract_uri(self):
        # The default scheme to be used is the one used to access the Swagger definition itself.
        scheme = self.swagger.get('schemes', [self.config.swagger_url_parsed.scheme])[0]
        # If the host is not included, the host serving the documentation is to be used (including the port).
        # service_host property is here to handle services behind a reverse proxy
        # (otherwise host will be the reverse proxy one)
        host = self.swagger.get('host', self.config.service_host)
        # Allow user to provide service_host starting with scheme (removing it)
        host_parsed = urlsplit(host)
        if host_parsed.netloc:
            host = host_parsed.netloc + host_parsed.path
        # If it is not included, the API is served directly under the host.
        base_path = self.swagger.get('basePath', None)

        return scheme + '://' + host + base_path if base_path else scheme + '://' + host

    def create_method(self, requests_method, swagger_method, method_path):
        udf = SwaggerMethod(self, requests_method, swagger_method, method_path)
        self.methods[udf.udf_name] = udf
        return udf

    def _retrieve_swagger(self):
        """
        Retrieve swagger JSON from service.
        :param swagger_url: URI of the service swagger JSON.
        :return: Dictionary representation of the retrieved swagger JSON.
        """
        requests_session = requests.session()
        requests_session.mount('file://', fileadapter.LocalFileAdapter())
        response = requests_session.get(self.config.swagger_url, proxies=self.config.proxies, verify=False,
                                        timeout=(self.config.connect_timeout, self.config.swagger_read_timeout))
        response.raise_for_status()
        # Always keep the order provided by server (for definitions)
        swagger = response.json(object_pairs_hook=OrderedDict)
        self._normalize_methods(swagger)
        return swagger

    # TODO Clean this method as it is too big and a smart refactoring of SwaggerService might be needed
    @classmethod
    def _normalize_methods(cls, swagger_json):
        """
        Normalize method parameters from dict representing the swagger JSON to:
        - rename parameters name that are VBA restricted keywords 
        - rename parameters name that uses '-' (to '_')
        - cascade parameters defined at path level to operation level

        Normalize method produces from dict representing the swagger JSON to:
        - cascade produces defined at root level to operation level

        :param swagger_json: Dictionary representing the swagger JSON.
        :return: None
        """

        def _normalise_names(parameters):
            for parameter in parameters:
                parameter['server_param_name'] = parameter['name']
                parameter['name'] = to_vba_valid_name(parameter['name'])
            return parameters

        def _update_method_parameters():
            method['parameters'] = root_parameters + methods_parameters + _normalise_names(method.get('parameters', []))

            method_parameters_names = [parameter['name'] for parameter in method['parameters']]
            if len(set(method_parameters_names)) != len(method_parameters_names):
                raise DuplicatedParameters(method)

        def _update_method_produces():
            method['produces'] = root_produces + methods_produces + method.get('produces', [])

        def _update_method_security():
            method['security'] = root_security + methods_security + method.get('security', [])

        def _update_method_consumes():
            method['consumes'] = root_consumes + methods_consumes + method.get('consumes', [])

        root_parameters = _normalise_names(swagger_json.get('parameters', []))
        root_produces = swagger_json.get('produces', [])
        root_security = swagger_json.get('security', [])
        root_consumes = swagger_json.get('consumes', [])

        for methods in swagger_json['paths'].values():
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

    def get_unique_operation_id(self, potential_duplicated_operation_id):
        unique_operation_id = potential_duplicated_operation_id  # At this time, this might not be unique
        if potential_duplicated_operation_id in self.existing_operation_ids:
            logger.warning('Duplicated operationId found: {0}.'.format(potential_duplicated_operation_id))
            unique_operation_id = 'duplicated_{0}'.format(potential_duplicated_operation_id)

        self.existing_operation_ids.append(unique_operation_id)
        return unique_operation_id

    def validate_swagger_version(self):
        if 'swagger' not in self.swagger:
            raise SwaggerVersionNotProvided()
        if self.swagger['swagger'] != '2.0':
            raise UnsupportedSwaggerVersion(self.swagger['swagger'])

    def __str__(self):
        if self.config.auth:
            return '[{0}] service. {1} (custom {2} authentication)'.format(self.config.name, self.uri, self.config.auth)
        return '[{0}] service. {1}'.format(self.config.name, self.uri)


class SwaggerMethod:
    def __init__(self, service, requests_method, swagger_method, path):
        self.uri = '{0}{1}'.format(service.uri, path)
        self.service = service
        self.requests_method = requests_method
        self.swagger_method = swagger_method
        self.path_parameters = []
        self.required_parameters = []
        self.optional_parameters = []
        self.contains_body_parameters = False
        self.contains_file_parameters = False
        self.contains_query_parameters = False
        self.parameters = {}
        for swagger_parameter in swagger_method.get('parameters', []):
            parameters = self._to_parameters(swagger_parameter)
            self.parameters.update({
                parameter.name: parameter
                for parameter in parameters
            })
            if swagger_parameter['in'] == 'path':
                self.path_parameters.extend(parameters)
            # Required but not in path
            elif swagger_parameter.get('required'):
                self.update_information_on_parameter_type(swagger_parameter)
                self.required_parameters.extend(parameters)
            else:
                self.update_information_on_parameter_type(swagger_parameter)
                self.optional_parameters.extend(parameters)
        # Uses "or" in case swagger contains None in description (explicitly set by service)
        self.help_url = SwaggerMethod.extract_url(swagger_method.get('description') or '')
        self._compute_operation_id(path)
        self.udf_name = '{0}_{1}'.format(service.config.udf_prefix, self.swagger_method['operationId'])
        self.responses = swagger_method.get('responses')
        if not self.responses:
            raise EmptyResponses(self.udf_name)

    def _to_parameters(self, swagger_parameter):
        if 'type' in swagger_parameter:  # Type usually means that this is not a complex type
            return [SwaggerParameter(swagger_parameter)]

        ref = swagger_parameter['schema']['$ref']
        ref = ref[len('#/definitions/'):]
        parameters = []
        for inner_parameter_name, inner_parameter in self.service.swagger_definitions[ref]['properties'].items():
            inner_parameter['server_param_name'] = inner_parameter_name
            inner_parameter['name'] = to_vba_valid_name(inner_parameter_name)
            inner_parameter['in'] = swagger_parameter['in']
            parameters.append(SwaggerParameter(inner_parameter))
        return parameters

    def _compute_operation_id(self, path):
        """
        Compute the operationId swagger field (as it may not be provided).
        Also ensure that there is no duplicate (in case a computed one matches a provided one)

        :param path: path provided in swagger definition for this method
        """
        operation_id = self.swagger_method.get('operationId') or \
                       '{0}{1}'.format(self.requests_method, path.replace('/', '_'))
        self.swagger_method['operationId'] = self.service.get_unique_operation_id(operation_id)

    def update_information_on_parameter_type(self, parameter):
        parameter_in = parameter['in']
        if parameter_in == 'body':
            self.contains_body_parameters = True
        elif parameter_in == 'formData':
            if parameter['type'] == 'file':
                self.contains_file_parameters = True
            else:
                self.contains_body_parameters = True
        elif parameter_in == 'query':
            self.contains_query_parameters = True

    def return_a_list(self):
        return ('application/json' in self.swagger_method['produces']) or \
               ('application/msgpackpandas' in self.swagger_method['produces'])

    def requires_authentication(self):
        return self.security() or self.service.config.auth

    def security(self):
        return self.swagger_method.get('security')

    def summary(self):
        return self.swagger_method.get('summary')

    def initial_header(self):
        """
        Initial header content
        For more details refer to https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
        """
        header = {}

        if self.contains_body_parameters:
            consumes = self.swagger_method.get('consumes')
            if not consumes or 'application/json' in consumes:
                header['Content-Type'] = 'application/json'
            else:
                logger.warning('{0} is expecting {0} encoded body. '
                               'For now PyxelRest only send JSON body so request might fail.'.format(
                    self.uri,
                    self.swagger_method['consumes']
                ))

        if 'application/msgpackpandas' in self.swagger_method['produces'] and support_pandas():
            header['Accept'] = 'application/msgpackpandas'
        elif 'application/json' in self.swagger_method['produces']:
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
        Swagger URLs are interpreted thanks to the following format:
        [description of the url](url)
        :return: URL or None if no URL can be found.
        """
        urls = re.findall('^.*\[.*\]\((.*)\).*$', text)
        if urls:
            return urls[0]


class SwaggerParameter:
    def __init__(self, swagger_parameter):
        self.name = swagger_parameter['name']
        self.server_param_name = swagger_parameter['server_param_name']
        self.description = swagger_parameter.get('description', '')
        if self.description:
            self.description = self.description.replace('\'', '')
        self.location = swagger_parameter['in']  # path, body, formData, query, header
        self.required = swagger_parameter.get('required')
        self.type = swagger_parameter.get('type')  # file (formData location), integer, number, string, boolean, array
        self.format = swagger_parameter.get('format')  # date (string type), date-time (string type)
        self.choices = swagger_parameter.get('enum')  # string type
        if self.type == 'array':
            swagger_array_parameter = dict(swagger_parameter)
            swagger_array_parameter.update(swagger_parameter['items'])
            self._convert_to_type = self._get_convert_array_method(SwaggerParameter(swagger_array_parameter))
        else:
            self._convert_to_type = self._get_convert_method()

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
        if self.choices and value not in self.choices:
            raise Exception('{0} value "{1}" should be {2}.'.format(self.name, value, self.choices.join(' or ')))
        return value

    def _convert_to_bool(self, value):
        if value not in ['true', 'false']:
            raise Exception('{0} value "{1}" must be either "true" or "false".'.format(self.name, value))
        return value == 'true'

    def _get_convert_array_method(self, array_parameter):
        return lambda value: [
            array_parameter._convert_to_type(item)
            for item in value if item is not None
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
        return lambda value: value  # Unhandled type, best effort


class RequestContent:
    def __init__(self, swagger_method):
        self.header = swagger_method.initial_header()
        self.payload = {}
        self.files = {}
        self.parameters = {}

    def add_value(self, parameter, value):
        if parameter.location == 'query':
            self.parameters[parameter.server_param_name] = value
        elif parameter.location == 'body':
            self.payload[parameter.server_param_name] = value
        elif parameter.location == 'formData':
            if parameter.type == 'file':
                self.files[parameter.server_param_name] = value
            else:
                self.payload[parameter.server_param_name] = value
        elif parameter.location == 'header':
            self.header[parameter.server_param_name] = value


def support_pandas():
    try:
        import pandas
        return True
    except:
        return False


def load_services():
    """
    Retrieve swagger JSON for each service defined in configuration file.
    :return: List of SwaggerService objects, size is the same one as the number of sections within configuration file
    (DEFAULT excluded) and the loaded pyxelrest configuration if provided
    """
    try:
        # Python 3
        config_parser = ConfigParser(interpolation=None)
    except:
        # Python 2
        config_parser = RawConfigParser()
    file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'services.ini')
    if not config_parser.read(file_path):
        raise ConfigurationFileNotFound(file_path)

    logging.debug('Loading services from "{0}"...'.format(file_path))
    loaded_services = []
    pyxelrest_config = None
    for service_name in config_parser.sections():
        if 'pyxelrest' == service_name:
            pyxelrest_config = PyxelRestConfigSection(service_name, config_parser)
        else:
            service = load_service(service_name, config_parser)
            if service:
                loaded_services.append(service)

    check_for_duplicates(loaded_services)
    return loaded_services, pyxelrest_config


def load_service(service_name, config_parser):
    logger.debug('Loading "{0}" service...'.format(service_name))
    try:
        service = SwaggerService(service_name, config_parser)
        logger.info('"{0}" service will be available.'.format(service_name))
        logger.debug(str(service))
        return service
    except Exception as e:
        logger.error('"{0}" service will not be available: {1}'.format(service_name, e))


def check_for_duplicates(loaded_services):
    services_by_prefix = {}
    for service in loaded_services:
        duplicates = services_by_prefix.get(service.config.udf_prefix, [])
        duplicates.append(service.config.name)
        services_by_prefix[service.config.udf_prefix] = duplicates
    for udf_prefix in services_by_prefix:
        service_names = services_by_prefix[udf_prefix]
        if len(service_names) > 1:
            logger.warning('{0} services will use the same "{1}" prefix, in case there is the same call available, '
                           'only the last declared one will be available.'.format(service_names, udf_prefix))

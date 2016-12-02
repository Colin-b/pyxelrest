"""
This file was generated. DO NOT EDIT manually.
Source file: {{ self._TemplateReference__context.name }}
Generation date (UTC): {{ current_utc_time }}
"""
import xlwings as xw
import requests
import datetime
from requests.exceptions import HTTPError

{% macro convert_to_return_type(str_value, method) %}
{% if 'application/json' in method['produces'] -%}
[{{ str_value }}]
{% else -%}
{{ str_value }}
{% endif %}
{% endmacro %}

{%- macro delete(server_uri, method_path) %}
    response = requests.delete(f'{{ server_uri }}{{ method_path }}', data=request_body, params=request_parameters)
{% endmacro -%}

{%- macro get(server_uri, method_path) %}
    response = requests.get(f'{{ server_uri }}{{ method_path }}', request_parameters, stream=True)
{% endmacro -%}

{%- macro post(server_uri, method_path) %}
    response = requests.post(f'{{ server_uri }}{{ method_path }}', data=request_body, params=request_parameters)
{% endmacro -%}

{%- macro put(server_uri, method_path) %}
    response = requests.put(f'{{ server_uri }}{{ method_path }}', data=request_body, params=request_parameters)
{% endmacro -%}

{% macro validate_parameter_value(parameter, method) %}
{% set param_name = parameter['name'] %}
{% set param_type = parameter['type'] %}
{% if param_type == 'integer' -%}
        if not isinstance({{param_name}}, int):
{% if 'application/json' in method['produces'] %}
            return ['{{ param_name }} must be an integer.']
{% else %}
            return '{{ param_name }} must be an integer.'
{% endif %}
{% elif param_type == 'number' -%}
        if not isinstance({{param_name}}, float):
{% if 'application/json' in method['produces'] %}
            return ['{{ param_name }} must be a number.']
{% else %}
            return '{{ param_name }} must be a number.'
{% endif %}
{% elif param_type == 'string' %}
{% set param_format = parameter['format'] %}
{% if param_format == 'date' -%}
        if not isinstance({{param_name}}, datetime.date):
{% if 'application/json' in method['produces'] %}
            return ['{{ param_name }} must be a date.']
{% else %}
            return '{{ param_name }} must be a date.'
{% endif %}
{% elif param_format == 'date-time' -%}
        if not isinstance({{param_name}}, datetime.datetime):
{% if 'application/json' in method['produces'] %}
            return ['{{ param_name }} must be a date time.']
{% else %}
            return '{{ param_name }} must be a date time.'
{% endif %}
{% else %}
{% set param_enum = parameter['enum'] %}
{% if param_enum|count > 0 -%}
        if {{param_name}} not in {{ param_enum }}:
{% if 'application/json' in method['produces'] %}
            return [f'{{ param_name }} value "{% raw %}{{% endraw %}{{ param_name }}{% raw %}}{% endraw %}" should be {{ param_enum|join(" or ") }}.']
{% else %}
            return f'{{ param_name }} value "{% raw %}{{% endraw %}{{ param_name }}{% raw %}}{% endraw %}" should be {{ param_enum|join(" or ") }}.'
{% endif %}
{% endif %}
{% endif %}
{% elif param_type == 'array' -%}
{# Array Type check #}
{% set param_items = parameter['items'] %}
{% set param_items_type = param_items['type'] %}
{% if param_items_type == 'integer' -%}
        if isinstance({{param_name}}, list):
            for {{param_name}}_item in {{param_name}}:
                if not isinstance({{param_name}}_item, int):
{% if 'application/json' in method['produces'] %}
                    return ['{{ param_name }} must contains integers.']
{% else %}
                    return '{{ param_name }} must contains integers.'
{% endif %}
        else:
            if not isinstance({{param_name}}, int):
{% if 'application/json' in method['produces'] %}
                return ['{{ param_name }} must contains integers.']
{% else %}
                return '{{ param_name }} must contains integers.'
{% endif %}
{% elif param_items_type == 'number' -%}
        if isinstance({{param_name}}, list):
            for {{param_name}}_item in {{param_name}}:
                if not isinstance({{param_name}}_item, float):
{% if 'application/json' in method['produces'] %}
                    return ['{{ param_name }} must contains numbers.']
{% else %}
                    return '{{ param_name }} must contains numbers.'
{% endif %}
        else:
            if not isinstance({{param_name}}, float):
{% if 'application/json' in method['produces'] %}
                return ['{{ param_name }} must contains numbers.']
{% else %}
                return '{{ param_name }} must contains numbers.'
{% endif %}
{% elif param_items_type == 'string' %}
{% set param_items_format = param_items['format'] %}
{% if param_items_format == 'date' -%}
        if isinstance({{param_name}}, list):
            for {{param_name}}_item in {{param_name}}:
                if not isinstance({{param_name}}_item, datetime.date):
{% if 'application/json' in method['produces'] %}
                    return ['{{ param_name }} must contains dates.']
{% else %}
                    return '{{ param_name }} must contains dates.'
{% endif %}
        else:
            if not isinstance({{param_name}}, datetime.date):
{% if 'application/json' in method['produces'] %}
                return ['{{ param_name }} must contains dates.']
{% else %}
                return '{{ param_name }} must contains dates.'
{% endif %}
{% elif param_items_format == 'date-time' -%}
        if isinstance({{param_name}}, list):
            for {{param_name}}_item in {{param_name}}:
                if not isinstance({{param_name}}_item, datetime.datetime):
{% if 'application/json' in method['produces'] %}
                    return ['{{ param_name }} must contains date times.']
{% else %}
                    return '{{ param_name }} must contains date times.'
{% endif %}
        else:
            if not isinstance({{param_name}}, datetime.datetime):
{% if 'application/json' in method['produces'] %}
                return ['{{ param_name }} must contains date times.']
{% else %}
                return '{{ param_name }} must contains date times.'
{% endif %}
{% else %}
{% set param_items_enum = param_items['enum'] %}
{% if param_items_enum|count > 0 -%}
        if isinstance({{param_name}}, list):
            for {{param_name}}_item in {{param_name}}:
                if {{param_name}}_item not in {{ param_items_enum }}:
{% if 'application/json' in method['produces'] %}
                    return [f'{{ param_name }} value "{% raw %}{{% endraw %}{{ param_name }}_item{% raw %}}{% endraw %}" should be {{ param_items_enum|join(" or ") }}.']
{% else %}
                    return f'{{ param_name }} value "{% raw %}{{% endraw %}{{ param_name }}_item{% raw %}}{% endraw %}" should be {{ param_items_enum|join(" or ") }}.'
{% endif %}
        else:
            if {{param_name}} not in {{ param_items_enum }}:
{% if 'application/json' in method['produces'] %}
                return [f'{{ param_name }} value "{% raw %}{{% endraw %}{{ param_name }}{% raw %}}{% endraw %}" should be {{ param_items_enum|join(" or ") }}.']
{% else %}
                return f'{{ param_name }} value "{% raw %}{{% endraw %}{{ param_name }}{% raw %}}{% endraw %}" should be {{ param_items_enum|join(" or ") }}.'
{% endif %}
{% endif %}
{% endif %}
{% endif %}
{# End of Array Type check #}
{% endif %}
{% endmacro %}

{% macro validate_parameter(parameter, method) %}
{% set param_name = parameter['name'] %}
{% set param_in = parameter['in'] %}
{% set param_required = parameter['required'] and not parameter['default'] %}
{% if param_in == 'path' %}
    if not {{ param_name }}:
{% if 'application/json' in method['produces'] %}
        return ['{{ param_name }} is required.']
{% else %}
        return '{{ param_name }} is required.'
{% endif %}
{% else %}
{% set server_param_name = param_name if param_name not in modified_parameters else modified_parameters[param_name] %}
{% if param_required %}
    if not {{ param_name }}:
{% if 'application/json' in method['produces'] %}
        return ['{{ param_name }} is required.']
{% else %}
        return '{{ param_name }} is required.'
{% endif %}
{% endif %}
    if {{ param_name }}:
        {{ validate_parameter_value(parameter, method) }}
{% if param_in == 'query' %}
        request_parameters['{{ server_param_name }}'] = {{ param_name }}
{% elif param_in == 'body' %}
        request_body['{{ server_param_name }}'] = {{ param_name }}
{% endif %}
{% endif %}
{% endmacro %}

{# Macro generating the converter for the parameter if needed #}
{% macro param_converter(parameter) %}
{% set param_type = parameter['type'] %}
{%- if param_type == 'integer' %}
 numbers=int,
{%- elif param_type == 'number' %}
 numbers=float,
{%- elif param_type == 'string' %}
    {%- set param_format = parameter['format'] %}
    {%- if param_format == 'date' %}
 dates=datetime.date,
    {%- elif param_format == 'date-time' %}
 dates=datetime.datetime,
    {%- endif %}
{% endif %}
{% endmacro %}

{# Macro generating the UDF related to provided method #}
{% macro add_udf(service, method_path, method, request_macro) %}
{% if 'application/octet-stream' not in method['produces'] %}
{% set method_parameters = method['parameters'] %}
@xw.func(category='{{ service.udf_prefix }}')
{% for parameter in method_parameters %}
@xw.arg('{{ parameter['name'] }}',{{ param_converter(parameter) }} doc='{{ parameter['description']|replace('\'', '') }}')
{% endfor %}
{% if 'application/json' in method['produces'] %}
@xw.ret(expand='table', index=True)
{% endif %}
def {{ service.udf_prefix }}_{{ method['operationId'] }}({{ method_parameters|map(attribute='name')|join(', ') }}):
{% if 'summary' in method and method['summary'] %}
    """{{ method['summary'] }}"""
{% endif %}
    request_parameters = {}
    request_body = {}

{% for parameter in method_parameters %}
{{ validate_parameter(parameter, method) }}
{% endfor %}
    try:
    {{ request_macro(service.uri, method_path) }}
{% if 'application/json' in method['produces'] %}
        response_json = response.json()
        response.close()
        return to_list(response_json)
{% else %}
        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
{% endif %}
    except Exception as error:
        return {{ convert_to_return_type('response.text[:255] if response else error.message[:255]', method) }}

{% endif %}
{% endmacro %}

{% for service in services %}
    {%- for method_path, methods in service.swagger['paths'].items() %}
        {%- if 'get' in service.methods -%}
            {%- if 'get' in methods -%}
                {{- add_udf(service, method_path, methods['get'], get) -}}
            {%- endif -%}
        {%- endif -%}
        {%- if 'post' in service.methods -%}
            {%- if 'post' in methods -%}
                {{- add_udf(service, method_path, methods['post'], post) -}}
            {%- endif -%}
        {%- endif -%}
        {%- if 'put' in service.methods -%}
            {%- if 'put' in methods -%}
                {{- add_udf(service, method_path, methods['put'], put) -}}
            {%- endif -%}
        {%- endif -%}
        {%- if 'delete' in service.methods -%}
            {%- if 'delete' in methods -%}
                {{- add_udf(service, method_path, methods['delete'], delete) -}}
            {%- endif -%}
        {%- endif -%}
    {%- endfor %}
{% endfor %}
def flattened_list_of_dicts(list_of_dicts):
    """
    Transform a list of dictionaries into a list of lists.
    First list is the header (first dictionary keys)
    Other lists are containing dictionary values.
    """
    flat_list = []
    header_list = list(list_of_dicts[0].keys())
    flat_list.append(header_list)
    for dictionary in list_of_dicts:
        flat_list.append(list(dictionary.values()))
    return flat_list


def to_list(data):
    """
    Transform this data into a list (if needed).
    If data is a dictionary:
        - If empty return a list with an empty string in it
        - If there is a single key and value is a list, then do not handle the key and return the list.
        - Otherwise return a list containing 2 lists, the keys and the values.
    If data is a list:
        - If this is a list of dictionaries, return a list of list containing keys (as first list) and values
        - Otherwise return this list
    Else:
        - Return a new list containing this item
    """
    if isinstance(data, dict):
        if len(data) == 0:
            return ['']
        if len(data) == 1:
            value = next(iter(data.values()))
            if isinstance(value, list):
                return to_list(value)
        return [list(data.keys()), list(data.values())]
    if isinstance(data, list):
        if len(data) == 0:
            return ['']
        if isinstance(data[0], dict):
            return flattened_list_of_dicts(data)
        return data
    return [data]

"""
This file was generated. DO NOT EDIT manually.
Source file: {{ self._TemplateReference__context.name }}
Generation date (UTC): {{ current_utc_time }}
"""
import xlwings as xw
import requests
import datetime
from requests.exceptions import HTTPError

{%- macro add_parameter_converter(parameter) -%}
{% set param_name = parameter['name'] %}
{% set param_type = parameter['type'] %}
{% if param_type == 'integer' %}
@xw.arg('{{param_name}}', numbers=int)
{% elif param_type == 'number' %}
@xw.arg('{{param_name}}', numbers=float)
{% elif param_type == 'string' %}
{% set param_format = parameter['format'] %}
{% if param_format == 'date' %}
@xw.arg('{{param_name}}', dates=datetime.date)
{% elif param_format == 'date-time' %}
@xw.arg('{{param_name}}', dates=datetime.datetime)
{% endif %}
{% endif %}
{%- endmacro -%}

{%- macro add_return_type(method) -%}
{% set method_produces = method['produces'] %}
{% if 'application/json' in method_produces %}
@xw.ret(expand='table')
{% elif 'text/plain' in method_produces %}
{% elif not method_produces %}
{% else %}
Return type is unknown and must be handled: {{ method_produces }}
{% endif %}
{%- endmacro -%}

{%- macro return_response(method) %}
{% set method_produces = method['produces'] %}
{% if 'application/json' in method_produces %}
{{ return_json_response() }}
{% elif 'text/plain' in method_produces %}
{{ return_text_response() }}
{% elif not method_produces %}
{{ return_text_response() }}
{% else %}
Return type is unknown and must be handled: {{ method_produces }}
{% endif %}
{%- endmacro -%}

{%- macro return_json_response() %}
    try:
        return to_list(response.json())
    except:
        # Text format cell is limited to 255 characters by Excel
        return [response.text[:255]]
{%- endmacro -%}

{%- macro return_text_response() %}
    try:
        response.raise_for_status()
        # Text format cell is limited to 255 characters by Excel
        return response.text[:255]
    except HTTPError as http_error:
        return http_error.message
{%- endmacro -%}

{% macro validate_parameter_value(parameter) %}
{% set param_name = parameter['name'] %}
{% set param_type = parameter['type'] %}
{% if param_type == 'integer' -%}
        if not isinstance({{param_name}}, int):
            return ['{{param_name}} must be an integer.']
{% elif param_type == 'number' -%}
        if not isinstance({{param_name}}, float):
            return ['{{param_name}} must be a number.']
{% elif param_type == 'string' %}
{% set param_format = parameter['format'] %}
{% if param_format == 'date' -%}
        if not isinstance({{param_name}}, datetime.date):
            return ['{{param_name}} must be a date.']
{% elif param_format == 'date-time' -%}
        if not isinstance({{param_name}}, datetime.datetime):
            return ['{{param_name}} must be a date time.']
{% else %}
{% set param_enum = parameter['enum'] %}
{% if param_enum|count > 0 -%}
        if {{param_name}} not in {{ param_enum }}:
            return ['{{param_name}} value "{0}" should be {1}.'.format({{param_name}}, ' or '.join({{ param_enum }}))]
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
                    return ['{{param_name}} must contains integers.']
        else:
            if not isinstance({{param_name}}, int):
                return ['{{param_name}} must contains integers.']
{% elif param_items_type == 'number' -%}
        if isinstance({{param_name}}, list):
            for {{param_name}}_item in {{param_name}}:
                if not isinstance({{param_name}}_item, float):
                    return ['{{param_name}} must contains numbers.']
        else:
            if not isinstance({{param_name}}, float):
                return ['{{param_name}} must contains numbers.']
{% elif param_items_type == 'string' %}
{% set param_items_format = param_items['format'] %}
{% if param_items_format == 'date' -%}
        if isinstance({{param_name}}, list):
            for {{param_name}}_item in {{param_name}}:
                if not isinstance({{param_name}}_item, datetime.date):
                    return ['{{param_name}} must contains dates.']
        else:
            if not isinstance({{param_name}}, datetime.date):
                return ['{{param_name}} must contains dates.']
{% elif param_items_format == 'date-time' -%}
        if isinstance({{param_name}}, list):
            for {{param_name}}_item in {{param_name}}:
                if not isinstance({{param_name}}_item, datetime.datetime):
                    return ['{{param_name}} must contains date times.']
        else:
            if not isinstance({{param_name}}, datetime.datetime):
                return ['{{param_name}} must contains date times.']
{% else %}
{% set param_items_enum = param_items['enum'] %}
{% if param_items_enum|count > 0 -%}
        if isinstance({{param_name}}, list):
            for {{param_name}}_item in {{param_name}}:
                if {{param_name}}_item not in {{ param_items_enum }}:
                    return ['{{param_name}} value "{0}" should be {1}.'.format({{param_name}}_item, ' or '.join({{ param_items_enum }}))]
        else:
            if {{param_name}} not in {{ param_items_enum }}:
                return ['{{param_name}} value "{0}" should be {1}.'.format({{param_name}}, ' or '.join({{ param_items_enum }}))]
{% endif %}
{% endif %}
{% endif %}
{# End of Array Type check #}
{% endif %}
{% endmacro %}

{%- macro add_request_parameter_or_body(parameter, dictionary) -%}
{% set param_name = parameter['name'] %}
{% set server_param_name = parameter['name'] if parameter['name'] not in modified_parameters else modified_parameters[parameter['name']] %}
{% set param_required = parameter['required'] %}
{% if param_required %}
    if not {{param_name}}:
        return ['{{param_name}} is required.']
    else:
        {{ validate_parameter_value(parameter) }}
        {{ dictionary }}['{{server_param_name}}'] = {{param_name}}
{% else %}
    if {{param_name}}:
        {{ validate_parameter_value(parameter) }}
        {{ dictionary }}['{{server_param_name}}'] = {{param_name}}
{% endif %}
{%- endmacro -%}

{%- macro add_parameter(parameter) -%}
{% set param_name = parameter['name'] %}
{% set server_param_name = parameter['name'] if parameter['name'] not in modified_parameters else modified_parameters[parameter['name']] %}
{% set param_required = parameter['required'] %}
{% set param_in = parameter['in'] %}
{% if param_in == 'path' %}
    if not {{param_name}}:
        return ['{{param_name}} is required.']
{% elif param_in == 'query' -%}
{{ add_request_parameter_or_body(parameter, 'request_parameters') }}
{%- elif param_in == 'body' -%}
{{ add_request_parameter_or_body(parameter, 'request_body') }}
{%- endif %}
{%- endmacro -%}

{# Iterate over services #}
{% for service in services %}
{% set server_uri = service.uri %}
{% set swagger = service.swagger %}
{# Iterate over server methods #}
{% for method_path, methods in swagger['paths'].iteritems() %}
{% if 'get' in service.methods %}
{# server GET method #}
{% if 'get' in methods %}

{% set method = methods['get'] %}
{% include 'get_user_defined_function.tpl' %}
{# End of server GET method #}
{% endif %}
{% endif %}
{% if 'post' in service.methods %}
{# server POST method #}
{% if 'post' in methods %}

{% set method = methods['post'] %}
{% include 'post_user_defined_function.tpl' %}
{# End of server POST method #}
{% endif %}
{% endif %}
{% if 'put' in service.methods %}
{# server PUT method #}
{% if 'put' in methods %}

{% set method = methods['put'] %}
{% include 'put_user_defined_function.tpl' %}
{# End of server PUT method #}
{% endif %}
{% endif %}
{% if 'delete' in service.methods %}
{# server DELETE method #}
{% if 'delete' in methods %}

{% set method = methods['delete'] %}
{% include 'delete_user_defined_function.tpl' %}
{# End of server DELETE method #}
{% endif %}
{% endif %}
{# End of iteration over server methods #}
{% endfor %}
{# End of iteration over services #}
{% endfor %}

def flattened_list_of_dicts(list_of_dicts):
    """
    Transform a list of dictionaries into a list of lists.
    First list is the header (first dictionary keys)
    Other lists are containing dictionary values.
    """
    flat_list = []
    header_list = list_of_dicts[0].keys()
    flat_list.append(header_list)
    for dictionary in list_of_dicts:
        flat_list.append(dictionary.values())
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
            key, value = data.iteritems().next()
            if isinstance(value, list):
                return to_list(value)
        return [data.keys(), data.values()]
    if isinstance(data, list):
        if len(data) == 0:
            return ['']
        if isinstance(data[0], dict):
            return flattened_list_of_dicts(data)
        return data
    return [data]

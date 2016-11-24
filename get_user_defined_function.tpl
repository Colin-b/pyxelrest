{% if 'application/octet-stream' not in method['produces'] %}
{% set method_parameters = method['parameters'] %}

@xw.func
{% for parameter in method_parameters -%}
{{ add_parameter_converter(parameter) }}
{%- endfor -%}
{{- add_return_type(method) -}}
def {{ service.udf_prefix }}_{{ method['operationId'] }}({{ method_parameters|map(attribute='name')|join(', ') }}):
{% if 'summary' in method and method['summary'] %}
    """{{ method['summary'] }}"""
{% endif %}
    request_parameters = {}
    request_body = {}

{% for parameter in method_parameters -%}
{{ add_parameter(parameter) }}
{%- endfor %}

{% set path_parameters = method_parameters|selectattr("in", "equalto", "path")|map(attribute='name') %}
{% set path_parameters_count = method_parameters|selectattr("in", "equalto", "path")|list|count %}
{% if path_parameters_count > 0 %}
    response = requests.get('{{server_uri}}{{ method_path }}'.format(
{%- for path_parameter in path_parameters -%}
        {{ path_parameter }}={{ path_parameter }}{% if not loop.last %}, {% endif %}
{% endfor %}
), request_parameters)
{% else %}
    response = requests.get('{{server_uri}}{{ method_path }}', request_parameters)
{% endif %}
{{ return_response(method) }}
{% endif %}

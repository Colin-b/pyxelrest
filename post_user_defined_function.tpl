{% if 'application/octet-stream' not in method['produces'] %}
{% set method_parameters = method['parameters'] %}

@xw.func(category='{{ service.udf_prefix }}')
{% for parameter in method_parameters -%}
{{add_parameter_converter(parameter)}}
{%- endfor %}
{{ add_return_type(method) }}
def {{ service.udf_prefix }}_{{ method['operationId'] }}({{ method_parameters|map(attribute='name')|join(', ') }}):
{% if 'summary' in method and method['summary'] %}
    """{{ method['summary'] }}"""
{% endif %}
    request_parameters = {}
    request_body = {}

{% for parameter in method_parameters -%}
{{ add_parameter(parameter) }}
{%- endfor %}

    response = requests.post(f'{{server_uri}}{{ method_path }}', data=request_body, params=request_parameters)
{{ return_response(method) }}
{% endif %}

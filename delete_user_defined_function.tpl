{% set method_parameters = method['parameters'] %}

@xw.func
{% for parameter in method_parameters -%}
{{add_parameter_converter(parameter)}}
{%- endfor %}
@xw.ret(expand='table')
def {{ service.udf_prefix }}_{{ method['operationId'] }}({{ method_parameters|map(attribute='name')|join(', ') }}):
{% if 'description' in method and method['description'] %}
    """{{ method['description'] }}"""
{% endif %}
    request_parameters = {}
    request_body = {}

{% for parameter in method_parameters -%}
{{ add_parameter(parameter) }}
{%- endfor %}

{% set path_parameters = method_parameters|selectattr("in", "equalto", "path")|map(attribute='name') %}
{% set path_parameters_count = method_parameters|selectattr("in", "equalto", "path")|list|count %}
{% if path_parameters_count > 0 %}
    response = requests.delete('{{server_uri}}{{ method_path }}'.format(
{%- for path_parameter in path_parameters -%}
        {{ path_parameter }}={{ path_parameter }}{% if not loop.last %}, {% endif %}
{% endfor %}
), data=request_body, params=request_parameters)
{% else %}
    response = requests.delete('{{server_uri}}{{ method_path }}', data=request_body, params=request_parameters)
{% endif %}
    try:
        response.raise_for_status()
        return to_list(response.json())
    except HTTPError as http_error:
        return [http_error.message]
    except:
        return [response.text]

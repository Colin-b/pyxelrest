from flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   paths={
                       '/test/without/parameter': {
                           'get': {
                               'operationId': 'get_test_without_parameter'
                           },
                           'post': {
                                'operationId': 'post_test_without_parameter'
                            },
                            'put': {
                                'operationId': 'put_test_without_parameter'
                            },
                            'delete': {
                                'operationId': 'delete_test_without_parameter'
                            }
                       },
                       '/test/plain/text/without/parameter': {
                            'get': {
                                'operationId': 'get_test_plain_text_without_parameter',
                                'produces': [
                                    'text/plain'
                                ]
                            },
                            'post': {
                                'operationId': 'post_test_plain_text_without_parameter',
                                'produces': [
                                    'text/plain'
                                ]
                            },
                            'put': {
                                'operationId': 'put_test_plain_text_without_parameter',
                                'produces': [
                                    'text/plain'
                                ]
                            },
                            'delete': {
                                'operationId': 'delete_test_plain_text_without_parameter',
                                'produces': [
                                    'text/plain'
                                ]
                            }
                       },
                       '/test/json/without/parameter': {
                            'get': {
                                'operationId': 'get_test_json_without_parameter',
                                'produces': [
                                    'application/json'
                                ]
                            },
                            'post': {
                                'operationId': 'post_test_json_without_parameter',
                                'produces': [
                                    'application/json'
                                ]
                            },
                            'put': {
                                'operationId': 'put_test_json_without_parameter',
                                'produces': [
                                    'application/json'
                                ]
                            },
                            'delete': {
                                'operationId': 'delete_test_json_without_parameter',
                                'produces': [
                                    'application/json'
                                ]
                            }
                       },
                       '/test/octet/without/parameter': {
                            'get': {
                                'operationId': 'get_test_octet_without_parameter',
                                'produces': [
                                    'application/octet-stream'
                                ]
                            },
                            'post': {
                                'operationId': 'post_test_octet_without_parameter',
                                'produces': [
                                    'application/octet-stream'
                                ]
                            },
                            'put': {
                                'operationId': 'put_test_octet_without_parameter',
                                'produces': [
                                    'application/octet-stream'
                                ]
                            },
                            'delete': {
                                'operationId': 'delete_test_octet_without_parameter',
                                'produces': [
                                    'application/octet-stream'
                                ]
                            }
                       },
                       '/test/with/all/parameters/types': {
                            'get': {
                                'operationId': 'get_test_with_all_parameters_types',
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'post': {
                                'operationId': 'post_test_with_all_parameters_types',
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'put': {
                                'operationId': 'put_test_with_all_parameters_types',
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'delete': {
                                'operationId': 'delete_test_with_all_parameters_types',
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            }
                        },
                       '/test/plain/text/with/all/parameters/types': {
                            'get': {
                                'operationId': 'get_test_plain_text_with_all_parameters_types',
                                'produces': [
                                    'text/plain'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'post': {
                                'operationId': 'post_test_plain_text_with_all_parameters_types',
                                'produces': [
                                    'text/plain'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'put': {
                                'operationId': 'put_test_plain_text_with_all_parameters_types',
                                'produces': [
                                    'text/plain'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'delete': {
                                'operationId': 'delete_test_plain_text_with_all_parameters_types',
                                'produces': [
                                    'text/plain'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            }
                        },
                       '/test/json/with/all/parameters/types': {
                            'get': {
                                'operationId': 'get_test_json_with_all_parameters_types',
                                'produces': [
                                    'application/json'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'post': {
                                'operationId': 'post_test_json_with_all_parameters_types',
                                'produces': [
                                    'application/json'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'put': {
                                'operationId': 'put_test_json_with_all_parameters_types',
                                'produces': [
                                    'application/json'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'delete': {
                                'operationId': 'delete_test_json_with_all_parameters_types',
                                'produces': [
                                    'application/json'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            }
                        },
                       '/test/octet/with/all/parameters/types': {
                            'get': {
                                'operationId': 'get_test_octet_with_all_parameters_types',
                                'produces': [
                                    'application/octet-stream'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'post': {
                                'operationId': 'post_test_octet_with_all_parameters_types',
                                'produces': [
                                    'application/octet-stream'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'put': {
                                'operationId': 'put_test_octet_with_all_parameters_types',
                                'produces': [
                                    'application/octet-stream'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'delete': {
                                'operationId': 'delete_test_octet_with_all_parameters_types',
                                'produces': [
                                    'application/octet-stream'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            }
                        },
                       '/test/with/all/optional/parameters/types': {
                            'get': {
                                'operationId': 'get_test_with_all_optional_parameters_types',
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': False,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': False,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': False,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': False,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': False,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': False,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': False,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': False,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'post': {
                                'operationId': 'post_test_with_all_optional_parameters_types',
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': False,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': False,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': False,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': False,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': False,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': False,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': False,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': False,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'put': {
                                'operationId': 'put_test_with_all_optional_parameters_types',
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': False,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': False,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': False,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': False,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': False,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': False,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': False,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': False,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'delete': {
                                'operationId': 'delete_test_with_all_optional_parameters_types',
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': False,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': False,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': False,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': False,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': False,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': False,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': False,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': False,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            }
                        },
                       '/test/plain/text/with/all/optional/parameters/types': {
                            'get': {
                                'operationId': 'get_test_plain_text_with_all_optional_parameters_types',
                                'produces': [
                                    'text/plain'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': False,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': False,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': False,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': False,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': False,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': False,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': False,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': False,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'post': {
                                'operationId': 'post_test_plain_text_with_all_optional_parameters_types',
                                'produces': [
                                    'text/plain'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': False,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': False,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': False,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': False,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': False,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': False,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': False,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': False,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'put': {
                                'operationId': 'put_test_plain_text_with_all_optional_parameters_types',
                                'produces': [
                                    'text/plain'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': False,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': False,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': False,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': False,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': False,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': False,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': False,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': False,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'delete': {
                                'operationId': 'delete_test_plain_text_with_all_optional_parameters_types',
                                'produces': [
                                    'text/plain'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': False,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': False,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': False,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': False,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': False,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': False,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': False,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': False,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            }
                        },
                       '/test/json/with/all/optional/parameters/types': {
                            'get': {
                                'operationId': 'get_test_json_with_all_optional_parameters_types',
                                'produces': [
                                    'application/json'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': False,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': False,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': False,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': False,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': False,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': False,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': False,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': False,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'post': {
                                'operationId': 'post_test_json_with_all_optional_parameters_types',
                                'produces': [
                                    'application/json'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': False,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': False,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': False,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': False,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': False,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': False,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': False,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': False,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'put': {
                                'operationId': 'put_test_json_with_all_optional_parameters_types',
                                'produces': [
                                    'application/json'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': False,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': False,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': False,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': False,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': False,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': False,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': False,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': False,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'delete': {
                                'operationId': 'delete_test_json_with_all_optional_parameters_types',
                                'produces': [
                                    'application/json'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': False,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': False,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': False,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': False,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': False,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': False,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': False,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': False,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            }
                        },
                       '/test/octet/with/all/optional/parameters/types': {
                            'get': {
                                'operationId': 'get_test_octet_with_all_optional_parameters_types',
                                'produces': [
                                    'application/octet-stream'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': False,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': False,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': False,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': False,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': False,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': False,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': False,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': False,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'post': {
                                'operationId': 'post_test_octet_with_all_optional_parameters_types',
                                'produces': [
                                    'application/octet-stream'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': False,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': False,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': False,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': False,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': False,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': False,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': False,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': False,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'put': {
                                'operationId': 'put_test_octet_with_all_optional_parameters_types',
                                'produces': [
                                    'application/octet-stream'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': False,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': False,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': False,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': False,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': False,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': False,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': False,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': False,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'delete': {
                                'operationId': 'delete_test_octet_with_all_optional_parameters_types',
                                'produces': [
                                    'application/octet-stream'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer parameter',
                                        'in': 'query',
                                        'name': 'query_integer',
                                        'required': False,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 parameter',
                                        'in': 'query',
                                        'name': 'query_integer32',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 parameter',
                                        'in': 'query',
                                        'name': 'query_integer64',
                                        'required': False,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number parameter',
                                        'in': 'query',
                                        'name': 'query_number',
                                        'required': False,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float parameter',
                                        'in': 'query',
                                        'name': 'query_float',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double parameter',
                                        'in': 'query',
                                        'name': 'query_double',
                                        'required': False,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string parameter',
                                        'in': 'query',
                                        'name': 'query_string',
                                        'required': False,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte parameter',
                                        'in': 'query',
                                        'name': 'query_string_byte',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary parameter',
                                        'in': 'query',
                                        'name': 'query_string_binary',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean parameter',
                                        'in': 'query',
                                        'name': 'query_boolean',
                                        'required': False,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date parameter',
                                        'in': 'query',
                                        'name': 'query_date',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time parameter',
                                        'in': 'query',
                                        'name': 'query_date_time',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password parameter',
                                        'in': 'query',
                                        'name': 'query_password',
                                        'required': False,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer',
                                        'required': False,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer32',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array parameter',
                                        'in': 'query',
                                        'name': 'query_array_integer64',
                                        'required': False,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array parameter',
                                        'in': 'query',
                                        'name': 'query_array_number',
                                        'required': False,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array parameter',
                                        'in': 'query',
                                        'name': 'query_array_float',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array parameter',
                                        'in': 'query',
                                        'name': 'query_array_double',
                                        'required': False,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': False,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_byte',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string_binary',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array parameter',
                                        'in': 'query',
                                        'name': 'query_array_boolean',
                                        'required': False,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array parameter',
                                        'in': 'query',
                                        'name': 'query_array_date_time',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array parameter',
                                        'in': 'query',
                                        'name': 'query_array_password',
                                        'required': False,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            }
                        },
                       '/test/with/all/paths/types': {
                            'get': {
                                'operationId': 'get_test_with_all_paths_types',
                                'parameters': [
                                    {
                                        'description': 'integer path',
                                        'in': 'path',
                                        'name': 'path_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 path',
                                        'in': 'path',
                                        'name': 'path_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 path',
                                        'in': 'path',
                                        'name': 'path_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number path',
                                        'in': 'path',
                                        'name': 'path_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float path',
                                        'in': 'path',
                                        'name': 'path_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double path',
                                        'in': 'path',
                                        'name': 'path_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string path',
                                        'in': 'path',
                                        'name': 'path_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte path',
                                        'in': 'path',
                                        'name': 'path_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary path',
                                        'in': 'path',
                                        'name': 'path_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean path',
                                        'in': 'path',
                                        'name': 'path_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date path',
                                        'in': 'path',
                                        'name': 'path_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time path',
                                        'in': 'path',
                                        'name': 'path_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password path',
                                        'in': 'path',
                                        'name': 'path_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array path',
                                        'in': 'path',
                                        'name': 'path_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array path',
                                        'in': 'path',
                                        'name': 'path_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array path',
                                        'in': 'path',
                                        'name': 'path_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array path',
                                        'in': 'path',
                                        'name': 'path_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array path',
                                        'in': 'path',
                                        'name': 'path_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array path',
                                        'in': 'path',
                                        'name': 'path_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array path',
                                        'in': 'path',
                                        'name': 'path_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array path',
                                        'in': 'path',
                                        'name': 'path_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array path',
                                        'in': 'path',
                                        'name': 'path_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array path',
                                        'in': 'path',
                                        'name': 'path_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array path',
                                        'in': 'path',
                                        'name': 'path_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'post': {
                                'operationId': 'post_test_with_all_paths_types',
                                'parameters': [
                                    {
                                        'description': 'integer path',
                                        'in': 'path',
                                        'name': 'path_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 path',
                                        'in': 'path',
                                        'name': 'path_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 path',
                                        'in': 'path',
                                        'name': 'path_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number path',
                                        'in': 'path',
                                        'name': 'path_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float path',
                                        'in': 'path',
                                        'name': 'path_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double path',
                                        'in': 'path',
                                        'name': 'path_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string path',
                                        'in': 'path',
                                        'name': 'path_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte path',
                                        'in': 'path',
                                        'name': 'path_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary path',
                                        'in': 'path',
                                        'name': 'path_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean path',
                                        'in': 'path',
                                        'name': 'path_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date path',
                                        'in': 'path',
                                        'name': 'path_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time path',
                                        'in': 'path',
                                        'name': 'path_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password path',
                                        'in': 'path',
                                        'name': 'path_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array path',
                                        'in': 'path',
                                        'name': 'path_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array path',
                                        'in': 'path',
                                        'name': 'path_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array path',
                                        'in': 'path',
                                        'name': 'path_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array path',
                                        'in': 'path',
                                        'name': 'path_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array path',
                                        'in': 'path',
                                        'name': 'path_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array path',
                                        'in': 'path',
                                        'name': 'path_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array path',
                                        'in': 'path',
                                        'name': 'path_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array path',
                                        'in': 'path',
                                        'name': 'path_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array path',
                                        'in': 'path',
                                        'name': 'path_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array path',
                                        'in': 'path',
                                        'name': 'path_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array path',
                                        'in': 'path',
                                        'name': 'path_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'put': {
                                'operationId': 'put_test_with_all_paths_types',
                                'parameters': [
                                    {
                                        'description': 'integer path',
                                        'in': 'path',
                                        'name': 'path_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 path',
                                        'in': 'path',
                                        'name': 'path_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 path',
                                        'in': 'path',
                                        'name': 'path_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number path',
                                        'in': 'path',
                                        'name': 'path_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float path',
                                        'in': 'path',
                                        'name': 'path_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double path',
                                        'in': 'path',
                                        'name': 'path_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string path',
                                        'in': 'path',
                                        'name': 'path_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte path',
                                        'in': 'path',
                                        'name': 'path_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary path',
                                        'in': 'path',
                                        'name': 'path_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean path',
                                        'in': 'path',
                                        'name': 'path_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date path',
                                        'in': 'path',
                                        'name': 'path_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time path',
                                        'in': 'path',
                                        'name': 'path_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password path',
                                        'in': 'path',
                                        'name': 'path_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array path',
                                        'in': 'path',
                                        'name': 'path_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array path',
                                        'in': 'path',
                                        'name': 'path_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array path',
                                        'in': 'path',
                                        'name': 'path_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array path',
                                        'in': 'path',
                                        'name': 'path_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array path',
                                        'in': 'path',
                                        'name': 'path_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array path',
                                        'in': 'path',
                                        'name': 'path_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array path',
                                        'in': 'path',
                                        'name': 'path_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array path',
                                        'in': 'path',
                                        'name': 'path_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array path',
                                        'in': 'path',
                                        'name': 'path_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array path',
                                        'in': 'path',
                                        'name': 'path_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array path',
                                        'in': 'path',
                                        'name': 'path_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'delete': {
                                'operationId': 'delete_test_with_all_paths_types',
                                'parameters': [
                                    {
                                        'description': 'integer path',
                                        'in': 'path',
                                        'name': 'path_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 path',
                                        'in': 'path',
                                        'name': 'path_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 path',
                                        'in': 'path',
                                        'name': 'path_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number path',
                                        'in': 'path',
                                        'name': 'path_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float path',
                                        'in': 'path',
                                        'name': 'path_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double path',
                                        'in': 'path',
                                        'name': 'path_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string path',
                                        'in': 'path',
                                        'name': 'path_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte path',
                                        'in': 'path',
                                        'name': 'path_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary path',
                                        'in': 'path',
                                        'name': 'path_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean path',
                                        'in': 'path',
                                        'name': 'path_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date path',
                                        'in': 'path',
                                        'name': 'path_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time path',
                                        'in': 'path',
                                        'name': 'path_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password path',
                                        'in': 'path',
                                        'name': 'path_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array path',
                                        'in': 'path',
                                        'name': 'path_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array path',
                                        'in': 'path',
                                        'name': 'path_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array path',
                                        'in': 'path',
                                        'name': 'path_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array path',
                                        'in': 'path',
                                        'name': 'path_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array path',
                                        'in': 'path',
                                        'name': 'path_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array path',
                                        'in': 'path',
                                        'name': 'path_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array path',
                                        'in': 'path',
                                        'name': 'path_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array path',
                                        'in': 'path',
                                        'name': 'path_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array path',
                                        'in': 'path',
                                        'name': 'path_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array path',
                                        'in': 'path',
                                        'name': 'path_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array path',
                                        'in': 'path',
                                        'name': 'path_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            }
                        },
                       '/test/plain/text/with/all/paths/types': {
                            'get': {
                                'operationId': 'get_test_plain_text_with_all_paths_types',
                                'produces': [
                                    'text/plain'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer path',
                                        'in': 'path',
                                        'name': 'path_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 path',
                                        'in': 'path',
                                        'name': 'path_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 path',
                                        'in': 'path',
                                        'name': 'path_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number path',
                                        'in': 'path',
                                        'name': 'path_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float path',
                                        'in': 'path',
                                        'name': 'path_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double path',
                                        'in': 'path',
                                        'name': 'path_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string path',
                                        'in': 'path',
                                        'name': 'path_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte path',
                                        'in': 'path',
                                        'name': 'path_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary path',
                                        'in': 'path',
                                        'name': 'path_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean path',
                                        'in': 'path',
                                        'name': 'path_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date path',
                                        'in': 'path',
                                        'name': 'path_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time path',
                                        'in': 'path',
                                        'name': 'path_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password path',
                                        'in': 'path',
                                        'name': 'path_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array path',
                                        'in': 'path',
                                        'name': 'path_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array path',
                                        'in': 'path',
                                        'name': 'path_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array path',
                                        'in': 'path',
                                        'name': 'path_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array path',
                                        'in': 'path',
                                        'name': 'path_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array path',
                                        'in': 'path',
                                        'name': 'path_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array path',
                                        'in': 'path',
                                        'name': 'path_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array path',
                                        'in': 'path',
                                        'name': 'path_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array path',
                                        'in': 'path',
                                        'name': 'path_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array path',
                                        'in': 'path',
                                        'name': 'path_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array path',
                                        'in': 'path',
                                        'name': 'path_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array path',
                                        'in': 'path',
                                        'name': 'path_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'post': {
                                'operationId': 'post_test_plain_text_with_all_paths_types',
                                'produces': [
                                    'text/plain'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer path',
                                        'in': 'path',
                                        'name': 'path_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 path',
                                        'in': 'path',
                                        'name': 'path_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 path',
                                        'in': 'path',
                                        'name': 'path_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number path',
                                        'in': 'path',
                                        'name': 'path_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float path',
                                        'in': 'path',
                                        'name': 'path_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double path',
                                        'in': 'path',
                                        'name': 'path_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string path',
                                        'in': 'path',
                                        'name': 'path_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte path',
                                        'in': 'path',
                                        'name': 'path_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary path',
                                        'in': 'path',
                                        'name': 'path_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean path',
                                        'in': 'path',
                                        'name': 'path_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date path',
                                        'in': 'path',
                                        'name': 'path_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time path',
                                        'in': 'path',
                                        'name': 'path_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password path',
                                        'in': 'path',
                                        'name': 'path_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array path',
                                        'in': 'path',
                                        'name': 'path_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array path',
                                        'in': 'path',
                                        'name': 'path_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array path',
                                        'in': 'path',
                                        'name': 'path_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array path',
                                        'in': 'path',
                                        'name': 'path_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array path',
                                        'in': 'path',
                                        'name': 'path_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array path',
                                        'in': 'path',
                                        'name': 'path_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array path',
                                        'in': 'path',
                                        'name': 'path_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array path',
                                        'in': 'path',
                                        'name': 'path_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array path',
                                        'in': 'path',
                                        'name': 'path_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array path',
                                        'in': 'path',
                                        'name': 'path_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array path',
                                        'in': 'path',
                                        'name': 'path_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'put': {
                                'operationId': 'put_test_plain_text_with_all_paths_types',
                                'produces': [
                                    'text/plain'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer path',
                                        'in': 'path',
                                        'name': 'path_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 path',
                                        'in': 'path',
                                        'name': 'path_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 path',
                                        'in': 'path',
                                        'name': 'path_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number path',
                                        'in': 'path',
                                        'name': 'path_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float path',
                                        'in': 'path',
                                        'name': 'path_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double path',
                                        'in': 'path',
                                        'name': 'path_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string path',
                                        'in': 'path',
                                        'name': 'path_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte path',
                                        'in': 'path',
                                        'name': 'path_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary path',
                                        'in': 'path',
                                        'name': 'path_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean path',
                                        'in': 'path',
                                        'name': 'path_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date path',
                                        'in': 'path',
                                        'name': 'path_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time path',
                                        'in': 'path',
                                        'name': 'path_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password path',
                                        'in': 'path',
                                        'name': 'path_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array path',
                                        'in': 'path',
                                        'name': 'path_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array path',
                                        'in': 'path',
                                        'name': 'path_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array path',
                                        'in': 'path',
                                        'name': 'path_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array path',
                                        'in': 'path',
                                        'name': 'path_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array path',
                                        'in': 'path',
                                        'name': 'path_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array path',
                                        'in': 'path',
                                        'name': 'path_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array path',
                                        'in': 'path',
                                        'name': 'path_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array path',
                                        'in': 'path',
                                        'name': 'path_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array path',
                                        'in': 'path',
                                        'name': 'path_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array path',
                                        'in': 'path',
                                        'name': 'path_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array path',
                                        'in': 'path',
                                        'name': 'path_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'delete': {
                                'operationId': 'delete_test_plain_text_with_all_paths_types',
                                'produces': [
                                    'text/plain'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer path',
                                        'in': 'path',
                                        'name': 'path_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 path',
                                        'in': 'path',
                                        'name': 'path_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 path',
                                        'in': 'path',
                                        'name': 'path_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number path',
                                        'in': 'path',
                                        'name': 'path_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float path',
                                        'in': 'path',
                                        'name': 'path_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double path',
                                        'in': 'path',
                                        'name': 'path_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string path',
                                        'in': 'path',
                                        'name': 'path_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte path',
                                        'in': 'path',
                                        'name': 'path_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary path',
                                        'in': 'path',
                                        'name': 'path_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean path',
                                        'in': 'path',
                                        'name': 'path_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date path',
                                        'in': 'path',
                                        'name': 'path_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time path',
                                        'in': 'path',
                                        'name': 'path_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password path',
                                        'in': 'path',
                                        'name': 'path_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array path',
                                        'in': 'path',
                                        'name': 'path_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array path',
                                        'in': 'path',
                                        'name': 'path_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array path',
                                        'in': 'path',
                                        'name': 'path_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array path',
                                        'in': 'path',
                                        'name': 'path_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array path',
                                        'in': 'path',
                                        'name': 'path_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array path',
                                        'in': 'path',
                                        'name': 'path_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array path',
                                        'in': 'path',
                                        'name': 'path_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array path',
                                        'in': 'path',
                                        'name': 'path_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array path',
                                        'in': 'path',
                                        'name': 'path_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array path',
                                        'in': 'path',
                                        'name': 'path_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array path',
                                        'in': 'path',
                                        'name': 'path_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            }
                        },
                       '/test/json/with/all/paths/types': {
                            'get': {
                                'operationId': 'get_test_json_with_all_paths_types',
                                'produces': [
                                    'application/json'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer path',
                                        'in': 'path',
                                        'name': 'path_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 path',
                                        'in': 'path',
                                        'name': 'path_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 path',
                                        'in': 'path',
                                        'name': 'path_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number path',
                                        'in': 'path',
                                        'name': 'path_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float path',
                                        'in': 'path',
                                        'name': 'path_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double path',
                                        'in': 'path',
                                        'name': 'path_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string path',
                                        'in': 'path',
                                        'name': 'path_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte path',
                                        'in': 'path',
                                        'name': 'path_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary path',
                                        'in': 'path',
                                        'name': 'path_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean path',
                                        'in': 'path',
                                        'name': 'path_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date path',
                                        'in': 'path',
                                        'name': 'path_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time path',
                                        'in': 'path',
                                        'name': 'path_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password path',
                                        'in': 'path',
                                        'name': 'path_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array path',
                                        'in': 'path',
                                        'name': 'path_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array path',
                                        'in': 'path',
                                        'name': 'path_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array path',
                                        'in': 'path',
                                        'name': 'path_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array path',
                                        'in': 'path',
                                        'name': 'path_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array path',
                                        'in': 'path',
                                        'name': 'path_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array path',
                                        'in': 'path',
                                        'name': 'path_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array path',
                                        'in': 'path',
                                        'name': 'path_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array path',
                                        'in': 'path',
                                        'name': 'path_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array path',
                                        'in': 'path',
                                        'name': 'path_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array path',
                                        'in': 'path',
                                        'name': 'path_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array path',
                                        'in': 'path',
                                        'name': 'path_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'post': {
                                'operationId': 'post_test_json_with_all_paths_types',
                                'produces': [
                                    'application/json'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer path',
                                        'in': 'path',
                                        'name': 'path_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 path',
                                        'in': 'path',
                                        'name': 'path_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 path',
                                        'in': 'path',
                                        'name': 'path_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number path',
                                        'in': 'path',
                                        'name': 'path_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float path',
                                        'in': 'path',
                                        'name': 'path_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double path',
                                        'in': 'path',
                                        'name': 'path_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string path',
                                        'in': 'path',
                                        'name': 'path_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte path',
                                        'in': 'path',
                                        'name': 'path_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary path',
                                        'in': 'path',
                                        'name': 'path_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean path',
                                        'in': 'path',
                                        'name': 'path_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date path',
                                        'in': 'path',
                                        'name': 'path_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time path',
                                        'in': 'path',
                                        'name': 'path_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password path',
                                        'in': 'path',
                                        'name': 'path_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array path',
                                        'in': 'path',
                                        'name': 'path_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array path',
                                        'in': 'path',
                                        'name': 'path_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array path',
                                        'in': 'path',
                                        'name': 'path_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array path',
                                        'in': 'path',
                                        'name': 'path_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array path',
                                        'in': 'path',
                                        'name': 'path_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array path',
                                        'in': 'path',
                                        'name': 'path_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array path',
                                        'in': 'path',
                                        'name': 'path_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array path',
                                        'in': 'path',
                                        'name': 'path_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array path',
                                        'in': 'path',
                                        'name': 'path_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array path',
                                        'in': 'path',
                                        'name': 'path_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array path',
                                        'in': 'path',
                                        'name': 'path_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'put': {
                                'operationId': 'put_test_json_with_all_paths_types',
                                'produces': [
                                    'application/json'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer path',
                                        'in': 'path',
                                        'name': 'path_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 path',
                                        'in': 'path',
                                        'name': 'path_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 path',
                                        'in': 'path',
                                        'name': 'path_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number path',
                                        'in': 'path',
                                        'name': 'path_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float path',
                                        'in': 'path',
                                        'name': 'path_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double path',
                                        'in': 'path',
                                        'name': 'path_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string path',
                                        'in': 'path',
                                        'name': 'path_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte path',
                                        'in': 'path',
                                        'name': 'path_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary path',
                                        'in': 'path',
                                        'name': 'path_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean path',
                                        'in': 'path',
                                        'name': 'path_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date path',
                                        'in': 'path',
                                        'name': 'path_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time path',
                                        'in': 'path',
                                        'name': 'path_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password path',
                                        'in': 'path',
                                        'name': 'path_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array path',
                                        'in': 'path',
                                        'name': 'path_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array path',
                                        'in': 'path',
                                        'name': 'path_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array path',
                                        'in': 'path',
                                        'name': 'path_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array path',
                                        'in': 'path',
                                        'name': 'path_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array path',
                                        'in': 'path',
                                        'name': 'path_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array path',
                                        'in': 'path',
                                        'name': 'path_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array path',
                                        'in': 'path',
                                        'name': 'path_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array path',
                                        'in': 'path',
                                        'name': 'path_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array path',
                                        'in': 'path',
                                        'name': 'path_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array path',
                                        'in': 'path',
                                        'name': 'path_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array path',
                                        'in': 'path',
                                        'name': 'path_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'delete': {
                                'operationId': 'delete_test_json_with_all_paths_types',
                                'produces': [
                                    'application/json'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer path',
                                        'in': 'path',
                                        'name': 'path_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 path',
                                        'in': 'path',
                                        'name': 'path_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 path',
                                        'in': 'path',
                                        'name': 'path_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number path',
                                        'in': 'path',
                                        'name': 'path_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float path',
                                        'in': 'path',
                                        'name': 'path_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double path',
                                        'in': 'path',
                                        'name': 'path_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string path',
                                        'in': 'path',
                                        'name': 'path_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte path',
                                        'in': 'path',
                                        'name': 'path_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary path',
                                        'in': 'path',
                                        'name': 'path_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean path',
                                        'in': 'path',
                                        'name': 'path_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date path',
                                        'in': 'path',
                                        'name': 'path_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time path',
                                        'in': 'path',
                                        'name': 'path_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password path',
                                        'in': 'path',
                                        'name': 'path_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array path',
                                        'in': 'path',
                                        'name': 'path_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array path',
                                        'in': 'path',
                                        'name': 'path_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array path',
                                        'in': 'path',
                                        'name': 'path_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array path',
                                        'in': 'path',
                                        'name': 'path_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array path',
                                        'in': 'path',
                                        'name': 'path_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array path',
                                        'in': 'path',
                                        'name': 'path_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array path',
                                        'in': 'path',
                                        'name': 'path_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array path',
                                        'in': 'path',
                                        'name': 'path_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array path',
                                        'in': 'path',
                                        'name': 'path_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array path',
                                        'in': 'path',
                                        'name': 'path_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array path',
                                        'in': 'path',
                                        'name': 'path_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            }
                        },
                       '/test/octet/with/all/paths/types': {
                            'get': {
                                'operationId': 'get_test_octet_with_all_paths_types',
                                'produces': [
                                    'application/octet-stream'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer path',
                                        'in': 'path',
                                        'name': 'path_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 path',
                                        'in': 'path',
                                        'name': 'path_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 path',
                                        'in': 'path',
                                        'name': 'path_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number path',
                                        'in': 'path',
                                        'name': 'path_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float path',
                                        'in': 'path',
                                        'name': 'path_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double path',
                                        'in': 'path',
                                        'name': 'path_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string path',
                                        'in': 'path',
                                        'name': 'path_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte path',
                                        'in': 'path',
                                        'name': 'path_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary path',
                                        'in': 'path',
                                        'name': 'path_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean path',
                                        'in': 'path',
                                        'name': 'path_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date path',
                                        'in': 'path',
                                        'name': 'path_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time path',
                                        'in': 'path',
                                        'name': 'path_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password path',
                                        'in': 'path',
                                        'name': 'path_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array path',
                                        'in': 'path',
                                        'name': 'path_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array path',
                                        'in': 'path',
                                        'name': 'path_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array path',
                                        'in': 'path',
                                        'name': 'path_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array path',
                                        'in': 'path',
                                        'name': 'path_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array path',
                                        'in': 'path',
                                        'name': 'path_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array path',
                                        'in': 'path',
                                        'name': 'path_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array path',
                                        'in': 'path',
                                        'name': 'path_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array path',
                                        'in': 'path',
                                        'name': 'path_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array path',
                                        'in': 'path',
                                        'name': 'path_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array path',
                                        'in': 'path',
                                        'name': 'path_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array path',
                                        'in': 'path',
                                        'name': 'path_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'post': {
                                'operationId': 'post_test_octet_with_all_paths_types',
                                'produces': [
                                    'application/octet-stream'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer path',
                                        'in': 'path',
                                        'name': 'path_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 path',
                                        'in': 'path',
                                        'name': 'path_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 path',
                                        'in': 'path',
                                        'name': 'path_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number path',
                                        'in': 'path',
                                        'name': 'path_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float path',
                                        'in': 'path',
                                        'name': 'path_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double path',
                                        'in': 'path',
                                        'name': 'path_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string path',
                                        'in': 'path',
                                        'name': 'path_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte path',
                                        'in': 'path',
                                        'name': 'path_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary path',
                                        'in': 'path',
                                        'name': 'path_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean path',
                                        'in': 'path',
                                        'name': 'path_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date path',
                                        'in': 'path',
                                        'name': 'path_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time path',
                                        'in': 'path',
                                        'name': 'path_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password path',
                                        'in': 'path',
                                        'name': 'path_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array path',
                                        'in': 'path',
                                        'name': 'path_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array path',
                                        'in': 'path',
                                        'name': 'path_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array path',
                                        'in': 'path',
                                        'name': 'path_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array path',
                                        'in': 'path',
                                        'name': 'path_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array path',
                                        'in': 'path',
                                        'name': 'path_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array path',
                                        'in': 'path',
                                        'name': 'path_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array path',
                                        'in': 'path',
                                        'name': 'path_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array path',
                                        'in': 'path',
                                        'name': 'path_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array path',
                                        'in': 'path',
                                        'name': 'path_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array path',
                                        'in': 'path',
                                        'name': 'path_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array path',
                                        'in': 'path',
                                        'name': 'path_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'put': {
                                'operationId': 'put_test_octet_with_all_paths_types',
                                'produces': [
                                    'application/octet-stream'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer path',
                                        'in': 'path',
                                        'name': 'path_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 path',
                                        'in': 'path',
                                        'name': 'path_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 path',
                                        'in': 'path',
                                        'name': 'path_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number path',
                                        'in': 'path',
                                        'name': 'path_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float path',
                                        'in': 'path',
                                        'name': 'path_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double path',
                                        'in': 'path',
                                        'name': 'path_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string path',
                                        'in': 'path',
                                        'name': 'path_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte path',
                                        'in': 'path',
                                        'name': 'path_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary path',
                                        'in': 'path',
                                        'name': 'path_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean path',
                                        'in': 'path',
                                        'name': 'path_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date path',
                                        'in': 'path',
                                        'name': 'path_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time path',
                                        'in': 'path',
                                        'name': 'path_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password path',
                                        'in': 'path',
                                        'name': 'path_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array path',
                                        'in': 'path',
                                        'name': 'path_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array path',
                                        'in': 'path',
                                        'name': 'path_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array path',
                                        'in': 'path',
                                        'name': 'path_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array path',
                                        'in': 'path',
                                        'name': 'path_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array path',
                                        'in': 'path',
                                        'name': 'path_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array path',
                                        'in': 'path',
                                        'name': 'path_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array path',
                                        'in': 'path',
                                        'name': 'path_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array path',
                                        'in': 'path',
                                        'name': 'path_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array path',
                                        'in': 'path',
                                        'name': 'path_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array path',
                                        'in': 'path',
                                        'name': 'path_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array path',
                                        'in': 'path',
                                        'name': 'path_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            },
                            'delete': {
                                'operationId': 'delete_test_octet_with_all_paths_types',
                                'produces': [
                                    'application/octet-stream'
                                ],
                                'parameters': [
                                    {
                                        'description': 'integer path',
                                        'in': 'path',
                                        'name': 'path_integer',
                                        'required': True,
                                        'type': 'integer'
                                    },
                                    {
                                        'description': 'integer 32 path',
                                        'in': 'path',
                                        'name': 'path_integer32',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int32'
                                    },
                                    {
                                        'description': 'integer 64 path',
                                        'in': 'path',
                                        'name': 'path_integer64',
                                        'required': True,
                                        'type': 'integer',
                                        'format': 'int64'
                                    },
                                    {
                                        'description': 'number path',
                                        'in': 'path',
                                        'name': 'path_number',
                                        'required': True,
                                        'type': 'number'
                                    },
                                    {
                                        'description': 'number float path',
                                        'in': 'path',
                                        'name': 'path_float',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'float'
                                    },
                                    {
                                        'description': 'number double path',
                                        'in': 'path',
                                        'name': 'path_double',
                                        'required': True,
                                        'type': 'number',
                                        'format': 'double'
                                    },
                                    {
                                        'description': 'string path',
                                        'in': 'path',
                                        'name': 'path_string',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'string byte path',
                                        'in': 'path',
                                        'name': 'path_string_byte',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'byte'
                                    },
                                    {
                                        'description': 'string binary path',
                                        'in': 'path',
                                        'name': 'path_string_binary',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'binary'
                                    },
                                    {
                                        'description': 'boolean path',
                                        'in': 'path',
                                        'name': 'path_boolean',
                                        'required': True,
                                        'type': 'boolean'
                                    },
                                    {
                                        'description': 'date path',
                                        'in': 'path',
                                        'name': 'path_date',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date'
                                    },
                                    {
                                        'description': 'date time path',
                                        'in': 'path',
                                        'name': 'path_date_time',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'date-time'
                                    },
                                    {
                                        'description': 'password path',
                                        'in': 'path',
                                        'name': 'path_password',
                                        'required': True,
                                        'type': 'string',
                                        'format': 'password'
                                    },
                                    {
                                        'description': 'integer array path',
                                        'in': 'path',
                                        'name': 'path_array_integer',
                                        'required': True,
                                        'items': {
                                            'type': 'integer'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 32 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer32',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int32'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'integer 64 array path',
                                        'in': 'path',
                                        'name': 'path_array_integer64',
                                        'required': True,
                                        'items': {
                                            'type': 'integer',
                                            'format': 'int64'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number array path',
                                        'in': 'path',
                                        'name': 'path_array_number',
                                        'required': True,
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number float array path',
                                        'in': 'path',
                                        'name': 'path_array_float',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'float'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'number double array path',
                                        'in': 'path',
                                        'name': 'path_array_double',
                                        'required': True,
                                        'items': {
                                            'type': 'number',
                                            'format': 'double'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string array path',
                                        'in': 'path',
                                        'name': 'path_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string byte array path',
                                        'in': 'path',
                                        'name': 'path_array_string_byte',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'byte'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'string binary array path',
                                        'in': 'path',
                                        'name': 'path_array_string_binary',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'binary'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'boolean array path',
                                        'in': 'path',
                                        'name': 'path_array_boolean',
                                        'required': True,
                                        'items': {
                                            'type': 'boolean'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date array path',
                                        'in': 'path',
                                        'name': 'path_array_date',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'date time array path',
                                        'in': 'path',
                                        'name': 'path_array_date_time',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'date-time'
                                        },
                                        'type': 'array'
                                    },
                                    {
                                        'description': 'password array path',
                                        'in': 'path',
                                        'name': 'path_array_password',
                                        'required': True,
                                        'items': {
                                            'type': 'string',
                                            'format': 'password'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            }
                        },
                       '/test/vba/restricted/keywords': {
                            'get': {
                                'operationId': 'get_test_vba_restricted_keywords',
                                'parameters': [
                                    {
                                        'description': 'currency parameter',
                                        'in': 'query',
                                        'name': 'currency',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'end parameter',
                                        'in': 'query',
                                        'name': 'end',
                                        'required': True,
                                        'type': 'string'
                                    }
                                ]
                            },
                            'post': {
                                'operationId': 'post_test_vba_restricted_keywords',
                                'parameters': [
                                    {
                                        'description': 'currency parameter',
                                        'in': 'query',
                                        'name': 'currency',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'end parameter',
                                        'in': 'query',
                                        'name': 'end',
                                        'required': True,
                                        'type': 'string'
                                    }
                                ]
                            },
                            'put': {
                                'operationId': 'put_test_vba_restricted_keywords',
                                'parameters': [
                                    {
                                        'description': 'currency parameter',
                                        'in': 'query',
                                        'name': 'currency',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'end parameter',
                                        'in': 'query',
                                        'name': 'end',
                                        'required': True,
                                        'type': 'string'
                                    }
                                ]
                            },
                            'delete': {
                                'operationId': 'delete_test_vba_restricted_keywords',
                                'parameters': [
                                    {
                                        'description': 'currency parameter',
                                        'in': 'query',
                                        'name': 'currency',
                                        'required': True,
                                        'type': 'string'
                                    },
                                    {
                                        'description': 'end parameter',
                                        'in': 'query',
                                        'name': 'end',
                                        'required': True,
                                        'type': 'string'
                                    }
                                ]
                            }
                       },
                       '/test/string/array/parameter': {
                            'get': {
                                'operationId': 'get_test_string_array_parameter',
                                'parameters': [
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            }
                       },
                       '/test/header/parameter': {
                            'get': {
                                'operationId': 'get_test_header_parameter',
                                'parameters': [
                                    {
                                        'description': 'header parameter',
                                        'in': 'header',
                                        'name': 'header_string',
                                        'required': True,
                                        'type': 'string'
                                    }
                                ]
                            }
                       },
                       '/test/form/parameter': {
                            'post': {
                                'operationId': 'post_test_form_parameter',
                                'parameters': [
                                    {
                                        'description': 'form parameter',
                                        'in': 'formData',
                                        'name': 'form_string',
                                        'required': True,
                                        'type': 'string'
                                    }
                                ]
                            }
                       },
                       '/test/dict/with/empty/nested/list': {
                           'get': {
                               'operationId': 'get_test_dict_with_empty_nested_list'
                           }
                       },
                       '/test/dict/with/three/imbricated/levels': {
                           'get': {
                               'operationId': 'get_test_dict_with_three_imbricated_levels'
                           }
                       },
                       '/test/dict/with/four/imbricated/levels': {
                           'get': {
                               'operationId': 'get_test_dict_with_four_imbricated_levels'
                           }
                       },
                       '/test/dict/with/multiple/imbricated/levels/and/duplicate/keys': {
                           'get': {
                               'operationId': 'get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys'
                           }
                       },
                       '/test/empty/dict': {
                           'get': {
                               'operationId': 'get_test_empty_dict'
                           }
                       },
                       '/test/empty/list': {
                           'get': {
                               'operationId': 'get_test_empty_list'
                           }
                       },
                       '/test/one/level/dict': {
                           'get': {
                               'operationId': 'get_test_one_level_dict'
                           }
                       },
                       '/test/one/level/list': {
                           'get': {
                               'operationId': 'get_test_one_level_list'
                           }
                       },
                       '/test/one/dict/entry/with/a/list': {
                           'get': {
                               'operationId': 'get_test_one_dict_entry_with_a_list'
                           }
                       },
                       '/test/one/dict/entry/with/a/list/of/dict': {
                           'get': {
                               'operationId': 'get_test_one_dict_entry_with_a_list_of_dict'
                           }
                       },
                       '/test/list/of/dict': {
                           'get': {
                               'operationId': 'get_test_list_of_dict'
                           }
                       }
    })


@app.route('/test/vba/restricted/keywords', methods=['GET'])
def get_test_vba_restricted_keywords():
    return jsonify(request.args)


@app.route('/test/vba/restricted/keywords', methods=['POST'])
def post_test_vba_restricted_keywords():
    return jsonify(request.args)


@app.route('/test/vba/restricted/keywords', methods=['PUT'])
def put_test_vba_restricted_keywords():
    return jsonify(request.args)


@app.route('/test/vba/restricted/keywords', methods=['DELETE'])
def delete_test_vba_restricted_keywords():
    return jsonify(request.args)


@app.route('/test/json/with/all/parameters/types', methods=['GET'])
def get_test_json_with_all_parameters_types():
    return jsonify(request.args)


@app.route('/test/json/with/all/optional/parameters/types', methods=['GET'])
def get_test_json_with_all_optional_parameters_types():
    return jsonify(request.args)


@app.route('/test/string/array/parameter', methods=['GET'])
def get_test_string_array_parameter():
    return ', '.join(_request_args(request.args))


@app.route('/test/plain/text/without/parameter', methods=['GET'])
def get_test_plain_text_without_parameter():
    return 'string value returned should be truncated so that the following information cannot be seen by user, ' \
           'because of the fact that Excel does not allow more than 255 characters in a cell. ' \
           'Only the 255 characters will be returned by the user defined functions:  YOU CANNOT RECEIVE THIS!!!!!!'


@app.route('/test/without/parameter', methods=['POST'])
def post_test_without_parameter():
    return 'POST performed properly'


@app.route('/test/without/parameter', methods=['PUT'])
def put_test_without_parameter():
    return 'PUT performed properly'


@app.route('/test/without/parameter', methods=['DELETE'])
def delete_test_without_parameter():
    return 'DELETE performed properly'


@app.route('/test/header/parameter', methods=['GET'])
def get_test_header_parameter():
    return jsonify(dict(request.headers))


@app.route('/test/form/parameter', methods=['POST'])
def post_test_form_parameter():
    return Response(request.data, mimetype='application/json')


def _request_args(args):
    return ['{0}="{1}"'.format(arg, args.getlist(arg)) for arg in args]


@app.route('/swagger_version_not_provided')
def swagger_version_not_provided():
    return jsonify(paths={
        '/test/should/not/be/available': {
            'get': {
                'operationId': 'get_test_should_not_be_available'
            }
        },
    })


@app.route('/swagger_version_not_supported')
def swagger_version_not_supported():
    return jsonify(swagger='1.0',
                   paths={
                       '/test/should/not/be/available': {
                           'get': {
                               'operationId': 'get_test_should_not_be_available'
                           }
                       }
                   })


@app.route('/test/dict/with/empty/nested/list', methods=['GET'])
def get_test_dict_with_empty_nested_list():
    dict_with_nested_list = {
        "Column 1": "0-0-1",
        "Column 2": [
            {
                "Column 2.1": "0-0-2 / 1-0-1",
                "Column 2.2": [],
                "Column 2.3": "0-0-2 / 1-0-3"
            },
            {
                "Column 2.1": "0-0-2 / 1-1-1",
                "Column 2.2": [
                    {
                        "Column 3.1": "0-0-2 / 1-1-2 / 2-0-1",
                        "Column 3.2": [],
                        "Column 3.3": "0-0-2 / 1-1-2 / 2-0-3"
                    },
                    {
                        "Column 3.1": "0-0-2 / 1-1-2 / 2-1-1",
                        "Column 3.2": [],
                        "Column 3.3": "0-0-2 / 1-1-2 / 2-1-3"
                    }
                ],
                "Column 2.3": "0-0-2 / 1-1-3"
            }
        ],
        "Column 3": "0-0-3"
    }
    return jsonify(dict_with_nested_list)


@app.route('/test/dict/with/three/imbricated/levels', methods=['GET'])
def get_test_dict_with_three_imbricated_levels():
    dict_with_imbricated_levels = {
        "Column 1": "0-0-1",
        "Column 2": [
            {
                "Column 2.1": "0-0-2 / 1-0-1",
                "Column 2.2": [
                    {
                        "Column 3.1": "0-0-2 / 1-0-2 / 2-0-1",
                        "Column 3.2": [],
                        "Column 3.3": "0-0-2 / 1-0-2 / 2-0-3"
                    },
                    {
                        "Column 3.1": "0-0-2 / 1-0-2 / 2-1-1",
                        "Column 3.2": [],
                        "Column 3.3": "0-0-2 / 1-0-2 / 2-1-3"
                    }
                ],
                "Column 2.3": "0-0-2 / 1-0-3"
            },
            {
                "Column 2.1": "0-0-2 / 1-1-1",
                "Column 2.2": [
                    {
                        "Column 3.1": "0-0-2 / 1-1-2 / 2-0-1",
                        "Column 3.2": [],
                        "Column 3.3": "0-0-2 / 1-1-2 / 2-0-3"
                    },
                    {
                        "Column 3.1": "0-0-2 / 1-1-2 / 2-1-1",
                        "Column 3.2": [],
                        "Column 3.3": "0-0-2 / 1-1-2 / 2-1-3"
                    }
                ],
                "Column 2.3": "0-0-2 / 1-1-3"
            }
        ],
        "Column 3": "0-0-3"
    }
    return jsonify(dict_with_imbricated_levels)


@app.route('/test/dict/with/four/imbricated/levels', methods=['GET'])
def get_test_dict_with_four_imbricated_levels():
    dict_with_imbricated_levels = {
        "Column 1": "0-0-1",
        "Column 2": [
            {
                "Column 2.1": "0-0-2 / 1-0-1",
                "Column 2.2": [
                    {
                        "Column 3.1": "0-0-2 / 1-0-2 / 2-0-1",
                        "Column 3.2": [
                            {
                                "Column 4.1": "0-0-2 / 1-0-2 / 2-0-2 / 3-0-1",
                                "Column 4.2": [],
                                "Column 4.3": "0-0-2 / 1-0-2 / 2-0-2 / 3-0-3"
                            },
                            {
                                "Column 4.1": "0-0-2 / 1-0-2 / 2-0-2 / 3-1-1",
                                "Column 4.2": [],
                                "Column 4.3": "0-0-2 / 1-0-2 / 2-0-2 / 3-1-3"
                            }
                        ],
                        "Column 3.3": "0-0-2 / 1-0-2 / 2-0-3"
                    },
                    {
                        "Column 3.1": "0-0-2 / 1-0-2 / 2-1-1",
                        "Column 3.2": [],
                        "Column 3.3": "0-0-2 / 1-0-2 / 2-1-3"
                    }
                ],
                "Column 2.3": "0-0-2 / 1-0-3"
            },
            {
                "Column 2.1": "0-0-2 / 1-1-1",
                "Column 2.2": [
                    {
                        "Column 3.1": "0-0-2 / 1-1-2 / 2-0-1",
                        "Column 3.2": [],
                        "Column 3.3": "0-0-2 / 1-1-2 / 2-0-3"
                    },
                    {
                        "Column 3.1": "0-0-2 / 1-1-2 / 2-1-1",
                        "Column 3.2": [],
                        "Column 3.3": "0-0-2 / 1-1-2 / 2-1-3"
                    }
                ],
                "Column 2.3": "0-0-2 / 1-1-3"
            }
        ],
        "Column 3": "0-0-3"
    }
    return jsonify(dict_with_imbricated_levels)


@app.route('/test/dict/with/multiple/imbricated/levels/and/duplicate/keys', methods=['GET'])
def get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys():
    dict_with_imbricated_levels = {
        "Column 1": "0-0-1",
        "Column 2": [
            {
                "Column 1": "0-0-2 / 1-0-1",
                "Column 2": [
                    {
                        "Column 1": "0-0-2 / 1-0-2 / 2-0-1",
                        "Column 2": [
                            {
                                "Column 1": "0-0-2 / 1-0-2 / 2-0-2 / 3-0-1",
                                "Column 2": [],
                                "Column 3": "0-0-2 / 1-0-2 / 2-0-2 / 3-0-3"
                            },
                            {
                                "Column 1": "0-0-2 / 1-0-2 / 2-0-2 / 3-1-1",
                                "Column 2": [],
                                "Column 3": "0-0-2 / 1-0-2 / 2-0-2 / 3-1-3"
                            }
                        ],
                        "Column 3": "0-0-2 / 1-0-2 / 2-0-3"
                    },
                    {
                        "Column 1": "0-0-2 / 1-0-2 / 2-1-1",
                        "Column 2": [],
                        "Column 3": "0-0-2 / 1-0-2 / 2-1-3"
                    }
                ],
                "Column 3": "0-0-2 / 1-0-3"
            },
            {
                "Column 1": "0-0-2 / 1-1-1",
                "Column 2": [
                    {
                        "Column 1": "0-0-2 / 1-1-2 / 2-0-1",
                        "Column 2": [],
                        "Column 3": "0-0-2 / 1-1-2 / 2-0-3"
                    },
                    {
                        "Column 1": "0-0-2 / 1-1-2 / 2-1-1",
                        "Column 2": [],
                        "Column 3": "0-0-2 / 1-1-2 / 2-1-3"
                    }
                ],
                "Column 3": "0-0-2 / 1-1-3"
            }
        ],
        "Column 3": "0-0-3"
    }
    return jsonify(dict_with_imbricated_levels)


@app.route('/test/empty/dict', methods=['GET'])
def get_test_empty_dict():
    return jsonify({})


@app.route('/test/empty/list', methods=['GET'])
def get_test_empty_list():
    return jsonify([])


@app.route('/test/one/level/dict', methods=['GET'])
def get_test_one_level_dict():
    return jsonify({
        "Column 1": "value 1",
        "Column 2": "value 2"
    })


@app.route('/test/one/level/list', methods=['GET'])
def get_test_one_level_list():
    return jsonify([
        "value 1",
        "value 2"
    ])


@app.route('/test/one/dict/entry/with/a/list', methods=['GET'])
def get_test_one_dict_entry_with_a_list():
    return jsonify({
        'Column 1': [
        "value 1",
        "value 2"
    ]})


@app.route('/test/one/dict/entry/with/a/list/of/dict', methods=['GET'])
def get_test_one_dict_entry_with_a_list_of_dict():
    return jsonify({
        'Column 1': [
            {
                'Column 2': "value 12",
                'Column 3': "value 13"
            },
            {
                'Column 2': "value 22",
                'Column 3': "value 23"
            }
        ]
    })


@app.route('/test/list/of/dict', methods=['GET'])
def get_test_list_of_dict():
    return jsonify([
            {
                'Column 1': "value 11",
                'Column 2': "value 12"
            },
            {
                'Column 1': "value 21",
                'Column 2': "value 22"
            }
        ])


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8943)

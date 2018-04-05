from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def open_api_definition():
    return jsonify(swagger='2.0',
                   paths={
                       '/with/all/parameters/types': {
                            'get': {
                                'operationId': 'get_with_all_parameters_types',
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
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            },
                            'post': {
                                'operationId': 'post_with_all_parameters_types',
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
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            },
                            'put': {
                                'operationId': 'put_with_all_parameters_types',
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
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            },
                            'delete': {
                                'operationId': 'delete_with_all_parameters_types',
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
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            }
                        },
                       '/with/all/optional/parameters/types': {
                            'get': {
                                'operationId': 'get_with_all_optional_parameters_types',
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
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            },
                            'post': {
                                'operationId': 'post_with_all_optional_parameters_types',
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
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            },
                            'put': {
                                'operationId': 'put_with_all_optional_parameters_types',
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
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            },
                            'delete': {
                                'operationId': 'delete_with_all_optional_parameters_types',
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
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            }
                        },
                       '/with/all/paths/types': {
                            'get': {
                                'operationId': 'get_with_all_paths_types',
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
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            },
                            'post': {
                                'operationId': 'post_with_all_paths_types',
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
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            },
                            'put': {
                                'operationId': 'put_with_all_paths_types',
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
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            },
                            'delete': {
                                'operationId': 'delete_with_all_paths_types',
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
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            }
                        },
                       '/date': {
                           'get': {
                               'operationId': 'get_date',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                       'schema': {
                                           'type': 'array',
                                           'items': {
                                               'type': 'string',
                                               'format': 'date'
                                           }
                                       }
                                   }
                               }
                           }
                       },
                       '/datetime': {
                           'get': {
                               'operationId': 'get_date_time',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                       'schema': {
                                           'type': 'array',
                                           'items': {
                                               'type': 'string',
                                               'format': 'date-time'
                                           }
                                       }
                                   }
                               }
                           }
                       },
                       '/datetime/encoding': {
                           'get': {
                               'operationId': 'get_date_time_encoding',
                               'parameters': [
                                   {
                                       'description': 'string parameter',
                                       'in': 'query',
                                       'name': 'encoded_date_time',
                                       'required': True,
                                       'type': 'string',
                                       'format': 'date-time'
                                   },
                               ],
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                   }
                               }
                           }
                       }
    })


@app.route('/date', methods=['GET'])
def get_date():
    return jsonify([
        '2014-03-05',
        '9999-01-01',
        '3001-01-01',
    ])


@app.route('/datetime', methods=['GET'])
def get_date_time():
    return jsonify([
        '2014-03-05T15:59:58.20198Z',
        '2014-03-05T15:59:58.20198z',
        '2014-03-05 15:59:58.20198Z',
        '2014-03-05t15:59:58.20198Z',
        '2014-03-05t15:59:58.20198z',
        '9999-01-01T00:00:00+00:00',
        '3001-01-01T08:00:00+00:00',
    ])


@app.route('/datetime/encoding', methods=['GET'])
def get_date_time_encoding():
    return request.args.get('encoded_date_time')


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8943)

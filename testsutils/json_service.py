from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def open_api_definition():
    return jsonify(swagger='2.0',
                   definitions={
                       'DictWithReadOnly': {
                           'type': 'object',
                           'required': [
                               'dict_field1',
                           ],
                           'properties': {
                               'dict_field1': {
                                   'type': 'integer',
                               },
                               'read_only_field': {
                                   'type': 'string',
                                   'readOnly': True,
                               },
                               'dict_field3': {
                                   'type': 'boolean',
                               }
                           },
                           'title': 'Test'
                       },
                       'Dict': {
                           'type': 'object',
                           'required': [
                               'dict_field1',
                           ],
                           'properties': {
                               'dict_field1': {
                                   'type': 'string',
                               },
                               'dict_field2': {
                                   'type': 'string',
                               }
                           },
                           'title': 'Test'
                       },
                       'DictWithDict': {
                           'type': 'object',
                           'properties': {
                               'inner_dict': {
                                   'type': 'object',
                               },
                               'dict_field1': {
                                   'type': 'string',
                               },
                               'dict_field2': {
                                   'type': 'string',
                               }
                           },
                           'title': 'Test'
                       },
                       'DictWithDictList': {
                           'type': 'object',
                           'properties': {
                               'inner_dict_list': {
                                   'type': 'array',
                                   'items': {
                                       '$ref': '#/definitions/Dict',
                                   },
                                   'collectionFormat': 'multi',
                               },
                               'dict_field1': {
                                   'type': 'string',
                               },
                               'dict_field2': {
                                   'type': 'string',
                               }
                           },
                           'title': 'Test'
                       },
                       'DictWithListOfList': {
                           'type': 'object',
                           'properties': {
                               'inner_list_of_list': {
                                   'type': 'array',
                                   'items': {
                                       'type': 'array',
                                       'items': {
                                           'type': 'string',
                                       },
                                       'collectionFormat': 'multi',
                                   },
                                   'collectionFormat': 'multi',
                               },
                               'dict_field1': {
                                   'type': 'string',
                               },
                               'dict_field2': {
                                   'type': 'string',
                               }
                           },
                           'title': 'Test'
                       },
                       'TestObject': {
                           'type': 'object',
                           'properties': {
                               'test': {
                                   'type': 'string',
                                   'description': 'test',
                               }
                           },
                           'title': 'Test'
                       },
                       'AllMandatoryParameters': {
                           'properties': {
                               'query_array_boolean': {
                               },
                               'query_array_date': {
                                   'type': 'array',
                                   'items': {
                                       'type': 'string',
                                       'format': 'date'
                                   },
                                   'collectionFormat': 'multi',
                               },
                               'query_array_date_time': {
                                   'type': 'array',
                                   'items': {
                                       'type': 'string',
                                       'format': 'date-time'
                                   },
                                   'collectionFormat': 'multi',
                               },
                               'query_array_double': {
                               },
                               'query_array_float': {
                               },
                               'query_array_integer': {
                               },
                               'query_array_integer32': {
                               },
                               'query_array_integer64': {
                               },
                               'query_array_number': {
                               },
                               'query_array_password': {
                               },
                               'query_array_string': {
                               },
                               'query_array_string_binary': {
                               },
                               'query_array_string_byte': {
                               },
                               'query_boolean': {
                               },
                               'query_date': {
                                   'type': 'string',
                                   'format': 'date'
                               },
                               'query_date_time': {
                                   'type': 'string',
                                   'format': 'date-time'
                               },
                               'query_double': {
                               },
                               'query_float': {
                               },
                               'query_integer': {
                               },
                               'query_integer32': {
                               },
                               'query_integer64': {
                               },
                               'query_number': {
                               },
                               'query_password': {
                               },
                               'query_string': {
                               },
                               'query_string_binary': {
                               },
                               'query_string_byte': {
                               }
                           }
                       }
                   },
                   paths={
                       '/different_location_same_name/{dict_field1}': {
                           'post': {
                               'operationId': 'post_different_location_same_name',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                   }
                               },
                               'parameters': [
                                   {
                                       'name': "payload",
                                       'required': True,
                                       'in': "body",
                                       'schema': {
                                           '$ref': "#/definitions/Dict",
                                       },
                                   },
                                   {
                                       'name': "dict_field1",
                                       'required': True,
                                       'in': "header",
                                       'type': 'string',
                                   },
                                   {
                                       'name': "dict_field1",
                                       'required': True,
                                       'in': "query",
                                       'type': 'string',
                                   },
                                   {
                                       'name': "dict_field1",
                                       'required': True,
                                       'in': "path",
                                       'type': 'string',
                                   },
                               ],
                           },
                       },
                       '/list_parameter': {
                           'get': {
                               'operationId': 'get_list_parameter',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                   }
                               },
                               'parameters': [
                                   {
                                       'name': "list_parameter",
                                       'required': True,
                                       'in': "query",
                                       'type': 'string',
                                   },
                               ],
                           },
                           'delete': {
                               'operationId': 'delete_list_parameter',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                   }
                               },
                               'parameters': [
                                   {
                                       'name': "list_parameter",
                                       'required': True,
                                       'in': "query",
                                       'type': 'string',
                                   },
                               ],
                           },
                       },
                       '/dict_with_read_only': {
                           'post': {
                               'operationId': 'post_dict_with_read_only',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                   }
                               },
                               'parameters': [
                                   {
                                       'name': "payload",
                                       'required': True,
                                       'in': "body",
                                       'schema': {
                                           'type': 'array',
                                           'items': {
                                               '$ref': "#/definitions/DictWithReadOnly",
                                           },
                                           'collectionFormat': 'multi',
                                       },
                                   },
                               ],
                           },
                       },
                       '/dict_string': {
                           'post': {
                               'operationId': 'post_dict_string',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                   }
                               },
                               'parameters': [
                                   {
                                       'name': "payload",
                                       'required': True,
                                       'in': "body",
                                       'schema': {
                                           '$ref': "#/definitions/Dict",
                                       },
                                   },
                               ],
                           },
                       },
                       '/dict_with_list_of_list': {
                           'post': {
                               'operationId': 'post_dict_with_list_of_list',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                   }
                               },
                               'parameters': [
                                   {
                                       'name': "payload",
                                       'required': True,
                                       'in': "body",
                                       'schema': {
                                           '$ref': "#/definitions/DictWithListOfList",
                                       },
                                   },
                               ],
                           },
                       },
                       '/dict_with_dict_list': {
                           'post': {
                               'operationId': 'post_dict_with_dict_list',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                   }
                               },
                               'parameters': [
                                   {
                                       'name': "payload",
                                       'required': True,
                                       'in': "body",
                                       'schema': {
                                           '$ref': "#/definitions/DictWithDictList",
                                       },
                                   },
                               ],
                           },
                       },
                       '/list_of_dict_with_dict': {
                           'post': {
                               'operationId': 'post_list_of_dict_with_dict',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                   }
                               },
                               'parameters': [
                                   {
                                       'name': "payload",
                                       'required': True,
                                       'in': "body",
                                       'schema': {
                                           'type': 'array',
                                           'items': {
                                               '$ref': "#/definitions/DictWithDict",
                                           },
                                           'collectionFormat': 'multi',
                                       },
                                   },
                               ],
                           },
                       },
                       '/dict_with_dict': {
                           'post': {
                               'operationId': 'post_dict_with_dict',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                   }
                               },
                               'parameters': [
                                   {
                                       'name': "payload",
                                       'required': True,
                                       'in': "body",
                                       'schema': {
                                           '$ref': "#/definitions/DictWithDict",
                                       },
                                   },
                               ],
                           },
                       },
                       '/list_of_list_form': {
                           'post': {
                               'operationId': 'post_list_of_list_form',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                   }
                               },
                               'parameters': [
                                   {
                                       'name': "all_matching",
                                       'in': "query",
                                       'type': "boolean"
                                   },
                                   {
                                       'name': "rules",
                                       'in': "formData",
                                       'collectionFormat': "multi",
                                       'type': "array",
                                       'items': {
                                           'items': {
                                               'type': "string"
                                           },
                                           'type': "array"
                                       }
                                   },
                                   {
                                       'name': "items",
                                       'in': "formData",
                                       'collectionFormat': "multi",
                                       'type': "array",
                                       'items': {
                                           'items': {
                                               'type': "string"
                                           },
                                           'type': "array"
                                       }
                                   }
                               ],
                               'consumes': [
                                   "application/x-www-form-urlencoded",
                                   "multipart/form-data"
                               ],
                           },
                       },
                       '/all_parameters_types': {
                           'get': {
                               'operationId': 'get_all_parameters_types',
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
                                       'type': 'array',
                                       'collectionFormat': 'multi',
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
                                       'type': 'array',
                                       'collectionFormat': 'multi',
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
                                       'type': 'array',
                                       'collectionFormat': 'multi',
                                   },
                                   {
                                       'description': 'number array parameter',
                                       'in': 'query',
                                       'name': 'query_array_number',
                                       'required': True,
                                       'items': {
                                           'type': 'number'
                                       },
                                       'type': 'array',
                                       'collectionFormat': 'multi',
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
                                       'type': 'array',
                                       'collectionFormat': 'multi',
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
                                       'type': 'array',
                                       'collectionFormat': 'multi',
                                   },
                                   {
                                       'description': 'string array parameter',
                                       'in': 'query',
                                       'name': 'query_array_string',
                                       'required': True,
                                       'items': {
                                           'type': 'string'
                                       },
                                       'type': 'array',
                                       'collectionFormat': 'multi',
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
                                       'type': 'array',
                                       'collectionFormat': 'multi',
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
                                       'type': 'array',
                                       'collectionFormat': 'multi',
                                   },
                                   {
                                       'description': 'boolean array parameter',
                                       'in': 'query',
                                       'name': 'query_array_boolean',
                                       'required': True,
                                       'items': {
                                           'type': 'boolean'
                                       },
                                       'type': 'array',
                                       'collectionFormat': 'multi',
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
                                       'type': 'array',
                                       'collectionFormat': 'multi',
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
                                       'type': 'array',
                                       'collectionFormat': 'multi',
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
                                       'type': 'array',
                                       'collectionFormat': 'multi',
                                   }
                               ],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           '$ref': '#/definitions/AllMandatoryParameters'
                                       }
                                   }
                               }
                           },
                           'post': {
                               'operationId': 'post_all_parameters_types',
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
                               ],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/TestObject'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           },
                           'put': {
                               'operationId': 'put_all_parameters_types',
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
                               ],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/TestObject'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           },
                           'delete': {
                               'operationId': 'delete_all_parameters_types',
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
                               ],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/TestObject'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           }
                       },
                       '/all_optional_parameters_types': {
                           'get': {
                               'operationId': 'get_all_optional_parameters_types',
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
                               ],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/TestObject'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           },
                           'post': {
                               'operationId': 'post_all_optional_parameters_types',
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
                               ],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/TestObject'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           },
                           'put': {
                               'operationId': 'put_all_optional_parameters_types',
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
                               ],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/TestObject'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           },
                           'delete': {
                               'operationId': 'delete_all_optional_parameters_types',
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
                               ],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/TestObject'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           }
                       },
                       '/all_paths_types': {
                           'get': {
                               'operationId': 'get_all_paths_types',
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
                               ],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/TestObject'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           },
                           'post': {
                               'operationId': 'post_all_paths_types',
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
                               ],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/TestObject'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           },
                           'put': {
                               'operationId': 'put_all_paths_types',
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
                               ],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/TestObject'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           },
                           'delete': {
                               'operationId': 'delete_all_paths_types',
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
                               ],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/TestObject'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           }
                       }
                   })


@app.route('/list_parameter', methods=['GET', 'DELETE'])
def list_parameter():
    return jsonify(request.args.getlist('list_parameter'))


@app.route('/dict_with_read_only', methods=['POST'])
def post_dict_with_read_only():
    return jsonify(request.json)


@app.route('/different_location_same_name/<string:dict_field1>', methods=['POST'])
def post_different_location_same_name(dict_field1):
    all_sent = request.json
    all_sent['header_dict_field1'] = request.headers.get('dict_field1')
    all_sent['query_dict_field1'] = request.args.get('dict_field1')
    all_sent['path_dict_field1'] = dict_field1
    return jsonify(all_sent)


@app.route('/dict_string', methods=['POST'])
def post_dict_string():
    return jsonify(request.json)


@app.route('/dict_with_list_of_list', methods=['POST'])
def post_dict_with_list_of_list():
    if request.json == {'dict_field1': 'value000', 'dict_field2': 'value010', 'inner_list_of_list': [['key1', 'key2', 'key3'], ['value10', 'value20', 'value30'], ['value11', 'value21', 'value31'], ['value12', 'value22', 'value32']]}:
        return jsonify('OK')
    if request.json == {'dict_field1': 'value000', 'dict_field2': 'value010', 'inner_list_of_list': [['key1'], ['key2'], ['key3']]}:
        return jsonify('OK')
    return jsonify(request.json)


@app.route('/dict_with_dict_list', methods=['POST'])
def post_dict_with_dict_list():
    return jsonify(request.json)


@app.route('/list_of_dict_with_dict', methods=['POST'])
def post_list_of_dict_with_dict():
    return jsonify(request.json)


@app.route('/dict_with_dict', methods=['POST'])
def post_dict_with_dict():
    return jsonify(request.json)


@app.route('/list_of_list_form', methods=['POST'])
def post_lists_of_list_form():
    if request.json == {'rules': [['1', 'EBE', 'SNCF', 'rule_1', 'output_1'], ['1', 'EFR,EDE', 'ENGIE', 'rule_2', 'output_2']], 'items': [['Deal Number', 'Underlying', 'Client'], ['0001', 'EBE', 'SNCF'], ['0002', 'EFR', 'ENGIE'], ['0003', 'EDE', 'ENGIE']]}:
        return jsonify('OK')
    if request.json == {'rules': [['rule1'], ['rule2'], ['rule3']], 'items': [['item1'], ['item2'], ['item3']]}:
        return jsonify('OK')
    return jsonify(request.json)


@app.route('/all_parameters_types', methods=['GET'])
def get_all_parameters_types():
    return jsonify(request.args)


@app.route('/all_optional_parameters_types', methods=['GET'])
def get_all_optional_parameters_types():
    return jsonify(request.args)


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8954)
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def open_api_definition():
    return jsonify(swagger='2.0',
                   definitions={
                       'ZeroInteger': {
                           'properties': {
                               'zero_integer': {
                                   'type': 'integer',
                                   'format': 'int32'
                               }
                           }
                       },
                       'ZeroFloat': {
                           'properties': {
                               'zero_float': {
                                   'type': 'number',
                                   'format': 'float'
                               }
                           }
                       },
                       'FalseBoolean': {
                           'properties': {
                               'false_boolean': {
                                   'type': 'boolean'
                               }
                           }
                       },
                       'EmptyString': {
                           'properties': {
                               'empty_string': {
                                   'type': 'string'
                               }
                           }
                       },
                       'EmptyList': {
                           'properties': {
                               'empty_list': {
                                   'type': 'array',
                                   'items': {
                                       '$ref': '#/definitions/Empty'
                                   }
                               }
                           }
                       },
                       'EmptyDictionary': {
                           'properties': {
                               'empty_dictionary': {
                                   'type': 'object',
                                   '$ref': '#/definitions/Empty'
                               }
                           }
                       },
                       'Empty': {
                           'properties': {
                           }
                       }
                   },
                   paths={
                       '/with/zero/integer': {
                           'get': {
                               'operationId': 'get_with_zero_integer',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                       'schema': {
                                           'type': 'array',
                                           'items': {
                                               '$ref': '#/definitions/ZeroInteger'
                                           }
                                       }
                                   }
                               }
                           }
                       },
                       '/with/zero/float': {
                           'get': {
                               'operationId': 'get_with_zero_float',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                       'schema': {
                                           'type': 'array',
                                           'items': {
                                               '$ref': '#/definitions/ZeroFloat'
                                           }
                                       }
                                   }
                               }
                           }
                       },
                       '/with/false/boolean': {
                           'get': {
                               'operationId': 'get_with_false_boolean',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                       'schema': {
                                           'type': 'array',
                                           'items': {
                                               '$ref': '#/definitions/FalseBoolean'
                                           }
                                       }
                                   }
                               }
                           }
                       },
                       '/with/empty/string': {
                           'get': {
                               'operationId': 'get_with_empty_string',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                       'schema': {
                                           'type': 'array',
                                           'items': {
                                               '$ref': '#/definitions/EmptyString'
                                           }
                                       }
                                   }
                               }
                           }
                       },
                       '/with/empty/list': {
                           'get': {
                               'operationId': 'get_with_empty_list',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                       'schema': {
                                           'type': 'array',
                                           'items': {
                                               '$ref': '#/definitions/EmptyList'
                                           }
                                       }
                                   }
                               }
                           }
                       },
                       '/with/empty/dictionary': {
                           'get': {
                               'operationId': 'get_with_empty_dictionary',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                       'schema': {
                                           'type': 'array',
                                           'items': {
                                               '$ref': '#/definitions/EmptyDictionary'
                                           }
                                       }
                                   }
                               }
                           }
                       }
                   })


@app.route('/with/zero/integer', methods=['GET'])
def get_with_zero_integer():
    return jsonify([{'zero_integer': 0}])


@app.route('/with/zero/float', methods=['GET'])
def get_with_zero_float():
    return jsonify([{'zero_float': 0.0}])


@app.route('/with/false/boolean', methods=['GET'])
def get_with_false_boolean():
    return jsonify([{'false_boolean': False}])


@app.route('/with/empty/string', methods=['GET'])
def get_with_empty_string():
    return jsonify([{'empty_string': ''}])


@app.route('/with/empty/list', methods=['GET'])
def get_with_empty_list():
    return jsonify([{'empty_list': []}])


@app.route('/with/empty/dictionary', methods=['GET'])
def get_with_empty_dictionary():
    return jsonify([{'empty_dictionary': {}}])


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8945)
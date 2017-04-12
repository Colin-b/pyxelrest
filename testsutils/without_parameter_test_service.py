from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   definitions={
                       'Test': {
                       }
                   },
                   paths={
                       '/test/without/parameter': {
                           'get': {
                               'operationId': 'get_test_without_parameter',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                       'schema': {
                                           'type': 'string'
                                       }
                                   }
                               }
                           },
                           'post': {
                                'operationId': 'post_test_without_parameter',
                                'responses': {
                                   '200': {
                                       'description': 'POST performed properly'
                                   }
                                }
                           },
                           'put': {
                                'operationId': 'put_test_without_parameter',
                                'responses': {
                                   '200': {
                                       'description': 'PUT performed properly'
                                   }
                                }
                           },
                           'delete': {
                                'operationId': 'delete_test_without_parameter',
                                'responses': {
                                   '200': {
                                       'description': 'DELETE performed properly'
                                   }
                                }
                           }
                       },
                       '/test/plain/text/without/parameter': {
                            'get': {
                                'operationId': 'get_test_plain_text_without_parameter',
                                'produces': [
                                    'text/plain'
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value',
                                       'schema': {
                                           'type': 'string'
                                       }
                                   }
                                }
                            },
                            'post': {
                                'operationId': 'post_test_plain_text_without_parameter',
                                'produces': [
                                    'text/plain'
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            },
                            'put': {
                                'operationId': 'put_test_plain_text_without_parameter',
                                'produces': [
                                    'text/plain'
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            },
                            'delete': {
                                'operationId': 'delete_test_plain_text_without_parameter',
                                'produces': [
                                    'text/plain'
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            }
                       },
                       '/test/json/without/parameter': {
                            'get': {
                                'operationId': 'get_test_json_without_parameter',
                                'produces': [
                                    'application/json'
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value',
                                       '$ref': '#/definitions/Test'
                                   }
                                }
                            },
                            'post': {
                                'operationId': 'post_test_json_without_parameter',
                                'produces': [
                                    'application/json'
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value',
                                       '$ref': '#/definitions/Test'
                                   }
                                }
                            },
                            'put': {
                                'operationId': 'put_test_json_without_parameter',
                                'produces': [
                                    'application/json'
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value',
                                       '$ref': '#/definitions/Test'
                                   }
                                }
                            },
                            'delete': {
                                'operationId': 'delete_test_json_without_parameter',
                                'produces': [
                                    'application/json'
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value',
                                       '$ref': '#/definitions/Test'
                                   }
                                }
                            }
                       },
                       '/test/octet/without/parameter': {
                            'get': {
                                'operationId': 'get_test_octet_without_parameter',
                                'produces': [
                                    'application/octet-stream'
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            },
                            'post': {
                                'operationId': 'post_test_octet_without_parameter',
                                'produces': [
                                    'application/octet-stream'
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            },
                            'put': {
                                'operationId': 'put_test_octet_without_parameter',
                                'produces': [
                                    'application/octet-stream'
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            },
                            'delete': {
                                'operationId': 'delete_test_octet_without_parameter',
                                'produces': [
                                    'application/octet-stream'
                                ],
                                'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                                }
                            }
                       }
                   })


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


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8950)

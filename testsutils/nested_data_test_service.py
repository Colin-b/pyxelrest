from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   definitions={
                       'Column': {
                           'type': 'object',
                           'properties': {
                               'Column 1': {
                                   'type': 'string',
                                   'description': 'column1',
                               },
                               'Column 2': {
                                   'type': 'array',
                                   'description': 'column2',
                                   'items': {
                                       '$ref': '#/definitions/Column'
                                   }
                               },
                               'Column 3': {
                                   'type': 'string',
                                   'description': 'column3',
                               }
                           },
                           'title': 'Column'
                       },
                       'Column1': {
                           'type': 'object',
                           'properties': {
                               'Column 1': {
                                   'type': 'array',
                                   'items': {
                                       '$ref': '#/definitions/Column2And3'
                                   },
                               }
                           },
                           'title': 'Column1'
                       },
                       'Column2And3': {
                           'type': 'object',
                           'properties': {
                               'Column 2': {
                                   'type': 'string',
                                   'description': 'column1',
                               },
                               'Column 3': {
                                   'type': 'string',
                                   'description': 'column3',
                               }
                           },
                           'title': 'Column2+3'
                       },
                       'Column1List': {
                           'type': 'object',
                           'properties': {
                               'Column 1': {
                                   'type': 'array',
                                   'items': {
                                       'type': 'string'
                                   },
                               }
                           },
                           'title': 'Column1'
                       }
                   },
                   paths={
                       '/test/dict/with/empty/nested/list': {
                           'get': {
                               'operationId': 'get_test_dict_with_empty_nested_list',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           '$ref': '#/definitions/Column'
                                       }
                                   }
                               }
                           }
                       },
                       '/test/dict/with/three/imbricated/levels': {
                           'get': {
                               'operationId': 'get_test_dict_with_three_imbricated_levels',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           '$ref': '#/definitions/Column'
                                       }
                                   }
                               }
                           }
                       },
                       '/test/dict/with/four/imbricated/levels': {
                           'get': {
                               'operationId': 'get_test_dict_with_four_imbricated_levels',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           '$ref': '#/definitions/Column'
                                       }
                                   }
                               }
                           }
                       },
                       '/test/dict/with/multiple/imbricated/levels/and/duplicate/keys': {
                           'get': {
                               'operationId': 'get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           '$ref': '#/definitions/Column'
                                       }
                                   }
                               }
                           }
                       },
                       '/test/empty/dict': {
                           'get': {
                               'operationId': 'get_test_empty_dict',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           '$ref': '#/definitions/Column'
                                       }
                                   }
                               }
                           }
                       },
                       '/test/empty/list': {
                           'get': {
                               'operationId': 'get_test_empty_list',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/Column'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           }
                       },
                       '/test/one/level/dict': {
                           'get': {
                               'operationId': 'get_test_one_level_dict',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           '$ref': '#/definitions/Column2And3'
                                       }
                                   }
                               }
                           }
                       },
                       '/test/one/level/list': {
                           'get': {
                               'operationId': 'get_test_one_level_list',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               'type': 'string'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           }
                       },
                       '/test/one/dict/entry/with/a/list': {
                           'get': {
                               'operationId': 'get_test_one_dict_entry_with_a_list',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           '$ref': '#/definitions/Column1List'
                                       }
                                   }
                               }
                           }
                       },
                       '/test/one/dict/entry/with/a/list/of/dict': {
                           'get': {
                               'operationId': 'get_test_one_dict_entry_with_a_list_of_dict',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           '$ref': '#/definitions/Column1'
                                       }
                                   }
                               }
                           }
                       },
                       '/test/list/of/dict': {
                           'get': {
                               'operationId': 'get_test_list_of_dict',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/Column2And3'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           }
                       },
                       '/test/dict/with/list': {
                           'get': {
                               'operationId': 'get_test_dict_with_list',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           }
                       },
                       '/test/dict/with/list/of/different/size': {
                           'get': {
                               'operationId': 'get_test_dict_with_list_of_different_size',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           }
                       }
                   })


@app.route('/test/dict/with/empty/nested/list', methods=['GET'])
def get_test_dict_with_empty_nested_list():
    dict_with_nested_list = {
        "Column 1": "0-0-1",
        "Column 2": [
            {
                "Column 1": "0-0-2 / 1-0-1",
                "Column 2": [],
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
    return jsonify(dict_with_nested_list)


@app.route('/test/dict/with/three/imbricated/levels', methods=['GET'])
def get_test_dict_with_three_imbricated_levels():
    dict_with_imbricated_levels = {
        "Column 1": "0-0-1",
        "Column 2": [
            {
                "Column 1": "0-0-2 / 1-0-1",
                "Column 2": [
                    {
                        "Column 1": "0-0-2 / 1-0-2 / 2-0-1",
                        "Column 2": [],
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


@app.route('/test/dict/with/four/imbricated/levels', methods=['GET'])
def get_test_dict_with_four_imbricated_levels():
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
        "Column 2": "value 1",
        "Column 3": "value 2"
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
            'Column 2': "value 11",
            'Column 3': "value 12"
        },
        {
            'Column 2': "value 21",
            'Column 3': "value 22"
        }
    ])


@app.route('/test/dict/with/list', methods=['GET'])
def get_test_dict_with_list():
    dict_with_list = {
        "Column 1": 23,
        "Column 2": True,
        "Column 3": [
            'this',
            'is',
            'a',
            'test'
        ]
    }
    return jsonify(dict_with_list)


@app.route('/test/dict/with/list/of/different/size', methods=['GET'])
def get_test_dict_with_list_of_different_size():
    dict_with_list = {
        "Column 1": [23],
        "Column 2": [24],
        "Column 3": [
            'value 1',
            'value 2',
            'value 3'
        ]
    }
    return jsonify(dict_with_list)


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8947)

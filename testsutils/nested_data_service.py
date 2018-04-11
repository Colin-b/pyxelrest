from flask import Flask, jsonify, Response
from datetime import datetime


def support_pandas():
    try:
        import pandas
        return True
    except:
        return False


app = Flask(__name__)


@app.route('/')
def open_api_definition():
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
                       '/dict_with_empty_nested_list': {
                           'get': {
                               'operationId': 'get_dict_with_empty_nested_list',
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
                       '/dict_with_three_imbricated_levels': {
                           'get': {
                               'operationId': 'get_dict_with_three_imbricated_levels',
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
                       '/dict_with_four_imbricated_levels': {
                           'get': {
                               'operationId': 'get_dict_with_four_imbricated_levels',
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
                       '/dict_with_multiple_imbricated_levels_and_duplicate_keys': {
                           'get': {
                               'operationId': 'get_dict_with_multiple_imbricated_levels_and_duplicate_keys',
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
                       '/empty_dict': {
                           'get': {
                               'operationId': 'get_empty_dict',
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
                       '/empty_list': {
                           'get': {
                               'operationId': 'get_empty_list',
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
                       '/one_level_dict': {
                           'get': {
                               'operationId': 'get_one_level_dict',
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
                       '/one_level_list': {
                           'get': {
                               'operationId': 'get_one_level_list',
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
                       '/one_dict_entry_with_a_list': {
                           'get': {
                               'operationId': 'get_one_dict_entry_with_a_list',
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
                       '/one_dict_entry_with_a_list_of_dict': {
                           'get': {
                               'operationId': 'get_one_dict_entry_with_a_list_of_dict',
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
                       '/list_of_dict': {
                           'get': {
                               'operationId': 'get_list_of_dict',
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
                       '/dict_with_list': {
                           'get': {
                               'operationId': 'get_dict_with_list',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           }
                       },
                       '/dict_with_list_of_different_size': {
                           'get': {
                               'operationId': 'get_dict_with_list_of_different_size',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           }
                       },
                       '/dict_with_various_columns': {
                           'get': {
                               'operationId': 'get_dict_with_various_columns',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           }
                       },
                       '/pandas_msgpack_default_encoding': {
                           'get': {
                               'operationId': 'get_pandas_msgpack_default_encoding',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           }
                       }
                   })


@app.route('/dict_with_empty_nested_list', methods=['GET'])
def get_dict_with_empty_nested_list():
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


@app.route('/dict_with_three_imbricated_levels', methods=['GET'])
def get_dict_with_three_imbricated_levels():
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


@app.route('/dict_with_four_imbricated_levels', methods=['GET'])
def get_dict_with_four_imbricated_levels():
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


@app.route('/dict_with_multiple_imbricated_levels_and_duplicate_keys', methods=['GET'])
def get_dict_with_multiple_imbricated_levels_and_duplicate_keys():
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


@app.route('/empty_dict', methods=['GET'])
def get_empty_dict():
    return jsonify({})


@app.route('/empty_list', methods=['GET'])
def get_empty_list():
    return jsonify([])


@app.route('/one_level_dict', methods=['GET'])
def get_one_level_dict():
    return jsonify({
        "Column 2": "value 1",
        "Column 3": "value 2"
    })


@app.route('/one_level_list', methods=['GET'])
def get_one_level_list():
    return jsonify([
        "value 1",
        "value 2"
    ])


@app.route('/one_dict_entry_with_a_list', methods=['GET'])
def get_one_dict_entry_with_a_list():
    return jsonify({
        'Column 1': [
            "value 1",
            "value 2"
        ]})


@app.route('/one_dict_entry_with_a_list_of_dict', methods=['GET'])
def get_one_dict_entry_with_a_list_of_dict():
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


@app.route('/list_of_dict', methods=['GET'])
def get_list_of_dict():
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


@app.route('/dict_with_list', methods=['GET'])
def get_dict_with_list():
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


@app.route('/dict_with_list_of_different_size', methods=['GET'])
def get_dict_with_list_of_different_size():
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


@app.route('/dict_with_various_columns', methods=['GET'])
def get_dict_with_various_columns():
    dict_with_list = {
        "Column 1": [
            [
                'value 1',
                'value 2',
                {
                    'column 20': ['value 20'],
                    'column 21': ['value 21-1','value 21-2']
                }
            ],
            [
                'value 3',
                {
                    'column 23': ['value 23']
                }
            ]
        ],
        "Column 2": [
            [
                'value 4',
                {
                    'column 24': ['value 24']
                }
            ]
        ]
    }
    return jsonify(dict_with_list)


def _get_dataframe():
    df = pandas.DataFrame(
        [
            ['data11', 'data12_é&ç', u'data13_é&ç', datetime(2017, 12, 26, 1, 2, 3), 1.1],
            ['data21', 'data22_é&ç', u'data23_é&ç', datetime(2017, 12, 27, 1, 2, 3), 2.2]
        ],
        columns=['col1', 'col2_é&ç', u'col3_é&ç', 'col4', 'col5']
    )
    return df


@app.route('/pandas_msgpack_default_encoding', methods=['GET'])
def get_pandas_msgpack_default_encoding():
    if support_pandas():
        df = _get_dataframe()
        output = df.to_msgpack(compress='zlib')
        return Response(output, mimetype='application/msgpackpandas')
    return 'Pandas not installed'


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8947)

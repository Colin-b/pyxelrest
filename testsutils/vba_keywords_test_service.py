from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   paths={
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


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8949)
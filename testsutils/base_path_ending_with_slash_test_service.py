from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   basePath='//',
                   paths={
                       '/test/method': {
                           'get': {
                               'operationId': 'get_test_method',
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
                                'operationId': 'post_test_method',
                                'responses': {
                                   '200': {
                                       'description': 'POST performed properly'
                                   }
                                }
                           },
                           'put': {
                                'operationId': 'put_test_method',
                                'responses': {
                                   '200': {
                                       'description': 'PUT performed properly'
                                   }
                                }
                           },
                           'delete': {
                                'operationId': 'delete_test_method',
                                'responses': {
                                   '200': {
                                       'description': 'DELETE performed properly'
                                   }
                                }
                           }
                       },
                   })


@app.route('/test/method', methods=['GET'])
def get_test_method():
    return request.url


@app.route('/test/method', methods=['POST'])
def post_test_method():
    return request.url


@app.route('/test/method', methods=['PUT'])
def put_test_method():
    return request.url


@app.route('/test/method', methods=['DELETE'])
def delete_test_method():
    return request.url


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8957)

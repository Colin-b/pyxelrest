from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   paths={
                       '/test/all/http/methods': {
                           'get': {
                               'operationId': 'get_test_all_http_methods',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           },
                           'post': {
                               'operationId': 'post_test_all_http_methods',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           },
                           'put': {
                               'operationId': 'put_test_all_http_methods',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           },
                           'delete': {
                               'operationId': 'delete_test_all_http_methods',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           },
                           'patch': {
                               'operationId': 'patch_test_all_http_methods',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           },
                           'options': {
                               'operationId': 'options_test_all_http_methods',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           },
                           'head': {
                               'operationId': 'head_test_all_http_methods',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           }
                       }
                   })


@app.route('/test/all/http/methods', methods=['GET'])
def get_test_all_http_methods():
    return "GET"


@app.route('/test/all/http/methods', methods=['POST'])
def post_test_all_http_methods():
    return "POST"


@app.route('/test/all/http/methods', methods=['PUT'])
def put_test_all_http_methods():
    return "PUT"


@app.route('/test/all/http/methods', methods=['DELETE'])
def delete_test_all_http_methods():
    return "DELETE"


@app.route('/test/all/http/methods', methods=['PATCH'])
def patch_test_all_http_methods():
    return "PATCH"


@app.route('/test/all/http/methods', methods=['OPTIONS'])
def options_test_all_http_methods():
    return "OPTIONS"


@app.route('/test/all/http/methods', methods=['HEAD'])
def head_test_all_http_methods():
    return "HEAD"


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8955)

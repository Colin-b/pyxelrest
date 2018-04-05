from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def open_api_definition():
    return jsonify(swagger='2.0',
                   paths={
                       '/http_methods': {
                           'get': {
                               'operationId': 'get_http_methods',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           },
                           'post': {
                               'operationId': 'post_http_methods',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           },
                           'put': {
                               'operationId': 'put_http_methods',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           },
                           'delete': {
                               'operationId': 'delete_http_methods',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           },
                           'patch': {
                               'operationId': 'patch_http_methods',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           },
                           'options': {
                               'operationId': 'options_http_methods',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           },
                           'head': {
                               'operationId': 'head_http_methods',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           }
                       }
                   })


@app.route('/http_methods', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
def http_methods():
    return request.method


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8955)

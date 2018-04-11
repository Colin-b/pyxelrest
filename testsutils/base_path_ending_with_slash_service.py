from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def open_api_definition():
    return jsonify(swagger='2.0',
                   basePath='//',
                   paths={
                       '/method': {
                           'get': {
                               'operationId': 'get_method',
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
                                'operationId': 'post_method',
                                'responses': {
                                   '200': {
                                       'description': 'POST performed properly'
                                   }
                                }
                           },
                           'put': {
                                'operationId': 'put_method',
                                'responses': {
                                   '200': {
                                       'description': 'PUT performed properly'
                                   }
                                }
                           },
                           'delete': {
                                'operationId': 'delete_method',
                                'responses': {
                                   '200': {
                                       'description': 'DELETE performed properly'
                                   }
                                }
                           }
                       },
                   })


@app.route('/method', methods=['GET', 'POST', 'PUT', 'DELETE'])
def method_single_slash():
    return request.url


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8957)

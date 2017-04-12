from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   definitions={
                       'Header': {
                           'type': 'object',
                           'properties': {
                               'Accept': {
                                   'type': 'string'
                               },
                               'Accept-Encoding': {
                                   'type': 'string'
                               },
                               'Connection': {
                                   'type': 'string'
                               },
                               'Content-Length': {
                                   'type': 'string'
                               },
                               'Content-Type': {
                                   'type': 'string'
                               },
                               'Header-String': {
                                   'type': 'string'
                               },
                               'Host': {
                                   'type': 'string'
                               },
                               'User-Agent': {
                                   'type': 'string'
                               }
                           },
                           'title': 'Test'
                       }
                   },
                   paths={
                       '/test/header/parameter': {
                           'get': {
                               'operationId': 'get_test_header_parameter',
                               'parameters': [
                                   {
                                       'description': 'header parameter',
                                       'in': 'header',
                                       'name': 'header_string',
                                       'required': True,
                                       'type': 'string'
                                   }
                               ],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/Header'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           }
                       }
                   })


@app.route('/test/header/parameter', methods=['GET'])
def get_test_header_parameter():
    return jsonify(dict(request.headers))


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8951)

from flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   paths={
                       '/test/async': {
                           'get': {
                               'operationId': 'get_test_async',
                               'responses': {
                                   '202': {
                                       'description': 'return value',
                                       'schema': {
                                           'type': 'string'
                                       }
                                   }
                               }
                           },
                       },
                   })


@app.route('/test/async', methods=['GET'])
def get_test_method():
    response = Response()
    response.status_code = 202
    response.headers['location'] = request.base_url + '/status'
    return response


@app.route('/test/async/status', methods=['GET'])
def get_test_status():
    return jsonify({'key': 'value'})


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8958)

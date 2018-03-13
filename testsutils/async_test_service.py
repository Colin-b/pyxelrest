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


skipped_headers = [
    'Accept',
    'Accept-Encoding',
    'Connection',
    'Host',
    'User-Agent',
    'Content-Length',
    'X-Pxl-Request',
    'X-Pxl-Session',
]


@app.route('/test/async/status', methods=['GET'])
def get_test_status():
    headers = dict(request.headers)
    return jsonify({
        header_name: header_value
        for header_name, header_value in headers.items()
        if header_name not in skipped_headers
    })


@app.route('/test/unlisted', methods=['DELETE'])
def delete_test_unlisted():
    headers = dict(request.headers)
    return jsonify({
        header_name: header_value
        for header_name, header_value in headers.items()
        if header_name not in skipped_headers
    })


@app.route('/test/dict', methods=['POST'])
def post_test_dict():
    headers = dict(request.headers)
    return jsonify(request.json)


@app.route('/test/dict', methods=['PUT'])
def put_test_dict():
    headers = dict(request.headers)
    return jsonify(request.json)


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8958)

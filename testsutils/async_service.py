from flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route('/')
def open_api_definition():
    return jsonify(swagger='2.0',
                   paths={
                       '/async': {
                           'get': {
                               'operationId': 'get_async',
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


@app.route('/async', methods=['GET'])
def get_async():
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


@app.route('/async/status', methods=['GET'])
def get_async_status():
    headers = dict(request.headers)
    return jsonify({
        header_name: header_value
        for header_name, header_value in headers.items()
        if header_name not in skipped_headers
    })


@app.route('/unlisted', methods=['DELETE'])
def delete_unlisted():
    headers = dict(request.headers)
    return jsonify({
        header_name: header_value
        for header_name, header_value in headers.items()
        if header_name not in skipped_headers
    })


@app.route('/dict', methods=['POST', 'PUT'])
def dict_body():
    headers = dict(request.headers)
    return jsonify(request.json)


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8958)

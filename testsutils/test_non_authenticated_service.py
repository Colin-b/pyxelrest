from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   paths={
                       '/test/without/auth': {
                           'get': {
                               'operationId': 'get_test_without_auth'
                           }
                       }
                   })


@app.route('/test/without/auth', methods=['GET'])
def get_test_without_auth():
    return jsonify([{'received token': request.headers.get('Bearer') is not None}])


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8948)

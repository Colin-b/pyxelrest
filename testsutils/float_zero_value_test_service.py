from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   paths={
                       '/test/with/float/zero': {
                           'get': {
                               'operationId': 'get_test_with_float_zero'
                           }
                       }
                   })


@app.route('/test/with/float/zero', methods=['GET'])
def get_test_with_tags():
    return jsonify([{'float_zero': 0}])


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8945)

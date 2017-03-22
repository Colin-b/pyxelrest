from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   paths={
                       '/test/with/zero/integer': {
                           'get': {
                               'operationId': 'get_test_with_zero_integer'
                           }
                       },
                       '/test/with/zero/float': {
                           'get': {
                               'operationId': 'get_test_with_zero_float'
                           }
                       },
                       '/test/with/false/boolean': {
                           'get': {
                               'operationId': 'get_test_with_false_boolean'
                           }
                       },
                       '/test/with/empty/string': {
                           'get': {
                               'operationId': 'get_test_with_empty_string'
                           }
                       },
                       '/test/with/empty/list': {
                           'get': {
                               'operationId': 'get_test_with_empty_list'
                           }
                       },
                       '/test/with/empty/dictionary': {
                           'get': {
                               'operationId': 'get_test_with_empty_dictionary'
                           }
                       }
                   })


@app.route('/test/with/zero/integer', methods=['GET'])
def get_test_with_zero_integer():
    return jsonify([{'zero_integer': 0}])


@app.route('/test/with/zero/float', methods=['GET'])
def get_test_with_zero_float():
    return jsonify([{'zero_float': 0.0}])


@app.route('/test/with/false/boolean', methods=['GET'])
def get_test_with_false_boolean():
    return jsonify([{'false_boolean': False}])


@app.route('/test/with/empty/string', methods=['GET'])
def get_test_with_empty_string():
    return jsonify([{'empty_string': ''}])


@app.route('/test/with/empty/list', methods=['GET'])
def get_test_with_empty_list():
    return jsonify([{'empty_list': []}])


@app.route('/test/with/empty/dictionary', methods=['GET'])
def get_test_with_empty_dictionary():
    return jsonify([{'empty_dictionary': {}}])


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8945)

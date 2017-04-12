from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   definitions={
                       'TestObject': {
                           'type': 'object',
                           'properties': {
                               'test': {
                                   'type': 'string',
                                   'description': 'test',
                               }
                           },
                           'title': 'Test'
                       }
                   },
                   paths={
                       '/test/with/tags': {
                           'get': {
                               'operationId': 'get_test_with_tags',
                               'tags': ['tag 0', 'tag 1'],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/TestObject'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           },
                           'post': {
                               'operationId': 'post_test_with_tags',
                               'tags': ['tag 1', 'tag 2'],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/TestObject'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           },
                           'put': {
                               'operationId': 'put_test_with_tags',
                               'tags': ['tag 2', 'tag 3'],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/TestObject'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           },
                           'delete': {
                               'operationId': 'delete_test_with_tags',
                               'tags': ['tag 3', 'tag 4'],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/TestObject'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           }
                       }
                   })


@app.route('/test/with/tags', methods=['GET'])
def get_test_with_tags():
    return 'Second tag is one of the accepted tags'


@app.route('/test/with/tags', methods=['POST'])
def post_test_with_tags():
    return 'All tags are accepted'


@app.route('/test/with/tags', methods=['PUT'])
def put_test_with_tags():
    return 'First tag is one of the accepted tags'


@app.route('/test/with/tags', methods=['DELETE'])
def delete_test_with_tags():
    return 'This method should not be available'


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8944)

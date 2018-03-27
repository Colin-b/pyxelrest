from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/swagger_version_not_provided')
def swagger_version_not_provided():
    return jsonify(paths={
        '/should_not_be_available': {
            'get': {
                'operationId': 'get_should_not_be_available',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
            }
        },
    })


@app.route('/swagger_version_not_supported')
def swagger_version_not_supported():
    return jsonify(swagger='1.0',
                   paths={
                       '/should_not_be_available': {
                           'get': {
                               'operationId': 'get_should_not_be_available',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           }
                       },
                   })


@app.route('/operation_id_not_provided')
def operation_id_not_provided():
    return jsonify(swagger='2.0',
                   paths={
                       '/without_operationId': {
                           'get': {
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           }
                       },
                   })


@app.route('/operation_id_not_always_provided')
def operation_id_not_always_provided():
    return jsonify(swagger='2.0',
                   paths={
                       '/without_operationId': {
                           'get': {
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           }
                       },
                       '/with_operationId': {
                           'get': {
                               # This is obviously misleading but it can happen...
                               'operationId': 'get_without_operationId',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               }
                           }
                       },
                   })


@app.route('/without_operationId')
def get_without_operation_id():
    return '/without_operationId called.'


@app.route('/with_operationId')
def get_with_operation_id():
    return '/with_operationId called.'


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8948)

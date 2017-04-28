from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   paths={
                       '/test/authentication/success': {
                           'get': {
                               'operationId': 'get_test_authentication_success',
                               'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                               },
                               'security': [
                                   {
                                       'auth_success': [
                                           'custom_label'
                                       ]
                                   }
                               ]
                           }
                       },
                       '/test/authentication/failure': {
                           'get': {
                               'operationId': 'get_test_authentication_failure',
                               'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                               },
                               'security': [
                                   {
                                       'auth_failure': [
                                           'custom_label'
                                       ]
                                   }
                               ]
                           }
                       },
                       '/test/authentication/timeout': {
                           'get': {
                               'operationId': 'get_test_authentication_timeout',
                               'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                               },
                               'security': [
                                   {
                                       'auth_timeout': [
                                           'custom_label'
                                       ]
                                   }
                               ]
                           }
                       }
                   },
                   securityDefinitions={
                       'auth_success': {
                           "type": "oauth2",
                           "authorizationUrl": 'http://localhost:8947/auth_success?response_type=id_token',
                           "flow": "implicit",
                           "scopes": {
                               "custom_label": "custom category"
                           }
                       },
                       'auth_failure': {
                           "type": "oauth2",
                           "authorizationUrl": 'http://localhost:8947/auth_failure?response_type=id_token',
                           "flow": "implicit",
                           "scopes": {
                               "custom_label": "custom category"
                           }
                       },
                       'auth_timeout': {
                           "type": "oauth2",
                           # Server should not exists to simulate a timeout
                           "authorizationUrl": 'http://localhost:8949/auth_timeout?response_type=id_token',
                           "flow": "implicit",
                           "scopes": {
                               "custom_label": "custom category"
                           }
                       }
                   })


@app.route('/test/authentication/success', methods=['GET'])
def get_test_authentication_success():
    return jsonify([{'received token': request.headers.get('Bearer') is not None}])


@app.route('/test/authentication/failure', methods=['GET'])
def get_test_authentication_failure():
    return 'You should never receive this message as authentication should fail.'


@app.route('/test/authentication/timeout', methods=['GET'])
def get_test_authentication_timeout():
    return 'You should never receive this message as authentication should timeout.'


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8946)

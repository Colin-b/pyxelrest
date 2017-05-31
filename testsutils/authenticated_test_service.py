from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   paths={
                       '/test/oauth2/authentication/success': {
                           'get': {
                               'operationId': 'get_test_oauth2_authentication_success',
                               'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                               },
                               'security': [
                                   {
                                       'oauth2_auth_success': [
                                           'custom_label'
                                       ]
                                   }
                               ]
                           }
                       },
                       '/test/oauth2/authentication/failure': {
                           'get': {
                               'operationId': 'get_test_oauth2_authentication_failure',
                               'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                               },
                               'security': [
                                   {
                                       'oauth2_auth_failure': [
                                           'custom_label'
                                       ]
                                   }
                               ]
                           }
                       },
                       '/test/oauth2/authentication/timeout': {
                           'get': {
                               'operationId': 'get_test_oauth2_authentication_timeout',
                               'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                               },
                               'security': [
                                   {
                                       'oauth2_auth_timeout': [
                                           'custom_label'
                                       ]
                                   }
                               ]
                           }
                       },
                       '/test/oauth2/authentication/success/quick/expiry': {
                           'get': {
                               'operationId': 'get_test_oauth2_authentication_success_quick_expiry',
                               'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                               },
                               'security': [
                                   {
                                       'oauth2_auth_success_quick_expiry': [
                                           'custom_label'
                                       ]
                                   }
                               ]
                           }
                       }
                   },
                   securityDefinitions={
                       'oauth2_auth_success': {
                           "type": "oauth2",
                           "authorizationUrl": 'http://localhost:8947/auth_success?response_type=id_token',
                           "flow": "implicit",
                           "scopes": {
                               "custom_label": "custom category"
                           }
                       },
                       'oauth2_auth_failure': {
                           "type": "oauth2",
                           "authorizationUrl": 'http://localhost:8947/auth_failure?response_type=id_token',
                           "flow": "implicit",
                           "scopes": {
                               "custom_label": "custom category"
                           }
                       },
                       'oauth2_auth_timeout': {
                           "type": "oauth2",
                           # Server should not exists to simulate a timeout
                           "authorizationUrl": 'http://localhost:8949/auth_timeout?response_type=id_token',
                           "flow": "implicit",
                           "scopes": {
                               "custom_label": "custom category"
                           }
                       },
                       'oauth2_auth_success_quick_expiry': {
                           "type": "oauth2",
                           "authorizationUrl": 'http://localhost:8947/auth_success_quick_expiry?response_type=id_token',
                           "flow": "implicit",
                           "scopes": {
                               "custom_label": "custom category"
                           }
                       }
                   })


@app.route('/test/oauth2/authentication/success', methods=['GET'])
def get_test_oauth2_authentication_success():
    return jsonify([{'Bearer': request.headers.get('Bearer')}])


@app.route('/test/oauth2/authentication/failure', methods=['GET'])
def get_test_oauth2_authentication_failure():
    return 'You should never receive this message as authentication should fail.'


@app.route('/test/oauth2/authentication/timeout', methods=['GET'])
def get_test_oauth2_authentication_timeout():
    return 'You should never receive this message as authentication should timeout.'


@app.route('/test/oauth2/authentication/success/quick/expiry', methods=['GET'])
def get_test_oauth2_authentication_success_quick_expiry():
    return jsonify([{
        'Bearer': request.headers.get('Bearer')
    }])


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8946)

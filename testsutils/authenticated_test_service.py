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
                       '/test/oauth2/authentication/success/with/custom/response/type': {
                           'get': {
                               'operationId': 'get_test_oauth2_authentication_success_with_custom_response_type',
                               'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                               },
                               'security': [
                                   {
                                       'oauth2_auth_success_with_custom_response_type': [
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
                       },
                       '/test/api/key/header/authentication/success': {
                           'get': {
                               'operationId': 'get_test_api_key_header_authentication_success',
                               'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                               },
                               'security': [
                                   {
                                       'api_key_header_auth_success': [
                                       ]
                                   }
                               ]
                           }
                       },
                       '/test/api/key/query/authentication/success': {
                           'get': {
                               'operationId': 'get_test_api_key_query_authentication_success',
                               'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                               },
                               'security': [
                                   {
                                       'api_key_query_auth_success': [
                                       ]
                                   }
                               ]
                           }
                       },
                       '/test/basic/authentication/success': {
                           'get': {
                               'operationId': 'get_test_basic_authentication_success',
                               'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                               },
                               'security': [
                                   {
                                       'basic_auth_success': [
                                       ]
                                   }
                               ]
                           }
                       },
                       '/test/basic/and/api/key/authentication/success': {
                           'get': {
                               'operationId': 'get_test_basic_and_api_key_authentication_success',
                               'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                               },
                               'security': [
                                   {
                                       'basic_auth_success': [
                                       ],
                                       'api_key_header_auth_success': [
                                       ]
                                   }
                               ]
                           }
                       },
                       '/test/basic/or/api/key/authentication/success': {
                           'get': {
                               'operationId': 'get_test_basic_or_api_key_authentication_success',
                               'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                               },
                               'security': [
                                   {
                                       'basic_auth_success': [
                                       ]
                                   },
                                   {
                                       'api_key_header_auth_success': [
                                       ]
                                   }
                               ]
                           }
                       },
                       '/test/api/key/or/basic/authentication/success': {
                           'get': {
                               'operationId': 'get_test_api_key_or_basic_authentication_success',
                               'responses': {
                                   '200': {
                                       'description': 'return value'
                                   }
                               },
                               'security': [
                                   {
                                       'api_key_header_auth_success': [
                                       ]
                                   },
                                   {
                                       'basic_auth_success': [
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
                       'auth_success_with_custom_response_type': {
                           "type": "oauth2",
                           "authorizationUrl": 'http://localhost:8947/auth_success?response_type=my_custom_token',
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
                           "authorizationUrl": 'http://localhost:8947/auth_timeout?response_type=id_token',
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
                       },
                       'api_key_header_auth_success': {
                           "type": "apiKey",
                           "in": "header",
                           "name": "X-API-HEADER-KEY"
                       },
                       'api_key_query_auth_success': {
                           "type": "apiKey",
                           "in": "query",
                           "name": "X-API-QUERY-KEY"
                       },
                       'basic_auth_success': {
                           "type": "basic"
                       }
                   })


@app.route('/test/oauth2/authentication/success', methods=['GET'])
def get_test_oauth2_authentication_success():
    return jsonify([{'Bearer': request.headers.get('Bearer')}])


@app.route('/test/oauth2/authentication/success/with/custom/response/type', methods=['GET'])
def get_test_oauth2_authentication_success_with_custom_response_type():
    return jsonify([{'Bearer': request.headers.get('Bearer')}])


@app.route('/test/oauth2/authentication/failure', methods=['GET'])
def get_test_oauth2_authentication_failure():
    return 'You should never receive this message as authentication should fail.'


@app.route('/test/oauth2/authentication/timeout', methods=['GET'])
def get_test_oauth2_authentication_timeout():
    return 'You should never receive this message as authentication should timeout.'


@app.route('/test/oauth2/authentication/success/quick/expiry', methods=['GET'])
def get_test_oauth2_authentication_success_quick_expiry():
    return jsonify([{'Bearer': request.headers.get('Bearer')}])


@app.route('/test/api/key/header/authentication/success', methods=['GET'])
def get_test_api_key_header_authentication_success():
    return jsonify([{'X-API-HEADER-KEY': request.headers.get('X-API-HEADER-KEY')}])


@app.route('/test/api/key/query/authentication/success', methods=['GET'])
def get_test_api_key_query_authentication_success():
    return jsonify([{'X-API-QUERY-KEY': request.args.get('X-API-QUERY-KEY')}])


@app.route('/test/basic/authentication/success', methods=['GET'])
def get_test_basic_authentication_success():
    return jsonify([{'Authorization': request.headers.get('Authorization')}])


@app.route('/test/basic/and/api/key/authentication/success', methods=['GET'])
def get_test_basic_and_api_key_authentication_success():
    return jsonify([
        {
            'Authorization': request.headers.get('Authorization'),
            'X-API-HEADER-KEY': request.headers.get('X-API-HEADER-KEY')
        }
    ])


@app.route('/test/basic/or/api/key/authentication/success', methods=['GET'])
def get_test_basic_or_api_key_authentication_success():
    return jsonify([
        {
            'Authorization': request.headers.get('Authorization'),
            'X-API-HEADER-KEY': request.headers.get('X-API-HEADER-KEY')
        }
    ])


@app.route('/test/api/key/or/basic/authentication/success', methods=['GET'])
def get_test_api_key_or_basic_authentication_success():
    return jsonify([
        {
            'Authorization': request.headers.get('Authorization'),
            'X-API-HEADER-KEY': request.headers.get('X-API-HEADER-KEY')
        }
    ])


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8946)

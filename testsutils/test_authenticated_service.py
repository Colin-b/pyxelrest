from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   paths={
                       '/test/with/auth': {
                           'get': {
                               'operationId': 'get_test_with_auth',
                               'security': [
                                   {
                                       'custom_auth': [
                                           'custom_label'
                                       ]
                                   }
                               ]
                           }
                       }
                   },
                   securityDefinitions={
                       'custom_auth': {
                           "type": "oauth2",
                           "authorizationUrl": 'http://localhost:8947/auth?response_type=id_token',
                           "flow": "implicit",
                           "scopes": {
                               "custom_label": "custom category"
                           }
                       }
                   })


@app.route('/test/with/auth', methods=['GET'])
def get_test_with_auth():
    return jsonify([{'received token': request.headers.get('Bearer') is not None}])


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8946)

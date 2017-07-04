from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   paths={
                       '/test/msgpackpandas': {
                           'get': {
                               'operationId': 'get_test_msgpackpandas',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               },
                               'produces': [
                                   'application/msgpackpandas'
                               ]
                           }
                       },
                       '/test/json': {
                           'get': {
                               'operationId': 'get_test_json',
                               'responses': {
                                   200: {
                                       'description': 'successful operation'
                                   }
                               },
                               'produces': [
                                   'application/json'
                               ]
                           }
                       }
                   })


@app.route('/test/msgpackpandas', methods=['GET'])
def get_test_msgpackpandas():
    return request.headers.get('Accept')


@app.route('/test/json', methods=['GET'])
def get_test_json():
    return request.headers.get('Accept')


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8956)

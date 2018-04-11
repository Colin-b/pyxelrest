from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def open_api_definition():
    return jsonify(swagger='2.0',
                   paths={
                       '/msgpackpandas': {
                           'get': {
                               'operationId': 'get_msgpackpandas',
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
                       '/json': {
                           'get': {
                               'operationId': 'get_json',
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


@app.route('/msgpackpandas', methods=['GET'])
def get_msgpackpandas():
    return request.headers.get('Accept')


@app.route('/json', methods=['GET'])
def get_json():
    return request.headers.get('Accept')


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8956)

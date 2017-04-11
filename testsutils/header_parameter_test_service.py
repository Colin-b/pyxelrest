from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   paths={
                       '/test/header/parameter': {
                            'get': {
                                'operationId': 'get_test_header_parameter',
                                'parameters': [
                                    {
                                        'description': 'header parameter',
                                        'in': 'header',
                                        'name': 'header_string',
                                        'required': True,
                                        'type': 'string'
                                    }
                                ]
                            }
                       }
                   })


@app.route('/test/header/parameter', methods=['GET'])
def get_test_header_parameter():
    return jsonify(dict(request.headers))


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8951)

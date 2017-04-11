from flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   paths={
                       '/test/form/parameter': {
                            'post': {
                                'operationId': 'post_test_form_parameter',
                                'parameters': [
                                    {
                                        'description': 'form parameter',
                                        'in': 'formData',
                                        'name': 'form_string',
                                        'required': True,
                                        'type': 'string'
                                    }
                                ]
                            }
                       }
                   })


@app.route('/test/form/parameter', methods=['POST'])
def post_test_form_parameter():
    return Response(request.data, mimetype='application/json')


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8952)

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   paths={
                       '/test/string/array/parameter': {
                            'get': {
                                'operationId': 'get_test_string_array_parameter',
                                'parameters': [
                                    {
                                        'description': 'string array parameter',
                                        'in': 'query',
                                        'name': 'query_array_string',
                                        'required': True,
                                        'items': {
                                            'type': 'string'
                                        },
                                        'type': 'array'
                                    }
                                ]
                            }
                       }
                   })


@app.route('/test/string/array/parameter', methods=['GET'])
def get_test_string_array_parameter():
    return ', '.join(_request_args(request.args))


def _request_args(args):
    return ['{0}="{1}"'.format(arg, args.getlist(arg)) for arg in args]


def start_server(port):
    app.run(port=port)

if __name__ == '__main__':
    start_server(8953)

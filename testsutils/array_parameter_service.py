from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def open_api_definition():
    return jsonify(swagger='2.0',
                   definitions={
                       'TestObject': {
                           'type': 'object',
                           'properties': {
                               'test': {
                                   'type': 'string',
                                   'description': 'test',
                               }
                           },
                           'title': 'Test'
                       }
                   },
                   paths={
                       '/string_array_parameter': {
                           'get': {
                               'operationId': 'get_string_array_parameter',
                               'parameters': [
                                   {
                                       'description': 'string array parameter',
                                       'in': 'query',
                                       'name': 'string_array',
                                       'required': True,
                                       'items': {
                                           'type': 'string'
                                       },
                                       'type': 'array'
                                   }
                               ],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/TestObject'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           }
                       }
                   })


@app.route('/string_array_parameter', methods=['GET'])
def string_array_parameter():
    return ', '.join(_request_args(request.args))


def _request_args(args):
    return ['{0}="{1}"'.format(arg, args.getlist(arg)) for arg in args]


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8953)

from flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   definitions={
                       'Form': {
                           'type': 'object',
                           'properties': {
                               'form_string': {
                                   'type': 'string'
                               }
                           },
                           'title': 'Test'
                       }
                   },
                   paths={
                       '/form': {
                           'post': {
                               'operationId': 'post_form',
                               'parameters': [
                                   {
                                       'description': 'form parameter',
                                       'in': 'formData',
                                       'name': 'form_string',
                                       'required': True,
                                       'type': 'string'
                                   }
                               ],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           '$ref': '#/definitions/Form'
                                       }
                                   }
                               }
                           }
                       }
                   })


@app.route('/form', methods=['POST'])
def post_form():
    return Response(request.data, mimetype='application/json')


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8952)

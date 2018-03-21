from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   paths={
                       '/test/files': {
                           'post': {
                               'operationId': 'post_test_files',
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                   }
                               },
                               'parameters': [
                                   {
                                       'name': "mandatory_file",
                                       'required': True,
                                       'in': "formData",
                                       'type':'file',
                                   },
                                   {
                                       'name': "optional_file",
                                       'required': False,
                                       'in': "formData",
                                       'type':'file',
                                   },
                               ],
                           },
                       },
                   },
                   consumes=[
                       "application/x-www-form-urlencoded",
                       "multipart/form-data",
                   ])


@app.route('/test/files', methods=['POST'])
def post_test_files():
    return jsonify({
        file_name: file.read().decode('utf8')
        for file_name, file in request.files.items()
    })


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8959)

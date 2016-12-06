from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(paths={
        '/test/string': {
            'get': {
                'operationId': 'get_test_string'
            }
        }
    })

app.run(port=8943)

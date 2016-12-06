from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(paths={
        '/test/without/parameter': {
            'get': {
                'operationId': 'get_test_without_parameter'
            },
            'post': {
                'operationId': 'post_test_without_parameter'
            },
            'put': {
                'operationId': 'put_test_without_parameter'
            },
            'delete': {
                'operationId': 'delete_test_without_parameter'
            }
        },
        '/test/plain/text/without/parameter': {
            'get': {
                'operationId': 'get_test_plain_text_without_parameter',
                'produces': [
                    'text/plain'
                ]
            },
            'post': {
                'operationId': 'post_test_plain_text_without_parameter',
                'produces': [
                    'text/plain'
                ]
            },
            'put': {
                'operationId': 'put_test_plain_text_without_parameter',
                'produces': [
                    'text/plain'
                ]
            },
            'delete': {
                'operationId': 'delete_test_plain_text_without_parameter',
                'produces': [
                    'text/plain'
                ]
            }
        },
        '/test/json/without/parameter': {
            'get': {
                'operationId': 'get_test_json_without_parameter',
                'produces': [
                    'application/json'
                ]
            },
            'post': {
                'operationId': 'post_test_json_without_parameter',
                'produces': [
                    'application/json'
                ]
            },
            'put': {
                'operationId': 'put_test_json_without_parameter',
                'produces': [
                    'application/json'
                ]
            },
            'delete': {
                'operationId': 'delete_test_json_without_parameter',
                'produces': [
                    'application/json'
                ]
            }
        },
        '/test/octet/without/parameter': {
            'get': {
                'operationId': 'get_test_octet_without_parameter',
                'produces': [
                    'application/octet-stream'
                ]
            },
            'post': {
                'operationId': 'post_test_octet_without_parameter',
                'produces': [
                    'application/octet-stream'
                ]
            },
            'put': {
                'operationId': 'put_test_octet_without_parameter',
                'produces': [
                    'application/octet-stream'
                ]
            },
            'delete': {
                'operationId': 'delete_test_octet_without_parameter',
                'produces': [
                    'application/octet-stream'
                ]
            }
        }
    })

app.run(port=8943)

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def open_api_definition():
    return jsonify(swagger='2.0',
                   produces=[
                       "application/json"
                   ],
                   paths={
                       '/cached': {
                           'parameters': [
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'test1',
                                   'required': True,
                                   'type': 'string'
                               },
                               {
                                   'description': '',
                                   'in': 'query',
                                   'name': 'test2',
                                   'required': True,
                                   'type': 'string'
                               },
                           ],
                           'get': {
                               'operationId': 'get_cached',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                   }
                               }
                           },
                           'post': {
                               'operationId': 'post_cached',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                   }
                               },
                           },
                           'put': {
                               'operationId': 'put_cached',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                   }
                                },
                           },
                           'delete': {
                               'operationId': 'delete_cached',
                               'responses': {
                                   '200': {
                                       'description': 'return value',
                                   }
                               },
                           }
                       },
                   })


request_nb = {
    'GET': 0,
    'POST': 0,
    'PUT': 0,
    'DELETE': 0,
}


@app.route('/cached', methods=['GET', 'POST', 'PUT', 'DELETE'])
def cached():
    global request_nb
    request_nb[request.method] += 1
    args = {
        name: value[0]
        for name, value in request.args.items()
    }
    args['request_nb'] = request_nb[request.method]
    return jsonify(args)


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8949)

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def swagger():
    return jsonify(swagger='2.0',
                   definition={
                       'Price': {
                           'required': [
                               'curve',
                               'date',
                               'mat',
                               'ts'
                           ],
                           'type': 'object',
                           'properties': {
                               'ts': {
                                   'type': 'string',
                                   'description': 'timeslot',
                                   'maxLength': 2
                               },
                               'date': {
                                   'type': 'string',
                                   'description': 'date',
                                   'format': 'date'
                               },
                               'curve': {
                                   'type': 'string',
                                   'description': 'curvename',
                                   'maxLength': 20
                               },
                               'mat': {
                                   'type': 'string',
                                   'description': 'maturity',
                                   'maxLength': 4
                               }
                           },
                           'title': 'RealizedPrice'
                       }
                   },
                   paths={
                       '/price/unordered': {
                           'get': {
                               'operationId': 'get_test_price_unordered',
                               'description': 'Price',
                               'parameters': [
                                   {
                                       'in': 'query',
                                       'description': 'date',
                                       'format': 'date',
                                       'required': False,
                                       'type': 'string',
                                       'name': 'date'
                                   },
                                   {
                                       'name': 'curve',
                                       'in': 'query',
                                       'required': False,
                                       'type': 'string',
                                       'description': 'curvename'
                                   },
                                   {
                                       'name': 'ts',
                                       'in': 'query',
                                       'required': False,
                                       'type': 'string',
                                       'description': 'timeslot'
                                   },
                                   {
                                       'name': 'mat',
                                       'in': 'query',
                                       'required': False,
                                       'type': 'string',
                                       'description': 'maturity'
                                   }
                               ],
                               'responses': {
                                   200: {
                                       'description': 'successful operation',
                                       'schema': {
                                           'items': {
                                               '$ref': '#/definitions/Price'
                                           },
                                           'type': 'array'
                                       }
                                   }
                               }
                           }
                       }
                   })


@app.route('/price/unordered', methods=['GET'])
def get_test_price_unordered():
    return jsonify([
        {
            'ts': None,
            'curve': 'PW_FR',
            'date': '2017-04-05',
            'mat': 'H01'
        },
        {
            'ts': None,
            'curve': 'PW_FR',
            'date': '2017-04-05',
            'mat': 'H02'
        }
    ])


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8946)

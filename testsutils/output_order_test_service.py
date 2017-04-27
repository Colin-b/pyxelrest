from collections import OrderedDict
from flask import Flask, Response, jsonify
import json

app = Flask(__name__)


@app.route('/')
def swagger():
    swagger_json = """{
    "swagger": "2.0",
    "definitions": {
        "Price": {
            "required": [
                "curve",
                "date",
                "mat",
                "ts"
            ],
            "type": "object",
            "properties": {
                "ts": {
                    "type": "string",
                    "description": "timeslot",
                    "maxLength": 2
                },
                "date": {
                    "type": "string",
                    "description": "date",
                    "format": "date"
                },
                "curve": {
                    "type": "string",
                    "description": "curvename",
                    "maxLength": 20
                },
                "mat": {
                    "type": "string",
                    "description": "maturity",
                    "maxLength": 4
                }
            },
            "title": "RealizedPrice"
        }
    },
    "paths": {
        "/price/unordered": {
            "get": {
                "operationId": "get_test_price_unordered",
                "description": "Price",
                "parameters": [
                    {
                        "in": "query",
                        "description": "date",
                        "format": "date",
                        "required": false,
                        "type": "string",
                        "name": "date"
                    },
                    {
                        "name": "curve",
                        "in": "query",
                        "required": false,
                        "type": "string",
                        "description": "curvename"
                    },
                    {
                        "name": "ts",
                        "in": "query",
                        "required": false,
                        "type": "string",
                        "description": "timeslot"
                    },
                    {
                        "name": "mat",
                        "in": "query",
                        "required": false,
                        "type": "string",
                        "description": "maturity"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "successful operation",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/Price"
                            },
                            "type": "array"
                        }
                    }
                }
            }
        }
    }
}"""
    return Response(swagger_json, content_type='application/json')


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
            'ts': '2017-04-05 12:03:15',
            'curve': 'PW_FR',
            'date': '2017-04-05',
            'mat': 'H02'
        },
        {
            'ts': None,
            'curve': 'PW_FR',
            'date': '2017-04-05',
            'mat': 'H03'
        }
    ])


def start_server(port):
    app.run(port=port)


if __name__ == '__main__':
    start_server(8946)

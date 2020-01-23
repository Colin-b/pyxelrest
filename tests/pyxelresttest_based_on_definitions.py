import datetime

from dateutil.tz import tzutc
import pytest
from responses import RequestsMock

from testsutils import serviceshandler, loader


@pytest.fixture
def services(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://localhost:8943/",
        json={
            "swagger": "2.0",
            "paths": {
                "/with/all/parameters/types": {
                    "get": {
                        "operationId": "get_with_all_parameters_types",
                        "parameters": [
                            {
                                "description": "integer parameter",
                                "in": "query",
                                "name": "query_integer",
                                "required": True,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 parameter",
                                "in": "query",
                                "name": "query_integer32",
                                "required": True,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 parameter",
                                "in": "query",
                                "name": "query_integer64",
                                "required": True,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number parameter",
                                "in": "query",
                                "name": "query_number",
                                "required": True,
                                "type": "number",
                            },
                            {
                                "description": "number float parameter",
                                "in": "query",
                                "name": "query_float",
                                "required": True,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double parameter",
                                "in": "query",
                                "name": "query_double",
                                "required": True,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string parameter",
                                "in": "query",
                                "name": "query_string",
                                "required": True,
                                "type": "string",
                            },
                            {
                                "description": "string byte parameter",
                                "in": "query",
                                "name": "query_string_byte",
                                "required": True,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary parameter",
                                "in": "query",
                                "name": "query_string_binary",
                                "required": True,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean parameter",
                                "in": "query",
                                "name": "query_boolean",
                                "required": True,
                                "type": "boolean",
                            },
                            {
                                "description": "date parameter",
                                "in": "query",
                                "name": "query_date",
                                "required": True,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time parameter",
                                "in": "query",
                                "name": "query_date_time",
                                "required": True,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password parameter",
                                "in": "query",
                                "name": "query_password",
                                "required": True,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array parameter",
                                "in": "query",
                                "name": "query_array_integer",
                                "required": True,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array parameter",
                                "in": "query",
                                "name": "query_array_integer32",
                                "required": True,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array parameter",
                                "in": "query",
                                "name": "query_array_integer64",
                                "required": True,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array parameter",
                                "in": "query",
                                "name": "query_array_number",
                                "required": True,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array parameter",
                                "in": "query",
                                "name": "query_array_float",
                                "required": True,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array parameter",
                                "in": "query",
                                "name": "query_array_double",
                                "required": True,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "query_array_string",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array parameter",
                                "in": "query",
                                "name": "query_array_string_byte",
                                "required": True,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array parameter",
                                "in": "query",
                                "name": "query_array_string_binary",
                                "required": True,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array parameter",
                                "in": "query",
                                "name": "query_array_boolean",
                                "required": True,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array parameter",
                                "in": "query",
                                "name": "query_array_date",
                                "required": True,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array parameter",
                                "in": "query",
                                "name": "query_array_date_time",
                                "required": True,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array parameter",
                                "in": "query",
                                "name": "query_array_password",
                                "required": True,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
                        ],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "post": {
                        "operationId": "post_with_all_parameters_types",
                        "parameters": [
                            {
                                "description": "integer parameter",
                                "in": "query",
                                "name": "query_integer",
                                "required": True,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 parameter",
                                "in": "query",
                                "name": "query_integer32",
                                "required": True,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 parameter",
                                "in": "query",
                                "name": "query_integer64",
                                "required": True,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number parameter",
                                "in": "query",
                                "name": "query_number",
                                "required": True,
                                "type": "number",
                            },
                            {
                                "description": "number float parameter",
                                "in": "query",
                                "name": "query_float",
                                "required": True,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double parameter",
                                "in": "query",
                                "name": "query_double",
                                "required": True,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string parameter",
                                "in": "query",
                                "name": "query_string",
                                "required": True,
                                "type": "string",
                            },
                            {
                                "description": "string byte parameter",
                                "in": "query",
                                "name": "query_string_byte",
                                "required": True,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary parameter",
                                "in": "query",
                                "name": "query_string_binary",
                                "required": True,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean parameter",
                                "in": "query",
                                "name": "query_boolean",
                                "required": True,
                                "type": "boolean",
                            },
                            {
                                "description": "date parameter",
                                "in": "query",
                                "name": "query_date",
                                "required": True,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time parameter",
                                "in": "query",
                                "name": "query_date_time",
                                "required": True,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password parameter",
                                "in": "query",
                                "name": "query_password",
                                "required": True,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array parameter",
                                "in": "query",
                                "name": "query_array_integer",
                                "required": True,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array parameter",
                                "in": "query",
                                "name": "query_array_integer32",
                                "required": True,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array parameter",
                                "in": "query",
                                "name": "query_array_integer64",
                                "required": True,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array parameter",
                                "in": "query",
                                "name": "query_array_number",
                                "required": True,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array parameter",
                                "in": "query",
                                "name": "query_array_float",
                                "required": True,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array parameter",
                                "in": "query",
                                "name": "query_array_double",
                                "required": True,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "query_array_string",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array parameter",
                                "in": "query",
                                "name": "query_array_string_byte",
                                "required": True,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array parameter",
                                "in": "query",
                                "name": "query_array_string_binary",
                                "required": True,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array parameter",
                                "in": "query",
                                "name": "query_array_boolean",
                                "required": True,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array parameter",
                                "in": "query",
                                "name": "query_array_date",
                                "required": True,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array parameter",
                                "in": "query",
                                "name": "query_array_date_time",
                                "required": True,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array parameter",
                                "in": "query",
                                "name": "query_array_password",
                                "required": True,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
                        ],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "put": {
                        "operationId": "put_with_all_parameters_types",
                        "parameters": [
                            {
                                "description": "integer parameter",
                                "in": "query",
                                "name": "query_integer",
                                "required": True,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 parameter",
                                "in": "query",
                                "name": "query_integer32",
                                "required": True,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 parameter",
                                "in": "query",
                                "name": "query_integer64",
                                "required": True,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number parameter",
                                "in": "query",
                                "name": "query_number",
                                "required": True,
                                "type": "number",
                            },
                            {
                                "description": "number float parameter",
                                "in": "query",
                                "name": "query_float",
                                "required": True,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double parameter",
                                "in": "query",
                                "name": "query_double",
                                "required": True,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string parameter",
                                "in": "query",
                                "name": "query_string",
                                "required": True,
                                "type": "string",
                            },
                            {
                                "description": "string byte parameter",
                                "in": "query",
                                "name": "query_string_byte",
                                "required": True,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary parameter",
                                "in": "query",
                                "name": "query_string_binary",
                                "required": True,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean parameter",
                                "in": "query",
                                "name": "query_boolean",
                                "required": True,
                                "type": "boolean",
                            },
                            {
                                "description": "date parameter",
                                "in": "query",
                                "name": "query_date",
                                "required": True,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time parameter",
                                "in": "query",
                                "name": "query_date_time",
                                "required": True,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password parameter",
                                "in": "query",
                                "name": "query_password",
                                "required": True,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array parameter",
                                "in": "query",
                                "name": "query_array_integer",
                                "required": True,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array parameter",
                                "in": "query",
                                "name": "query_array_integer32",
                                "required": True,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array parameter",
                                "in": "query",
                                "name": "query_array_integer64",
                                "required": True,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array parameter",
                                "in": "query",
                                "name": "query_array_number",
                                "required": True,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array parameter",
                                "in": "query",
                                "name": "query_array_float",
                                "required": True,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array parameter",
                                "in": "query",
                                "name": "query_array_double",
                                "required": True,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "query_array_string",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array parameter",
                                "in": "query",
                                "name": "query_array_string_byte",
                                "required": True,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array parameter",
                                "in": "query",
                                "name": "query_array_string_binary",
                                "required": True,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array parameter",
                                "in": "query",
                                "name": "query_array_boolean",
                                "required": True,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array parameter",
                                "in": "query",
                                "name": "query_array_date",
                                "required": True,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array parameter",
                                "in": "query",
                                "name": "query_array_date_time",
                                "required": True,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array parameter",
                                "in": "query",
                                "name": "query_array_password",
                                "required": True,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
                        ],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "delete": {
                        "operationId": "delete_with_all_parameters_types",
                        "parameters": [
                            {
                                "description": "integer parameter",
                                "in": "query",
                                "name": "query_integer",
                                "required": True,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 parameter",
                                "in": "query",
                                "name": "query_integer32",
                                "required": True,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 parameter",
                                "in": "query",
                                "name": "query_integer64",
                                "required": True,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number parameter",
                                "in": "query",
                                "name": "query_number",
                                "required": True,
                                "type": "number",
                            },
                            {
                                "description": "number float parameter",
                                "in": "query",
                                "name": "query_float",
                                "required": True,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double parameter",
                                "in": "query",
                                "name": "query_double",
                                "required": True,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string parameter",
                                "in": "query",
                                "name": "query_string",
                                "required": True,
                                "type": "string",
                            },
                            {
                                "description": "string byte parameter",
                                "in": "query",
                                "name": "query_string_byte",
                                "required": True,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary parameter",
                                "in": "query",
                                "name": "query_string_binary",
                                "required": True,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean parameter",
                                "in": "query",
                                "name": "query_boolean",
                                "required": True,
                                "type": "boolean",
                            },
                            {
                                "description": "date parameter",
                                "in": "query",
                                "name": "query_date",
                                "required": True,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time parameter",
                                "in": "query",
                                "name": "query_date_time",
                                "required": True,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password parameter",
                                "in": "query",
                                "name": "query_password",
                                "required": True,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array parameter",
                                "in": "query",
                                "name": "query_array_integer",
                                "required": True,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array parameter",
                                "in": "query",
                                "name": "query_array_integer32",
                                "required": True,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array parameter",
                                "in": "query",
                                "name": "query_array_integer64",
                                "required": True,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array parameter",
                                "in": "query",
                                "name": "query_array_number",
                                "required": True,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array parameter",
                                "in": "query",
                                "name": "query_array_float",
                                "required": True,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array parameter",
                                "in": "query",
                                "name": "query_array_double",
                                "required": True,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "query_array_string",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array parameter",
                                "in": "query",
                                "name": "query_array_string_byte",
                                "required": True,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array parameter",
                                "in": "query",
                                "name": "query_array_string_binary",
                                "required": True,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array parameter",
                                "in": "query",
                                "name": "query_array_boolean",
                                "required": True,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array parameter",
                                "in": "query",
                                "name": "query_array_date",
                                "required": True,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array parameter",
                                "in": "query",
                                "name": "query_array_date_time",
                                "required": True,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array parameter",
                                "in": "query",
                                "name": "query_array_password",
                                "required": True,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
                        ],
                        "responses": {"200": {"description": "return value"}},
                    },
                },
                "/with/all/optional/parameters/types": {
                    "get": {
                        "operationId": "get_with_all_optional_parameters_types",
                        "parameters": [
                            {
                                "description": "integer parameter",
                                "in": "query",
                                "name": "query_integer",
                                "required": False,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 parameter",
                                "in": "query",
                                "name": "query_integer32",
                                "required": False,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 parameter",
                                "in": "query",
                                "name": "query_integer64",
                                "required": False,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number parameter",
                                "in": "query",
                                "name": "query_number",
                                "required": False,
                                "type": "number",
                            },
                            {
                                "description": "number float parameter",
                                "in": "query",
                                "name": "query_float",
                                "required": False,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double parameter",
                                "in": "query",
                                "name": "query_double",
                                "required": False,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string parameter",
                                "in": "query",
                                "name": "query_string",
                                "required": False,
                                "type": "string",
                            },
                            {
                                "description": "string byte parameter",
                                "in": "query",
                                "name": "query_string_byte",
                                "required": False,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary parameter",
                                "in": "query",
                                "name": "query_string_binary",
                                "required": False,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean parameter",
                                "in": "query",
                                "name": "query_boolean",
                                "required": False,
                                "type": "boolean",
                            },
                            {
                                "description": "date parameter",
                                "in": "query",
                                "name": "query_date",
                                "required": False,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time parameter",
                                "in": "query",
                                "name": "query_date_time",
                                "required": False,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password parameter",
                                "in": "query",
                                "name": "query_password",
                                "required": False,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array parameter",
                                "in": "query",
                                "name": "query_array_integer",
                                "required": False,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array parameter",
                                "in": "query",
                                "name": "query_array_integer32",
                                "required": False,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array parameter",
                                "in": "query",
                                "name": "query_array_integer64",
                                "required": False,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array parameter",
                                "in": "query",
                                "name": "query_array_number",
                                "required": False,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array parameter",
                                "in": "query",
                                "name": "query_array_float",
                                "required": False,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array parameter",
                                "in": "query",
                                "name": "query_array_double",
                                "required": False,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "query_array_string",
                                "required": False,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array parameter",
                                "in": "query",
                                "name": "query_array_string_byte",
                                "required": False,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array parameter",
                                "in": "query",
                                "name": "query_array_string_binary",
                                "required": False,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array parameter",
                                "in": "query",
                                "name": "query_array_boolean",
                                "required": False,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array parameter",
                                "in": "query",
                                "name": "query_array_date",
                                "required": False,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array parameter",
                                "in": "query",
                                "name": "query_array_date_time",
                                "required": False,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array parameter",
                                "in": "query",
                                "name": "query_array_password",
                                "required": False,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
                        ],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "post": {
                        "operationId": "post_with_all_optional_parameters_types",
                        "parameters": [
                            {
                                "description": "integer parameter",
                                "in": "query",
                                "name": "query_integer",
                                "required": False,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 parameter",
                                "in": "query",
                                "name": "query_integer32",
                                "required": False,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 parameter",
                                "in": "query",
                                "name": "query_integer64",
                                "required": False,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number parameter",
                                "in": "query",
                                "name": "query_number",
                                "required": False,
                                "type": "number",
                            },
                            {
                                "description": "number float parameter",
                                "in": "query",
                                "name": "query_float",
                                "required": False,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double parameter",
                                "in": "query",
                                "name": "query_double",
                                "required": False,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string parameter",
                                "in": "query",
                                "name": "query_string",
                                "required": False,
                                "type": "string",
                            },
                            {
                                "description": "string byte parameter",
                                "in": "query",
                                "name": "query_string_byte",
                                "required": False,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary parameter",
                                "in": "query",
                                "name": "query_string_binary",
                                "required": False,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean parameter",
                                "in": "query",
                                "name": "query_boolean",
                                "required": False,
                                "type": "boolean",
                            },
                            {
                                "description": "date parameter",
                                "in": "query",
                                "name": "query_date",
                                "required": False,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time parameter",
                                "in": "query",
                                "name": "query_date_time",
                                "required": False,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password parameter",
                                "in": "query",
                                "name": "query_password",
                                "required": False,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array parameter",
                                "in": "query",
                                "name": "query_array_integer",
                                "required": False,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array parameter",
                                "in": "query",
                                "name": "query_array_integer32",
                                "required": False,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array parameter",
                                "in": "query",
                                "name": "query_array_integer64",
                                "required": False,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array parameter",
                                "in": "query",
                                "name": "query_array_number",
                                "required": False,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array parameter",
                                "in": "query",
                                "name": "query_array_float",
                                "required": False,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array parameter",
                                "in": "query",
                                "name": "query_array_double",
                                "required": False,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "query_array_string",
                                "required": False,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array parameter",
                                "in": "query",
                                "name": "query_array_string_byte",
                                "required": False,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array parameter",
                                "in": "query",
                                "name": "query_array_string_binary",
                                "required": False,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array parameter",
                                "in": "query",
                                "name": "query_array_boolean",
                                "required": False,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array parameter",
                                "in": "query",
                                "name": "query_array_date",
                                "required": False,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array parameter",
                                "in": "query",
                                "name": "query_array_date_time",
                                "required": False,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array parameter",
                                "in": "query",
                                "name": "query_array_password",
                                "required": False,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
                        ],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "put": {
                        "operationId": "put_with_all_optional_parameters_types",
                        "parameters": [
                            {
                                "description": "integer parameter",
                                "in": "query",
                                "name": "query_integer",
                                "required": False,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 parameter",
                                "in": "query",
                                "name": "query_integer32",
                                "required": False,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 parameter",
                                "in": "query",
                                "name": "query_integer64",
                                "required": False,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number parameter",
                                "in": "query",
                                "name": "query_number",
                                "required": False,
                                "type": "number",
                            },
                            {
                                "description": "number float parameter",
                                "in": "query",
                                "name": "query_float",
                                "required": False,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double parameter",
                                "in": "query",
                                "name": "query_double",
                                "required": False,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string parameter",
                                "in": "query",
                                "name": "query_string",
                                "required": False,
                                "type": "string",
                            },
                            {
                                "description": "string byte parameter",
                                "in": "query",
                                "name": "query_string_byte",
                                "required": False,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary parameter",
                                "in": "query",
                                "name": "query_string_binary",
                                "required": False,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean parameter",
                                "in": "query",
                                "name": "query_boolean",
                                "required": False,
                                "type": "boolean",
                            },
                            {
                                "description": "date parameter",
                                "in": "query",
                                "name": "query_date",
                                "required": False,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time parameter",
                                "in": "query",
                                "name": "query_date_time",
                                "required": False,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password parameter",
                                "in": "query",
                                "name": "query_password",
                                "required": False,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array parameter",
                                "in": "query",
                                "name": "query_array_integer",
                                "required": False,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array parameter",
                                "in": "query",
                                "name": "query_array_integer32",
                                "required": False,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array parameter",
                                "in": "query",
                                "name": "query_array_integer64",
                                "required": False,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array parameter",
                                "in": "query",
                                "name": "query_array_number",
                                "required": False,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array parameter",
                                "in": "query",
                                "name": "query_array_float",
                                "required": False,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array parameter",
                                "in": "query",
                                "name": "query_array_double",
                                "required": False,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "query_array_string",
                                "required": False,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array parameter",
                                "in": "query",
                                "name": "query_array_string_byte",
                                "required": False,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array parameter",
                                "in": "query",
                                "name": "query_array_string_binary",
                                "required": False,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array parameter",
                                "in": "query",
                                "name": "query_array_boolean",
                                "required": False,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array parameter",
                                "in": "query",
                                "name": "query_array_date",
                                "required": False,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array parameter",
                                "in": "query",
                                "name": "query_array_date_time",
                                "required": False,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array parameter",
                                "in": "query",
                                "name": "query_array_password",
                                "required": False,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
                        ],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "delete": {
                        "operationId": "delete_with_all_optional_parameters_types",
                        "parameters": [
                            {
                                "description": "integer parameter",
                                "in": "query",
                                "name": "query_integer",
                                "required": False,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 parameter",
                                "in": "query",
                                "name": "query_integer32",
                                "required": False,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 parameter",
                                "in": "query",
                                "name": "query_integer64",
                                "required": False,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number parameter",
                                "in": "query",
                                "name": "query_number",
                                "required": False,
                                "type": "number",
                            },
                            {
                                "description": "number float parameter",
                                "in": "query",
                                "name": "query_float",
                                "required": False,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double parameter",
                                "in": "query",
                                "name": "query_double",
                                "required": False,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string parameter",
                                "in": "query",
                                "name": "query_string",
                                "required": False,
                                "type": "string",
                            },
                            {
                                "description": "string byte parameter",
                                "in": "query",
                                "name": "query_string_byte",
                                "required": False,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary parameter",
                                "in": "query",
                                "name": "query_string_binary",
                                "required": False,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean parameter",
                                "in": "query",
                                "name": "query_boolean",
                                "required": False,
                                "type": "boolean",
                            },
                            {
                                "description": "date parameter",
                                "in": "query",
                                "name": "query_date",
                                "required": False,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time parameter",
                                "in": "query",
                                "name": "query_date_time",
                                "required": False,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password parameter",
                                "in": "query",
                                "name": "query_password",
                                "required": False,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array parameter",
                                "in": "query",
                                "name": "query_array_integer",
                                "required": False,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array parameter",
                                "in": "query",
                                "name": "query_array_integer32",
                                "required": False,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array parameter",
                                "in": "query",
                                "name": "query_array_integer64",
                                "required": False,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array parameter",
                                "in": "query",
                                "name": "query_array_number",
                                "required": False,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array parameter",
                                "in": "query",
                                "name": "query_array_float",
                                "required": False,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array parameter",
                                "in": "query",
                                "name": "query_array_double",
                                "required": False,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array parameter",
                                "in": "query",
                                "name": "query_array_string",
                                "required": False,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array parameter",
                                "in": "query",
                                "name": "query_array_string_byte",
                                "required": False,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array parameter",
                                "in": "query",
                                "name": "query_array_string_binary",
                                "required": False,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array parameter",
                                "in": "query",
                                "name": "query_array_boolean",
                                "required": False,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array parameter",
                                "in": "query",
                                "name": "query_array_date",
                                "required": False,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array parameter",
                                "in": "query",
                                "name": "query_array_date_time",
                                "required": False,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array parameter",
                                "in": "query",
                                "name": "query_array_password",
                                "required": False,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
                        ],
                        "responses": {"200": {"description": "return value"}},
                    },
                },
                "/with/all/paths/types": {
                    "get": {
                        "operationId": "get_with_all_paths_types",
                        "parameters": [
                            {
                                "description": "integer path",
                                "in": "path",
                                "name": "path_integer",
                                "required": True,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 path",
                                "in": "path",
                                "name": "path_integer32",
                                "required": True,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 path",
                                "in": "path",
                                "name": "path_integer64",
                                "required": True,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number path",
                                "in": "path",
                                "name": "path_number",
                                "required": True,
                                "type": "number",
                            },
                            {
                                "description": "number float path",
                                "in": "path",
                                "name": "path_float",
                                "required": True,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double path",
                                "in": "path",
                                "name": "path_double",
                                "required": True,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string path",
                                "in": "path",
                                "name": "path_string",
                                "required": True,
                                "type": "string",
                            },
                            {
                                "description": "string byte path",
                                "in": "path",
                                "name": "path_string_byte",
                                "required": True,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary path",
                                "in": "path",
                                "name": "path_string_binary",
                                "required": True,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean path",
                                "in": "path",
                                "name": "path_boolean",
                                "required": True,
                                "type": "boolean",
                            },
                            {
                                "description": "date path",
                                "in": "path",
                                "name": "path_date",
                                "required": True,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time path",
                                "in": "path",
                                "name": "path_date_time",
                                "required": True,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password path",
                                "in": "path",
                                "name": "path_password",
                                "required": True,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array path",
                                "in": "path",
                                "name": "path_array_integer",
                                "required": True,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array path",
                                "in": "path",
                                "name": "path_array_integer32",
                                "required": True,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array path",
                                "in": "path",
                                "name": "path_array_integer64",
                                "required": True,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array path",
                                "in": "path",
                                "name": "path_array_number",
                                "required": True,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array path",
                                "in": "path",
                                "name": "path_array_float",
                                "required": True,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array path",
                                "in": "path",
                                "name": "path_array_double",
                                "required": True,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array path",
                                "in": "path",
                                "name": "path_array_string",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array path",
                                "in": "path",
                                "name": "path_array_string_byte",
                                "required": True,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array path",
                                "in": "path",
                                "name": "path_array_string_binary",
                                "required": True,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array path",
                                "in": "path",
                                "name": "path_array_boolean",
                                "required": True,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array path",
                                "in": "path",
                                "name": "path_array_date",
                                "required": True,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array path",
                                "in": "path",
                                "name": "path_array_date_time",
                                "required": True,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array path",
                                "in": "path",
                                "name": "path_array_password",
                                "required": True,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
                        ],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "post": {
                        "operationId": "post_with_all_paths_types",
                        "parameters": [
                            {
                                "description": "integer path",
                                "in": "path",
                                "name": "path_integer",
                                "required": True,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 path",
                                "in": "path",
                                "name": "path_integer32",
                                "required": True,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 path",
                                "in": "path",
                                "name": "path_integer64",
                                "required": True,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number path",
                                "in": "path",
                                "name": "path_number",
                                "required": True,
                                "type": "number",
                            },
                            {
                                "description": "number float path",
                                "in": "path",
                                "name": "path_float",
                                "required": True,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double path",
                                "in": "path",
                                "name": "path_double",
                                "required": True,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string path",
                                "in": "path",
                                "name": "path_string",
                                "required": True,
                                "type": "string",
                            },
                            {
                                "description": "string byte path",
                                "in": "path",
                                "name": "path_string_byte",
                                "required": True,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary path",
                                "in": "path",
                                "name": "path_string_binary",
                                "required": True,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean path",
                                "in": "path",
                                "name": "path_boolean",
                                "required": True,
                                "type": "boolean",
                            },
                            {
                                "description": "date path",
                                "in": "path",
                                "name": "path_date",
                                "required": True,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time path",
                                "in": "path",
                                "name": "path_date_time",
                                "required": True,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password path",
                                "in": "path",
                                "name": "path_password",
                                "required": True,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array path",
                                "in": "path",
                                "name": "path_array_integer",
                                "required": True,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array path",
                                "in": "path",
                                "name": "path_array_integer32",
                                "required": True,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array path",
                                "in": "path",
                                "name": "path_array_integer64",
                                "required": True,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array path",
                                "in": "path",
                                "name": "path_array_number",
                                "required": True,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array path",
                                "in": "path",
                                "name": "path_array_float",
                                "required": True,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array path",
                                "in": "path",
                                "name": "path_array_double",
                                "required": True,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array path",
                                "in": "path",
                                "name": "path_array_string",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array path",
                                "in": "path",
                                "name": "path_array_string_byte",
                                "required": True,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array path",
                                "in": "path",
                                "name": "path_array_string_binary",
                                "required": True,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array path",
                                "in": "path",
                                "name": "path_array_boolean",
                                "required": True,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array path",
                                "in": "path",
                                "name": "path_array_date",
                                "required": True,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array path",
                                "in": "path",
                                "name": "path_array_date_time",
                                "required": True,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array path",
                                "in": "path",
                                "name": "path_array_password",
                                "required": True,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
                        ],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "put": {
                        "operationId": "put_with_all_paths_types",
                        "parameters": [
                            {
                                "description": "integer path",
                                "in": "path",
                                "name": "path_integer",
                                "required": True,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 path",
                                "in": "path",
                                "name": "path_integer32",
                                "required": True,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 path",
                                "in": "path",
                                "name": "path_integer64",
                                "required": True,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number path",
                                "in": "path",
                                "name": "path_number",
                                "required": True,
                                "type": "number",
                            },
                            {
                                "description": "number float path",
                                "in": "path",
                                "name": "path_float",
                                "required": True,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double path",
                                "in": "path",
                                "name": "path_double",
                                "required": True,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string path",
                                "in": "path",
                                "name": "path_string",
                                "required": True,
                                "type": "string",
                            },
                            {
                                "description": "string byte path",
                                "in": "path",
                                "name": "path_string_byte",
                                "required": True,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary path",
                                "in": "path",
                                "name": "path_string_binary",
                                "required": True,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean path",
                                "in": "path",
                                "name": "path_boolean",
                                "required": True,
                                "type": "boolean",
                            },
                            {
                                "description": "date path",
                                "in": "path",
                                "name": "path_date",
                                "required": True,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time path",
                                "in": "path",
                                "name": "path_date_time",
                                "required": True,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password path",
                                "in": "path",
                                "name": "path_password",
                                "required": True,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array path",
                                "in": "path",
                                "name": "path_array_integer",
                                "required": True,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array path",
                                "in": "path",
                                "name": "path_array_integer32",
                                "required": True,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array path",
                                "in": "path",
                                "name": "path_array_integer64",
                                "required": True,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array path",
                                "in": "path",
                                "name": "path_array_number",
                                "required": True,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array path",
                                "in": "path",
                                "name": "path_array_float",
                                "required": True,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array path",
                                "in": "path",
                                "name": "path_array_double",
                                "required": True,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array path",
                                "in": "path",
                                "name": "path_array_string",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array path",
                                "in": "path",
                                "name": "path_array_string_byte",
                                "required": True,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array path",
                                "in": "path",
                                "name": "path_array_string_binary",
                                "required": True,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array path",
                                "in": "path",
                                "name": "path_array_boolean",
                                "required": True,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array path",
                                "in": "path",
                                "name": "path_array_date",
                                "required": True,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array path",
                                "in": "path",
                                "name": "path_array_date_time",
                                "required": True,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array path",
                                "in": "path",
                                "name": "path_array_password",
                                "required": True,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
                        ],
                        "responses": {"200": {"description": "return value"}},
                    },
                    "delete": {
                        "operationId": "delete_with_all_paths_types",
                        "parameters": [
                            {
                                "description": "integer path",
                                "in": "path",
                                "name": "path_integer",
                                "required": True,
                                "type": "integer",
                            },
                            {
                                "description": "integer 32 path",
                                "in": "path",
                                "name": "path_integer32",
                                "required": True,
                                "type": "integer",
                                "format": "int32",
                            },
                            {
                                "description": "integer 64 path",
                                "in": "path",
                                "name": "path_integer64",
                                "required": True,
                                "type": "integer",
                                "format": "int64",
                            },
                            {
                                "description": "number path",
                                "in": "path",
                                "name": "path_number",
                                "required": True,
                                "type": "number",
                            },
                            {
                                "description": "number float path",
                                "in": "path",
                                "name": "path_float",
                                "required": True,
                                "type": "number",
                                "format": "float",
                            },
                            {
                                "description": "number double path",
                                "in": "path",
                                "name": "path_double",
                                "required": True,
                                "type": "number",
                                "format": "double",
                            },
                            {
                                "description": "string path",
                                "in": "path",
                                "name": "path_string",
                                "required": True,
                                "type": "string",
                            },
                            {
                                "description": "string byte path",
                                "in": "path",
                                "name": "path_string_byte",
                                "required": True,
                                "type": "string",
                                "format": "byte",
                            },
                            {
                                "description": "string binary path",
                                "in": "path",
                                "name": "path_string_binary",
                                "required": True,
                                "type": "string",
                                "format": "binary",
                            },
                            {
                                "description": "boolean path",
                                "in": "path",
                                "name": "path_boolean",
                                "required": True,
                                "type": "boolean",
                            },
                            {
                                "description": "date path",
                                "in": "path",
                                "name": "path_date",
                                "required": True,
                                "type": "string",
                                "format": "date",
                            },
                            {
                                "description": "date time path",
                                "in": "path",
                                "name": "path_date_time",
                                "required": True,
                                "type": "string",
                                "format": "date-time",
                            },
                            {
                                "description": "password path",
                                "in": "path",
                                "name": "path_password",
                                "required": True,
                                "type": "string",
                                "format": "password",
                            },
                            {
                                "description": "integer array path",
                                "in": "path",
                                "name": "path_array_integer",
                                "required": True,
                                "items": {"type": "integer"},
                                "type": "array",
                            },
                            {
                                "description": "integer 32 array path",
                                "in": "path",
                                "name": "path_array_integer32",
                                "required": True,
                                "items": {"type": "integer", "format": "int32"},
                                "type": "array",
                            },
                            {
                                "description": "integer 64 array path",
                                "in": "path",
                                "name": "path_array_integer64",
                                "required": True,
                                "items": {"type": "integer", "format": "int64"},
                                "type": "array",
                            },
                            {
                                "description": "number array path",
                                "in": "path",
                                "name": "path_array_number",
                                "required": True,
                                "items": {"type": "number"},
                                "type": "array",
                            },
                            {
                                "description": "number float array path",
                                "in": "path",
                                "name": "path_array_float",
                                "required": True,
                                "items": {"type": "number", "format": "float"},
                                "type": "array",
                            },
                            {
                                "description": "number double array path",
                                "in": "path",
                                "name": "path_array_double",
                                "required": True,
                                "items": {"type": "number", "format": "double"},
                                "type": "array",
                            },
                            {
                                "description": "string array path",
                                "in": "path",
                                "name": "path_array_string",
                                "required": True,
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            {
                                "description": "string byte array path",
                                "in": "path",
                                "name": "path_array_string_byte",
                                "required": True,
                                "items": {"type": "string", "format": "byte"},
                                "type": "array",
                            },
                            {
                                "description": "string binary array path",
                                "in": "path",
                                "name": "path_array_string_binary",
                                "required": True,
                                "items": {"type": "string", "format": "binary"},
                                "type": "array",
                            },
                            {
                                "description": "boolean array path",
                                "in": "path",
                                "name": "path_array_boolean",
                                "required": True,
                                "items": {"type": "boolean"},
                                "type": "array",
                            },
                            {
                                "description": "date array path",
                                "in": "path",
                                "name": "path_array_date",
                                "required": True,
                                "items": {"type": "string", "format": "date"},
                                "type": "array",
                            },
                            {
                                "description": "date time array path",
                                "in": "path",
                                "name": "path_array_date_time",
                                "required": True,
                                "items": {"type": "string", "format": "date-time"},
                                "type": "array",
                            },
                            {
                                "description": "password array path",
                                "in": "path",
                                "name": "path_array_password",
                                "required": True,
                                "items": {"type": "string", "format": "password"},
                                "type": "array",
                            },
                        ],
                        "responses": {"200": {"description": "return value"}},
                    },
                },
                "/date": {
                    "get": {
                        "operationId": "get_date",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {
                                    "type": "array",
                                    "items": {"type": "string", "format": "date"},
                                },
                            }
                        },
                    }
                },
                "/datetime": {
                    "get": {
                        "operationId": "get_date_time",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {
                                    "type": "array",
                                    "items": {"type": "string", "format": "date-time"},
                                },
                            }
                        },
                    }
                },
                "/datetime/encoding": {
                    "get": {
                        "operationId": "get_date_time_encoding",
                        "parameters": [
                            {
                                "description": "string parameter",
                                "in": "query",
                                "name": "encoded_date_time",
                                "required": True,
                                "type": "string",
                                "format": "date-time",
                            }
                        ],
                        "responses": {"200": {"description": "return value"}},
                    }
                },
            },
        },
        match_querystring=True,
    )
    # filtered tags service
    responses.add(
        responses.GET,
        url="http://localhost:8944/",
        json={
            "swagger": "2.0",
            "definitions": {
                "TestObject": {
                    "type": "object",
                    "properties": {"test": {"type": "string", "description": "test"}},
                    "title": "Test",
                }
            },
            "paths": {
                "/tags": {
                    "get": {
                        "operationId": "get_tags",
                        "tags": ["tag 0", "tag 1"],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"$ref": "#/definitions/TestObject"},
                                    "type": "array",
                                },
                            }
                        },
                    },
                    "post": {
                        "operationId": "post_tags",
                        "tags": ["tag 1", "tag 2"],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"$ref": "#/definitions/TestObject"},
                                    "type": "array",
                                },
                            }
                        },
                    },
                    "put": {
                        "operationId": "put_tags",
                        "tags": ["tag 2", "tag 3"],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"$ref": "#/definitions/TestObject"},
                                    "type": "array",
                                },
                            }
                        },
                    },
                    "delete": {
                        "operationId": "delete_tags",
                        "tags": ["tag 3", "tag 4"],
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"$ref": "#/definitions/TestObject"},
                                    "type": "array",
                                },
                            }
                        },
                    },
                }
            },
        },
        match_querystring=True,
    )
    # values false service
    responses.add(
        responses.GET,
        url="http://localhost:8945/",
        json={
            "swagger": "2.0",
            "definitions": {
                "ZeroInteger": {
                    "properties": {
                        "zero_integer": {"type": "integer", "format": "int32"}
                    }
                },
                "ZeroFloat": {
                    "properties": {"zero_float": {"type": "number", "format": "float"}}
                },
                "FalseBoolean": {"properties": {"false_boolean": {"type": "boolean"}}},
                "EmptyString": {"properties": {"empty_string": {"type": "string"}}},
                "EmptyList": {
                    "properties": {
                        "empty_list": {
                            "type": "array",
                            "items": {"$ref": "#/definitions/Empty"},
                        }
                    }
                },
                "EmptyDictionary": {
                    "properties": {
                        "empty_dictionary": {
                            "type": "object",
                            "$ref": "#/definitions/Empty",
                        }
                    }
                },
                "Empty": {"properties": {}},
            },
            "paths": {
                "/with/zero/integer": {
                    "get": {
                        "operationId": "get_with_zero_integer",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/definitions/ZeroInteger"},
                                },
                            }
                        },
                    }
                },
                "/with/zero/float": {
                    "get": {
                        "operationId": "get_with_zero_float",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/definitions/ZeroFloat"},
                                },
                            }
                        },
                    }
                },
                "/with/false/boolean": {
                    "get": {
                        "operationId": "get_with_false_boolean",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/definitions/FalseBoolean"},
                                },
                            }
                        },
                    }
                },
                "/with/empty/string": {
                    "get": {
                        "operationId": "get_with_empty_string",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/definitions/EmptyString"},
                                },
                            }
                        },
                    }
                },
                "/with/empty/list": {
                    "get": {
                        "operationId": "get_with_empty_list",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/definitions/EmptyList"},
                                },
                            }
                        },
                    }
                },
                "/with/empty/dictionary": {
                    "get": {
                        "operationId": "get_with_empty_dictionary",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/definitions/EmptyDictionary"},
                                },
                            }
                        },
                    }
                },
            },
        },
        match_querystring=True,
    )
    # output order service
    responses.add(
        responses.GET,
        url="http://localhost:8946/",
        json={
            "swagger": "2.0",
            "definitions": {
                "Price": {
                    "required": ["curve", "date", "mat", "ts"],
                    "type": "object",
                    "properties": {
                        "ts": {
                            "type": "string",
                            "description": "timeslot",
                            "maxLength": 2,
                        },
                        "date": {
                            "type": "string",
                            "description": "date",
                            "format": "date",
                        },
                        "curve": {
                            "type": "string",
                            "description": "curvename",
                            "maxLength": 20,
                        },
                        "mat": {
                            "type": "string",
                            "description": "maturity",
                            "maxLength": 4,
                        },
                    },
                    "title": "RealizedPrice",
                }
            },
            "paths": {
                "/price/unordered": {
                    "get": {
                        "operationId": "get_price_unordered",
                        "description": "Price",
                        "parameters": [
                            {
                                "in": "query",
                                "description": "date",
                                "format": "date",
                                "required": False,
                                "type": "string",
                                "name": "date",
                            },
                            {
                                "name": "curve",
                                "in": "query",
                                "required": False,
                                "type": "string",
                                "description": "curvename",
                            },
                            {
                                "name": "ts",
                                "in": "query",
                                "required": False,
                                "type": "string",
                                "description": "timeslot",
                            },
                            {
                                "name": "mat",
                                "in": "query",
                                "required": False,
                                "type": "string",
                                "description": "maturity",
                            },
                        ],
                        "responses": {
                            "200": {
                                "description": "successful operation",
                                "schema": {
                                    "items": {"$ref": "#/definitions/Price"},
                                    "type": "array",
                                },
                            }
                        },
                    }
                }
            },
        },
        match_querystring=True,
    )
    from testsutils import (
        without_parameter_service,
        header_parameter_service,
        form_parameter_service,
        array_parameter_service,
    )

    serviceshandler.start_services(
        (without_parameter_service, 8950),
        (header_parameter_service, 8951),
        (form_parameter_service, 8952),
        (array_parameter_service, 8953),
    )
    loader.load("based_on_definitions_services.yml")


def test_string_multi_array_parameter(services):
    from pyxelrest import pyxelrestgenerator

    result = "string_array=\"['str1', 'str2']\""
    assert (
        pyxelrestgenerator.array_parameter_get_string_multi_array_parameter(
            ["str1", "str2"]
        )
        == result
    )


def test_string_default_array_parameter(services):
    from pyxelrest import pyxelrestgenerator

    result = "string_array=\"['str1,str2']\""
    assert (
        pyxelrestgenerator.array_parameter_get_string_default_array_parameter(
            ["str1", "str2"]
        )
        == result
    )


def test_string_csv_array_parameter(services):
    from pyxelrest import pyxelrestgenerator

    result = "string_array=\"['str1,str2']\""
    assert (
        pyxelrestgenerator.array_parameter_get_string_csv_array_parameter(
            ["str1", "str2"]
        )
        == result
    )


def test_string_ssv_array_parameter(services):
    from pyxelrest import pyxelrestgenerator

    result = "string_array=\"['str1 str2']\""
    assert (
        pyxelrestgenerator.array_parameter_get_string_ssv_array_parameter(
            ["str1", "str2"]
        )
        == result
    )


def test_string_tsv_array_parameter(services):
    from pyxelrest import pyxelrestgenerator

    result = "string_array=\"['str1\\tstr2']\""
    assert (
        pyxelrestgenerator.array_parameter_get_string_tsv_array_parameter(
            ["str1", "str2"]
        )
        == result
    )


def test_string_pipes_array_parameter(services):
    from pyxelrest import pyxelrestgenerator

    result = "string_array=\"['str1|str2']\""
    assert (
        pyxelrestgenerator.array_parameter_get_string_pipes_array_parameter(
            ["str1", "str2"]
        )
        == result
    )


def test_plain_text_without_parameter(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.without_parameter_get_plain_text_without_parameter()
        == "string value returned should be truncated so that the following information cannot be seen by user, because of the fact that Excel does not allow more than 255 characters in a cell. Only the 255 characters will be returned by the user defined functions:  "
    )


def test_post_without_parameter(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.without_parameter_post_without_parameter()
        == "POST performed properly"
    )


def test_put_without_parameter(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.without_parameter_put_without_parameter()
        == "PUT performed properly"
    )


def test_delete_without_parameter(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.without_parameter_delete_without_parameter()
        == "DELETE performed properly"
    )


def test_get_header_parameter(services):
    from pyxelrest import pyxelrestgenerator

    headers = pyxelrestgenerator.header_parameter_get_header("sent header")
    header_param_index = headers[0].index("Header-String")
    assert headers[1][header_param_index] == "sent header"


def test_post_form_parameter(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.form_parameter_post_form("sent string form data") == [
        ["form_string"],
        ["sent string form data"],
    ]


def test_get_with_tags(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        "Second tag is one of the accepted tags"
        == pyxelrestgenerator.filtered_tags_get_tags()
    )


def test_post_with_tags(services):
    from pyxelrest import pyxelrestgenerator

    assert "All tags are accepted" == pyxelrestgenerator.filtered_tags_post_tags()


def test_put_with_tags(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        "First tag is one of the accepted tags"
        == pyxelrestgenerator.filtered_tags_put_tags()
    )


def test_delete_with_tags(services):
    from pyxelrest import pyxelrestgenerator

    assert not hasattr(pyxelrestgenerator, "filtered_tags_delete_tags")


def test_get_with_zero_integer(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.values_false_get_with_zero_integer() == [
        ["zero_integer"],
        [0],
    ]


def test_get_with_zero_float(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.values_false_get_with_zero_float() == [
        ["zero_float"],
        [0.0],
    ]


def test_get_with_false_boolean(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.values_false_get_with_false_boolean() == [
        ["false_boolean"],
        [False],
    ]


def test_get_with_empty_string(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.values_false_get_with_empty_string() == [
        ["empty_string"],
        [""],
    ]


def test_get_with_empty_list(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.values_false_get_with_empty_list() == [""]


def test_get_with_empty_dictionary(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.values_false_get_with_empty_dictionary() == [""]


def test_get_compare_output_order(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.output_order_get_price_unordered() == [
        [u"ts", u"date", u"curve", u"mat"],
        [u"", datetime.datetime(2017, 4, 5, 0, 0), u"PW_FR", u"H01"],
        [u"2017-04-05 12:03:15", datetime.datetime(2017, 4, 5, 0, 0), u"PW_FR", u"H02"],
        [u"", datetime.datetime(2017, 4, 5, 0, 0), u"PW_FR", u"H03"],
    ]


def test_get_date(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.usual_parameters_get_date() == [
        [datetime.datetime(2014, 3, 5, 0, 0)],
        [datetime.datetime(9999, 1, 1, 0, 0)],
        [datetime.datetime(3001, 1, 1, 0, 0)],
        [datetime.datetime(1970, 1, 1, 0, 0)],
        [datetime.datetime(1900, 1, 1, 0, 0)],
    ]


def test_get_datetime(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.usual_parameters_get_date_time() == [
        [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
        [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
        [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
        [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
        [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
        [datetime.datetime(9999, 1, 1, 0, 0, tzinfo=tzutc())],
        [datetime.datetime(3001, 1, 1, 8, 0, tzinfo=tzutc())],
        [datetime.datetime(1970, 1, 1, 1, 0, tzinfo=tzutc())],
        [datetime.datetime(1970, 1, 1, 2, 0, tzinfo=tzutc())],
    ]

import os
from importlib import import_module, reload

import yaml

import pyxelrest._generator_config
from responses import RequestsMock

from tests.loader import stdout_logging


def test_without_logging_configuration_file(responses: RequestsMock, tmpdir):
    """
    This test case assert that pyxelrest can be loaded without logging configuration
    """
    responses.add(
        responses.GET,
        url="http://localhost:8943/",
        json={
            "swagger": "2.0",
            "paths": {
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
                }
            },
        },
        match_querystring=True,
    )
    pyxelrest._generator_config.LOGGING_CONFIGURATION_FILE_PATH = os.path.join(
        tmpdir, "non_existing_configuration.yml"
    )
    config_file_path = os.path.join(tmpdir, "test_config.yml")
    config = {
        "usual_parameters": {
            "open_api": {"definition": "http://localhost:8943/"},
            "formulas": {"dynamic_array": {"lock_excel": True}},
        }
    }
    with open(config_file_path, "wt") as file:
        file.write(yaml.dump(config))

    pyxelrest._generator_config.SERVICES_CONFIGURATION_FILE_PATH = config_file_path
    reload(import_module("pyxelrest._generator"))


def test_with_logging_configuration_file(responses: RequestsMock, tmpdir):
    """
    This test case assert that pyxelrest can be loaded with logging configuration
    """
    responses.add(
        responses.GET,
        url="http://localhost:8943/",
        json={
            "swagger": "2.0",
            "paths": {
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
                }
            },
        },
        match_querystring=True,
    )
    pyxelrest._generator_config.LOGGING_CONFIGURATION_FILE_PATH = stdout_logging(tmpdir)
    config_file_path = os.path.join(tmpdir, "test_config.yml")
    config = {
        "usual_parameters": {
            "open_api": {"definition": "http://localhost:8943/"},
            "formulas": {"dynamic_array": {"lock_excel": True}},
        }
    }
    with open(config_file_path, "wt") as file:
        file.write(yaml.dump(config))

    pyxelrest._generator_config.SERVICES_CONFIGURATION_FILE_PATH = config_file_path
    reload(import_module("pyxelrest._generator"))

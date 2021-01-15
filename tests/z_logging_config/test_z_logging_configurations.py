import os
import winreg
from importlib import import_module, reload

import yaml

import pyxelrest._generator_config
from responses import RequestsMock

from tests.conftest import FakeRegistryKey


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


def test_with_logging_configuration_file(
    responses: RequestsMock, tmpdir, fake_registry
):
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
    install_location = fake_install_location(fake_registry, tmpdir)
    os.mkdir(os.path.join(install_location, "configuration"))

    log_config_file_path = os.path.join(
        install_location, "configuration", "logging.yml"
    )
    create_logging_conf(log_config_file_path)

    config_file_path = os.path.join(install_location, "configuration", "services.yml")
    config = {
        "usual_parameters": {
            "open_api": {"definition": "http://localhost:8943/"},
            "formulas": {"dynamic_array": {"lock_excel": True}},
        }
    }
    with open(config_file_path, "wt") as file:
        file.write(yaml.dump(config))

    reload(import_module("pyxelrest._generator_config"))
    reload(import_module("pyxelrest._generator"))


def create_logging_conf(config_file_path):
    with open(config_file_path, "wt") as file:
        file.write(
            """version: 1
formatters:
  clean:
    format: '%(asctime)s [%(threadName)s] [%(levelname)s] %(message)s'
handlers:
  standard_output:
    class: logging.StreamHandler
    formatter: clean
    stream: ext://sys.stdout
loggers:
  pyxelrest:
    level: DEBUG
  xlwings:
    level: DEBUG
  requests_auth:
    level: DEBUG
  requests.packages.urllib3:
    level: DEBUG
root:
  level: DEBUG
  handlers: [standard_output]"""
        )


def fake_install_location(fake_registry, tmpdir) -> str:
    location = os.path.join(tmpdir, "install_location")
    os.makedirs(location)

    registry_key = FakeRegistryKey()
    registry_key.set("InstallLocation", 0, winreg.REG_SZ, location)

    fake_registry[
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest",
    ] = registry_key

    return location

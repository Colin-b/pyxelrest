from importlib import import_module, reload
import os

import yaml

import pyxelrest


def load(tmpdir, config: dict):
    # Create services configuration
    config_file_path = os.path.join(tmpdir, "test_config.yml")
    with open(config_file_path, "wt") as file:
        file.write(yaml.dump(config))

    pyxelrest.SERVICES_CONFIGURATION_FILE_PATH = config_file_path

    # Create logging configuration
    config_file_path = os.path.join(tmpdir, "test_logging.yml")
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

    pyxelrest.LOGGING_CONFIGURATION_FILE_PATH = config_file_path

    return reload(import_module("pyxelrest._generator"))

from importlib import import_module, reload
import os

import yaml

import pyxelrest


def load(new_configuration_file_name: str):
    pyxelrest.SERVICES_CONFIGURATION_FILE_PATH = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), new_configuration_file_name
    )
    return reload(import_module("pyxelrest.pyxelrestgenerator"))


def load2(tmpdir, config: dict):
    config_file_path = os.path.join(tmpdir, "test_config.yml")
    with open(config_file_path, "wt") as file:
        file.write(yaml.dump(config))

    pyxelrest.SERVICES_CONFIGURATION_FILE_PATH = config_file_path
    return reload(import_module("pyxelrest.pyxelrestgenerator"))

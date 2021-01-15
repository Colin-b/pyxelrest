from importlib import import_module, reload
import os
import time

import yaml

import pyxelrest._generator_config


def load(tmpdir, config: dict):
    # Create services configuration
    config_file_path = os.path.join(tmpdir, "test_config.yml")
    with open(config_file_path, "wt") as file:
        file.write(yaml.dump(config))

    pyxelrest._generator_config.SERVICES_CONFIGURATION_FILE_PATH = config_file_path

    module = import_module("pyxelrest._generator")
    cache_file = getattr(module, "__cached__")
    if os.path.exists(cache_file):
        os.remove(cache_file)
    time.sleep(1)
    return reload(module)

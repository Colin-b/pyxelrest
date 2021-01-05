import importlib
import logging
import os

from importlib import reload, import_module

import pyxelrest._generator_config
from tests.loader import stdout_logging


def test_loading_failure(monkeypatch, tmpdir, caplog):
    caplog.set_level(logging.ERROR, logger="pyxelrest")
    config_file_path = os.path.join(tmpdir, "test_config.yml")
    with open(config_file_path, "wb") as file:
        file.write(b"")
    pyxelrest._generator_config.SERVICES_CONFIGURATION_FILE_PATH = config_file_path
    # pyxelrest._generator_config.LOGGING_CONFIGURATION_FILE_PATH = stdout_logging(tmpdir)

    original = import_module

    def reload_failure(module_name):
        if module_name == "pyxelrest.generated":
            raise Exception("Loading failed")
        else:
            original(module_name)

    monkeypatch.setattr(importlib, "import_module", reload_failure)
    reload(import_module("pyxelrest._generator"))

    assert caplog.messages == [
        "Cannot expose generated functions.",
    ]

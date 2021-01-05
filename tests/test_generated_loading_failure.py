import importlib
import os

import pyxelrest._generator_config


def test_loading_failure(monkeypatch, tmpdir, caplog):
    config_file_path = os.path.join(tmpdir, "test_config.yml")
    with open(config_file_path, "wb") as file:
        file.write(b"")
    pyxelrest._generator_config.SERVICES_CONFIGURATION_FILE_PATH = config_file_path

    def reload_failure(*args):
        raise Exception("Loading failed")

    monkeypatch.setattr(importlib, "reload", reload_failure)
    from pyxelrest import _generator

    assert caplog.messages == [
        "Logging configuration file () cannot be found.",
        "Cannot expose generated functions.",
    ]

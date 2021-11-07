import logging
import os
from importlib import reload, import_module

import pytest
import yaml

import pyxelrest._generator_config


def test_incorrect_configuration(monkeypatch, tmpdir, caplog):
    caplog.set_level(logging.ERROR, logger="pyxelrest")
    config_file_path = os.path.join(tmpdir, "test_config.yml")
    with open(config_file_path, "wb") as file:
        file.write(b"\x1f")
    pyxelrest._generator_config.SERVICES_CONFIGURATION_FILE_PATH = config_file_path
    with pytest.raises(yaml.reader.ReaderError):
        reload(import_module("pyxelrest._generator"))
    assert caplog.messages == [
        "Cannot generate python files.",
    ]

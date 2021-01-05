import os

import pytest
import yaml

import pyxelrest._generator_config


def test_incorrect_configuration(monkeypatch, tmpdir, caplog):
    config_file_path = os.path.join(tmpdir, "test_config.yml")
    with open(config_file_path, "wb") as file:
        file.write(b"\x1f")
    pyxelrest._generator_config.SERVICES_CONFIGURATION_FILE_PATH = config_file_path
    with pytest.raises(yaml.reader.ReaderError):
        from pyxelrest import _generator
    assert caplog.messages == [
        "Logging configuration file () cannot be found.",
        "Cannot generate python files.",
    ]

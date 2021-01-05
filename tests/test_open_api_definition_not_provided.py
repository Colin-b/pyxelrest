import os

import yaml

import pyxelrest._generator_config


def test_service_without_openapi_definition(monkeypatch, tmpdir, caplog):
    config_file_path = os.path.join(tmpdir, "test_config.yml")
    with open(config_file_path, "wt") as file:
        file.write(
            yaml.dump(
                {
                    "without_open_api_definition": {
                        "udf": {
                            "return_types": ["sync_auto_expand"],
                            "shift_result": False,
                        },
                    }
                }
            )
        )
    pyxelrest._generator_config.SERVICES_CONFIGURATION_FILE_PATH = config_file_path
    from pyxelrest import _generator

    assert caplog.messages == [
        "Logging configuration file () cannot be found.",
        '"without_open_api_definition" will not be available: "without_open_api_definition" configuration section must provide "open_api" "definition".',
    ]

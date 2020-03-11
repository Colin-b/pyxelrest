import os
import timeit

import requests.adapters
import yaml
from requests import ReadTimeout

import pyxelrest


def test_service_can_be_loaded_without_hitting_timeout(monkeypatch, tmpdir):
    def timeout_send(*args, **kwargs):
        # Assert default timeout
        assert kwargs["timeout"] == (1, 5)
        raise ReadTimeout

    monkeypatch.setattr(requests.adapters.HTTPAdapter, "send", timeout_send)

    config_file_path = os.path.join(tmpdir, "test_config.yml")
    with open(config_file_path, "wt") as file:
        file.write(
            yaml.dump(
                {
                    "without_available_swagger": {
                        "open_api": {
                            "definition": "http://localhost:8950/swagger.json"
                        },
                        "udf": {
                            "return_types": ["sync_auto_expand"],
                            "shift_result": False,
                        },
                    }
                }
            )
        )
    pyxelrest.SERVICES_CONFIGURATION_FILE_PATH = config_file_path
    nb_seconds = timeit.timeit("from pyxelrest import _generator", number=1)
    assert nb_seconds < 3, "Time to load pyxelrest should be around timeout."

import os
import timeit
import time

import pytest
import yaml

import pyxelrest
from responses import RequestsMock


@pytest.fixture
def open_api_definition_not_responding_service(responses: RequestsMock):
    def reply_after_one_hour(request):
        # Do not respond to this call (simulate service down behind a reverse proxy)
        time.sleep(3600)

    responses.add_callback(
        responses.GET,
        url="http://localhost:8950/swagger.json",
        callback=reply_after_one_hour,
    )


def test_service_can_be_loaded_without_hitting_timeout(
    open_api_definition_not_responding_service, tmpdir
):
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
    nb_seconds = timeit.timeit("from pyxelrest import pyxelrestgenerator", number=1)
    assert nb_seconds < 8, "Time to load pyxelrest should be around timeout."

import logging

from tests import loader


def test_service_without_openapi_definition(tmpdir, caplog):
    caplog.set_level(logging.ERROR, logger="pyxelrest")
    loader.load(
        tmpdir,
        {
            "without_open_api_definition": {
                "udf": {
                    "return_types": ["sync_auto_expand"],
                    "shift_result": False,
                },
            }
        },
    )
    assert caplog.messages == [
        '"without_open_api_definition" will not be available: "without_open_api_definition" configuration section must provide "open_api" "definition".',
    ]

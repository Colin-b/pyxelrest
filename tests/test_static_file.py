from responses import RequestsMock

from testsutils import loader


def test_get_static_open_api_definition(responses: RequestsMock, tmpdir):
    pyxelrestgenerator = loader.load2(
        tmpdir,
        {
            "open_api_definition_loaded_from_file": {
                "open_api": {
                    "definition": "file://../testsutils/static_open_api_definition.json"
                },
                "udf": {"return_types": ["sync_auto_expand"], "shift_result": False},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://localhost:8954/sub/static/file/call",
        json={},
        match_querystring=True,
    )

    assert pyxelrestgenerator.open_api_definition_loaded_from_file_get_static_file_call() == [
        [""]
    ]

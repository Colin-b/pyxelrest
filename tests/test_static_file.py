from responses import RequestsMock

from testsutils import loader


def test_get_static_open_api_definition(responses: RequestsMock):
    pyxelrestgenerator = loader.load("static_file_service.yml")

    responses.add(
        responses.GET,
        url="http://localhost:8954/sub/static/file/call",
        json={},
        match_querystring=True,
    )

    assert pyxelrestgenerator.open_api_definition_loaded_from_file_get_static_file_call() == [
        [""]
    ]

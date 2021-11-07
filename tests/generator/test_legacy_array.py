from responses import RequestsMock

from tests import loader


def test_formula_prefix(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "responses": {200: {"description": "successful operation"}},
                    }
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "legacy": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"legacy_array": {"lock_excel": True}},
            }
        },
    )

    responses.add(
        responses.GET,
        url="http://test/test",
        json={},
        match_querystring=True,
    )
    assert generated_functions.legacy_legacy_get_test() == [[""]]

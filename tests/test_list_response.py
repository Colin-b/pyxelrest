from responses import RequestsMock

from tests import loader


def test_list_of_dict_with_list_response(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "type": "string",
                            }
                        },
                    }
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "list_response": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/test",
        json=[{"a": [1, 2, 3]}, {"b": [10, 20, 30]}, {"c": [100, 200, 300]}],
        match_querystring=True,
    )

    assert generated_functions.list_response_get_test() == [
        ["a", "b", "a", "b", "c", "c"],
        ["", 1],
        ["", 2],
        ["", 3],
        ["", "", 10],
        ["", "", 20, 100],
        ["", "", 30],
        ["", "", 200],
        ["", "", 300],
    ]

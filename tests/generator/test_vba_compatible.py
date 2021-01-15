from responses import RequestsMock

from tests import loader


def test_vba_prefixed_if_single_formula_type_is_vba_compatible(
    responses: RequestsMock, tmpdir
):
    responses.add(
        responses.GET,
        url="http://localhost:8951/",
        json={
            "swagger": "2.0",
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "get_header",
                        "responses": {
                            200: {
                                "description": "successful operation",
                                "schema": {"type": "string"},
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
            "vba_compat": {
                "open_api": {"definition": "http://localhost:8951/"},
                "formulas": {"vba_compatible": {}},
            }
        },
    )

    assert hasattr(generated_functions, "vba_vba_compat_get_header")

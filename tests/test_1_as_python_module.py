from requests import PreparedRequest
from responses import RequestsMock


def _get_request(responses: RequestsMock, url: str) -> PreparedRequest:
    for call in responses.calls:
        if call.request.url == url:
            # Pop out verified request (to be able to check multiple requests)
            responses.calls._calls.remove(call)
            return call.request


def test_raw_text_response(responses: RequestsMock):
    import pyxelrest

    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/text": {
                    "get": {
                        "operationId": "get_text",
                        "responses": {"200": {"description": "return value"}},
                    }
                }
            },
        },
        match_querystring=True,
    )

    pyxelrest.load(
        {
            "text_api": {
                "open_api": {"definition": "http://test/"},
            }
        }
    )
    responses.add(
        responses.GET,
        url="http://test/text",
        body=b"This is the content of the response.",
        match_querystring=True,
    )

    from pyxelrest.user_defined_functions import text_api

    assert text_api.get_text() == "This is the content of the response."

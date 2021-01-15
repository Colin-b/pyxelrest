import os.path

from requests import PreparedRequest
from responses import RequestsMock

from tests import loader


def _get_request(responses: RequestsMock, url: str) -> PreparedRequest:
    for call in responses.calls:
        if call.request.url == url:
            # Pop out verified request (to be able to check multiple requests)
            responses.calls._calls.remove(call)
            return call.request


def test_files_parameter(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://localhost:8959/",
        json={
            "swagger": "2.0",
            "paths": {
                "/files": {
                    "post": {
                        "operationId": "post_files",
                        "responses": {200: {"description": "successful operation"}},
                        "parameters": [
                            {
                                "name": "mandatory_file",
                                "required": True,
                                "in": "formData",
                                "type": "file",
                            },
                            {
                                "name": "optional_file",
                                "required": False,
                                "in": "formData",
                                "type": "file",
                            },
                        ],
                    }
                }
            },
            "consumes": ["application/x-www-form-urlencoded", "multipart/form-data"],
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "files": {
                "open_api": {"definition": "http://localhost:8959/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )

    with open(os.path.join(tmpdir, "temp_file"), "wb") as temp_file:
        temp_file.write(b"This is the content of the temporary file.")

    responses.add(
        responses.POST,
        url="http://localhost:8959/files",
        json={},
        match_querystring=True,
    )
    assert (
        generated_functions.files_post_files(
            mandatory_file="This is the content of the mandatory file.",
            optional_file=temp_file.name,
        )
        == [[""]]
    )
    actual_body = _get_request(responses, "http://localhost:8959/files").body
    assert (
        b'\r\nContent-Disposition: form-data; name="mandatory_file"; filename="mandatory_file"\r\n\r\nThis is the content of the mandatory file.\r\n'
        in actual_body
    )
    assert (
        b'\r\nContent-Disposition: form-data; name="optional_file"; filename="temp_file"\r\n\r\nThis is the content of the temporary file.\r\n'
        in actual_body
    )

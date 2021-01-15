import pytest
from responses import RequestsMock

from tests import loader


def test_without_responses(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {"/test": {"get": {}}},
        },
        match_querystring=True,
    )
    with pytest.raises(Exception) as exception_info:
        loader.load(
            tmpdir,
            {
                "no_responses": {
                    "open_api": {"definition": "http://test/"},
                    "formulas": {"dynamic_array": {"lock_excel": True}},
                }
            },
        )
    assert (
        str(exception_info.value)
        == 'Invalid Definition: At least one response must be specified for "no_responses_get_test".'
    )

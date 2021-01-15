import datetime

from dateutil.tz import tzutc
from responses import RequestsMock

from tests import loader


def test_get_date(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/date": {
                    "get": {
                        "operationId": "get_date",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {
                                    "type": "array",
                                    "items": {"type": "string", "format": "date"},
                                },
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
            "usual_parameters": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/date",
        json=["2014-03-05", "9999-01-01", "3001-01-01", "1970-01-01", "1900-01-01", ""],
        match_querystring=True,
    )

    assert generated_functions.usual_parameters_get_date() == [
        [datetime.datetime(2014, 3, 5, 0, 0)],
        [datetime.datetime(9999, 1, 1, 0, 0)],
        [datetime.datetime(3001, 1, 1, 0, 0)],
        [datetime.datetime(1970, 1, 1, 0, 0)],
        [datetime.datetime(1900, 1, 1, 0, 0)],
        [""],
    ]


def test_get_datetime(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/datetime": {
                    "get": {
                        "operationId": "get_date_time",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "schema": {
                                    "type": "array",
                                    "items": {"type": "string", "format": "date-time"},
                                },
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
            "usual_parameters": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/datetime",
        json=[
            "2014-03-05T15:59:58.20198Z",
            "2014-03-05T15:59:58.20198z",
            "2014-03-05 15:59:58.20198Z",
            "2014-03-05t15:59:58.20198Z",
            "2014-03-05t15:59:58.20198z",
            "9999-01-01T00:00:00+00:00",
            "3001-01-01T08:00:00+00:00",
            "1970-01-01T01:00:00+00:00",
            "1970-01-01T02:00:00+00:00",
            "",
        ],
        match_querystring=True,
    )

    assert generated_functions.usual_parameters_get_date_time() == [
        [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
        [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
        [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
        [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
        [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
        [datetime.datetime(9999, 1, 1, 0, 0, 0, 0, tzinfo=tzutc())],
        [datetime.datetime(3001, 1, 1, 8, 0, 0, 0, tzinfo=tzutc())],
        [datetime.datetime(1970, 1, 1, 1, 0, 0, 0, tzinfo=tzutc())],
        [datetime.datetime(1970, 1, 1, 2, 0, 0, 0, tzinfo=tzutc())],
        [""],
    ]


def test_get_datetime_encoding(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/datetime/encoding": {
                    "get": {
                        "operationId": "get_date_time_encoding",
                        "parameters": [
                            {
                                "description": "string parameter",
                                "in": "query",
                                "name": "encoded_date_time",
                                "required": True,
                                "type": "string",
                                "format": "date-time",
                            }
                        ],
                        "responses": {"200": {"description": "return value"}},
                    }
                }
            },
        },
        match_querystring=True,
    )
    generated_functions = loader.load(
        tmpdir,
        {
            "usual_parameters": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/datetime/encoding?encoded_date_time=2017-09-13T15:20:35",
        json={},
        match_querystring=True,
    )

    date_time = datetime.datetime.strptime("2017-09-13T15:20:35", "%Y-%m-%dT%H:%M:%S")
    assert generated_functions.usual_parameters_get_date_time_encoding(
        encoded_date_time=date_time
    ) == [[""]]

    responses.add(
        responses.GET,
        url="http://test/datetime/encoding?encoded_date_time=2017-09-13T15:20:00",
        json={},
        match_querystring=True,
    )
    date_time = datetime.datetime.strptime("2017-09-13T15:20", "%Y-%m-%dT%H:%M")
    assert generated_functions.usual_parameters_get_date_time_encoding(
        encoded_date_time=date_time
    ) == [[""]]

    responses.add(
        responses.GET,
        url="http://test/datetime/encoding?encoded_date_time=2017-09-13T15:00:00",
        json={},
        match_querystring=True,
    )
    date_time = datetime.datetime.strptime("2017-09-13 15", "%Y-%m-%d %H")
    assert generated_functions.usual_parameters_get_date_time_encoding(
        encoded_date_time=date_time
    ) == [[""]]


def test_get_date_with_invalid_format_in_definition(responses: RequestsMock, tmpdir):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/single_date": {
                    "get": {
                        "operationId": "get_single_date",
                        "responses": {
                            "200": {
                                "description": "return value",
                                "items": {"type": "string", "format": "date"},
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
            "usual_parameters": {
                "open_api": {"definition": "http://test/"},
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    responses.add(
        responses.GET,
        url="http://test/single_date",
        json="2014-03-05",
        match_querystring=True,
    )

    assert generated_functions.usual_parameters_get_single_date() == [
        [datetime.datetime(2014, 3, 5, 0, 0)],
    ]

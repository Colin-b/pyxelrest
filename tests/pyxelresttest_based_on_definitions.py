import datetime

from dateutil.tz import tzutc
import pytest
from responses import RequestsMock

from testsutils import serviceshandler, loader


@pytest.fixture
def services(responses: RequestsMock):
    from testsutils import (
        usual_parameters_service,
        filtered_tags_service,
        values_false_service,
        output_order_service,
        without_parameter_service,
        header_parameter_service,
        form_parameter_service,
        array_parameter_service,
    )

    serviceshandler.start_services(
        (usual_parameters_service, 8943),
        (filtered_tags_service, 8944),
        (values_false_service, 8945),
        (output_order_service, 8946),
        (without_parameter_service, 8950),
        (header_parameter_service, 8951),
        (form_parameter_service, 8952),
        (array_parameter_service, 8953),
    )
    loader.load("based_on_definitions_services.yml")
    yield 1
    serviceshandler.stop_services()


def test_string_multi_array_parameter(services):
    from pyxelrest import pyxelrestgenerator

    result = "string_array=\"['str1', 'str2']\""
    assert (
        pyxelrestgenerator.array_parameter_get_string_multi_array_parameter(
            ["str1", "str2"]
        )
        == result
    )


def test_string_default_array_parameter(services):
    from pyxelrest import pyxelrestgenerator

    result = "string_array=\"['str1,str2']\""
    assert (
        pyxelrestgenerator.array_parameter_get_string_default_array_parameter(
            ["str1", "str2"]
        )
        == result
    )


def test_string_csv_array_parameter(services):
    from pyxelrest import pyxelrestgenerator

    result = "string_array=\"['str1,str2']\""
    assert (
        pyxelrestgenerator.array_parameter_get_string_csv_array_parameter(
            ["str1", "str2"]
        )
        == result
    )


def test_string_ssv_array_parameter(services):
    from pyxelrest import pyxelrestgenerator

    result = "string_array=\"['str1 str2']\""
    assert (
        pyxelrestgenerator.array_parameter_get_string_ssv_array_parameter(
            ["str1", "str2"]
        )
        == result
    )


def test_string_tsv_array_parameter(services):
    from pyxelrest import pyxelrestgenerator

    result = "string_array=\"['str1\\tstr2']\""
    assert (
        pyxelrestgenerator.array_parameter_get_string_tsv_array_parameter(
            ["str1", "str2"]
        )
        == result
    )


def test_string_pipes_array_parameter(services):
    from pyxelrest import pyxelrestgenerator

    result = "string_array=\"['str1|str2']\""
    assert (
        pyxelrestgenerator.array_parameter_get_string_pipes_array_parameter(
            ["str1", "str2"]
        )
        == result
    )


def test_plain_text_without_parameter(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.without_parameter_get_plain_text_without_parameter()
        == "string value returned should be truncated so that the following information cannot be seen by user, because of the fact that Excel does not allow more than 255 characters in a cell. Only the 255 characters will be returned by the user defined functions:  "
    )


def test_post_without_parameter(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.without_parameter_post_without_parameter()
        == "POST performed properly"
    )


def test_put_without_parameter(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.without_parameter_put_without_parameter()
        == "PUT performed properly"
    )


def test_delete_without_parameter(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.without_parameter_delete_without_parameter()
        == "DELETE performed properly"
    )


def test_get_header_parameter(services):
    from pyxelrest import pyxelrestgenerator

    headers = pyxelrestgenerator.header_parameter_get_header("sent header")
    header_param_index = headers[0].index("Header-String")
    assert headers[1][header_param_index] == "sent header"


def test_post_form_parameter(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.form_parameter_post_form("sent string form data") == [
        ["form_string"],
        ["sent string form data"],
    ]


def test_get_with_tags(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        "Second tag is one of the accepted tags"
        == pyxelrestgenerator.filtered_tags_get_tags()
    )


def test_post_with_tags(services):
    from pyxelrest import pyxelrestgenerator

    assert "All tags are accepted" == pyxelrestgenerator.filtered_tags_post_tags()


def test_put_with_tags(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        "First tag is one of the accepted tags"
        == pyxelrestgenerator.filtered_tags_put_tags()
    )


def test_delete_with_tags(services):
    from pyxelrest import pyxelrestgenerator

    assert not hasattr(pyxelrestgenerator, "filtered_tags_delete_tags")


def test_get_with_zero_integer(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.values_false_get_with_zero_integer() == [
        ["zero_integer"],
        [0],
    ]


def test_get_with_zero_float(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.values_false_get_with_zero_float() == [
        ["zero_float"],
        [0.0],
    ]


def test_get_with_false_boolean(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.values_false_get_with_false_boolean() == [
        ["false_boolean"],
        [False],
    ]


def test_get_with_empty_string(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.values_false_get_with_empty_string() == [
        ["empty_string"],
        [""],
    ]


def test_get_with_empty_list(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.values_false_get_with_empty_list() == [""]


def test_get_with_empty_dictionary(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.values_false_get_with_empty_dictionary() == [""]


def test_get_compare_output_order(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.output_order_get_price_unordered() == [
        [u"ts", u"date", u"curve", u"mat"],
        [u"", datetime.datetime(2017, 4, 5, 0, 0), u"PW_FR", u"H01"],
        [u"2017-04-05 12:03:15", datetime.datetime(2017, 4, 5, 0, 0), u"PW_FR", u"H02"],
        [u"", datetime.datetime(2017, 4, 5, 0, 0), u"PW_FR", u"H03"],
    ]


def test_get_date(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.usual_parameters_get_date() == [
        [datetime.datetime(2014, 3, 5, 0, 0)],
        [datetime.datetime(9999, 1, 1, 0, 0)],
        [datetime.datetime(3001, 1, 1, 0, 0)],
        [datetime.datetime(1970, 1, 1, 0, 0)],
        [datetime.datetime(1900, 1, 1, 0, 0)],
    ]


def test_get_datetime(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.usual_parameters_get_date_time() == [
        [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
        [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
        [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
        [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
        [datetime.datetime(2014, 3, 5, 15, 59, 58, 201980, tzinfo=tzutc())],
        [datetime.datetime(9999, 1, 1, 0, 0, tzinfo=tzutc())],
        [datetime.datetime(3001, 1, 1, 8, 0, tzinfo=tzutc())],
        [datetime.datetime(1970, 1, 1, 1, 0, tzinfo=tzutc())],
        [datetime.datetime(1970, 1, 1, 2, 0, tzinfo=tzutc())],
    ]

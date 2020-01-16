import datetime
import os
import re

from dateutil.tz import tzutc
import pytest
from responses import RequestsMock

from testsutils import serviceshandler, loader


def support_pandas():
    try:
        import pandas

        return True
    except:
        return False


@pytest.fixture
def services(responses: RequestsMock):
    from testsutils import (
        usual_parameters_service,
        filtered_tags_service,
        values_false_service,
        output_order_service,
        open_api_definition_parsing_service,
        without_parameter_service,
        header_parameter_service,
        form_parameter_service,
        array_parameter_service,
        static_file_call_service,
        http_methods_service,
        content_type_service,
        base_path_ending_with_slash_service,
        async_service,
    )

    serviceshandler.start_services(
        (usual_parameters_service, 8943),
        (filtered_tags_service, 8944),
        (values_false_service, 8945),
        (output_order_service, 8946),
        (open_api_definition_parsing_service, 8948),
        (without_parameter_service, 8950),
        (header_parameter_service, 8951),
        (form_parameter_service, 8952),
        (array_parameter_service, 8953),
        (static_file_call_service, 8954),
        (http_methods_service, 8955),
        (content_type_service, 8956),
        (base_path_ending_with_slash_service, 8957),
        (async_service, 8958),
    )
    loader.load("services.yml")
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


def test_plain_without_parameter(services):
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


def test_service_without_sync_does_not_have_sync(services):
    from pyxelrest import pyxelrestgenerator

    with pytest.raises(AttributeError) as exception_info:
        pyxelrestgenerator.vba_without_parameter_delete_without_parameter()
    assert (
        str(exception_info.value)
        == "module 'pyxelrest.pyxelrestgenerator' has no attribute 'vba_without_parameter_delete_without_parameter'"
    )


def test_get_header_parameter(services):
    from pyxelrest import pyxelrestgenerator

    headers = pyxelrestgenerator.header_parameter_get_header("sent header")
    header_param_index = headers[0].index("Header-String")
    assert headers[1][header_param_index] == "sent header"


def test_get_header_parameter_sync(services):
    from pyxelrest import pyxelrestgenerator

    headers = pyxelrestgenerator.vba_header_parameter_get_header("sent header")
    header_param_index = headers[0].index("Header-String")
    assert headers[1][header_param_index] == "sent header"


def test_service_only_sync_does_not_have_vba_prefix(services):
    from pyxelrest import pyxelrestgenerator

    with pytest.raises(AttributeError) as exception_info:
        pyxelrestgenerator.vba_header_advanced_configuration_get_header("sent header")
    assert (
        str(exception_info.value)
        == "module 'pyxelrest.pyxelrestgenerator' has no attribute 'vba_header_advanced_configuration_get_header'"
    )


def test_get_header_advanced_configuration(services):
    from pyxelrest import pyxelrestgenerator

    headers = pyxelrestgenerator.header_advanced_configuration_get_header("sent header")

    custom_header_index = headers[0].index("X-Pxl-Custom")
    assert headers[1][custom_header_index] == "MyCustomValue"

    other_header_index = headers[0].index("X-Pxl-Other")
    assert headers[1][other_header_index] == "MyOtherValue"

    envvar_header_index = headers[0].index("X-Pxl-Envvar")
    assert headers[1][envvar_header_index] == os.environ["USERNAME"]

    request_header_index = headers[0].index("X-Pxl-Request")
    assert request_header_index

    session_header_index = headers[0].index("X-Pxl-Session")
    assert re.match(
        "\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d.\d\d\d\d\d\d",
        headers[1][session_header_index],
    )

    user_agent_index = headers[0].index("User-Agent")
    assert headers[1][user_agent_index] == "PyxelRest v0.69.0"

    cell_header_index = headers[0].index("X-Pxl-Cell")
    assert headers[1][cell_header_index] == "Python"


def test_post_form_parameter(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.form_parameter_post_form("sent string form data") == [
        ["form_string"],
        ["sent string form data"],
    ]


def test_get_with_selected_tags(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.selected_tags_get_tags()
        == "Second tag is one of the accepted tags"
    )


def test_post_with_selected_tags(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.selected_tags_post_tags() == "All tags are accepted"


def test_put_with_selected_tags(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.selected_tags_put_tags()
        == "First tag is one of the accepted tags"
    )


def test_delete_with_selected_tags(services):
    from pyxelrest import pyxelrestgenerator

    assert not hasattr(pyxelrestgenerator, "selected_tags_delete_tags")


def test_get_with_excluded_tags(services):
    from pyxelrest import pyxelrestgenerator

    assert not hasattr(pyxelrestgenerator, "excluded_tags_get_tags")


def test_post_with_excluded_tags(services):
    from pyxelrest import pyxelrestgenerator

    assert not hasattr(pyxelrestgenerator, "excluded_tags_post_tags")


def test_put_with_excluded_tags(services):
    from pyxelrest import pyxelrestgenerator

    assert not hasattr(pyxelrestgenerator, "excluded_tags_put_tags")


def test_delete_with_excluded_tags(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.excluded_tags_delete_tags()
        == "This method should not be available"
    )


def test_get_with_selected_operation_ids(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.selected_operation_ids_get_tags()
        == "Second tag is one of the accepted tags"
    )


def test_post_with_selected_operation_ids(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.selected_operation_ids_post_tags() == "All tags are accepted"
    )


def test_put_with_selected_operation_ids(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.selected_operation_ids_put_tags()
        == "First tag is one of the accepted tags"
    )


def test_delete_with_selected_operation_ids(services):
    from pyxelrest import pyxelrestgenerator

    assert not hasattr(pyxelrestgenerator, "selected_operation_ids_delete_tags")


def test_get_with_excluded_operation_ids(services):
    from pyxelrest import pyxelrestgenerator

    assert not hasattr(pyxelrestgenerator, "excluded_operation_ids_get_tags")


def test_post_with_excluded_operation_ids(services):
    from pyxelrest import pyxelrestgenerator

    assert not hasattr(pyxelrestgenerator, "excluded_operation_ids_post_tags")


def test_put_with_excluded_operation_ids(services):
    from pyxelrest import pyxelrestgenerator

    assert not hasattr(pyxelrestgenerator, "excluded_operation_ids_put_tags")


def test_delete_with_excluded_operation_ids(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.excluded_operation_ids_delete_tags()
        == "This method should not be available"
    )


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

    assert pyxelrestgenerator.values_false_get_with_empty_list() == [
        ["empty_list"],
        [""],
    ]


def test_get_with_empty_dictionary(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.values_false_get_with_empty_dictionary() == [
        ["empty_dictionary"],
        [""],
    ]


def test_get_compare_output_order(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.output_order_get_price_unordered() == [
        [u"curve", u"date", u"mat", u"ts"],
        [u"PW_FR", datetime.datetime(2017, 4, 5, 0, 0), u"H01", u""],
        [u"PW_FR", datetime.datetime(2017, 4, 5, 0, 0), u"H02", u"2017-04-05 12:03:15"],
        [u"PW_FR", datetime.datetime(2017, 4, 5, 0, 0), u"H03", u""],
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
        [datetime.datetime(9999, 1, 1, 0, 0, 0, 0, tzinfo=tzutc())],
        [datetime.datetime(3001, 1, 1, 8, 0, 0, 0, tzinfo=tzutc())],
        [datetime.datetime(1970, 1, 1, 1, 0, 0, 0, tzinfo=tzutc())],
        [datetime.datetime(1970, 1, 1, 2, 0, 0, 0, tzinfo=tzutc())],
    ]


def test_get_datetime_encoding(services):
    from pyxelrest import pyxelrestgenerator

    date_time = datetime.datetime.strptime("2017-09-13T15:20:35", "%Y-%m-%dT%H:%M:%S")
    assert (
        pyxelrestgenerator.usual_parameters_get_date_time_encoding(
            encoded_date_time=date_time
        )
        == "2017-09-13T15:20:35"
    )
    date_time = datetime.datetime.strptime("2017-09-13T15:20", "%Y-%m-%dT%H:%M")
    assert (
        pyxelrestgenerator.usual_parameters_get_date_time_encoding(
            encoded_date_time=date_time
        )
        == "2017-09-13T15:20:00"
    )
    date_time = datetime.datetime.strptime("2017-09-13 15", "%Y-%m-%d %H")
    assert (
        pyxelrestgenerator.usual_parameters_get_date_time_encoding(
            encoded_date_time=date_time
        )
        == "2017-09-13T15:00:00"
    )


def test_get_static_open_api_definition(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.open_api_definition_loaded_from_file_get_static_file_call()
        == "success"
    )


def test_get_http_method(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.http_methods_get_http_methods() == "GET"


def test_post_http_method(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.http_methods_post_http_methods() == "POST"


def test_put_http_method(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.http_methods_put_http_methods() == "PUT"


def test_delete_http_method(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.http_methods_delete_http_methods() == "DELETE"


def test_patch_http_method(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.http_methods_patch_http_methods() == "PATCH"


def test_options_http_method(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.http_methods_options_http_methods() == "OPTIONS"


def test_head_http_method(services):
    from pyxelrest import pyxelrestgenerator

    # HEAD is already handled by Flask
    assert pyxelrestgenerator.http_methods_head_http_methods() == ""


def test_msgpackpandas_content_type(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.content_type_get_msgpackpandas()
        == ["application/msgpackpandas"]
        if support_pandas()
        else ["*/*"]
    )


def test_json_content_type(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.content_type_get_json() == ["application/json"]


def test_missing_operation_id(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.operation_id_not_provided_get_without_operationId()
        == "/without_operationId called."
    )


def test_mixed_operation_id(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.operation_id_not_always_provided_get_without_operationId()
        == "/with_operationId called."
    )
    assert (
        pyxelrestgenerator.operation_id_not_always_provided_duplicated_get_without_operationId()
        == "/without_operationId called."
    )


def test_get_base_path_ending_with_slash(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.base_path_ending_with_slash_get_method()
        == "http://localhost:8957/method"
    )


def test_post_base_path_ending_with_slash(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.base_path_ending_with_slash_post_method()
        == "http://localhost:8957/method"
    )


def test_put_base_path_ending_with_slash(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.base_path_ending_with_slash_put_method()
        == "http://localhost:8957/method"
    )


def test_delete_base_path_ending_with_slash(services):
    from pyxelrest import pyxelrestgenerator

    assert (
        pyxelrestgenerator.base_path_ending_with_slash_delete_method()
        == "http://localhost:8957/method"
    )


def test_get_async_url(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.async_get_async() == [
        ["Status URL"],
        ["http://localhost:8958/async/status"],
    ]


def test_get_custom_url_sync(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.vba_pyxelrest_get_url(
        "http://localhost:8958/async/status",
        extra_headers=[
            ["X-Custom-Header1", "custom1"],
            ["X-Custom-Header2", "custom2"],
        ],
    ) == [["X-Custom-Header1", "X-Custom-Header2"], ["custom1", "custom2"]]


def test_get_custom_url(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.pyxelrest_get_url(
        "http://localhost:8958/async/status",
        extra_headers=[
            ["X-Custom-Header1", "custom1"],
            ["X-Custom-Header2", "custom2"],
        ],
    ) == [["X-Custom-Header1", "X-Custom-Header2"], ["custom1", "custom2"]]


def test_delete_custom_url_sync(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.vba_pyxelrest_delete_url(
        "http://localhost:8958/unlisted",
        extra_headers=[
            ["X-Custom-Header1", "custom1"],
            ["X-Custom-Header2", "custom2"],
        ],
    ) == [["X-Custom-Header1", "X-Custom-Header2"], ["custom1", "custom2"]]


def test_delete_custom_url(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.pyxelrest_delete_url(
        "http://localhost:8958/unlisted",
        extra_headers=[
            ["X-Custom-Header1", "custom1"],
            ["X-Custom-Header2", "custom2"],
        ],
    ) == [["X-Custom-Header1", "X-Custom-Header2"], ["custom1", "custom2"]]


def test_post_custom_url_dict(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.pyxelrest_post_url(
        "http://localhost:8958/dict",
        [["key1", "key2", "key3"], ["value1", 1, "value3"]],
        extra_headers=[["Content-Type", "application/json"]],
        parse_body_as="dict",
    ) == [["key1", "key2", "key3"], ["value1", 1, "value3"]]


def test_post_custom_url_dict_list_sync(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.vba_pyxelrest_post_url(
        "http://localhost:8958/dict",
        [["key1", "key2", "key3"], ["value1", 1, "value3"], ["other1", 2, "other3"]],
        extra_headers=[["Content-Type", "application/json"]],
        parse_body_as="dict_list",
    ) == [["key1", "key2", "key3"], ["value1", 1, "value3"], ["other1", 2, "other3"]]


def test_post_custom_url_dict_list(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.pyxelrest_post_url(
        "http://localhost:8958/dict",
        [["key1", "key2", "key3"], ["value1", 1, "value3"], ["other1", 2, "other3"]],
        extra_headers=[["Content-Type", "application/json"]],
        parse_body_as="dict_list",
    ) == [["key1", "key2", "key3"], ["value1", 1, "value3"], ["other1", 2, "other3"]]


def test_put_custom_url_dict_list(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.pyxelrest_put_url(
        "http://localhost:8958/dict",
        [["key1", "key2", "key3"], ["value1", 1, "value3"], ["other1", 2, "other3"]],
        extra_headers=[["Content-Type", "application/json"]],
        parse_body_as="dict_list",
    ) == [["key1", "key2", "key3"], ["value1", 1, "value3"], ["other1", 2, "other3"]]


def test_put_custom_url_dict(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.pyxelrest_put_url(
        "http://localhost:8958/dict",
        [["key1", "key2", "key3"], ["value1", 1, "value3"]],
        extra_headers=[["Content-Type", "application/json"]],
        parse_body_as="dict",
    ) == [["key1", "key2", "key3"], ["value1", 1, "value3"]]


def test_put_custom_url_dict_sync(services):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.vba_pyxelrest_put_url(
        "http://localhost:8958/dict",
        [["key1", "key2", "key3"], ["value1", 1, "value3"]],
        extra_headers=[["Content-Type", "application/json"]],
        parse_body_as="dict",
    ) == [["key1", "key2", "key3"], ["value1", 1, "value3"]]

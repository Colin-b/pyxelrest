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
def nested_data_service(responses: RequestsMock):
    import testsutils.nested_data_service as nested_data_service

    serviceshandler.start_services((nested_data_service, 8947))
    loader.load("nested_data_services.yml")
    yield 1
    serviceshandler.stop_services()


def test_get_dict_with_empty_nested_list(nested_data_service):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.nested_data_get_dict_with_empty_nested_list() == [
        [
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 3",
            "Column 3",
            "Column 3",
        ],
        ["0-0-1", "", "0-0-2 / 1-0-1", "", "", "", "", "0-0-2 / 1-0-3", "0-0-3"],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-0-1",
            "",
            "0-0-2 / 1-1-2 / 2-0-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-1-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
    ]


def test_get_dict_with_three_imbricated_levels(nested_data_service):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.nested_data_get_dict_with_three_imbricated_levels() == [
        [
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 3",
            "Column 3",
            "Column 3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-1-1",
            "",
            "0-0-2 / 1-0-2 / 2-1-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-0-1",
            "",
            "0-0-2 / 1-1-2 / 2-0-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-1-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
    ]


def test_get_dict_with_four_imbricated_levels(nested_data_service):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.nested_data_get_dict_with_four_imbricated_levels() == [
        [
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 3",
            "Column 3",
            "Column 3",
            "Column 3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-0-3",
            "0-0-2 / 1-0-2 / 2-0-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-1-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-1-3",
            "0-0-2 / 1-0-2 / 2-0-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-1-1",
            "",
            "",
            "",
            "",
            "0-0-2 / 1-0-2 / 2-1-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-0-1",
            "",
            "",
            "",
            "",
            "0-0-2 / 1-1-2 / 2-0-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-1-1",
            "",
            "",
            "",
            "",
            "0-0-2 / 1-1-2 / 2-1-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
    ]


def test_get_dict_with_multiple_imbricated_levels_and_duplicate_keys(
    nested_data_service,
):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.nested_data_get_dict_with_multiple_imbricated_levels_and_duplicate_keys() == [
        [
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 1",
            "Column 2",
            "Column 3",
            "Column 3",
            "Column 3",
            "Column 3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-0-3",
            "0-0-2 / 1-0-2 / 2-0-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-1-1",
            "",
            "0-0-2 / 1-0-2 / 2-0-2 / 3-1-3",
            "0-0-2 / 1-0-2 / 2-0-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-0-1",
            "",
            "0-0-2 / 1-0-2 / 2-1-1",
            "",
            "",
            "",
            "",
            "0-0-2 / 1-0-2 / 2-1-3",
            "0-0-2 / 1-0-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-0-1",
            "",
            "",
            "",
            "",
            "0-0-2 / 1-1-2 / 2-0-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
        [
            "0-0-1",
            "",
            "0-0-2 / 1-1-1",
            "",
            "0-0-2 / 1-1-2 / 2-1-1",
            "",
            "",
            "",
            "",
            "0-0-2 / 1-1-2 / 2-1-3",
            "0-0-2 / 1-1-3",
            "0-0-3",
        ],
    ]


def test_get_empty_dict(nested_data_service):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.nested_data_get_empty_dict() == [[""]]


def test_get_empty_list(nested_data_service):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.nested_data_get_empty_list() == [[""]]


def test_get_one_level_dict(nested_data_service):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.nested_data_get_one_level_dict() == [
        ["Column 2", "Column 3"],
        ["value 1", "value 2"],
    ]


def test_get_one_level_list(nested_data_service):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.nested_data_get_one_level_list() == [
        ["value 1"],
        ["value 2"],
    ]


def test_get_one_dict_entry_with_a_list(nested_data_service):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.nested_data_get_one_dict_entry_with_a_list() == [
        ["Column 1", "Column 1"],
        ["", "value 1"],
        ["", "value 2"],
    ]


def test_get_one_dict_entry_with_a_list_of_dict(nested_data_service):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.nested_data_get_one_dict_entry_with_a_list_of_dict() == [
        ["Column 1", "Column 2", "Column 3"],
        ["", "value 12", "value 13"],
        ["", "value 22", "value 23"],
    ]


def test_get_list_of_dict(nested_data_service):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.nested_data_get_list_of_dict() == [
        ["Column 2", "Column 3"],
        ["value 11", "value 12"],
        ["value 21", "value 22"],
    ]


def test_get_dict_with_list(nested_data_service):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.nested_data_get_dict_with_list() == [
        ["Column 1", "Column 2", "Column 3", "Column 3"],
        [23, True, "this", ""],
        [23, True, "is", ""],
        [23, True, "a", ""],
        [23, True, "test", ""],
    ]


def test_get_dict_with_list_of_different_size(nested_data_service):
    from pyxelrest import pyxelrestgenerator

    assert pyxelrestgenerator.nested_data_get_dict_with_list_of_different_size() == [
        ["Column 1", "Column 2", "Column 1", "Column 2", "Column 3", "Column 3"],
        ["", "", 23, 24, "value 1", ""],
        ["", "", "value 2", ""],
        ["", "", "value 3", ""],
    ]


def test_pandas_msgpack_default_encoding(nested_data_service):
    from pyxelrest import pyxelrestgenerator

    actual = pyxelrestgenerator.nested_data_get_pandas_msgpack_default_encoding()
    if support_pandas():
        from pandas import Timestamp

        expected = [
            ["col1", "col2_é&ç", u"col3_é&ç", "col4", "col5"],
            [
                "data11",
                "data12_é&ç",
                u"data13_é&ç",
                Timestamp("2017-12-26 01:02:03"),
                1.1,
            ],
            [
                "data21",
                "data22_é&ç",
                u"data23_é&ç",
                Timestamp("2017-12-27 01:02:03"),
                2.2,
            ],
        ]
    else:
        expected = "Pandas not installed"
    assert actual == expected

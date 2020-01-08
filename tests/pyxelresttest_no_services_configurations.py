import pytest

from testsutils import loader
import pyxelrest


def test_without_service_configuration_file():
    with pytest.raises(Exception) as exception_info:
        loader.load("non_existing.yml")
    assert (
        str(exception_info.value)
        == f'"{pyxelrest.SERVICES_CONFIGURATION_FILE_PATH}" configuration file cannot be read.'
    )

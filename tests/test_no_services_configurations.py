import os
from importlib import reload, import_module

import pytest

import pyxelrest


def test_without_service_configuration_file(tmpdir):
    pyxelrest.SERVICES_CONFIGURATION_FILE_PATH = os.path.join(
        tmpdir, "non_existing_file.yml"
    )
    with pytest.raises(Exception) as exception_info:
        reload(import_module("pyxelrest.pyxelrestgenerator"))
    assert (
        str(exception_info.value)
        == f'"{os.path.join(tmpdir, "non_existing_file.yml")}" configuration file cannot be read.'
    )

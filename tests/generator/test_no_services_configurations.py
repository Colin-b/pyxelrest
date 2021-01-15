import os
from importlib import reload, import_module

import pyxelrest._generator_config


def test_without_service_configuration_file(tmpdir):
    pyxelrest._generator_config.SERVICES_CONFIGURATION_FILE_PATH = os.path.join(
        tmpdir, "non_existing_file.yml"
    )
    reload(import_module("pyxelrest._generator"))

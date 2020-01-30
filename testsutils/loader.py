from importlib import import_module, reload
import os

import pyxelrest


def load(new_configuration_file_name: str):
    pyxelrest.SERVICES_CONFIGURATION_FILE_PATH = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), new_configuration_file_name
    )
    return reload(import_module("pyxelrest.pyxelrestgenerator"))

from importlib import import_module, reload
import os

import pyxelrest


def load(
    new_configuration_file_name,
    logging_configuration_file_name=None,
    load_pyxelrest=True,
):
    this_dir = os.path.abspath(os.path.dirname(__file__))
    pyxelrest.SERVICES_CONFIGURATION_FILE_PATH = os.path.join(
        this_dir, new_configuration_file_name
    )

    if logging_configuration_file_name:
        pyxelrest.LOGGING_CONFIGURATION_FILE_PATH = os.path.join(
            this_dir, logging_configuration_file_name
        )

    if load_pyxelrest:
        reload(import_module("pyxelrest.pyxelrestgenerator"))

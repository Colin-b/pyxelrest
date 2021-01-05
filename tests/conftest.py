from distutils import dir_util
import os.path

import pytest


@pytest.fixture
def clean_generated_functions():
    yield 1
    generated_folder = os.path.join(
        os.path.dirname(__file__), "..", "pyxelrest", "generated"
    )
    dir_util.remove_tree(generated_folder)

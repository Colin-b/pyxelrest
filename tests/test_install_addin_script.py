import os.path
import sys

import pyxelrest.install_addin


def test_xlwings_bas(tmpdir):
    created_file_path = pyxelrest.install_addin.create_xlwings_config(tmpdir)
    actual = open(created_file_path).read()
    actual = actual.replace(os.path.dirname(sys.executable), "test_python_path")
    assert (
        actual
        == open(
            os.path.join(os.path.dirname(__file__), "resources", "expected_xlwings.bas")
        ).read()
    )

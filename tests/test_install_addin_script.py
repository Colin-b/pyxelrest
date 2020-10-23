import os.path
import sys

import pyxelrest.install_addin


def test_xlwings_bas(tmpdir):
    conf = pyxelrest.install_addin.XlWingsConfig(tmpdir)
    conf.create_vb_addin()
    actual = open(os.path.join(tmpdir, "xlwings.bas")).read()
    actual = actual.replace(str(tmpdir), "test_config_path")
    assert actual == open(os.path.join(os.path.dirname(__file__), "resources", "expected_xlwings.bas")).read()


def test_xlwings_config(tmpdir):
    conf = pyxelrest.install_addin.XlWingsConfig(tmpdir)
    conf.create_file()
    actual = open(os.path.join(tmpdir, "xlwings.conf")).read()
    assert actual == f'"INTERPRETER", "{os.path.dirname(sys.executable)}\\pythonw.exe""UDF MODULES","pyxelrest._generator"'

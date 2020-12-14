import os.path
import subprocess
import sys
import winreg
from dataclasses import dataclass
from typing import List, Tuple

import pytest

import pyxelrest.install_addin


def fake_sub_processes(monkeypatch, calls: List[Tuple[List[str], int]]):
    def result_for_call(received: List[str]) -> int:
        for call, result in calls:
            if call == received:
                return result
        return -1

    monkeypatch.setattr(subprocess, "call", result_for_call)


@pytest.fixture
def fake_registry(monkeypatch):
    keys = {}

    @dataclass
    class FakeRegistryKey:
        entries = {}

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            return

        def set(self, value_name, reserved, type, value):
            self.entries[value_name] = (reserved, type, value)

        def __eq__(self, other):
            if isinstance(other, dict):
                return other == self.entries

    monkeypatch.setattr(
        winreg,
        "CreateKey",
        lambda section, key: keys.setdefault((section, key), FakeRegistryKey()),
    )
    monkeypatch.setattr(
        winreg,
        "SetValueEx",
        lambda key, value_name, reserved, type, value: key.set(
            value_name, reserved, type, value
        ),
    )
    return keys


def test_success(fake_registry, monkeypatch, tmpdir):
    # TODO Fake VSTO Installer path

    fake_sub_processes(
        monkeypatch,
        [
            (
                [
                    r"C:\Program Files\Common Files\microsoft shared\VSTO\10.0\VSTOInstaller.exe",
                    "/Install",
                    os.path.join(
                        tmpdir, "destination", "excel_addin", "PyxelRestAddIn.vsto"
                    ),
                ],
                0,
            ),
        ],
    )
    root = os.path.dirname(os.path.dirname(__file__))
    pyxelrest.install_addin.main(
        "--trusted_location",
        os.path.join(tmpdir, "trusted"),
        "--source",
        os.path.join(root, "addin", "PyxelRestAddIn", "bin", "Release"),
        "--vb_addin",
        os.path.join(root, "addin", "pyxelrest.xlam"),
        "--destination",
        os.path.join(tmpdir, "destination"),
    )
    assert fake_registry == {
        (
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest",
        ): {
            "InstallLocation": (0, winreg.REG_SZ, os.path.join(tmpdir, "destination")),
        }
    }
    assert_resource(
        os.path.join(tmpdir, "destination", "configuration", "logging.yml"),
        "expected_logging.yml",
        replace={os.path.join(tmpdir, "destination").encode(): b"test_destination"},
    )
    assert_content(
        os.path.join(tmpdir, "trusted", "pyxelrest.xlam"),
        os.path.join(root, "addin", "pyxelrest.xlam"),
    )
    assert_content(
        os.path.join(tmpdir, "destination", "excel_addin", "PyxelRestAddIn.vsto"),
        os.path.join(
            root, "addin", "PyxelRestAddIn", "bin", "Release", "PyxelRestAddIn.vsto"
        ),
    )
    assert_resource(
        os.path.join(tmpdir, "destination", "excel_addin", "PyxelRestAddIn.dll.config"),
        "expected_PyxelRestAddIn.dll.config",
        replace={
            os.path.dirname(sys.executable).encode(): b"test_python_path",
            os.path.join(tmpdir, "destination").encode(): b"test_destination",
        },
    )
    assert_resource(
        os.path.join(tmpdir, "destination", "excel_addin", "xlwings.bas"),
        "expected_xlwings.bas",
        replace={os.path.dirname(sys.executable).encode(): b"test_python_path"},
    )


def test_success_with_pre_release(fake_registry, monkeypatch, tmpdir):
    # TODO Fake VSTO Installer path

    fake_sub_processes(
        monkeypatch,
        [
            (
                [
                    r"C:\Program Files\Common Files\microsoft shared\VSTO\10.0\VSTOInstaller.exe",
                    "/Install",
                    os.path.join(
                        tmpdir, "destination", "excel_addin", "PyxelRestAddIn.vsto"
                    ),
                ],
                0,
            ),
        ],
    )
    root = os.path.dirname(os.path.dirname(__file__))
    pyxelrest.install_addin.main(
        "--trusted_location",
        os.path.join(tmpdir, "trusted"),
        "--source",
        os.path.join(root, "addin", "PyxelRestAddIn", "bin", "Release"),
        "--vb_addin",
        os.path.join(root, "addin", "pyxelrest.xlam"),
        "--destination",
        os.path.join(tmpdir, "destination"),
        "--check_pre_releases",
    )
    assert fake_registry == {
        (
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest",
        ): {
            "InstallLocation": (0, winreg.REG_SZ, os.path.join(tmpdir, "destination")),
        }
    }
    assert_resource(
        os.path.join(tmpdir, "destination", "configuration", "logging.yml"),
        "expected_logging.yml",
        replace={os.path.join(tmpdir, "destination").encode(): b"test_destination"},
    )
    assert_content(
        os.path.join(tmpdir, "trusted", "pyxelrest.xlam"),
        os.path.join(root, "addin", "pyxelrest.xlam"),
    )
    assert_content(
        os.path.join(tmpdir, "destination", "excel_addin", "PyxelRestAddIn.vsto"),
        os.path.join(
            root, "addin", "PyxelRestAddIn", "bin", "Release", "PyxelRestAddIn.vsto"
        ),
    )
    assert_resource(
        os.path.join(tmpdir, "destination", "excel_addin", "PyxelRestAddIn.dll.config"),
        "expected_prerelease_PyxelRestAddIn.dll.config",
        replace={
            os.path.dirname(sys.executable).encode(): b"test_python_path",
            os.path.join(tmpdir, "destination").encode(): b"test_destination",
        },
    )
    assert_resource(
        os.path.join(tmpdir, "destination", "excel_addin", "xlwings.bas"),
        "expected_xlwings.bas",
        replace={os.path.dirname(sys.executable).encode(): b"test_python_path"},
    )


def assert_resource(file_path: str, resource: str, replace: dict = None):
    assert_content(
        file_path,
        os.path.join(os.path.dirname(__file__), "resources", resource),
        replace,
    )


def assert_content(file_path: str, expected_file_path: str, replace: dict = None):
    with open(file_path, "rb") as file:
        actual = file.read()

    for previous, new in (replace or {}).items():
        actual = actual.replace(previous, new)

    expected = open(expected_file_path, "rb").read()
    assert actual == expected

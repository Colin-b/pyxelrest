import os.path
import subprocess
import sys
import winreg
from dataclasses import dataclass
from typing import List, Tuple

import pytest

import pyxelrest.install_addin


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
    fake_sub_processes(
        monkeypatch,
        addin_installation(
            installer_path=r"C:\Program Files\Common Files\microsoft shared\VSTO\10.0\VSTOInstaller.exe",
            install_location=os.path.join(tmpdir, "destination"),
            return_code=0,
        ),
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
    assert_registry(fake_registry, install_location=os.path.join(tmpdir, "destination"))
    assert_logging_conf(install_location=os.path.join(tmpdir, "destination"))
    assert_vb_addin(
        vb_source=os.path.join(root, "addin"),
        trusted_location=os.path.join(tmpdir, "trusted"),
    )
    assert_addin(
        source=os.path.join(root, "addin", "PyxelRestAddIn", "bin", "Release"),
        install_location=os.path.join(tmpdir, "destination"),
    )
    assert_addin_config(
        "expected_PyxelRestAddIn.dll.config",
        install_location=os.path.join(tmpdir, "destination"),
    )
    assert_xlwings_bas(install_location=os.path.join(tmpdir, "destination"))


def test_success_with_pre_release(fake_registry, monkeypatch, tmpdir):
    fake_sub_processes(
        monkeypatch,
        addin_installation(
            installer_path=r"C:\Program Files\Common Files\microsoft shared\VSTO\10.0\VSTOInstaller.exe",
            install_location=os.path.join(tmpdir, "destination"),
            return_code=0,
        ),
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
    assert_registry(fake_registry, install_location=os.path.join(tmpdir, "destination"))
    assert_logging_conf(install_location=os.path.join(tmpdir, "destination"))
    assert_vb_addin(
        vb_source=os.path.join(root, "addin"),
        trusted_location=os.path.join(tmpdir, "trusted"),
    )
    assert_addin(
        source=os.path.join(root, "addin", "PyxelRestAddIn", "bin", "Release"),
        install_location=os.path.join(tmpdir, "destination"),
    )
    assert_addin_config(
        "expected_prerelease_PyxelRestAddIn.dll.config",
        install_location=os.path.join(tmpdir, "destination"),
    )
    assert_xlwings_bas(install_location=os.path.join(tmpdir, "destination"))


def fake_sub_processes(monkeypatch, *calls: Tuple[List[str], int]):
    def result_for_call(received: List[str]) -> int:
        for call, result in calls:
            if call == received:
                return result
        return -1

    monkeypatch.setattr(subprocess, "call", result_for_call)


def addin_installation(
    installer_path: str, install_location: str, return_code: int
) -> Tuple[List[str], int]:
    return (
        [
            installer_path,
            "/Install",
            os.path.join(install_location, "excel_addin", "PyxelRestAddIn.vsto"),
        ],
        return_code,
    )


def assert_logging_conf(install_location: str):
    assert_resource(
        os.path.join(install_location, "configuration", "logging.yml"),
        "expected_logging.yml",
        replace={install_location.encode(): b"test_destination"},
    )


def assert_vb_addin(vb_source: str, trusted_location: str):
    assert_content(
        os.path.join(trusted_location, "pyxelrest.xlam"),
        os.path.join(vb_source, "pyxelrest.xlam"),
    )


def assert_addin(source: str, install_location: str):
    assert_content(
        os.path.join(install_location, "excel_addin", "PyxelRestAddIn.vsto"),
        os.path.join(source, "PyxelRestAddIn.vsto"),
    )


def assert_addin_config(expected: str, install_location: str):
    assert_resource(
        os.path.join(install_location, "excel_addin", "PyxelRestAddIn.dll.config"),
        expected,
        replace={
            os.path.dirname(sys.executable).encode(): b"test_python_path",
            install_location.encode(): b"test_destination",
        },
    )


def assert_registry(fake_registry, install_location: str):
    assert fake_registry == {
        (
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest",
        ): {
            "InstallLocation": (0, winreg.REG_SZ, install_location),
        }
    }


def assert_xlwings_bas(install_location: str):
    assert_resource(
        os.path.join(install_location, "excel_addin", "xlwings.bas"),
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

import os.path
import subprocess
import sys
import winreg
from dataclasses import dataclass
from typing import List, Tuple, Dict

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


def redirect_paths(monkeypatch, redirects: Dict[str, str]):
    original = os.path.join

    def redirect(*args) -> str:
        original_path = original(*args)
        return redirects.get(original_path, original_path)

    monkeypatch.setattr(os.path, "join", redirect)


def fake_vsto_installer(tmpdir, monkeypatch) -> str:
    vsto_installer_path = os.path.join(tmpdir, "existing.exe")
    with open(vsto_installer_path, "wb") as file:
        file.write(b"")
    redirect_paths(
        monkeypatch,
        {
            r"C:\Program Files\Common Files\microsoft shared\VSTO\10.0\VSTOInstaller.exe": vsto_installer_path,
        },
    )
    return vsto_installer_path


def test_success(fake_registry, monkeypatch, tmpdir):
    vsto_installer_path = fake_vsto_installer(tmpdir, monkeypatch)
    fake_sub_processes(
        monkeypatch,
        clear_clickonce_cache(return_code=-1),
        silent_addin_installation(
            installer_path=vsto_installer_path,
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
    vsto_installer_path = fake_vsto_installer(tmpdir, monkeypatch)
    fake_sub_processes(
        monkeypatch,
        clear_clickonce_cache(return_code=-1),
        silent_addin_installation(
            installer_path=vsto_installer_path,
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


def test_success_with_uptodate_configuration(fake_registry, monkeypatch, tmpdir):
    vsto_installer_path = fake_vsto_installer(tmpdir, monkeypatch)
    fake_sub_processes(
        monkeypatch,
        clear_clickonce_cache(return_code=-1),
        silent_addin_installation(
            installer_path=vsto_installer_path,
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
        "--path_to_up_to_date_configuration",
        "https://location_of_configurations",
    )
    assert_registry(
        fake_registry,
        install_location=os.path.join(tmpdir, "destination"),
        path_to_up_to_date_configurations="https://location_of_configurations",
    )
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


def test_success_default_source(fake_registry, monkeypatch, tmpdir):
    vsto_installer_path = fake_vsto_installer(tmpdir, monkeypatch)
    fake_sub_processes(
        monkeypatch,
        clear_clickonce_cache(return_code=-1),
        silent_addin_installation(
            installer_path=vsto_installer_path,
            install_location=os.path.join(tmpdir, "destination"),
            return_code=0,
        ),
    )
    root = os.path.dirname(os.path.dirname(__file__))
    pyxelrest.install_addin.main(
        "--trusted_location",
        os.path.join(tmpdir, "trusted"),
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


def test_non_silent_installation(fake_registry, monkeypatch, tmpdir):
    vsto_installer_path = fake_vsto_installer(tmpdir, monkeypatch)
    fake_sub_processes(
        monkeypatch,
        clear_clickonce_cache(return_code=-1),
        silent_addin_installation(
            installer_path=vsto_installer_path,
            install_location=os.path.join(tmpdir, "destination"),
            return_code=-1,
        ),
        addin_installation(
            installer_path=vsto_installer_path,
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


def test_update(fake_registry, monkeypatch, tmpdir):
    vsto_installer_path = fake_vsto_installer(tmpdir, monkeypatch)
    fake_sub_processes(
        monkeypatch,
        silent_addin_uninstallation(
            installer_path=vsto_installer_path,
            install_location=os.path.join(tmpdir, "destination"),
            return_code=0,
        ),
        clear_clickonce_cache(return_code=-1),
        silent_addin_installation(
            installer_path=vsto_installer_path,
            install_location=os.path.join(tmpdir, "destination"),
            return_code=0,
        ),
    )
    # Create a fake add-in to simulate that it was already installed
    os.makedirs(os.path.join(tmpdir, "destination", "excel_addin"))
    with open(
        os.path.join(tmpdir, "destination", "excel_addin", "PyxelRestAddIn.vsto"), "wb"
    ) as file:
        file.write(b"")

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


def test_non_silent_uninstallation(fake_registry, monkeypatch, tmpdir):
    vsto_installer_path = fake_vsto_installer(tmpdir, monkeypatch)
    fake_sub_processes(
        monkeypatch,
        silent_addin_uninstallation(
            installer_path=vsto_installer_path,
            install_location=os.path.join(tmpdir, "destination"),
            return_code=-1,
        ),
        addin_uninstallation(
            installer_path=vsto_installer_path,
            install_location=os.path.join(tmpdir, "destination"),
            return_code=0,
        ),
        clear_clickonce_cache(return_code=-1),
        silent_addin_installation(
            installer_path=vsto_installer_path,
            install_location=os.path.join(tmpdir, "destination"),
            return_code=0,
        ),
    )
    # Create a fake add-in to simulate that it was already installed
    os.makedirs(os.path.join(tmpdir, "destination", "excel_addin"))
    with open(
        os.path.join(tmpdir, "destination", "excel_addin", "PyxelRestAddIn.vsto"), "wb"
    ) as file:
        file.write(b"")

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


def test_source_not_existing(fake_registry, monkeypatch, tmpdir):
    with pytest.raises(Exception) as exception_info:
        pyxelrest.install_addin.main(
            "--source",
            os.path.join(tmpdir, "non_existing"),
        )
    assert (
        str(exception_info.value)
        == f"PyxelRest Microsoft Excel add-in source folder cannot be found in {os.path.join(tmpdir, 'non_existing')}."
    )


def test_vb_addin_source_not_existing(fake_registry, monkeypatch, tmpdir):
    os.makedirs(os.path.join(tmpdir, "empty"))
    with pytest.raises(Exception) as exception_info:
        pyxelrest.install_addin.main(
            "--source",
            os.path.join(tmpdir, "empty"),
        )
    assert (
        str(exception_info.value)
        == f"Visual Basic PyxelRest Excel Add-In cannot be found in {os.path.join(tmpdir, 'empty', 'pyxelrest.xlam')}."
    )


def test_vsto_does_not_exists(fake_registry, monkeypatch, tmpdir):
    # Create empty source dir (missing VSTO)
    os.makedirs(os.path.join(tmpdir, "source"))
    root = os.path.dirname(os.path.dirname(__file__))
    with pytest.raises(Exception) as exception_info:
        pyxelrest.install_addin.main(
            "--trusted_location",
            os.path.join(tmpdir, "trusted"),
            "--source",
            os.path.join(tmpdir, "source"),
            "--vb_addin",
            os.path.join(root, "addin", "pyxelrest.xlam"),
            "--destination",
            os.path.join(tmpdir, "destination"),
        )
    assert (
        str(exception_info.value)
        == f'PyxelRest Microsoft Excel add-in cannot be found in {os.path.join(tmpdir, "destination", "excel_addin", "PyxelRestAddIn.vsto")}.'
    )


@pytest.fixture
def remove_xlwings_bas(tmpdir):
    import xlwings
    import shutil

    xlwings_path = xlwings.__path__[0]
    original = os.path.join(xlwings_path, "xlwings.bas")
    shutil.move(original, os.path.join(tmpdir, "original_xlwings.bas"))
    yield original
    shutil.copyfile(os.path.join(tmpdir, "original_xlwings.bas"), original)


def test_xlwings_bas_does_not_exists(
    fake_registry, monkeypatch, tmpdir, remove_xlwings_bas
):
    vsto_installer_path = fake_vsto_installer(tmpdir, monkeypatch)
    fake_sub_processes(
        monkeypatch,
        clear_clickonce_cache(return_code=-1),
        silent_addin_installation(
            installer_path=vsto_installer_path,
            install_location=os.path.join(tmpdir, "destination"),
            return_code=0,
        ),
    )
    root = os.path.dirname(os.path.dirname(__file__))
    with pytest.raises(Exception) as exception_info:
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
    assert (
        str(exception_info.value)
        == f"XLWings BAS file cannot be found in {remove_xlwings_bas}"
    )


@pytest.fixture
def remove_pythonw_executable(tmpdir):
    import shutil

    python_path = os.path.dirname(sys.executable)
    original = os.path.join(python_path, "pythonw.exe")
    shutil.move(original, os.path.join(tmpdir, "original_pythonw.exe"))
    yield original
    shutil.copyfile(os.path.join(tmpdir, "original_pythonw.exe"), original)


def test_pythonw_executable_does_not_exists(
    fake_registry, monkeypatch, tmpdir, remove_pythonw_executable
):
    vsto_installer_path = fake_vsto_installer(tmpdir, monkeypatch)
    fake_sub_processes(
        monkeypatch,
        clear_clickonce_cache(return_code=-1),
        silent_addin_installation(
            installer_path=vsto_installer_path,
            install_location=os.path.join(tmpdir, "destination"),
            return_code=0,
        ),
    )
    root = os.path.dirname(os.path.dirname(__file__))
    with pytest.raises(Exception) as exception_info:
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
    assert (
        str(exception_info.value)
        == f"Python executable cannot be found in {remove_pythonw_executable}"
    )


def test_vsto_installer_x86(fake_registry, monkeypatch, tmpdir):
    vsto_installer_path = os.path.join(tmpdir, "existing.exe")
    with open(vsto_installer_path, "wb") as file:
        file.write(b"")
    redirect_paths(
        monkeypatch,
        {
            r"C:\Program Files\Common Files\microsoft shared\VSTO\10.0\VSTOInstaller.exe": os.path.join(
                tmpdir, "non_existing.exe"
            ),
            r"C:\Program Files (x86)\Common Files\microsoft shared\VSTO\10.0\VSTOInstaller.exe": vsto_installer_path,
        },
    )
    fake_sub_processes(
        monkeypatch,
        clear_clickonce_cache(return_code=-1),
        silent_addin_installation(
            installer_path=vsto_installer_path,
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


def test_vsto_installer_not_existing(fake_registry, monkeypatch, tmpdir):
    redirect_paths(
        monkeypatch,
        {
            r"C:\Program Files\Common Files\microsoft shared\VSTO\10.0\VSTOInstaller.exe": os.path.join(
                tmpdir, "non_existing.exe"
            ),
            r"C:\Program Files (x86)\Common Files\microsoft shared\VSTO\10.0\VSTOInstaller.exe": os.path.join(
                tmpdir, "non_existing.exe"
            ),
        },
    )
    root = os.path.dirname(os.path.dirname(__file__))
    with pytest.raises(Exception) as exception_info:
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
    assert (
        str(exception_info.value)
        == f'PyxelRest Microsoft Excel add-in cannot be installed as VSTO installer cannot be found in {os.path.join(tmpdir, "non_existing.exe")}.'
    )


def fake_sub_processes(monkeypatch, *calls: Tuple[List[str], int]) -> list:
    remaining_calls = list(calls)

    def result_for_call(received: List[str]) -> int:
        for call, result in calls:
            if call == received:
                remaining_calls.remove((call, result))
                return result
        raise Exception(f"Missing mock for {received}")

    monkeypatch.setattr(subprocess, "call", result_for_call)
    return remaining_calls


def clear_clickonce_cache(return_code: int):
    return (["rundll32", "dfshim", "CleanOnlineAppCache"], return_code)


def silent_addin_installation(
    installer_path: str, install_location: str, return_code: int
) -> Tuple[List[str], int]:
    return (
        [
            installer_path,
            "/Silent",
            "/Install",
            os.path.join(install_location, "excel_addin", "PyxelRestAddIn.vsto"),
        ],
        return_code,
    )


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


def silent_addin_uninstallation(
    installer_path: str, install_location: str, return_code: int
) -> Tuple[List[str], int]:
    return (
        [
            installer_path,
            "/Silent",
            "/Uninstall",
            os.path.join(install_location, "excel_addin", "PyxelRestAddIn.vsto"),
        ],
        return_code,
    )


def addin_uninstallation(
    installer_path: str, install_location: str, return_code: int
) -> Tuple[List[str], int]:
    return (
        [
            installer_path,
            "/Uninstall",
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


def assert_registry(
    fake_registry, install_location: str, path_to_up_to_date_configurations: str = None
):
    entries = {
        "InstallLocation": (0, winreg.REG_SZ, install_location),
    }
    if path_to_up_to_date_configurations:
        entries["PathToUpToDateConfigurations"] = (
            0,
            winreg.REG_SZ,
            path_to_up_to_date_configurations,
        )
    assert fake_registry == {
        (
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest",
        ): entries
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

import winreg
from distutils import dir_util
import os.path
from typing import Dict, Tuple

import pytest


@pytest.fixture
def clean_generated_functions():
    yield 1
    generated_folder = os.path.join(
        os.path.dirname(__file__), "..", "pyxelrest", "generated"
    )
    dir_util.remove_tree(generated_folder)


class FakeRegistryKey:
    def __init__(self):
        self.entries = {}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return

    def set(self, value_name, reserved, typ, value):
        self.entries[value_name] = (reserved, typ, value)

    def get(self, value_name):
        reserved, typ, value = self.entries[value_name]
        return value, None

    def __eq__(self, other):
        if isinstance(other, dict):
            return other == self.entries

    def __repr__(self):
        return repr(self.entries)


@pytest.fixture
def fake_registry(monkeypatch) -> Dict[Tuple[int, str], FakeRegistryKey]:
    keys = {}

    def create_key(section: int, key: str) -> FakeRegistryKey:
        return keys.setdefault((section, key), FakeRegistryKey())

    def open_key(section: int, key: str) -> FakeRegistryKey:
        registry_key = keys.get((section, key))
        if not registry_key:
            raise FileNotFoundError
        return registry_key

    monkeypatch.setattr(
        winreg,
        "CreateKey",
        create_key,
    )
    monkeypatch.setattr(
        winreg,
        "OpenKey",
        open_key,
    )
    monkeypatch.setattr(
        winreg,
        "SetValueEx",
        lambda key, value_name, reserved, typ, value: key.set(
            value_name, reserved, typ, value
        ),
    )
    monkeypatch.setattr(
        winreg,
        "QueryValueEx",
        lambda key, value_name: key.get(value_name),
    )
    return keys


@pytest.fixture
def fake_install_location(fake_registry, tmpdir) -> str:
    location = os.path.join(tmpdir, "install_location")
    os.makedirs(location)

    registry_key = FakeRegistryKey()
    registry_key.set("InstallLocation", 0, winreg.REG_SZ, location)

    fake_registry[
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest",
    ] = registry_key

    return location

import os
import winreg
from typing import Optional


def get_registry_key(key: str) -> Optional[str]:
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest") as pyxelrest_registry_key:
            value, _ = winreg.QueryValueEx(pyxelrest_registry_key, key)
        return value
    except FileNotFoundError:
        return


SERVICES_CONFIGURATION_FILE_PATH = ""
LOGGING_CONFIGURATION_FILE_PATH = ""
TOKEN_CACHE_FILE_PATH = ""

install_location = get_registry_key("InstallLocation") or ""

if install_location:
    SERVICES_CONFIGURATION_FILE_PATH = os.path.join(
        install_location, "configuration", "services.yml"
    )
    LOGGING_CONFIGURATION_FILE_PATH = os.path.join(
        install_location, "configuration", "logging.yml"
    )
    TOKEN_CACHE_FILE_PATH = os.path.join(
        install_location, "tokens.json"
    )

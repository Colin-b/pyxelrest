import os
import winreg
from typing import Optional


def get_registry_key(key: str) -> Optional[str]:
    try:
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest",
        ) as pyxelrest_registry_key:
            value, _ = winreg.QueryValueEx(pyxelrest_registry_key, key)
        return value
    except FileNotFoundError:
        return


install_location = get_registry_key("InstallLocation")

SERVICES_CONFIGURATION_FILE_PATH = (
    os.path.join(install_location, "configuration", "services.yml")
    if install_location
    else ""
)
LOGGING_CONFIGURATION_FILE_PATH = (
    os.path.join(install_location, "configuration", "logging.yml")
    if install_location
    else ""
)
TOKEN_CACHE_FILE_PATH = (
    os.path.join(install_location, "tokens.json") if install_location else ""
)

import os

SERVICES_CONFIGURATION_FILE_PATH = os.path.join(
    os.getenv("APPDATA"), "pyxelrest", "configuration", "services.yml"
)
LOGGING_CONFIGURATION_FILE_PATH = os.path.join(
    os.getenv("APPDATA"), "pyxelrest", "configuration", "logging.yml"
)
TOKEN_CACHE_FILE_PATH = os.path.join(
    os.getenv("APPDATA"), "pyxelrest", "configuration", "tokens.json"
)

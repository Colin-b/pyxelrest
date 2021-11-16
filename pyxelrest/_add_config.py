import argparse
import logging
import os
from typing import Optional

import requests
import yaml

if __name__ == "__main__":
    logger = logging.getLogger("pyxelrest._add_config")
else:
    logger = logging.getLogger(__name__)


def open_file_config(configuration_file_path: str) -> Optional[dict]:
    if not os.path.isfile(configuration_file_path):
        return {}

    try:
        with open(configuration_file_path, "r") as config_file:
            return yaml.load(config_file, Loader=yaml.FullLoader)
    except Exception as e:
        logger.exception(
            f'Configuration file "{configuration_file_path}" cannot be read: {e}.'
        )


def open_url_config(configuration_file_url: str) -> Optional[dict]:
    try:
        response = requests.get(configuration_file_url)
        response.raise_for_status()
        return yaml.load(response.text, Loader=yaml.SafeLoader)
    except requests.HTTPError as e:
        logger.warning(
            f'Configuration file URL "{configuration_file_url}" cannot be reached: {e}.'
        )
    except Exception as e:
        logger.exception(
            f'Configuration file retrieved from URL "{configuration_file_url}" cannot be loaded: {e}'
        )


class ServicesConfigUpdater:
    def __init__(self, config_file_path: str):
        """

        :param config_file_path: The path to the configuration to update.
        :raise Exception: In case services configuration file located into config_file_path cannot be opened.
        """
        self._config_file_path = config_file_path
        self._user_config = open_file_config(self._config_file_path)
        if self._user_config is None:
            raise Exception("Services configuration cannot be opened.")

    def update_configuration(self, source_url: str):
        """

        :param source_url: URL to a configuration file.
        """
        logger.info("Updating services configuration...")

        source_config = open_url_config(source_url)
        if source_config is None:
            logger.error("Services configuration cannot be updated.")
            return

        for name, settings in source_config.items():
            self._user_config[name] = settings
            logger.info(f'"{name}" configuration added.')

        self._save_configuration()
        logger.info("Services configuration updated.")

    def _save_configuration(self):
        config_folder_path = os.path.dirname(self._config_file_path)
        if not os.path.exists(config_folder_path):
            os.makedirs(config_folder_path)
        with open(self._config_file_path, "w") as file:
            yaml.dump(self._user_config, file, default_flow_style=False)


def main(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "config_to_update",
        help="File path of the configuration file to update.",
        type=str,
    )
    parser.add_argument(
        "source",
        help="URL to the configuration to add.",
        type=str,
    )
    options = parser.parse_args(args if args else None)
    try:
        installer = ServicesConfigUpdater(config_file_path=options.config_to_update)
        installer.update_configuration(options.source)
    except:
        logger.exception("Unable to add services configuration.")


if __name__ == "__main__":
    main()

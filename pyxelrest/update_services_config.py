import argparse
import logging
import os
from typing import Optional, List

import requests
import yaml

if __name__ == "__main__":
    logger = logging.getLogger("pyxelrest.update_services_config")
else:
    logger = logging.getLogger(__name__)

# Below are the values for the action option
ADD_SECTIONS = "add"  # Provided configuration(s) will be appended (updated if section is already existing)
UPDATE_SECTIONS = "update"  # Provided configuration(s) will be updated (if section is already existing)
REMOVE_SECTIONS = (
    "remove"  # Provided configuration(s) will be removed (only based on section name)
)
LIST_SECTIONS = (
    "list"  # Provided configuration(s) will be listed (section name and description)
)


def open_config(source: str) -> Optional[dict]:
    """
    Open provided services configuration.

    :param source: Can be a file path, a path to a directory or an URL to a file content.
    :return loaded configuration or None if it was unable to be loaded.
    """
    if os.path.isfile(source) or os.path.isdir(source):
        return open_file_config(source)
    return open_url_config(source)


def open_file_config(file_or_directory: str) -> Optional[dict]:
    try:
        loaded_yaml = {}
        config_file_names = to_file_paths(file_or_directory)
        for config_file_name in config_file_names:
            with open(config_file_name, "r") as config_file:
                loaded_yaml.update(yaml.load(config_file, Loader=yaml.FullLoader))
        return loaded_yaml
    except:
        logger.exception(f'Configuration files "{file_or_directory}" cannot be read.')


def open_url_config(configuration_file_url: str) -> Optional[dict]:
    try:
        response = requests.get(configuration_file_url)
        response.raise_for_status()
        return yaml.load(response.text, Loader=yaml.FullLoader)
    except requests.HTTPError as e:
        logger.warning(
            f'Configuration file URL "{configuration_file_url}" cannot be reached: {e}.'
        )
    except requests.exceptions.InvalidSchema:
        # Consider that this is a file path that does not exists yet
        return {}
    except:
        logger.exception(
            f'Configuration file URL "{configuration_file_url}" cannot be reached.'
        )


def to_absolute_path(file_path: str) -> str:
    return file_path if os.path.isabs(file_path) else os.path.abspath(file_path)


def to_file_paths(file_or_directory: str) -> List[str]:
    if os.path.isfile(file_or_directory):
        return [to_absolute_path(file_or_directory)]

    if not os.path.isdir(file_or_directory):
        raise Exception(f'Invalid path "{file_or_directory}" provided.')

    directory_files = []
    for file in os.listdir(file_or_directory):
        file_path = to_absolute_path(os.path.join(file_or_directory, file))
        if os.path.isfile(file_path):
            directory_files.append(file_path)
        else:
            logger.warning(f'"{file_path}" is not a file and will be skipped.')
    return directory_files


class ServicesConfigUpdater:
    def __init__(self, action: str, config_file_path: str):
        """

        :param action: Valid value amongst ADD_SECTIONS, UPDATE_SECTIONS or REMOVE_SECTIONS
        :param config_file_path: The path to the configuration to update.
        :raise Exception: In case services configuration file located into config_file_path cannot be opened.
        """
        self._config_file_path = config_file_path
        self._user_config = open_config(self._config_file_path)
        if self._user_config is None:
            raise Exception("Services configuration cannot be opened.")
        self._action = action

    def update_configuration(self, source: str, services: List[str] = None):
        """

        :param source: Absolute or relative path to a configuration file
        or a directory or an URL to a file containing configuration file(s).
        :param services: List of service names to be affected.
        """
        if LIST_SECTIONS != self._action:
            logger.info("Updating services configuration...")

        source_config = open_config(source)
        if source_config is None:
            logger.error("Services configuration cannot be updated.")
            return

        for service_name, service_config in source_config.items():
            if services and service_name not in services:
                continue

            if ADD_SECTIONS == self._action:
                self._add_service(service_name, service_config)
            elif UPDATE_SECTIONS == self._action:
                self._update_service(service_name, service_config)
            elif REMOVE_SECTIONS == self._action:
                self._remove_service(service_name)
            elif LIST_SECTIONS == self._action:
                self._print_service(service_name, service_config)

        if LIST_SECTIONS != self._action:
            self._save_configuration()
            logger.info("Services configuration updated.")

    def _save_configuration(self):
        config_folder_path = os.path.dirname(self._config_file_path)
        if not os.path.exists(config_folder_path):
            os.makedirs(config_folder_path)
        with open(self._config_file_path, "w") as file:
            yaml.dump(self._user_config, file, default_flow_style=False)

    def _add_service(self, service_name: str, updated_config: dict):
        self._user_config[service_name] = updated_config
        logger.info(f'"{service_name}" configuration added.')

    def _update_service(self, service_name: str, updated_config: dict):
        if service_name not in self._user_config:
            logger.debug(
                f"User does not have the {service_name} section in configuration. Nothing to update."
            )
            return

        skip_update = updated_config.get("skip_update_for", [])
        previous_config = self._user_config[service_name]
        # Add up to date fields
        self._user_config[service_name] = {
            key: value
            for key, value in updated_config.items()
            if key not in skip_update
        }
        # Add non updated fields
        self._user_config[service_name].update(
            {key: value for key, value in previous_config.items() if key in skip_update}
        )
        logger.info(f'"{service_name}" configuration updated.')

    def _remove_service(self, service_name: str):
        if self._user_config.pop(service_name):
            logger.info(f'"{service_name}" configuration removed.')

    def _print_service(self, service_name: str, updated_config: dict):
        if "description" in updated_config:
            print(f"{service_name} - {updated_config.get('description')}")
        else:
            print(service_name)


def main(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "config_to_update",
        help="File path of the configuration file to update.",
        type=str,
    )
    parser.add_argument(
        "source",
        help="File (path or URL) or directory (path) containing services configuration.",
        type=str,
    )
    parser.add_argument(
        "action",
        help="Action to perform with provided file(s).",
        type=str,
        choices=[ADD_SECTIONS, UPDATE_SECTIONS, REMOVE_SECTIONS, LIST_SECTIONS],
    )
    parser.add_argument(
        "--services",
        help="Subset of services to be affected by the action.",
        default=None,
        type=str,
        nargs="*",
    )
    options = parser.parse_args(args if args else None)
    try:
        installer = ServicesConfigUpdater(action=options.action, config_file_path=options.config_to_update)
        installer.update_configuration(options.source, options.services)
    except:
        logger.exception("Unable to perform services configuration update.")


if __name__ == "__main__":
    main()

import argparse
import sys
import os
import logging
try:
    # Python 3
    from configparser import ConfigParser
except ImportError:
    # Python 2
    from ConfigParser import ConfigParser

if __name__ == '__main__':
    logger = logging.getLogger("pyxelrest.pyxelrest_update_services_config")
else:
    logger = logging.getLogger(__name__)

_USER_CONFIG_FILE_PATH = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'services.ini')

# Below are the values for the action option
ADD_SECTIONS = 'add'  # Provided configuration(s) will be appended (updated if section is already existing)
UPDATE_SECTIONS = 'update'  # Provided configuration(s) will be updated (if section is already existing)
REMOVE_SECTIONS = 'remove'  # Provided configuration(s) will be removed (only based on section name)


def open_config(config_file_names):
    config_parser = ConfigParser(interpolation=None)
    if not config_parser.read(config_file_names):
        logger.warning('Configuration files "{0}" cannot be read.'.format(config_file_names))
        return None
    return config_parser


def to_absolute_path(file_path):
    return file_path if os.path.isabs(file_path) else os.path.abspath(file_path)


def to_file_paths(file_or_directory):
    if os.path.isfile(file_or_directory):
        return to_absolute_path(file_or_directory)

    if not os.path.isdir(file_or_directory):
        raise Exception('Invalid path "{}" provided.'.format(file_or_directory))

    directory_files = []
    for file in os.listdir(file_or_directory):
        file_path = to_absolute_path(os.path.join(file_or_directory, file))
        if os.path.isfile(file_path):
            directory_files.append(file_path)
        else:
            logger.warning('"{0}" is not a file and will be skipped.'.format(file_path))
    return directory_files


class ServicesConfigUpdater:

    def __init__(self, file_or_directory, action):
        """

        :param file_or_directory: Absolute or relative path to a configuration file
        or a directory containing configuration file(s).
        :param action: Valid value amongst ADD_SECTIONS, UPDATE_SECTIONS or REMOVE_SECTIONS
        :raise Exception: In case services configuration file located into _USER_CONFIG_FILE_PATH cannot be opened.
        """
        self._user_config = open_config(_USER_CONFIG_FILE_PATH)
        if not self._user_config:
            raise Exception('Services configuration cannot be opened.')
        self.files = to_file_paths(file_or_directory)
        self._action = action

    def update_configuration(self):
        logger.info('Updating services configuration...')
        updated_config = open_config(self.files)
        if not updated_config:
            logger.error('Services configuration cannot be updated.')
            return

        for service_name in updated_config.sections():
            if ADD_SECTIONS == self._action:
                self._add_service(service_name, updated_config)
            if UPDATE_SECTIONS == self._action:
                self._update_service(service_name, updated_config)
            if REMOVE_SECTIONS == self._action:
                self._remove_service(service_name)

        self._save_configuration()
        logger.info('Services configuration updated.')

    def _save_configuration(self):
        with open(_USER_CONFIG_FILE_PATH, 'w') as file:
            self._user_config.write(file)

    def _add_service(self, service_name, updated_config):
        # Update section content in case it already exists
        if self._user_config.has_section(service_name):
            self._user_config.remove_section(service_name)

        self._user_config.add_section(service_name)
        for updated_key, updated_value in updated_config.items(service_name):
            self._user_config.set(service_name, updated_key, updated_value)
        logger.info('"{0}" configuration added.'.format(service_name))

    def _update_service(self, service_name, updated_config):
        if not self._user_config.has_section(service_name):
            logger.debug('User does not have the {0} section in configuration. Nothing to update.'.format(service_name))
            return

        self._user_config.remove_section(service_name)
        self._user_config.add_section(service_name)
        for updated_key, updated_value in updated_config.items(service_name):
            self._user_config.set(service_name, updated_key, updated_value)
        logger.info('"{0}" configuration updated.'.format(service_name))

    def _remove_service(self, service_name):
        if self._user_config.has_section(service_name):
            self._user_config.remove_section(service_name)
            logger.info('"{0}" configuration removed.'.format(service_name))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_or_directory', help='File or directory containing services configuration.', type=str)
    parser.add_argument('action', help='Action to perform with provided file(s).', type=str, choices=[
        ADD_SECTIONS, UPDATE_SECTIONS, REMOVE_SECTIONS])
    options = parser.parse_args(sys.argv[1:])

    try:
        installer = ServicesConfigUpdater(options.file_or_directory, options.action)
        installer.update_configuration()
    except:
        logger.exception('Unable to perform services configuration update.')

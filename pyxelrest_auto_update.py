import argparse
import win32con
import win32ui
import win32com.client
import os
import time
import sys
import yaml
import logging
import logging.config
import logging.handlers
from pip.commands.list import ListCommand
from pip.commands.install import InstallCommand
from pip.utils import get_installed_distributions


def create_logger():
    global default_log_file_path
    global logger
    if __name__ == '__main__':
        logger = logging.getLogger("pyxelrest.pyxelrest_auto_update")
    else:
        logger = logging.getLogger(__name__)

    logging_configuration_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration',
                                                   'auto_update_logging.ini')
    default_log_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'logs', 'pyxelrest_auto_update.log')
    if os.path.isfile(logging_configuration_file_path):
        with open(logging_configuration_file_path, 'r') as config_file:
            log_config_dict = yaml.load(config_file)
            logging.config.dictConfig(log_config_dict)
    else:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
                            handlers=[logging.handlers.TimedRotatingFileHandler(default_log_file_path, when='D')],
                            level=logging.DEBUG)
        logger.warning('Logging configuration file ({0}) cannot be found. Using default logging configuration.'.format(
            logging_configuration_file_path))


create_logger()


def _outdated_package():
    """Faster outdated check when running it for a single package."""
    list_command = ListCommand()
    command_options, _ = list_command.parse_args([])
    packages = list_command.get_outdated([_pyxelrest_package()], command_options)
    return packages[0] if packages else None


def _pyxelrest_package():
    # Break from the loop in order to retrieve it faster in huge environments
    for package in get_installed_distributions():
        if package.project_name == 'pyxelrest':
            return package


def _update_is_finished():
    update_is_in_progress = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'update_is_in_progress')
    os.remove(update_is_in_progress)


class PyxelRestUpdater:
    def __init__(self, path_to_up_to_date_configurations=None):
        self.path_to_up_to_date_configurations = path_to_up_to_date_configurations

    def check_update(self):
        if self._is_already_updating():
            logger.debug('Skip update check as another update is ongoing.')
            return

        logger.debug('Checking if an update is available...')
        if self._is_update_available():
            logger.info('Update {0} available (from {1}).'.format(self.pyxelrest_package.latest_version, self.pyxelrest_package.version))
            if self._want_update():
                logger.debug('Update accepted. Waiting for Microsoft Excel to close...')
                # If Microsoft Excel is running, user might still use pyxelrest, do not update yet
                while self._is_excel_running():
                    # As closing Microsoft Excel is a manual user action, wait for 1 second between each check.
                    time.sleep(1)
                logger.debug('Microsoft Excel is closed. Installing update.')
                self._update_pyxelrest()
            else:
                logger.info('Update rejected.')
        else:
            logger.debug('No update available.')

    def _is_update_available(self):
        self.pyxelrest_package = _outdated_package()
        return self.pyxelrest_package

    def _is_already_updating(self):
        update_is_in_progress = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'update_is_in_progress')
        if os.path.isfile(update_is_in_progress):
            return True
        # Create file if this is the first update (most cases)
        with open(update_is_in_progress, 'w'):
            return False

    def _want_update(self):
        msg = "PyxelRest {0} is available. Do you want to install it now?\n" \
              "Update will be installed when Microsoft Excel will be closed.".format(self.pyxelrest_package.latest_version)
        return win32ui.MessageBox(msg, "PyxelRest update available", win32con.MB_YESNO) == win32con.IDYES

    def _is_excel_running(self):
        processes = win32com.client.GetObject('winmgmts:').InstancesOf('Win32_Process')
        for process in processes:
            if process.Properties_('Name').Value == 'EXCEL.EXE':
                return True
        return False

    def _update_pyxelrest(self):
        result = InstallCommand().main(['pyxelrest', '--upgrade', '--log', default_log_file_path])
        create_logger()  # PyxelRest logger is lost while trying to update
        if result == 0:
            logger.info('PyxelRest package updated.')
            if self._update_addin():
                # Only perform configuration update when we are sure that latest version is installed
                self._update_configuration()
        else:
            logger.warning('PyxelRest package update failed.')

    def _update_addin(self):
        try:
            # This script is always in the same folder as the add-in update script
            from pyxelrest_install_addin import Installer

            scripts_dir = os.path.abspath(os.path.dirname(__file__))
            data_dir = os.path.join(scripts_dir, '..')
            addin_installer = Installer(os.path.join(data_dir, 'pyxelrest_addin'),
                                        os.path.join(data_dir, 'pyxelrest_vb_addin'),
                                        path_to_up_to_date_configuration=self.path_to_up_to_date_configurations)
            addin_installer.perform_post_installation_tasks()
            logger.info('Microsoft Excel add-in successfully updated.')
            return True
        except:
            logger.exception('Unable to update add-in.')

    def _update_configuration(self):
        if not self.path_to_up_to_date_configurations:
            logger.info('Services configuration will not be updated.')
            return

        try:
            # This script is always in the same folder as the configuration update script
            from pyxelrest_update_services_config import ServicesConfigUpdater, UPDATE_SECTIONS

            config_updater = ServicesConfigUpdater(UPDATE_SECTIONS)
            config_updater.update_configuration(self.path_to_up_to_date_configurations)
            logger.info('Services configuration successfully updated.')
        except:
            logger.exception('Unable to update configuration.')


if __name__ == '__main__':
    logger.debug('Starting auto update script...')
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_to_up_to_date_configurations',
                        help='File (path or URL) or directory (path) containing up to date services configuration.',
                        default=None,
                        type=str)
    options = parser.parse_args(sys.argv[1:])
    try:
        updater = PyxelRestUpdater(options.path_to_up_to_date_configurations)
        updater.check_update()
    except:
        logger.exception('An error occurred while checking for update.')
        raise
    finally:
        _update_is_finished()

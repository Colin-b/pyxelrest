import argparse
import win32con
import win32ui
import win32com.client
import subprocess
import os
import time
import sys
import yaml
import logging
import logging.config
import logging.handlers

if __name__ == '__main__':
    logger = logging.getLogger("pyxelrest.pyxelrest_auto_update")
else:
    logger = logging.getLogger(__name__)

logging_configuration_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration',
                                               'auto_update_logging.ini')
if os.path.isfile(logging_configuration_file_path):
    with open(logging_configuration_file_path, 'r') as config_file:
        log_config_dict = yaml.load(config_file)
        logging.config.dictConfig(log_config_dict)
else:
    default_log_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'logs', 'pyxelrest_auto_update.log')
    logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
                        handlers=[logging.handlers.TimedRotatingFileHandler(default_log_file_path, when='D')],
                        level=logging.DEBUG)
    logger.warning('Logging configuration file ({0}) cannot be found. Using default logging configuration.'.format(
        logging_configuration_file_path))


class PyxelRestUpdater:
    def __init__(self, pip_path):
        if not os.path.isfile(pip_path):
            raise Exception('PIP executable cannot be found at {0}.'.format(pip_path))
        self._pip_path = pip_path

    def check_update(self):
        if self._is_already_updating():
            logger.debug('Skip update check as another update is ongoing.')
            return

        logger.debug('Checking if an update is available...')
        if self._is_update_available():
            logger.info('Update available.')
            if self._want_update():
                logger.debug('Update accepted. Waiting for Microsoft Excel to close...')
                while self._is_excel_running():
                    # As closing Microsoft Excel is a manual user action, wait for 1 second between each check.
                    time.sleep(1)
                logger.debug('Microsoft Excel is closed. Installing update.')
                self._update_pyxelrest()
            else:
                logger.info('Update rejected.')
        else:
            logger.debug('No update available.')
        self._update_is_finished()

    def _is_update_available(self):
        outdated_packages = subprocess.check_output([self._pip_path, 'list', '--outdated'])
        return 'pyxelrest' in str(outdated_packages)

    def _update_is_finished(self):
        update_is_in_progress = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'update_is_in_progress')
        os.remove(update_is_in_progress)

    def _is_already_updating(self):
        update_is_in_progress = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'update_is_in_progress')
        if os.path.isfile(update_is_in_progress):
            return True
        # Create file if this is the first update (most cases)
        with open(update_is_in_progress, 'w'):
            return False

    def _want_update(self):
        return win32ui.MessageBox("A PyxelRest update is available. Do you want to install it now?\n"
                                  "Update will be installed when Microsoft Excel will be closed.",
                                  "PyxelRest update available",
                                  win32con.MB_YESNO) == win32con.IDYES

    def _is_excel_running(self):
        processes = win32com.client.GetObject('winmgmts:').InstancesOf('Win32_Process')
        for process in processes:
            if process.Properties_('Name').Value == 'EXCEL.EXE':
                return True
        return False

    def _update_pyxelrest(self):
        update_result = subprocess.check_output([self._pip_path, 'install', 'pyxelrest', '--upgrade'])
        logger.info(str(update_result))
        # TODO This step will be removed as well as the auto-update feature as soon as infra will provide an installer
        self._update_addin()

    def _update_addin(self):
        try:
            # This script is always in the same folder as the add-in update script
            from pyxelrest_install_addin import Installer

            scripts_dir = os.path.abspath(os.path.dirname(__file__))
            data_dir = os.path.join(scripts_dir, '..')
            addin_installer = Installer(os.path.join(data_dir, 'pyxelrest_addin'),
                                        os.path.join(data_dir, 'pyxelrest_vb_addin'))
            addin_installer.perform_post_installation_tasks()
            logger.info('Microsoft Excel add-in successfully updated.')
        except:
            logger.exception('Unable to update add-in.')


if __name__ == '__main__':
    logger.debug('Starting auto update script...')
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_pip', help='Path to PIP where PyxelRest is already installed.', type=str)
    options = parser.parse_args(sys.argv[1:])
    try:
        PyxelRestUpdater(options.path_to_pip).check_update()
    except:
        logger.exception('An error occurred while checking for update.')
        raise

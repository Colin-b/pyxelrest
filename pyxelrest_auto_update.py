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
    logging.warning('Logging configuration file ({0}) cannot be found. Using default logging configuration.'.format(
        logging_configuration_file_path))


class PyxelRestUpdater:
    def __init__(self, pip_path):
        if not os.path.isfile(pip_path):
            raise Exception('PIP executable cannot be found at {0}.'.format(pip_path))
        self._pip_path = pip_path

    def check_update(self):
        logging.debug('Checking if an update is available...')
        if self._is_update_available():
            logging.info('Update available.')
            if self._want_update():
                logging.debug('Update accepted. Waiting for Microsoft Excel to close...')
                while self._is_excel_running():
                    # As closing Microsoft Excel is a manual user action, wait for 1 second between each check.
                    time.sleep(1)
                logging.debug('Microsoft Excel is closed. Installing update.')
                self._end_logging()
                self._update_pyxelrest()
            else:
                logging.info('Update rejected.')
        else:
            logging.debug('No update available.')

    def _is_update_available(self):
        outdated_packages = subprocess.check_output([self._pip_path, 'list', '--outdated'])
        return 'pyxelrest' in str(outdated_packages)

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
        subprocess.call([self._pip_path, 'install', 'pyxelrest', '--upgrade'])

    def _end_logging(self):
        for handler in logging.getLogger().handlers[:]:
            handler.close()


if __name__ == '__main__':
    logging.debug('Starting auto update script...')
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_pip', help='Path to PIP where PyxelRest is already installed.', type=str)
    options = parser.parse_args(sys.argv[1:])
    try:
        PyxelRestUpdater(options.path_to_pip).check_update()
    except:
        logging.exception('An error occurred while checking for update.')
        raise

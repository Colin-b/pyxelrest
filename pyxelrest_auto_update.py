import argparse
import win32con
import win32ui
import win32com.client
import subprocess
import os
import time
import sys


class PyxelRestUpdater:
    def __init__(self, pip_path):
        if not os.path.isfile(pip_path):
            raise Exception('PIP executable cannot be found at {0}.'.format(pip_path))
        self._pip_path = pip_path

    def check_update(self):
        if self._is_update_available():
            if self._want_update():
                while self._is_excel_running():
                    # As closing Microsoft Excel is a manual user action, wait for 1 second between each check.
                    time.sleep(1)
                self._update_pyxelrest()

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_to_pip', help='Path to PIP where PyxelRest is already installed.', type=str)
    options = parser.parse_args(sys.argv[1:])
    PyxelRestUpdater(options.path_to_pip).check_update()

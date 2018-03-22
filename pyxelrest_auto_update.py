import argparse
import win32con
import win32ui
import win32com.client
import multiprocessing
import os
import os.path
import time
import sys
import yaml
import pywintypes
import logging
import logging.config
import logging.handlers
from pip.commands.list import ListCommand
from pip.commands.install import InstallCommand
from pip.utils import get_installed_distributions

try:
    # Python 3
    import tkinter
except ImportError:
    # Python 2
    import Tkinter as tkinter


CLOSING_EXCEL_STEP = 'Closing Microsoft Excel'
PYTHON_STEP = 'PyxelRest package'
EXCEL_STEP = 'Microsoft Excel add-in'
SETTINGS_STEP = 'Services configuration'
END_STEP = 'End of update'

IN_PROGRESS = 'in progress'
DONE = 'done'
FAILURE = 'failure'

IMAGE_NAMES = {
    PYTHON_STEP: 'python_logo_greyscale_100.png',
    '{0}_{1}'.format(PYTHON_STEP, DONE): 'python_logo_100.png',
    '{0}_{1}'.format(PYTHON_STEP, FAILURE): 'python_logo_error_100.png',

    EXCEL_STEP: 'excel_logo_greyscale_100.png',
    '{0}_{1}'.format(EXCEL_STEP, DONE): 'excel_logo_100.png',
    '{0}_{1}'.format(EXCEL_STEP, FAILURE): 'excel_logo_error_100.png',

    SETTINGS_STEP: 'settings_logo_greyscale_100.png',
    '{0}_{1}'.format(SETTINGS_STEP, DONE): 'settings_logo_100.png',
    '{0}_{1}'.format(SETTINGS_STEP, FAILURE): 'settings_logo_error_100.png',
}


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


class UpdateProcess:
    def __init__(self, path_to_up_to_date_configurations, updating_queue):
        self.path_to_up_to_date_configurations = path_to_up_to_date_configurations
        self.updating_queue = updating_queue

    def start_update(self):
        logger.debug('Update accepted. Waiting for Microsoft Excel to close...')
        self.updating_queue.put((CLOSING_EXCEL_STEP, IN_PROGRESS))
        # If Microsoft Excel is running, user might still use pyxelrest, do not update yet
        while self._is_excel_running():
            # As closing Microsoft Excel is a manual user action, wait for 1 second between each check.
            time.sleep(1)
        logger.debug('Microsoft Excel is closed. Installing update.')
        self.updating_queue.put((CLOSING_EXCEL_STEP, DONE))
        self._update_pyxelrest()
        self.updating_queue.put((END_STEP, DONE))

    def _is_excel_running(self):
        try:
            processes = win32com.client.GetObject('winmgmts:').InstancesOf('Win32_Process')
            for process in processes:
                if process.Properties_('Name').Value == 'EXCEL.EXE':
                    return True
            return False
        except:
            logger.exception('Unable to retrieve Microsoft Excel process list. Considering as closed.')
            return False

    def _update_pyxelrest(self):
        self.updating_queue.put((PYTHON_STEP, IN_PROGRESS))
        result = InstallCommand().main(['pyxelrest', '--upgrade', '--log', default_log_file_path])
        create_logger()  # PyxelRest logger is lost while trying to update
        if result == 0:
            self.updating_queue.put((PYTHON_STEP, DONE))
            logger.info('PyxelRest package updated.')
            if self._update_addin():
                # Only perform configuration update when we are sure that latest version is installed
                self._update_configuration()
        else:
            logger.warning('PyxelRest package update failed.')
            self.updating_queue.put((PYTHON_STEP, FAILURE))

    def _update_addin(self):
        self.updating_queue.put((EXCEL_STEP, IN_PROGRESS))
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
            self.updating_queue.put((EXCEL_STEP, DONE))
            return True
        except:
            logger.exception('Unable to update add-in.')
            self.updating_queue.put((EXCEL_STEP, FAILURE))

    def _update_configuration(self):
        if not self.path_to_up_to_date_configurations:
            logger.info('Services configuration will not be updated.')
            return

        self.updating_queue.put((SETTINGS_STEP, IN_PROGRESS))
        try:
            # This script is always in the same folder as the configuration update script
            from pyxelrest_update_services_config import ServicesConfigUpdater, UPDATE_SECTIONS

            config_updater = ServicesConfigUpdater(UPDATE_SECTIONS)
            config_updater.update_configuration(self.path_to_up_to_date_configurations)
            logger.info('Services configuration successfully updated.')
            self.updating_queue.put((SETTINGS_STEP, DONE))
        except:
            logger.exception('Unable to update configuration.')
            self.updating_queue.put((SETTINGS_STEP, FAILURE))


def _start_update_process(path_to_up_to_date_configurations, updating_queue):
    UpdateProcess(path_to_up_to_date_configurations, updating_queue).start_update()


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
            self.start_update_gui()
        else:
            logger.debug('No update available.')

    def start_update_gui(self):
        root = tkinter.Tk()
        root.title = "PyxelRest update available"
        root.wm_title = "PyxelRest update available"
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        root.resizable(width=False, height=False)
        updating_queue = multiprocessing.JoinableQueue()
        updating_process = multiprocessing.Process(target=_start_update_process, args=(self.path_to_up_to_date_configurations, updating_queue))
        app = UpdateGUI(root, updating_process, updating_queue, self.pyxelrest_package.latest_version)
        root.mainloop()

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


class UpdateGUI(tkinter.Frame):

    def __init__(self, master, updating_thread, updating_queue, new_version):
        tkinter.Frame.__init__(self, master)
        master.protocol("WM_DELETE_WINDOW", self.on_close)
        self.grid(row=0, column=0, rowspan=3, sticky='nsew')

        scripts_dir = os.path.abspath(os.path.dirname(__file__))
        data_dir = os.path.join(scripts_dir, '..')
        self.resources_path = os.path.join(data_dir, 'pyxelrest_resources')

        images_frame = tkinter.Frame(self)
        images_frame.grid(row=0, column=0, columnspan=3)

        image = self.create_image(PYTHON_STEP)
        python_image = tkinter.Label(images_frame, width=100, height=100, text='Python', image=image)
        python_image.image_reference = image
        python_image.grid(in_=images_frame, row=0, column=0)

        image = self.create_image(EXCEL_STEP)
        excel_image = tkinter.Label(images_frame, width=100, height=100, text='Microsoft Excel', image=image)
        excel_image.image_reference = image
        excel_image.grid(in_=images_frame, row=0, column=1)

        image = self.create_image(SETTINGS_STEP)
        settings_image = tkinter.Label(images_frame, width=100, height=100, text='Settings', image=image)
        settings_image.image_reference = image
        settings_image.grid(in_=images_frame, row=0, column=2)

        self.images = {
            PYTHON_STEP: python_image,
            EXCEL_STEP: excel_image,
            SETTINGS_STEP: settings_image,
        }

        install_message = "PyxelRest {0} is available".format(new_version)
        self.status = tkinter.Label(self, text=install_message)
        self.status.grid(in_=self, row=1, column=0)

        self.update_button = tkinter.Button(self, text="Update now", width=50, command=self.install_update)
        self.update_button.grid(in_=self, row=2, column=0)
        self.update_button.configure(background='black', foreground='white')

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)

        self.updating_thread = updating_thread
        self.updating_queue = updating_queue
        self.update_failed = False

    def create_image(self, image_name):
        return tkinter.PhotoImage(file=os.path.join(self.resources_path, IMAGE_NAMES[image_name]))

    def on_close(self):
        if self.updating_thread.is_alive():
            return  # Avoid closing while update is already in progress
        if not self.updating_thread.pid:  # In case user exit without starting the update
            logger.info('Update rejected.')
        self.master.destroy()

    def install_update(self):
        self.update_button.config(state='disabled')
        self.update_button.configure(text='Update in progress')
        self.status.configure(text='Launching update')
        self.updating_thread.start()
        self.update_installation_status()

    def update_installation_status(self):
        self.check_queue()
        if self.updating_thread.is_alive() or not self.updating_queue.empty():
            self.after(100, self.update_installation_status)
        elif self.update_failed:
            self.update_button.configure(text='Update failed. Contact support.')
            pass  # Keep alive and let user close the window
        else:  # Close window once update is complete
            self.on_close()

    def update_status(self, step, status):
        if DONE == status:
            self.images[step].image_reference = self.create_image('{0}_{1}'.format(step, status))
            self.images[step]['image'] = self.images[step].image_reference
            self.status['text'] = '{0} updated'.format(step)
        elif IN_PROGRESS == status:
            self.status['text'] = 'Updating {0}'.format(step)
        elif FAILURE == status:
            self.update_failed = True
            self.images[step].image_reference = self.create_image('{0}_{1}'.format(step, status))
            self.images[step]['image'] = self.images[step].image_reference
            self.status['text'] = '{0} could not be updated'.format(step)

    def check_queue(self):
        try:
            step, status = self.updating_queue.get()
            if END_STEP == step:
                self.updating_queue.task_done()
                self.updating_thread.join()
                return

            if CLOSING_EXCEL_STEP == step:
                if DONE == status:
                    self.status['text'] = 'Microsoft Excel is closed.'
                elif IN_PROGRESS == status:
                    self.status['text'] = 'Microsoft Excel must be closed for update to continue.'
                elif FAILURE == status:
                    self.update_failed = True
                    self.status['text'] = 'Microsoft Excel was not closed.'
            else:
                self.update_status(step, status)

            self.updating_queue.task_done()
        except:
            logger.exception('Error while handling new status.')
            self.updating_queue.task_done()


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

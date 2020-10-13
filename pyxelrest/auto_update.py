import argparse
import multiprocessing
import os
import os.path
import time
import re
import logging
import logging.config
import logging.handlers
from typing import Tuple, Optional

from pip._internal.commands.list import ListCommand
from pip._internal.commands.install import InstallCommand
from pip._internal.utils.misc import get_installed_distributions

import tkinter
import win32com.client


CLOSING_EXCEL_STEP = "Closing Microsoft Excel"
PYTHON_STEP = "PyxelRest package"
EXCEL_STEP = "Microsoft Excel add-in"
SETTINGS_STEP = "Services configuration"
END_STEP = "End of update"

IN_PROGRESS = "in progress"
DONE = "done"
FAILURE = "failure"

IMAGE_NAMES = {
    PYTHON_STEP: "python_logo_greyscale_100.png",
    f"{PYTHON_STEP}_{DONE}": "python_logo_100.png",
    f"{PYTHON_STEP}_{FAILURE}": "python_logo_error_100.png",
    EXCEL_STEP: "excel_logo_greyscale_100.png",
    f"{EXCEL_STEP}_{DONE}": "excel_logo_100.png",
    f"{EXCEL_STEP}_{FAILURE}": "excel_logo_error_100.png",
    SETTINGS_STEP: "settings_logo_greyscale_100.png",
    f"{SETTINGS_STEP}_{DONE}": "settings_logo_100.png",
    f"{SETTINGS_STEP}_{FAILURE}": "settings_logo_error_100.png",
}


def create_logger():
    global default_log_file_path
    global logger
    if __name__ == "__main__":
        logger = logging.getLogger("pyxelrest.auto_update")
    else:
        logger = logging.getLogger(__name__)

    default_log_file_path = os.path.join(
        os.getenv("APPDATA"), "pyxelrest", "logs", "pyxelrest_auto_update.log"
    )
    logging.config.dictConfig(
        {
            "version": 1,
            "formatters": {
                "clean": {
                    "format": "%(asctime)s [%(threadName)s] [%(levelname)s] %(message)s"
                }
            },
            "handlers": {
                "daily_rotating": {
                    "class": "logging.handlers.TimedRotatingFileHandler",
                    "formatter": "clean",
                    "filename": default_log_file_path,
                    "when": "D",
                    "backupCount": 10,
                }
            },
            "loggers": {"pyxelrest": {"level": "DEBUG"}},
            "root": {"level": "INFO", "handlers": ["daily_rotating"]},
        }
    )


create_logger()


def _outdated_package(package_name: str, check_pre_releases: bool):
    """Faster outdated check when running it for a single package."""
    list_command = ListCommand(name="", summary="")
    command_options, _ = list_command.parse_args(
        ["--pre"] if check_pre_releases else []
    )
    installed_package = _installed_package(package_name)
    if installed_package:
        packages = list_command.get_outdated([installed_package], command_options)
        return packages[0] if packages else None


def _installed_package(package_name: str):
    # Break from the loop in order to retrieve it faster in huge environments
    for package in get_installed_distributions():
        if package.project_name == package_name:
            return package


def _process_ids():
    processes = win32com.client.GetObject("winmgmts:").InstancesOf("Win32_Process")
    return [p.Properties_("ProcessId").Value for p in processes]


def _is_already_updating() -> bool:
    try:
        update_is_in_progress = os.path.join(
            os.getenv("APPDATA"), "pyxelrest", "update_is_in_progress"
        )
        if os.path.isfile(update_is_in_progress):
            with open(update_is_in_progress, "r") as update_details:
                process_id = int(update_details.readline())
                if process_id in _process_ids():
                    return True
                else:
                    logger.warning(
                        "Update is theoratically still in progress but process cannot be found. Considering that no update is in progress."
                    )
    except:
        logger.exception(
            "Unable to know if an update is in progress. Considering that no update is in progress."
        )

    try:
        # Create file if this is the first update (most cases)
        with open(update_is_in_progress, "w") as update_details:
            update_details.write(str(os.getpid()))
    except:
        logger.exception(
            "Unable to set update as in progress. Concurrent update might occur."
        )
    finally:
        return False


def _update_is_finished():
    update_is_in_progress = os.path.join(
        os.getenv("APPDATA"), "pyxelrest", "update_is_in_progress"
    )
    os.remove(update_is_in_progress)


class UpdateProcess:
    def __init__(
        self,
        path_to_up_to_date_configurations: str,
        check_pre_releases: bool,
        updating_queue: multiprocessing.Queue,
    ):
        self.path_to_up_to_date_configurations = path_to_up_to_date_configurations
        self.check_pre_releases = check_pre_releases
        self.updating_queue = updating_queue

    def start_update(self):
        logger.debug("Update accepted. Waiting for Microsoft Excel to close...")
        self.updating_queue.put((CLOSING_EXCEL_STEP, IN_PROGRESS))
        # If Microsoft Excel is running, user might still use pyxelrest, do not update yet
        while self._is_excel_running():
            # As closing Microsoft Excel is a manual user action, wait for 1 second between each check.
            time.sleep(1)
        logger.debug("Microsoft Excel is closed. Installing update.")
        self.updating_queue.put((CLOSING_EXCEL_STEP, DONE))
        self._update_pyxelrest()
        self.updating_queue.put((END_STEP, DONE))

    def _is_excel_running(self) -> bool:
        try:
            processes = win32com.client.GetObject("winmgmts:").InstancesOf(
                "Win32_Process"
            )
            for process in processes:
                if process.Properties_("Name").Value == "EXCEL.EXE":
                    return True
            return False
        except:
            logger.exception(
                "Unable to retrieve Microsoft Excel process list. Considering as closed."
            )
            return False

    def _update_pyxelrest(self):
        self.updating_queue.put((PYTHON_STEP, IN_PROGRESS))
        upgrade_options = ["--pre"] if self.check_pre_releases else []
        result = InstallCommand().main(
            [
                "pyxelrest",
                "--upgrade",
                "--disable-pip-version-check",
                "--log",
                default_log_file_path,
                *upgrade_options,
            ]
        )
        create_logger()  # PyxelRest logger is lost while trying to update
        if result == 0:
            self.updating_queue.put((PYTHON_STEP, DONE))
            logger.info("PyxelRest package updated.")
            if self._update_addin():
                # Only perform configuration update when we are sure that latest version is installed
                self._update_configuration()
        else:
            logger.warning("PyxelRest package update failed.")
            self.updating_queue.put((PYTHON_STEP, FAILURE))

    def _update_addin(self):
        self.updating_queue.put((EXCEL_STEP, IN_PROGRESS))
        try:
            from pyxelrest.install_addin import Installer

            addin_installer = Installer(
                path_to_up_to_date_configuration=self.path_to_up_to_date_configurations
            )
            addin_installer.perform_post_installation_tasks()
            logger.info("Microsoft Excel add-in successfully updated.")
            self.updating_queue.put((EXCEL_STEP, DONE))
            return True
        except:
            logger.exception("Unable to update add-in.")
            self.updating_queue.put((EXCEL_STEP, FAILURE))

    def _update_configuration(self):
        if not self.path_to_up_to_date_configurations:
            logger.info("Services configuration will not be updated.")
            return

        self.updating_queue.put((SETTINGS_STEP, IN_PROGRESS))
        try:
            from pyxelrest.update_services_config import (
                ServicesConfigUpdater,
                UPDATE_SECTIONS,
            )

            config_updater = ServicesConfigUpdater(UPDATE_SECTIONS)
            config_updater.update_configuration(self.path_to_up_to_date_configurations)
            logger.info("Services configuration successfully updated.")
            self.updating_queue.put((SETTINGS_STEP, DONE))
        except:
            logger.exception("Unable to update configuration.")
            self.updating_queue.put((SETTINGS_STEP, FAILURE))


def _start_update_process(
    path_to_up_to_date_configurations: str,
    check_pre_releases: bool,
    updating_queue: multiprocessing.Queue,
):
    UpdateProcess(
        path_to_up_to_date_configurations, check_pre_releases, updating_queue
    ).start_update()


class PyxelRestUpdater:
    def __init__(
        self,
        *,
        path_to_up_to_date_configurations=None,
        check_pre_releases: bool = False,
    ):
        self.path_to_up_to_date_configurations = path_to_up_to_date_configurations
        self.check_pre_releases = check_pre_releases

    def check_update(self):
        logger.debug("Checking if an update is available...")
        if self._is_update_available():
            logger.info(
                f"Update {self.pyxelrest_package.latest_version} available (from {self.pyxelrest_package.version})."
            )
            self.start_update_gui()
        else:
            logger.debug("No update available.")

    def start_update_gui(self):
        root = tkinter.Tk()
        root.title("PyxelRest update available")
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        root.resizable(width=False, height=False)
        updating_queue = multiprocessing.JoinableQueue()
        updating_process = multiprocessing.Process(
            target=_start_update_process,
            args=(
                self.path_to_up_to_date_configurations,
                self.check_pre_releases,
                updating_queue,
            ),
        )
        app = UpdateGUI(
            root,
            updating_process,
            updating_queue,
            self.pyxelrest_package.version,
            self.pyxelrest_package.latest_version,
        )
        root.wm_attributes("-topmost", True)
        root.tkraise()
        root.mainloop()

    def _is_update_available(self):
        self.pyxelrest_package = _outdated_package("pyxelrest", self.check_pre_releases)
        return self.pyxelrest_package


def _get_versions(
    current_version, new_version, group_number: int
) -> Tuple[Optional[int], Optional[int]]:
    current_match = re.search("(\d+).(\d+).(\d+)", str(current_version))
    new_match = re.search("(\d+).(\d+).(\d+)", str(new_version))
    if current_match and new_match:
        return (
            int(current_match.group(group_number)),
            int(new_match.group(group_number)),
        )
    return None, None


def is_breaking_compatibility(current_version, new_version) -> bool:
    current_major, new_major = _get_versions(current_version, new_version, 1)
    if current_major is not None and new_major is not None:
        return new_major > current_major
    return False


def is_adding_features(current_version, new_version) -> bool:
    current_minor, new_minor = _get_versions(current_version, new_version, 2)
    if current_minor is not None and new_minor is not None:
        return new_minor > current_minor
    return False


def is_fixing_bugs(current_version, new_version) -> bool:
    current_patch, new_patch = _get_versions(current_version, new_version, 3)
    if current_patch is not None and new_patch is not None:
        return new_patch > current_patch
    return False


class UpdateGUI(tkinter.Frame):
    def __init__(
        self,
        master,
        updating_process: multiprocessing.Process,
        updating_queue: multiprocessing.Queue,
        current_version,
        new_version,
    ):
        tkinter.Frame.__init__(self, master)
        master.protocol("WM_DELETE_WINDOW", self.on_close)
        self.grid(row=0, column=0, rowspan=3, sticky="nsew")

        scripts_dir = os.path.abspath(os.path.dirname(__file__))
        data_dir = os.path.join(scripts_dir, "..")
        self.resources_path = os.path.join(data_dir, "pyxelrest_resources")

        images_frame = tkinter.Frame(self)
        images_frame.grid(row=0, column=0, columnspan=3)

        image = self.create_image(PYTHON_STEP)
        python_image = tkinter.Label(
            images_frame, width=100, height=100, text="Python", image=image
        )
        python_image.image_reference = image
        python_image.grid(in_=images_frame, row=0, column=0)

        image = self.create_image(EXCEL_STEP)
        excel_image = tkinter.Label(
            images_frame, width=100, height=100, text="Microsoft Excel", image=image
        )
        excel_image.image_reference = image
        excel_image.grid(in_=images_frame, row=0, column=1)

        image = self.create_image(SETTINGS_STEP)
        settings_image = tkinter.Label(
            images_frame, width=100, height=100, text="Settings", image=image
        )
        settings_image.image_reference = image
        settings_image.grid(in_=images_frame, row=0, column=2)

        self.images = {
            PYTHON_STEP: python_image,
            EXCEL_STEP: excel_image,
            SETTINGS_STEP: settings_image,
        }

        self.new_version = new_version
        if is_breaking_compatibility(current_version, new_version):
            install_message = f"Major PyxelRest release {new_version} is available. Read change log before updating."
        elif is_adding_features(current_version, new_version):
            install_message = f"PyxelRest bug fixes and enhancements are available (version {new_version})"
        elif is_fixing_bugs(current_version, new_version):
            install_message = (
                f"PyxelRest bug fixes are available (version {new_version})"
            )
        else:  # This case should not happen but if the way version handling is done change it should be handled
            install_message = f"PyxelRest {new_version} is available"
        self.status = tkinter.Label(self, text=install_message)
        self.status.grid(in_=self, row=1, column=0)

        self.update_button = tkinter.Button(
            self, text="Update now", width=50, command=self.install_update
        )
        self.update_button.grid(in_=self, row=2, column=0)
        self.update_button.configure(background="black", foreground="white")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)

        self.updating_process = updating_process
        self.updating_queue = updating_queue
        self.update_failed = False

    def create_image(self, image_name: str):
        return tkinter.PhotoImage(
            file=os.path.join(self.resources_path, IMAGE_NAMES[image_name])
        )

    def on_close(self):
        if self.updating_process.is_alive():
            return  # Avoid closing while update is already in progress
        if (
            not self.updating_process.pid
        ):  # In case user exit without starting the update
            logger.info("Update rejected.")
        self.master.destroy()

    def install_update(self):
        self.update_button.config(state="disabled")
        self.master.title("Updating PyxelRest...")
        self.update_button.configure(text="Update in progress")
        self.status.configure(text="Launching update")
        self.updating_process.start()
        self.update_installation_status()

    def update_installation_status(self):
        self.check_queue()
        if self.updating_process.is_alive() or not self.updating_queue.empty():
            self.after(100, self.update_installation_status)
        elif self.update_failed:
            self.update_button.configure(text="Update failed. Contact support.")
        else:  # Update complete
            self.master.title("PyxelRest updated")
            self.status.configure(
                text=f"PyxelRest is now up to date (version {self.new_version})"
            )
            self.update_button.configure(command=self.on_close)
            self.update_button.configure(text="OK")
            self.update_button.config(state="normal")

    def update_status(self, step: str, status: str):
        if DONE == status:
            self.images[step].image_reference = self.create_image(f"{step}_{status}")
            self.images[step]["image"] = self.images[step].image_reference
            self.status["text"] = f"{step} updated"
        elif IN_PROGRESS == status:
            self.status["text"] = f"Updating {step}"
        elif FAILURE == status:
            self.update_failed = True
            self.images[step].image_reference = self.create_image(f"{step}_{status}")
            self.images[step]["image"] = self.images[step].image_reference
            self.status["text"] = f"{step} could not be updated"

    def check_queue(self):
        try:
            step, status = self.updating_queue.get()
            if END_STEP == step:
                self.updating_queue.task_done()
                self.updating_process.join()
                return

            if CLOSING_EXCEL_STEP == step:
                if DONE == status:
                    self.status["text"] = "Microsoft Excel is closed."
                elif IN_PROGRESS == status:
                    self.status[
                        "text"
                    ] = "Microsoft Excel must be closed for update to continue."
                elif FAILURE == status:
                    self.update_failed = True
                    self.status["text"] = "Microsoft Excel was not closed."
            else:
                self.update_status(step, status)

            self.updating_queue.task_done()
        except:
            logger.exception("Error while handling new status.")
            self.updating_queue.task_done()


def main(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path_to_up_to_date_configurations",
        help="File (path or URL) or directory (path) containing up to date services configuration.",
        default=None,
        type=str,
    )
    parser.add_argument(
        "--check_pre_releases", help="Also fetch pre-releases.", action="store_true"
    )
    options = parser.parse_args(args if args else None)
    logger.debug("Starting auto update script...")
    if _is_already_updating():
        logger.debug("Skip update check as another update is ongoing.")
    else:
        try:
            updater = PyxelRestUpdater(
                path_to_up_to_date_configurations=options.path_to_up_to_date_configurations,
                check_pre_releases=options.check_pre_releases,
            )
            updater.check_update()
        except:
            logger.exception("An error occurred while checking for update.")
            raise
        finally:
            _update_is_finished()


if __name__ == "__main__":
    main()

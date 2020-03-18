import argparse
import os
import shutil
import subprocess
import sys
import logging
import distutils.dir_util as dir_util

if __name__ == "__main__":
    logger = logging.getLogger("pyxelrest.install_addin")
else:
    logger = logging.getLogger(__name__)


def to_absolute_path(file_path: str) -> str:
    return file_path if os.path.isabs(file_path) else os.path.abspath(file_path)


def create_folder(folder_path: str):
    if not os.path.exists(folder_path):
        logger.info(f"Creating {folder_path} folder")
        os.makedirs(folder_path)


class VSTOManager:
    def __init__(self, version: str):
        # Try 64 bits version first
        self.vsto_installer_path = os.path.join(
            os.getenv("commonprogramfiles"),
            "microsoft shared",
            "VSTO",
            version,
            "VSTOInstaller.exe",
        )
        if not os.path.isfile(self.vsto_installer_path):
            # Try 32 bits version as backup
            self.vsto_installer_path = os.path.join(
                os.getenv("commonprogramfiles(x86)"),
                "microsoft shared",
                "VSTO",
                version,
                "VSTOInstaller.exe",
            )
            if not os.path.isfile(self.vsto_installer_path):
                raise Exception(
                    f"Auto Load PyxelRest add-in cannot be installed as VSTO installer cannot be found in {self.vsto_installer_path}."
                )

    def install_auto_load_addin(self, add_in_folder: str):
        logger.info("Try to install Microsoft Excel add-in...")
        vsto_file_path = VSTOManager.get_auto_load_vsto_file_path(add_in_folder)
        if not os.path.isfile(vsto_file_path):
            raise Exception(
                f"Auto Load PyxelRest add-in cannot be found in {vsto_file_path}."
            )
        self._clear_click_once_cache()
        failed_silent_install = subprocess.call(
            [self.vsto_installer_path, "/Silent", "/Install", vsto_file_path]
        )
        if failed_silent_install:
            logger.warning(
                f"Silent add-in installation failed (returned {failed_silent_install}). Try non-silent installation..."
            )
            subprocess.check_call(
                [self.vsto_installer_path, "/Install", vsto_file_path]
            )
        logger.info("Add-in installation completed.")

    def uninstall_auto_load_addin(self, add_in_folder: str):
        vsto_file_path = VSTOManager.get_auto_load_vsto_file_path(add_in_folder)
        if os.path.isfile(vsto_file_path):
            logger.info("Try to uninstall Microsoft Excel add-in...")
            # Check result of uninstall as failed uninstall should never occurs
            failed_silent_uninstall = subprocess.call(
                [self.vsto_installer_path, "/Silent", "/Uninstall", vsto_file_path]
            )
            if failed_silent_uninstall:
                logger.warning(
                    f"Silent add-in uninstallation failed (returned {failed_silent_uninstall}). Try non-silent uninstallation..."
                )
                subprocess.check_call(
                    [self.vsto_installer_path, "/Uninstall", vsto_file_path]
                )
            logger.info("Add-in uninstallation completed.")

    def _clear_click_once_cache(self):
        """
        Clear ClickOnce cache as it might be inconsistent if Microsoft Excel was running
        """
        logger.info("Clearing ClickOnce application cache...")
        # Do not check result of cache clearing as it might not be required.
        failed_clickonce_cache_cleanup = subprocess.call(
            ["rundll32", "dfshim", "CleanOnlineAppCache"]
        )
        logger.info(
            f"ClickOnce application cache cleared (returned {failed_clickonce_cache_cleanup})"
        )

    @staticmethod
    def get_auto_load_vsto_file_path(add_in_folder: str) -> str:
        return os.path.join(add_in_folder, "AutoLoadPyxelRestAddIn.vsto")


class XlWingsConfig:
    def __init__(self, xlwings_config_folder: str):
        self.xlwings_config_path = os.path.join(xlwings_config_folder, "xlwings.conf")
        self.xlwings_bas_path = os.path.join(xlwings_config_folder, "xlwings.bas")

    def create_file(self):
        """
        Create XLWings specific configuration for PyxelRest.
        """
        logger.info("Creating XLWings specific configuration for PyxelRest...")

        python_path = os.path.dirname(sys.executable)
        pythonw_path = os.path.join(python_path, "pythonw.exe")
        if not os.path.isfile(pythonw_path):
            raise Exception(f"Python executable cannot be found in {pythonw_path}")

        with open(self.xlwings_config_path, "w") as config_file:
            config_file.writelines(
                [
                    f'"INTERPRETER", "{pythonw_path}"',
                    '"UDF MODULES","pyxelrest._generator"',
                ]
            )
        logger.info("XLWings PyxelRest configuration created.")

    def create_vb_addin(self):
        """
        Create XLWings specific BAS file for PyxelRest.
        """
        logger.info("Creating XLWings PyxelRest VB add-in...")
        with open(self.xlwings_bas_path, "w") as add_in_file:
            import xlwings

            xlwings_path = xlwings.__path__[0]
            xlwings_bas_path = os.path.join(xlwings_path, "xlwings.bas")
            if not os.path.isfile(xlwings_bas_path):
                raise Exception(
                    f"XLWings BAS file cannot be found in {xlwings_bas_path}"
                )
            with open(xlwings_bas_path) as default_settings:
                for line in default_settings:
                    add_in_file.write(self._to_add_in_line(line))
        logger.info("XLWings PyxelRest VB add-in created.")

    def _to_add_in_line(self, line: str) -> str:
        # Ensure that Xlwings will load PyxelRest configuration
        if '        If SheetExists("xlwings.conf") = True Then\n' == line:
            return (
                '        If GetConfigFromFile("'
                + self.xlwings_config_path
                + '", configKey, configValue) Then\n'
                "            GetConfig = configValue\n"
                "        End If\n"
                "\n"
                '        If SheetExists("xlwings.conf") = True Then\n'
            )
        elif "ThisWorkbook" in line:
            if "GetUdfModules" in line:
                # Keep refering to ThisWorkbook for pyxelrest
                return line
            # Allow users to use xlwings with workbooks
            return line.replace("ThisWorkbook", "ActiveWorkbook")
        return line


class Installer:
    def __init__(
        self,
        *,
        add_in_folder: str = None,
        vsto_version: str = "10.0",
        path_to_up_to_date_configuration: str = None,
        check_pre_releases: bool = False,
    ):
        if not sys.platform.startswith("win"):
            raise Exception(
                "Auto Load add-in can only be installed on Microsoft Windows."
            )

        if not add_in_folder:
            scripts_folder = os.path.abspath(os.path.dirname(sys.executable))
            data_dir = os.path.join(scripts_folder, "..")
            add_in_folder = os.path.join(data_dir, "pyxelrest_addin")

        self.add_in_folder = to_absolute_path(add_in_folder)
        if not os.path.isdir(self.add_in_folder):
            raise Exception(
                f"PyxelRest Microsoft Excel Auto-Load Add-In cannot be found in {self.add_in_folder}."
            )

        self.pyxelrest_appdata_folder = os.path.join(os.getenv("APPDATA"), "pyxelrest")
        self.pyxelrest_appdata_addin_folder = os.path.join(
            self.pyxelrest_appdata_folder, "excel_addin"
        )
        self.pyxelrest_appdata_logs_folder = os.path.join(
            self.pyxelrest_appdata_folder, "logs"
        )
        self.pyxelrest_appdata_config_folder = os.path.join(
            self.pyxelrest_appdata_folder, "configuration"
        )
        self.path_to_up_to_date_configuration = path_to_up_to_date_configuration
        self.check_pre_releases = check_pre_releases
        self.vsto_version = vsto_version

    def perform_post_installation_tasks(self):
        create_folder(self.pyxelrest_appdata_folder)
        # Logs folder is required by default add-in configuration
        create_folder(self.pyxelrest_appdata_logs_folder)
        create_folder(self.pyxelrest_appdata_config_folder)
        # Assert that Microsoft Excel is closed
        # otherwise ClickOnce cache will still contains the add-in application manifest
        # Resulting in failure when installing a new add-in version
        if self._is_excel_running():
            logger.warning(
                "Microsoft Excel should be closed otherwise add-in update might fail."
            )
        self._install_pyxelrest_vb_addin()

        xlwings_config = XlWingsConfig(self.pyxelrest_appdata_config_folder)
        xlwings_config.create_file()
        xlwings_config.create_vb_addin()

        self._install_auto_load_addin()

    @staticmethod
    def _is_excel_running() -> bool:
        import win32com.client

        processes = win32com.client.GetObject("winmgmts:").InstancesOf("Win32_Process")
        for process in processes:
            if process.Properties_("Name").Value == "EXCEL.EXE":
                return True
        return False

    def _install_pyxelrest_vb_addin(self):
        pyxelrest_vb_file_path = os.path.join(self.add_in_folder, "pyxelrest.xlam")
        if not os.path.isfile(pyxelrest_vb_file_path):
            raise Exception(
                f"Visual Basic PyxelRest Excel Add-In cannot be found in {pyxelrest_vb_file_path}."
            )

        xlstart_folder = os.path.join(
            os.getenv("APPDATA"), "Microsoft", "Excel", "XLSTART"
        )
        if not os.path.exists(xlstart_folder):
            os.makedirs(xlstart_folder)
        pyxelrest_vb_addin_path = os.path.join(xlstart_folder, "pyxelrest.xlam")
        shutil.copyfile(pyxelrest_vb_file_path, pyxelrest_vb_addin_path)

    def _install_auto_load_addin(self):
        """
        Install Excel addin in a different folder than the python copied one as it must be uninstalled prior to
        installation and python copy is performed before running post installation script.
        """
        vsto = VSTOManager(self.vsto_version)
        if os.path.exists(self.pyxelrest_appdata_addin_folder):
            vsto.uninstall_auto_load_addin(self.pyxelrest_appdata_addin_folder)
            dir_util.remove_tree(self.pyxelrest_appdata_addin_folder)

        os.makedirs(self.pyxelrest_appdata_addin_folder)
        dir_util.copy_tree(self.add_in_folder, self.pyxelrest_appdata_addin_folder)
        try:
            vsto.install_auto_load_addin(self.pyxelrest_appdata_addin_folder)
        except:
            # Avoid next install trying to uninstall an addin that was not properly installed
            dir_util.remove_tree(self.pyxelrest_appdata_addin_folder)
            raise
        self._update_auto_load_addin_config()

    def _update_auto_load_addin_config(self):
        def write_addin_configuration_line(addin_settings_line, addin_settings_file):
            if "PYTHON_PATH_TO_BE_REPLACED_AT_POST_INSTALLATION" in addin_settings_line:
                python_executable_folder_path = os.path.dirname(sys.executable)
                python_path = os.path.join(python_executable_folder_path, "python.exe")
                # Do not set python path to a value that we know wrong, this case should not happen but you never know
                # Do not raise an exception here as the auto update feature is optional
                if os.path.isfile(python_path):
                    new_line = addin_settings_line.replace(
                        "PYTHON_PATH_TO_BE_REPLACED_AT_POST_INSTALLATION", python_path
                    )
                    addin_settings_file.write(new_line)
            elif "</appSettings>" in addin_settings_line:
                if self.path_to_up_to_date_configuration:
                    addin_settings_file.write(
                        f'    <add key="PathToUpToDateConfigurations" value="{self.path_to_up_to_date_configuration}" />\n'
                    )
                if self.check_pre_releases:
                    addin_settings_file.write(
                        '    <add key="CheckPreReleases" value="true" />\n'
                    )
                addin_settings_file.write(addin_settings_line)
            else:
                addin_settings_file.write(addin_settings_line)

        config_file_path = os.path.join(
            self.pyxelrest_appdata_config_folder, "addin.config"
        )
        default_config_file_path = os.path.join(
            self.pyxelrest_appdata_addin_folder, "AutoLoadPyxelRestAddIn.dll.config"
        )
        if os.path.isfile(default_config_file_path):
            with open(config_file_path, "w") as new_file:
                with open(default_config_file_path) as default_file:
                    for line in default_file:
                        write_addin_configuration_line(line, new_file)


def main(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--add_in_directory",
        help="Directory containing PyxelRest Microsoft Excel auto load add-in.",
        default=None,
        type=str,
    )
    parser.add_argument(
        "--path_to_up_to_date_configuration",
        help="Path to up to date configuration file(s). This path will be used in case of auto update to keep services configuration up to date.",
        default=None,
        type=str,
    )
    parser.add_argument(
        "--check_pre_releases", help="Also fetch pre-releases.", action="store_true"
    )
    options = parser.parse_args(args if args else None)
    installer = Installer(
        add_in_folder=options.add_in_directory,
        path_to_up_to_date_configuration=options.path_to_up_to_date_configuration,
        check_pre_releases=options.check_pre_releases,
    )
    installer.perform_post_installation_tasks()


if __name__ == "__main__":
    main()
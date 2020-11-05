import argparse
import os
import io
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
                    f"PyxelRest Microsoft Excel add-in cannot be installed as VSTO installer cannot be found in {self.vsto_installer_path}."
                )

    def install_addin(self, add_in_folder: str):
        logger.info("Try to install Microsoft Excel add-in...")
        vsto_file_path = VSTOManager.get_vsto_file_path(add_in_folder)
        if not os.path.isfile(vsto_file_path):
            raise Exception(
                f"PyxelRest Microsoft Excel add-in cannot be found in {vsto_file_path}."
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

    def uninstall_addin(self, add_in_folder: str):
        vsto_file_path = VSTOManager.get_vsto_file_path(add_in_folder)
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
    def get_vsto_file_path(add_in_folder: str) -> str:
        return os.path.join(add_in_folder, "PyxelRestAddIn.vsto")


class XlWingsConfig:
    def __init__(self, xlwings_config_folder: str):
        self.xlwings_config_path = os.path.join(xlwings_config_folder, "xlwings.conf")
        self.xlwings_bas_path = os.path.join(xlwings_config_folder, "xlwings.bas")

    def create_file(self) -> None:
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
                    f'"INTERPRETER_WIN", "{pythonw_path}"',
                    '"UDF MODULES","pyxelrest._generator"',
                ]
            )
        logger.info("XLWings PyxelRest configuration created.")

    def create_vb_addin(self) -> None:
        """
        Create XLWings specific BAS file for PyxelRest.
        This BAS file will be loaded into pyxelrest.xlam by the PyxelRestAddIn.

        The GetConfig function will now only load pyxelrest configuration
        and UDFs will be generated in the pyxelrest XLAM (to allow // run with xlwings and sharing them across books).
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
                process_get_config = False
                for line in default_settings:
                    if line.startswith("Function GetConfig("):
                        add_in_file.write(line)
                        add_in_file.write(f"""    Dim configValue As String
    
    If Application.Name = "Microsoft Excel" Then
        If GetConfigFromFile("{self.xlwings_config_path}", configKey, configValue) Then
            GetConfig = configValue
        End If
    End If

    If GetConfig = "" Then
        GetConfig = default
    End If
    
    GetConfig = ExpandEnvironmentStrings(GetConfig)
""")
                        process_get_config = True
                    elif process_get_config:
                        if line.startswith("End Function"):
                            add_in_file.write(line)
                            process_get_config = False
                        else:
                            # Skip the xlwings content of GetConfig function as it is replaced
                            pass
                    elif "ThisWorkbook" in line:
                        if "GetUdfModules" in line:
                            # Keep refering to ThisWorkbook for pyxelrest
                            add_in_file.write(line)
                        else:
                            # Allow users to use xlwings with workbooks
                            add_in_file.write(line.replace("ThisWorkbook", "ActiveWorkbook"))
                    else:
                        add_in_file.write(line)
        logger.info("XLWings PyxelRest VB add-in created.")


class Installer:
    def __init__(
        self,
        *,
        source: str = None,
        vsto_version: str = "10.0",
        path_to_up_to_date_configuration: str = None,
        check_pre_releases: bool = False,
    ):
        if not sys.platform.startswith("win"):
            raise Exception(
                "Microsoft Excel add-in can only be installed on Microsoft Windows."
            )

        if not source:
            executable_folder_path = os.path.abspath(os.path.dirname(sys.executable))
            # python executable is in the Scripts folder in case of a virtual environment. In the root folder otherwise.
            data_dir = os.path.join(executable_folder_path, "..") if (os.path.basename(executable_folder_path) == "Scripts") else executable_folder_path
            source = os.path.join(data_dir, "pyxelrest_addin")

        self.source = to_absolute_path(source)
        if not os.path.isdir(self.source):
            raise Exception(
                f"PyxelRest Microsoft Excel add-in source folder cannot be found in {self.source}."
            )

        self.pyxelrest_appdata_folder = os.path.join(os.getenv("APPDATA"), "pyxelrest")
        self.destination_addin_folder = os.path.join(
            self.pyxelrest_appdata_folder, "excel_addin"
        )
        self.path_to_up_to_date_configuration = path_to_up_to_date_configuration
        self.check_pre_releases = check_pre_releases
        self.vsto_version = vsto_version

    def install_addin(self):
        create_folder(self.pyxelrest_appdata_folder)
        create_folder(self.destination_addin_folder)
        # Assert that Microsoft Excel is closed
        # otherwise ClickOnce cache will still contains the add-in application manifest
        # Resulting in failure when installing a new add-in version
        if self._is_excel_running():
            logger.warning(
                "Microsoft Excel should be closed otherwise add-in update might fail."
            )
        self._install_pyxelrest_vb_addin()

        self.xlwings_config = XlWingsConfig(self.destination_addin_folder)
        self.xlwings_config.create_file()
        self.xlwings_config.create_vb_addin()

        self._install_addin()

    @staticmethod
    def _is_excel_running() -> bool:
        import win32com.client

        processes = win32com.client.GetObject("winmgmts:").InstancesOf("Win32_Process")
        for process in processes:
            if process.Properties_("Name").Value == "EXCEL.EXE":
                return True
        return False

    def _install_pyxelrest_vb_addin(self):
        source_file = os.path.join(self.source, "pyxelrest.xlam")
        if not os.path.isfile(source_file):
            raise Exception(
                f"Visual Basic PyxelRest Excel Add-In cannot be found in {source_file}."
            )

        trusted_location = os.path.join(
            os.getenv("APPDATA"), "Microsoft", "Excel", "XLSTART"
        )
        if not os.path.exists(trusted_location):
            os.makedirs(trusted_location)
        shutil.copyfile(source_file, os.path.join(trusted_location, "pyxelrest.xlam"))

    def _install_addin(self):
        """
        Install Excel addin in a different folder than the python copied one as it must be uninstalled prior to
        installation and python copy is performed before running post installation script.
        """
        vsto = VSTOManager(self.vsto_version)
        if os.path.exists(self.destination_addin_folder):
            vsto.uninstall_addin(self.destination_addin_folder)
            dir_util.remove_tree(self.destination_addin_folder)

        os.makedirs(self.destination_addin_folder)
        dir_util.copy_tree(self.source, self.destination_addin_folder)
        try:
            vsto.install_addin(self.destination_addin_folder)
        except:
            # Avoid next install trying to uninstall an addin that was not properly installed
            dir_util.remove_tree(self.destination_addin_folder)
            raise
        self._update_addin_config()

    def _update_addin_config(self):
        def write_addin_configuration_line(default_settings_line: str, new_settings: io.StringIO):
            if "PYTHON_PATH_TO_BE_REPLACED_AT_ADDIN_INSTALLATION" in default_settings_line:
                python_executable_folder_path = os.path.dirname(sys.executable)
                python_path = os.path.join(python_executable_folder_path, "python.exe")
                # Do not set python path to a value that we know wrong, this case should not happen but you never know
                # Do not raise an exception here as the auto update feature is optional
                if os.path.isfile(python_path):
                    new_line = default_settings_line.replace(
                        "PYTHON_PATH_TO_BE_REPLACED_AT_ADDIN_INSTALLATION", python_path
                    )
                    new_settings.write(new_line)
            elif r'<file value=".\" />' in default_settings_line:
                logs_folder = os.path.join(self.pyxelrest_appdata_folder, "logs")
                create_folder(logs_folder)
                new_line = default_settings_line.replace(".", logs_folder)
                new_settings.write(new_line)
            elif "</appSettings>" in default_settings_line:
                if self.path_to_up_to_date_configuration:
                    new_settings.write(
                        f'    <add key="PathToUpToDateConfigurations" value="{self.path_to_up_to_date_configuration}" />\n'
                    )
                if self.check_pre_releases:
                    new_settings.write(
                        '    <add key="CheckPreReleases" value="true" />\n'
                    )
                new_settings.write(
                    f'    <add key="PathToXlWingsBasFile" value="{self.xlwings_config.xlwings_bas_path}" />\n'
                )
                new_settings.write(default_settings_line)
            else:
                new_settings.write(default_settings_line)

        default_config_file_path = os.path.join(
            self.destination_addin_folder, "PyxelRestAddIn.dll.config"
        )
        if os.path.isfile(default_config_file_path):
            new_config = io.StringIO()
            with open(default_config_file_path) as default_file:
                for line in default_file:
                    write_addin_configuration_line(line, new_config)
            with open(default_config_file_path, "w") as default_file:
                default_file.write(new_config.getvalue())


def main(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        help="Directory containing add-in as provided by pyxelrest module installation.",
        default=None,
        type=str,
    )
    parser.add_argument(
        "--path_to_up_to_date_configuration",
        help="Path to up to date configuration file(s). This path will be used to keep services configuration up to date and provide a list of available services within the Microsoft Excel add-in.",
        default=None,
        type=str,
    )
    parser.add_argument(
        "--check_pre_releases", help="Also fetch pre-releases when checking for updates.", action="store_true"
    )
    options = parser.parse_args(args if args else None)
    installer = Installer(
        add_in_folder=options.source,
        path_to_up_to_date_configuration=options.path_to_up_to_date_configuration,
        check_pre_releases=options.check_pre_releases,
    )
    installer.install_addin()


if __name__ == "__main__":
    main()

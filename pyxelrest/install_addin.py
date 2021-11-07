import argparse
import os
import io
import re
import shutil
import subprocess
import sys
import logging
import distutils.dir_util as dir_util
import winreg
from typing import Optional

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
    def __init__(self):
        version = "10.0"
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
        Clear ClickOnce cache as it might be inconsistent (still contains the application manifest)
        if Microsoft Excel was running during installation.
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


def create_xlwings_config(xlwings_config_folder: str) -> str:
    """
    Create XLWings specific BAS file for PyxelRest.
    This BAS file will be loaded into pyxelrest.xlam by the PyxelRestAddIn.

    The GetConfig function will now only load pyxelrest configuration
    and UDFs will be generated in the pyxelrest XLAM (to allow // run with xlwings and sharing them across books).
    """
    logger.info("Creating XLWings PyxelRest VB add-in...")
    xlwings_bas_path = os.path.join(xlwings_config_folder, "xlwings.bas")
    with open(xlwings_bas_path, "w") as add_in_file:
        import xlwings

        xlwings_path = xlwings.__path__[0]
        original_xlwings_bas_path = os.path.join(xlwings_path, "xlwings.bas")
        if not os.path.isfile(original_xlwings_bas_path):
            raise Exception(
                f"XLWings BAS file cannot be found in {original_xlwings_bas_path}"
            )

        python_path = os.path.dirname(sys.executable)
        pythonw_path = os.path.join(python_path, "pythonw.exe")
        if not os.path.isfile(pythonw_path):
            raise Exception(f"Python executable cannot be found in {pythonw_path}")

        with open(original_xlwings_bas_path) as original_xlwings_file:
            current_function = None
            for line in original_xlwings_file:
                previous_function = current_function
                current_function = _function_or_sub_name(line, current_function)
                if current_function == "GetConfig":
                    # If this is the definition of GetConfig function
                    if previous_function != current_function:
                        add_in_file.write(line)
                        add_in_file.write(
                            f"""    Dim configValue As String

    If Application.Name = "Microsoft Excel" Then
        If configKey = "INTERPRETER_WIN" Then
            GetConfig = "{pythonw_path}"
        ElseIf configKey = "UDF MODULES" Then
            GetConfig = "pyxelrest._generator"
        End If
    End If

    If GetConfig = "" Then
        GetConfig = default
    End If
"""
                        )
                    else:
                        # Skip the xlwings content of GetConfig function as it is replaced
                        pass
                elif current_function in (
                    "ImportPythonUDFsBase",
                    "ImportXlwingsUdfsModule",
                ):
                    # Keep referring to ThisWorkbook for pyxelrest
                    add_in_file.write(line)
                elif "ThisWorkbook" in line:
                    # Allow users to use xlwings with workbooks
                    add_in_file.write(line.replace("ThisWorkbook", "ActiveWorkbook"))
                else:
                    add_in_file.write(line)
    logger.info("XLWings PyxelRest VB add-in created.")
    return xlwings_bas_path


def _function_or_sub_name(line: str, previous_function_name: str) -> Optional[str]:
    # End of previous function
    if line in ("End Function\n", "End Sub\n"):
        return

    # Start of a new function
    function_definition_match = re.match(r"^Function (.*)\(.*$", line)
    if function_definition_match:
        return function_definition_match.group(1)

    # Start of a new sub
    sub_definition_match = re.match(r"^Sub (.*)\(.*$", line)
    if sub_definition_match:
        return sub_definition_match.group(1)

    # Not a new function
    return previous_function_name


class Installer:
    def __init__(
        self,
        *,
        trusted_location: str,
        source: str = None,
        vb_addin: str = None,
        destination: str = None,
        check_pre_releases: bool = False,
    ):
        if not source:
            executable_folder_path = os.path.abspath(os.path.dirname(sys.executable))
            # python executable is in the Scripts folder in case of a virtual environment. In the root folder otherwise.
            data_dir = (
                os.path.dirname(executable_folder_path)
                if (os.path.basename(executable_folder_path) == "Scripts")
                else executable_folder_path
            )
            source = os.path.join(data_dir, "pyxelrest_addin")

        self.source = to_absolute_path(source)
        if not os.path.isdir(self.source):
            raise Exception(
                f"PyxelRest Microsoft Excel add-in source folder cannot be found in {self.source}."
            )

        self.vb_addin = vb_addin or os.path.join(self.source, "pyxelrest.xlam")
        if not os.path.isfile(self.vb_addin):
            raise Exception(
                f"Visual Basic PyxelRest Excel Add-In cannot be found in {self.vb_addin}."
            )

        self.destination = destination or os.path.abspath(".")
        self.check_pre_releases = check_pre_releases
        self.trusted_location = trusted_location

    def install_addin(self, path_to_up_to_date_configuration: str = None):
        create_folder(self.destination)
        self._write_registry_key("InstallLocation", self.destination)
        if path_to_up_to_date_configuration:
            self._write_registry_key(
                "PathToUpToDateConfigurations", path_to_up_to_date_configuration
            )
        self._create_module_logging()
        self._install_vb_addin()
        self._install_addin()

    def _install_vb_addin(self):
        create_folder(self.trusted_location)
        shutil.copyfile(
            self.vb_addin, os.path.join(self.trusted_location, "pyxelrest.xlam")
        )

    def _install_addin(self):
        """
        Install Excel addin in a different folder than the python copied one
        as previous version must be uninstalled prior to re-installation.
        """
        vsto = VSTOManager()
        destination_addin_folder = os.path.join(self.destination, "excel_addin")
        if os.path.exists(destination_addin_folder):
            vsto.uninstall_addin(destination_addin_folder)
            dir_util.remove_tree(destination_addin_folder)

        os.makedirs(destination_addin_folder)
        dir_util.copy_tree(self.source, destination_addin_folder)
        try:
            vsto.install_addin(destination_addin_folder)
        except:
            # Avoid next install trying to uninstall an addin that was not properly installed
            dir_util.remove_tree(destination_addin_folder)
            raise
        self._update_addin_config(destination_addin_folder)

    def _update_addin_config(self, destination_addin_folder: str):
        def write_addin_configuration_line(
            default_settings_line: str, new_settings: io.StringIO
        ):
            if (
                "PYTHON_PATH_TO_BE_REPLACED_AT_ADDIN_INSTALLATION"
                in default_settings_line
            ):
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
                logs_folder = os.path.join(self.destination, "logs")
                create_folder(logs_folder)
                new_line = default_settings_line.replace(".", logs_folder)
                new_settings.write(new_line)
            elif "</appSettings>" in default_settings_line:
                if self.check_pre_releases:
                    new_settings.write(
                        '    <add key="CheckPreReleases" value="true" />\n'
                    )
                new_settings.write(
                    f'    <add key="PathToXlWingsBasFile" value="{create_xlwings_config(destination_addin_folder)}" />\n'
                )
                new_settings.write(default_settings_line)
            else:
                new_settings.write(default_settings_line)

        default_config_file_path = os.path.join(
            destination_addin_folder, "PyxelRestAddIn.dll.config"
        )
        if os.path.isfile(default_config_file_path):
            new_config = io.StringIO()
            with open(default_config_file_path) as default_file:
                for line in default_file:
                    write_addin_configuration_line(line, new_config)
            with open(default_config_file_path, "w") as default_file:
                default_file.write(new_config.getvalue())

    def _write_registry_key(self, key: str, value: str):
        with winreg.CreateKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest",
        ) as pyxelrest_registry_key:
            winreg.SetValueEx(pyxelrest_registry_key, key, 0, winreg.REG_SZ, value)

    def _create_module_logging(self):
        logs_folder = os.path.join(self.destination, "logs")
        create_folder(logs_folder)

        config_folder = os.path.join(self.destination, "configuration")
        create_folder(config_folder)

        with open(os.path.join(config_folder, "logging.yml"), "w") as generated_file:
            generated_file.write(
                f"""version: 1
formatters:
  clean:
    format: '%(asctime)s [%(threadName)s] [%(levelname)s] %(message)s'
handlers:
  daily_rotating:
    class: logging.handlers.TimedRotatingFileHandler
    formatter: clean
    filename: {os.path.join(logs_folder, "pyxelrest.log")}
    when: 'D'
    backupCount: 10
loggers:
  pyxelrest:
    level: DEBUG
  xlwings:
    level: DEBUG
  requests_auth:
    level: DEBUG
  requests.packages.urllib3:
    level: DEBUG
root:
  level: INFO
  handlers: [daily_rotating]
"""
            )


def main(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--trusted_location",
        help="Trusted Microsoft Excel location where visual basic add-in will be located.",
        default=os.path.join(os.getenv("APPDATA"), "Microsoft", "Excel", "XLSTART"),
        type=str,
    )
    parser.add_argument(
        "--source",
        help="Directory containing Microsoft Excel add-in as provided by pyxelrest module installation.",
        default=None,
        type=str,
    )
    parser.add_argument(
        "--vb_addin",
        help="Directory containing Microsoft Excel Visual Basic add-in as provided by pyxelrest module installation.",
        default=None,
        type=str,
    )
    parser.add_argument(
        "--destination",
        help="Directory where add-in will be installed and add-in logs will be located. Current location by default.",
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
        "--check_pre_releases",
        help="Also fetch pre-releases when checking for updates.",
        action="store_true",
    )
    options = parser.parse_args(args if args else None)
    installer = Installer(
        trusted_location=options.trusted_location,
        source=options.source,
        vb_addin=options.vb_addin,
        destination=options.destination,
        check_pre_releases=options.check_pre_releases,
    )
    installer.install_addin(options.path_to_up_to_date_configuration)


if __name__ == "__main__":
    main()

import argparse
import os
import shutil
import subprocess
import sys
import distutils.dir_util as dir_util


def to_absolute_path(file_path):
    return file_path if os.path.isabs(file_path) else os.path.abspath(file_path)


class VSTOManager:
    def __init__(self, version):
        self.vsto_installer_path = os.path.join(os.getenv('commonprogramfiles'),
                                                'microsoft shared',
                                                'VSTO',
                                                version,
                                                'VSTOInstaller.exe')
        if not os.path.isfile(self.vsto_installer_path):
            raise Exception('Auto Load PyxelRest add-in cannot be installed as VSTO installer cannot be found in {0}.'
                            .format(self.vsto_installer_path))

    def install_auto_load_addin(self, add_in_folder):
        vsto_file_path = VSTOManager.get_auto_load_vsto_file_path(add_in_folder)
        if not os.path.isfile(vsto_file_path):
            raise Exception('Auto Load PyxelRest add-in cannot be found in {0}.'.format(vsto_file_path))
        subprocess.check_call([self.vsto_installer_path, '/Install', vsto_file_path])

    def uninstall_auto_load_addin(self, add_in_folder):
        vsto_file_path = VSTOManager.get_auto_load_vsto_file_path(add_in_folder)
        if os.path.isfile(vsto_file_path):
            # Check result of uninstall as failed uninstall should never occurs
            subprocess.check_call([self.vsto_installer_path, '/Uninstall', vsto_file_path])

    @staticmethod
    def get_auto_load_vsto_file_path(add_in_folder):
        return os.path.join(add_in_folder, 'AutoLoadPyxelRestAddIn.vsto')


class XlWingsConfig:
    def __init__(self, pyxelrest_module_dir, xlwings_config_folder):
        self.pyxelrest_module_dir = pyxelrest_module_dir
        self.xlwings_config_folder = xlwings_config_folder

    def create_pyxelrest_bas_file(self):
        """
        Create XLWings specific configuration for PyxelRest.
        :return: None
        """
        pyxelrest_settings = os.path.join(self.xlwings_config_folder, 'xlwings.bas')
        with open(pyxelrest_settings, 'w') as new_settings:
            self._fill_pyxelrest_bas_file(new_settings)

    def _fill_pyxelrest_bas_file(self, pyxelrest_settings):
        """
        Fill XLWings specific configuration for PyxelRest.
        :param pyxelrest_settings: PyxelRest XLWings specific settings file.
        :return: None
        """
        import xlwings
        xlwings_path = xlwings.__path__[0]
        with open(os.path.join(xlwings_path, 'xlwings.bas')) as previous_settings:
            for line in previous_settings:
                self._write_pyxelrest_settings_line(line, pyxelrest_settings)

    def _write_pyxelrest_settings_line(self, xlwings_settings_line, pyxelrest_settings):
        """
        Write a new line in PyxelRest XLWings settings file.
        :param xlwings_settings_line: Line in default XLWings settings file.
        :param pyxelrest_settings: PyxelRest XLWings specific settings file.
        :return: None
        """
        # TODO Use regular expressions to update settings
        # In case this installation is not performed using the default python executable in the system
        if '    PYTHON_WIN = ""\n' == xlwings_settings_line:
            python_path = os.path.dirname(sys.executable)
            pyxelrest_settings.write('    PYTHON_WIN = "' + os.path.join(python_path, 'pythonw.exe') + '"\n')
        # Allow to call pyxelrest from any Excel file
        elif '    PYTHONPATH = ThisWorkbook.Path\n' == xlwings_settings_line:
            pyxelrest_settings.write('    PYTHONPATH = "' + self.pyxelrest_module_dir + '"\n')
        # Allow to call pyxelrest
        elif '    UDF_MODULES = ""\n' == xlwings_settings_line:
            pyxelrest_settings.write('    UDF_MODULES = "pyxelrestgenerator"\n')
        else:
            pyxelrest_settings.write(xlwings_settings_line)


class PostInstall:
    def __init__(self, add_in_folder, vba_add_in_folder, installation_files_folder=None, modules_folder=None,
                 scripts_folder=None, vsto_version='10.0'):
        if not sys.platform.startswith('win'):
            raise Exception('PyxelRest can only be installed on Microsoft Windows.')
        if not add_in_folder:
            raise Exception('Path to Auto Load add-in folder must be provided.')
        if not vba_add_in_folder:
            raise Exception('Path to Visual Basic add-in folder must be provided.')

        self.add_in_folder = to_absolute_path(add_in_folder)
        self.vba_add_in_folder = to_absolute_path(vba_add_in_folder)
        self.installation_files_folder = installation_files_folder or os.path.abspath(os.path.dirname(__file__))
        self.modules_folder = modules_folder or os.path.abspath(os.path.dirname(__file__))
        self.scripts_folder = scripts_folder or os.path.abspath(os.path.dirname(__file__))
        self.pyxelrest_module_dir = os.path.join(self.modules_folder, 'pyxelrest')
        self.pyxelrest_appdata_folder = os.path.join(os.getenv('APPDATA'), 'pyxelrest')
        self.pyxelrest_appdata_addin_folder = os.path.join(self.pyxelrest_appdata_folder, 'excel_addin')
        self.pyxelrest_appdata_logs_folder = os.path.join(self.pyxelrest_appdata_folder, 'logs')
        self.pyxelrest_appdata_config_folder = os.path.join(self.pyxelrest_appdata_folder, 'configuration')
        self.vsto_version = vsto_version

    def perform_post_installation_tasks(self):
        self._create_pyxelrest_appdata_folder()
        self._clear_logs()
        self._create_pyxelrest_configuration_folder()
        self._create_services_configuration()
        self._create_logging_configuration()
        # Assert that Microsoft Excel is closed otherwise Add-In uninstall will silently fail and result to failure in
        # installation of a new add-in version
        if self._is_excel_running():
            raise Exception('Microsoft Excel must be closed for add-ins to be installed.')
        self._install_pyxelrest_vb_addin()

        xlwings_config = XlWingsConfig(self.pyxelrest_module_dir, self.pyxelrest_appdata_config_folder)
        xlwings_config.create_pyxelrest_bas_file()

        self._install_auto_load_addin()

    @staticmethod
    def _is_excel_running():
        import win32com.client
        processes = win32com.client.GetObject('winmgmts:').InstancesOf('Win32_Process')
        for process in processes:
            if process.Properties_('Name').Value == 'EXCEL.EXE':
                return True
        return False

    def _create_pyxelrest_appdata_folder(self):
        if not os.path.exists(self.pyxelrest_appdata_folder):
            os.makedirs(self.pyxelrest_appdata_folder)

    def _create_pyxelrest_configuration_folder(self):
        if not os.path.exists(self.pyxelrest_appdata_config_folder):
            os.makedirs(self.pyxelrest_appdata_config_folder)

    def _create_services_configuration(self):
        default_config_file = os.path.join(self.installation_files_folder,
                                           'pyxelrest',
                                           'default_services_configuration.ini')
        if os.path.isfile(default_config_file):
            user_config_file = os.path.join(self.pyxelrest_appdata_config_folder, 'services.ini')
            if not os.path.isfile(user_config_file):
                shutil.copyfile(default_config_file, user_config_file)
        else:
            raise Exception('Default services configuration file cannot be found in provided PyxelRest directory. {0}'
                            .format(default_config_file))

    def _create_logging_configuration(self):
        # TODO Use regular expressions to update settings
        def write_logging_configuration_line(logging_settings_line, logging_settings_file):
            if 'FILE_PATH_TO_BE_REPLACED_AT_POST_INSTALLATION' in logging_settings_line:
                default_log_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'logs', 'pyxelrest.log')
                new_line = logging_settings_line.replace('FILE_PATH_TO_BE_REPLACED_AT_POST_INSTALLATION',
                                                         default_log_file_path)
                logging_settings_file.write(new_line)
            else:
                logging_settings_file.write(logging_settings_line)

        default_config_file = os.path.join(self.installation_files_folder,
                                           'pyxelrest',
                                           'default_logging_configuration.ini')
        if os.path.isfile(default_config_file):
            user_config_file = os.path.join(self.pyxelrest_appdata_config_folder, 'logging.ini')
            if not os.path.isfile(user_config_file):
                with open(user_config_file, 'w') as new_file:
                    with open(default_config_file) as default_file:
                        for line in default_file:
                            write_logging_configuration_line(line, new_file)
        else:
            raise Exception('Default logging configuration file cannot be found in provided pyxelrest directory. {0}'
                            .format(default_config_file))

    def _install_pyxelrest_vb_addin(self):
        pyxelrest_vb_file_path = os.path.join(self.vba_add_in_folder, 'pyxelrest.xlam')
        if not os.path.isfile(pyxelrest_vb_file_path):
            raise Exception('Visual Basic PixelRest Excel Add-In cannot be found in {0}.'
                            .format(pyxelrest_vb_file_path))
        xlstart_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Excel', 'XLSTART')
        if not os.path.exists(xlstart_folder):
            os.makedirs(xlstart_folder)
        loaded_pyxelrest_vb_file = os.path.join(xlstart_folder, 'pyxelrest.xlam')
        if not os.path.exists(loaded_pyxelrest_vb_file):
            shutil.copyfile(pyxelrest_vb_file_path, loaded_pyxelrest_vb_file)

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
        # TODO Use regular expressions to update settings
        def write_addin_configuration_line(addin_settings_line, addin_settings_file):
            if 'PIP_PATH_TO_BE_REPLACED_AT_POST_INSTALLATION' in addin_settings_line:
                python_executable_folder_path = os.path.dirname(sys.executable)
                pip_path = os.path.join(python_executable_folder_path, 'pip.exe')
                new_line = addin_settings_line.replace('PIP_PATH_TO_BE_REPLACED_AT_POST_INSTALLATION', pip_path)
                addin_settings_file.write(new_line)
            elif 'PYTHON_PATH_TO_BE_REPLACED_AT_POST_INSTALLATION' in addin_settings_line:
                python_executable_folder_path = os.path.dirname(sys.executable)
                python_path = os.path.join(python_executable_folder_path, 'python.exe')
                new_line = addin_settings_line.replace('PYTHON_PATH_TO_BE_REPLACED_AT_POST_INSTALLATION', python_path)
                addin_settings_file.write(new_line)
            elif 'AUTO_UPDATE_SCRIPT_PATH_TO_BE_REPLACED_AT_POST_INSTALLATION' in addin_settings_line:
                auto_update_script_path = os.path.join(self.scripts_folder, 'pyxelrest_auto_update.py')
                new_line = addin_settings_line.replace('AUTO_UPDATE_SCRIPT_PATH_TO_BE_REPLACED_AT_POST_INSTALLATION',
                                                       auto_update_script_path)
                addin_settings_file.write(new_line)
            else:
                addin_settings_file.write(addin_settings_line)

        config_file_path = os.path.join(self.pyxelrest_appdata_addin_folder, 'AutoLoadPyxelRestAddIn.dll.config')
        if os.path.exists(config_file_path):
            default_config_file_path = config_file_path + '.bak'
            shutil.move(config_file_path, default_config_file_path)
            with open(config_file_path, 'w') as new_file:
                with open(default_config_file_path) as default_file:
                    for line in default_file:
                        write_addin_configuration_line(line, new_file)

    def _clear_logs(self):
        if os.path.exists(self.pyxelrest_appdata_logs_folder):
            dir_util.remove_tree(self.pyxelrest_appdata_logs_folder)
        os.makedirs(self.pyxelrest_appdata_logs_folder)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('add_in_directory', help='Directory containing PyxelRest Microsoft Excel auto load add-in.',
                        type=str)
    parser.add_argument('vb_add_in_directory', help='Directory containing PyxelRest Microsoft Visual Basic add-in.',
                        type=str)
    parser.add_argument('--install_directory', help='Directory containing PyxelRest files for installation.',
                        default=None, type=str)
    parser.add_argument('--modules_directory', help='Directory containing installed Python modules.',
                        default=None, type=str)
    parser.add_argument('--scripts_directory', help='Directory containing installed Python scripts.',
                        default=None, type=str)
    options = parser.parse_args(sys.argv[1:])

    post_install = PostInstall(options.add_in_directory,
                               options.vb_add_in_directory,
                               installation_files_folder=options.install_directory,
                               modules_folder=options.modules_directory,
                               scripts_folder=options.scripts_directory)
    post_install.perform_post_installation_tasks()

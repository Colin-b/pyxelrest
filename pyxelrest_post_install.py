import argparse
import os
import shutil
import subprocess
import sys
try:
    # Python 3
    import winreg
except:
    # Python 2
    import _winreg as winreg


def configure_xlwings_for_pyxelrest(pyxelrest_appdata_folder, pyxelrest_module_dir):
    def create_pyxelrest_bas_file():
        """
        Create XLWings specific configuration for PyxelRest.
        :return: None
        """
        pyxelrest_settings = os.path.join(pyxelrest_appdata_folder, 'xlwings.bas')
        with open(pyxelrest_settings, 'w') as new_settings:
            fill_pyxelrest_bas_file(new_settings)

    def fill_pyxelrest_bas_file(pyxelrest_settings):
        """
        Fill XLWings specific configuration for PyxelRest.
        :param pyxelrest_settings: PyxelRest XLWings specific settings file.
        :return: None
        """
        import xlwings
        xlwings_path = xlwings.__path__[0]
        with open(os.path.join(xlwings_path, 'xlwings.bas')) as previous_settings:
            for line in previous_settings:
                write_pyxelrest_settings_line(line, pyxelrest_settings)

    # TODO Use regular expressions to update settings
    def write_pyxelrest_settings_line(xlwings_settings_line, pyxelrest_settings):
        """
        Write a new line in PyxelRest XLWings settings file.
        :param xlwings_settings_line: Line in default XLWings settings file.
        :param pyxelrest_settings: PyxelRest XLWings specific settings file.
        :return: None
        """
        # In case this installation is not performed using the default python executable in the system
        if '    PYTHON_WIN = ""\n' == xlwings_settings_line:
            python_path = os.path.dirname(sys.executable)
            pyxelrest_settings.write('    PYTHON_WIN = "' + os.path.join(python_path, 'pythonw.exe') + '"\n')
        # Allow to call pyxelrest from any Excel file
        elif '    PYTHONPATH = ThisWorkbook.Path\n' == xlwings_settings_line:
            pyxelrest_settings.write('    PYTHONPATH = "' + pyxelrest_module_dir + '"\n')
        # Allow to call pyxelrest
        elif '    UDF_MODULES = ""\n' == xlwings_settings_line:
            pyxelrest_settings.write('    UDF_MODULES = "pyxelrest"\n')
        else:
            pyxelrest_settings.write(xlwings_settings_line)

    create_pyxelrest_bas_file()


def create_services_configuration(pyxelrest_appdata_folder, install_dir):
    default_config_file = os.path.join(install_dir, 'pyxelrest', 'default_services_configuration.ini')
    if os.path.isfile(default_config_file):
        user_config_file = os.path.join(pyxelrest_appdata_folder, 'services_configuration.ini')
        if not os.path.isfile(user_config_file):
            shutil.copyfile(default_config_file, user_config_file)
    else:
        raise Exception('Default services configuration file cannot be found in provided pyxelrest directory. {0}'.format(default_config_file))


def create_logging_configuration(pyxelrest_appdata_folder, install_dir):
    # TODO Use regular expressions to update settings
    def write_logging_configuration_line(logging_settings_line, logging_settings_file):
        if 'FILE_PATH_TO_BE_REPLACED_AT_POST_INSTALLATION' in logging_settings_line:
            default_log_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'pyxelrest.log')
            new_line = logging_settings_line.replace('FILE_PATH_TO_BE_REPLACED_AT_POST_INSTALLATION', default_log_file_path)
            logging_settings_file.write(new_line)
        else:
            logging_settings_file.write(logging_settings_line)

    default_config_file = os.path.join(install_dir, 'pyxelrest', 'default_logging_configuration.ini')
    if os.path.isfile(default_config_file):
        user_config_file = os.path.join(pyxelrest_appdata_folder, 'logging_configuration.ini')
        if not os.path.isfile(user_config_file):
            with open(user_config_file, 'w') as new_file:
                with open(default_config_file) as default_file:
                    for line in default_file:
                        write_logging_configuration_line(line, new_file)
    else:
        raise Exception('Default logging configuration file cannot be found in provided pyxelrest directory. {0}'.format(default_config_file))


def install_auto_load_pyxelrest(pyxelrest_addin_dir):
    vsto_installer_path = os.path.join(os.getenv('commonprogramfiles'), 'microsoft shared', 'VSTO', '10.0',
                                       'VSTOInstaller.exe')
    if not os.path.isfile(vsto_installer_path):
        raise Exception('Auto Load PixelRest Excel Add-In cannot be installed as VSTO installer cannnot be found.')
    vsto_file_path = os.path.join(pyxelrest_addin_dir, 'AutoLoadPyxelRestAddIn.vsto')
    if not os.path.isfile(vsto_file_path):
        raise Exception('Auto Load PixelRest Excel Add-In cannot be found in {0}.'.format(vsto_file_path))
    subprocess.check_call([vsto_installer_path, '/i', vsto_file_path])


def get_addin_folder(addin_folder_option, modules_dir):
    if addin_folder_option:
        if os.path.isabs(addin_folder_option):
            return addin_folder_option
        return os.path.abspath(addin_folder_option)
    return os.path.join(modules_dir, '..', '..', 'pyxelrest_addin')


def install_pyxelrest_vb_addin(pyxelrest_vb_addin_dir):
    pyxelrest_vb_file_path = os.path.join(pyxelrest_vb_addin_dir, 'pyxelrest.xlam')
    if not os.path.isfile(pyxelrest_vb_file_path):
        raise Exception('Visual Basic PixelRest Excel Add-In cannot be found in {0}.'.format(pyxelrest_vb_file_path))
    xlstart_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Excel', 'XLSTART')
    if not os.path.exists(xlstart_folder):
        os.makedirs(xlstart_folder)
    loaded_pyxelrest_vb_file = os.path.join(xlstart_folder, 'pyxelrest.xlam')
    if not os.path.exists(loaded_pyxelrest_vb_file):
        shutil.copyfile(pyxelrest_vb_file_path, loaded_pyxelrest_vb_file)


def get_vb_addin_folder(vb_addin_folder_option, modules_dir):
    if vb_addin_folder_option:
        if os.path.isabs(vb_addin_folder_option):
            return vb_addin_folder_option
        return os.path.abspath(vb_addin_folder_option)
    return os.path.join(modules_dir, '..', '..', 'pyxelrest_vb_addin')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-idir', '--installdirectory', help='directory containing pyxelrest files for installation', default=None, type=str)
    parser.add_argument('-mdir', '--modulesdirectory', help='directory containing installed python modules', default=None, type=str)
    parser.add_argument('-adir', '--addindirectory', help='directory containing pyxelrest auto load addin', default=None, type=str)
    parser.add_argument('-vbdir', '--vbaddindirectory', help='directory containing pyxelrest visual basic addin', default=None, type=str)
    options = parser.parse_args(sys.argv[1:])

    modules_dir = options.modulesdirectory if options.modulesdirectory else os.path.abspath(os.path.dirname(__file__))
    pyxelrest_module_dir = os.path.join(modules_dir, 'pyxelrest')
    pyxelrest_addin_dir = get_addin_folder(options.addindirectory, modules_dir)
    pyxelrest_vb_addin_dir = get_vb_addin_folder(options.vbaddindirectory, modules_dir)
    install_dir = options.installdirectory if options.installdirectory else os.path.abspath(os.path.dirname(__file__))
    pyxelrest_appdata_folder = os.path.join(os.getenv('APPDATA'), 'pyxelrest')
    if not os.path.exists(pyxelrest_appdata_folder):
        os.makedirs(pyxelrest_appdata_folder)

    create_services_configuration(pyxelrest_appdata_folder, install_dir)
    create_logging_configuration(pyxelrest_appdata_folder, install_dir)
    if sys.platform.startswith('win'):
        install_pyxelrest_vb_addin(pyxelrest_vb_addin_dir)
        configure_xlwings_for_pyxelrest(pyxelrest_appdata_folder, pyxelrest_module_dir)
        install_auto_load_pyxelrest(pyxelrest_addin_dir)

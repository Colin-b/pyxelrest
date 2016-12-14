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


def configure_xlwings_for_pyxelrest(pyxelrest_module_dir):
    def create_pyxelrest_bas_file():
        pyxelrest_settings = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'xlwings.bas')
        with open(pyxelrest_settings, 'w') as new_settings:
            fill_pyxelrest_bas_file(new_settings)
        return pyxelrest_settings

    def fill_pyxelrest_bas_file(pyxelrest_settings):
        import xlwings
        xlwings_path = xlwings.__path__[0]
        with open(os.path.join(xlwings_path, 'xlwings.bas')) as previous_settings:
            for line in previous_settings:
                write_pyxelrest_settings_line(line, pyxelrest_settings)

    # TODO Use regular expressions to update settings
    def write_pyxelrest_settings_line(xlwings_settings_line, pyxelrest_settings):
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

    create_environment_variable('PathToXlWingsBasFile', create_pyxelrest_bas_file())


def create_environment_variable(string_name, string_value):
    """
    Create environment variable that stay available after execution of this python script.
    The method must be run as administrator.
    :param string_name: Name of the environment variable
    :param string_value: String value of the environment variable
    :return: None
    """
    reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    env = winreg.OpenKey(reg, "Environment", 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(env, string_name, 0, winreg.REG_EXPAND_SZ, string_value)
    winreg.CloseKey(env)
    winreg.CloseKey(reg)


def create_user_configuration(install_dir):
    default_config_file = os.path.join(install_dir, 'pyxelrest', 'default_configuration.ini')
    if os.path.isfile(default_config_file):
        user_config_file = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'pixelrest_config.ini')
        shutil.copyfile(default_config_file, user_config_file)
    else:
        raise Exception('Default configuration file cannot be found in provided pyxelrest directory. {0}'.format(default_config_file))


def install_auto_load_pyxelrest(pyxelrest_addin_dir):
    vsto_installer_path = os.path.join(os.getenv('commonprogramfiles'), 'microsoft shared', 'VSTO', '10.0',
                                       'VSTOInstaller.exe')
    if not os.path.isfile(vsto_installer_path):
        raise Exception('Auto Load PixelRest Excel Add-In cannot be installed as VSTO installer cannnot be found.')
    vsto_file_path = os.path.join(pyxelrest_addin_dir, 'AutoLoadPyxelRestAddIn.vsto')
    if not os.path.isfile(vsto_file_path):
        raise Exception('Auto Load PixelRest Excel Add-In cannot be found in {0}.'.format(vsto_file_path))
    subprocess.check_call([vsto_installer_path, '/i', vsto_file_path])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-idir', '--installdirectory', help='directory containing pyxelrest files for installation', default=None, type=str)
    parser.add_argument('-mdir', '--modulesdirectory', help='directory containing installed python modules', default=None, type=str)
    options = parser.parse_args(sys.argv[1:])

    modules_dir = options.modulesdirectory if options.modulesdirectory else os.path.abspath(os.path.dirname(__file__))
    pyxelrest_module_dir = os.path.join(modules_dir, 'pyxelrest')
    pyxelrest_addin_dir = os.path.join(modules_dir, '..', '..', 'pyxelrest_addin')
    install_dir = options.installdirectory if options.installdirectory else os.path.abspath(os.path.dirname(__file__))
    create_user_configuration(install_dir)
    if sys.platform.startswith('win'):
        configure_xlwings_for_pyxelrest(pyxelrest_module_dir)
        install_auto_load_pyxelrest(pyxelrest_addin_dir)

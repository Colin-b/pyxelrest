import os
import sys
import subprocess
import zipfile
import winreg
from shutil import copyfile

this_dir = os.path.abspath(os.path.dirname(__file__))


def configure_xlwings_for_pyxelrest():
    def create_pyxelrest_bas_file():
        pyxelrest_settings = os.path.join(this_dir, 'xlwings.bas')
        with open(pyxelrest_settings, 'w') as new_settings:
            fill_pyxelrest_bas_file(new_settings)
        return pyxelrest_settings

    def fill_pyxelrest_bas_file(pyxelrest_settings):
        with open(os.path.join(xlwings_path, 'xlwings.bas')) as previous_settings:
            for line in previous_settings:
                write_pyxelrest_settings_line(line, pyxelrest_settings)

    # TODO Use regular expressions to update settings
    def write_pyxelrest_settings_line(xlwings_settings_line, pyxelrest_settings):
        # In case this installation is not performed using the default python executable in the system
        if '    PYTHON_WIN = ""\n' == xlwings_settings_line:
            # TODO Check if this works properly when calling it using pip?
            python_path = os.path.dirname(sys.executable)
            pyxelrest_settings.write('    PYTHON_WIN = "' + os.path.join(python_path, 'pythonw.exe') + '"\n')
        # Allow to call pyxelrest from any Excel file
        elif '    PYTHONPATH = ThisWorkbook.Path\n' == xlwings_settings_line:
            pyxelrest_settings.write('    PYTHONPATH = "' + os.path.join(this_dir, 'pyxelrest') + '"\n')
        # Allow to call pyxelrest
        elif '    UDF_MODULES = ""\n' == xlwings_settings_line:
            pyxelrest_settings.write('    UDF_MODULES = "pyxelrest"\n')
        else:
            pyxelrest_settings.write(xlwings_settings_line)

    import xlwings
    xlwings_path = xlwings.__path__[0]
    if not os.getenv('PathToXlWingsBasFile'):
        create_environment_variable('PathToXlWingsBasFile', create_pyxelrest_bas_file())
    # Install Excel AddIn for XLWings (avoid call to external process)
    addin_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Excel', 'XLSTART', 'xlwings.xlam')
    copyfile(os.path.join(xlwings_path, 'xlwings.xlam'), addin_path)


def create_environment_variable(string_name, string_value):
    """
    Create environment variable that stay available after execution of this python script.
    The method must be run as administrator.
    :param string_name: Name of the environment variable
    :param string_value: String value of the environment variable
    :return: None
    """
    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    env = winreg.OpenKey(reg, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment", 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(env, string_name, 0, winreg.REG_EXPAND_SZ, string_value)
    winreg.CloseKey(env)
    winreg.CloseKey(reg)


def create_user_configuration():
    default_config_file = os.path.join(this_dir, 'pyxelrest', 'resources', 'config', 'default.ini')
    user_config_file = os.path.join(os.getenv('USERPROFILE'), 'pixelrest_config.ini')
    copyfile(default_config_file, user_config_file)


def get_auto_load_pyxelrest_addin():
    auto_load_pyxelrest_addin_folder = os.path.join(this_dir, '..', 'c#', 'AutoLoadPyxelRestAddIn',
                                                    'AutoLoadPyxelRestAddIn', 'bin', 'Release')
    auto_load_pyxelrest_addin_path = os.path.join(auto_load_pyxelrest_addin_folder, 'AutoLoadPyxelRestAddIn.vsto')
    if not os.path.isfile(auto_load_pyxelrest_addin_path):
        with zipfile.ZipFile(r'\\XS008183\Exchange\AutoLoadPyxelRestAddIn.zip', 'r') as packaged_addin:
            packaged_addin.extractall(auto_load_pyxelrest_addin_folder)
    return auto_load_pyxelrest_addin_path


def install_auto_load_pyxelrest():
    vsto_installer_path = os.path.join(os.getenv('commonprogramfiles'), 'microsoft shared', 'VSTO', '10.0',
                                       'VSTOInstaller.exe')
    if not os.path.isfile(vsto_installer_path):
        raise Exception('Auto Load PixelRest Excel Add-In cannot be installed as VSTO installer cannnot be found.')
    subprocess.check_call([vsto_installer_path, '/i', get_auto_load_pyxelrest_addin(), '/silent'])

create_user_configuration()
if sys.platform.startswith('win'):
    configure_xlwings_for_pyxelrest()
    install_auto_load_pyxelrest()

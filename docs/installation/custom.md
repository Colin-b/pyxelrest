# Custom pyxelrest installation

Note that the recommended way to install pyxelrest is [via the installer](installer.md).

1. [Python >= 3.7](https://www.python.org/downloads/) must be installed (with [`pip`](https://pip.pypa.io/en/stable/) for auto update to work).
2. Use [`pip`](https://pip.pypa.io/en/stable/) to install module:
```bash
python -m pip install pyxelrest
```

## Microsoft Excel add-in installation (optional)

Once `pyxelrest` python module is installed, `pyxelrest_install_addin` executable is available to install the [Microsoft Excel] COM add-in.

1. [Microsoft Excel >= 2010](https://products.office.com/en-us/excel) must be installed (Office 365 is supported).
2. [Microsoft .NET Framework >= 4.5.2](http://go.microsoft.com/fwlink/?linkid=328856) must be installed (Chances are that it is already installed).
3. Within [Microsoft Excel], `Trust access to the VBA project object model` should be enabled.
   > File > Options > Trust Center > Trust Center Settings > Macro Settings
4. [Microsoft Excel] must be closed while executing the following command:
```bash
pyxelrest_install_addin
```

Note: The add-in is not required if you only want to use `pyxelrest` [as a python module](#using-as-a-module).

### Microsoft Excel add-in installer options

| Name | Description | Possible values |
|------|-------------|-----------------|
| path_to_up_to_date_configuration | Path to up to date configuration file(s). This path will be used to keep services configuration up to date and provide a list of available services within the [Microsoft Excel] add-in. | file path, folder path or an URL returning a file content. |
| check_pre_releases | Also fetch pre-releases when checking for updates. | No value is required, providing the option is enough. Prompt only for stable releases by default. |
| source | Directory containing [Microsoft Excel] COM add-in (and optionally `pyxelrest.xlam` file). | Default to `pyxelrest_addin` folder in the python executable data directory. |
| vb_addin | Directory containing [Microsoft Excel] Visual Basic `pyxelrest.xlam` file. | Default to `pyxelrest.xlam` within `source` folder. |
| destination | Directory where add-in will be installed and add-in logs will be located. | Default to `.` folder (current location). |
| trusted_location | Trusted Microsoft Excel location where visual basic add-in will be located. | Default to `%APPDATA%\Microsoft\Excel\XLSTART` folder. |

Note: option name must be prefixed with `--` such as:
```bash
pyxelrest_install_addin --check_pre_releases
```

# How to uninstall

1. Go to `Control Panel/Programs and Features` and uninstall `PyxelRestAddIn`.
2. Execute the following command:
```bash
python -m pip uninstall pyxelrest
```
3. Remove the folder provided at add-in installation.
4. Remove `%APPDATA%\Microsoft\Excel\XLSTART\pyxelrest.xlam` file.
5. Remove `HKEY_CURRENT_USER` `Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest` registry key.

[Microsoft Excel]: https://products.office.com/en-us/excel

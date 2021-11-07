# Advanced configuration

## Microsoft Excel COM add-in configuration

<p align="center">
  <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/check_for_update_on_close.gif" alt='Managing auto update'>
</p>
<p align="center"><em>Auto update can be (de)activated from Microsoft Excel thanks to the <span style="color: #1382CE">Check for update on close</span> button within <span style="color: #1E1E1F">PyxelRest</span> tab.</em></p>

Configuration can also be manually updated thanks to `excel_addin\PyxelRestAddIn.dll.config` file located in the folder provided at add-in installation.

The following application settings are available:

| Name | Description | Mandatory | Possible values |
|------|-------------|-----------|-----------------|
| PathToPython | Path to the python.exe (including) executable where pyxelrest python module was installed. | Mandatory | Installation script is already setting this value properly. |
| AutoCheckForUpdates | Activate or Deactivate automatic check for PyxelRest update while Microsoft Excel is running. | Optional | True (default), False |
| GenerateUDFAtStartup | Activate or Deactivate generation of user defined functions at Microsoft Excel startup. | Optional | True (default), False |
| PathToXlWingsBasFile | Path to the XlWings modified BAS file used to configure XlWings for PyxelRest. | Mandatory | Installation script is already setting this value properly. |
| CheckPreReleases | Should auto update fetch pre-releases. | Optional | True, False (default). |

The path to up to date configurations can be modified thanks to `PathToUpToDateConfigurations` registry key within `HKEY_CURRENT_USER` `Software\Microsoft\Windows\CurrentVersion\Uninstall\PyxelRest`.

## Logging configuration

`pyxelrest` module logging configuration can be updated thanks to `configuration\logging.yml` file within the folder provided at add-in installation.

[Microsoft Excel] COM add-in logging configuration can be updated thanks to `excel_addin\PyxelRestAddIn.dll.config` file located in the folder provided at add-in installation.

Log files can be found in your `logs` folder located in the folder provided at add-in installation.

<p align="center">
  <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/open_logs.gif" alt='How to open logs'>
</p>
<p align="center"><em>This folder can be accessed from Microsoft Excel thanks to the <span style="color: #1382CE">Open Logs</span> button within <span style="color: #1E1E1F">PyxelRest</span> tab.</em></p>

[Microsoft Excel]: https://products.office.com/en-us/excel

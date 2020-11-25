# Developer Installation

1. Within [Microsoft Excel], `Trust access to the VBA project object model` should be enabled.
   > File > Options > Trust Center > Trust Center Settings > Macro Settings
2. Build the add-in C# solution using [Microsoft Visual Studio](https://visualstudio.microsoft.com):

   In order to do so, you need [Office Developer Tools for Visual Studio](https://visualstudio.microsoft.com/vs/features/office-tools/) to be installed.
   You also need to create a test certificate.
   > Project > PyxelRestAddIn > Signing
3. [Microsoft Excel] must be closed while executing the following script from within `pyxelrest` root folder (make sure your virtual environment is activated beforehand if needed):
```batch
developer_install.bat
```

[Microsoft Excel]: https://products.office.com/en-us/excel

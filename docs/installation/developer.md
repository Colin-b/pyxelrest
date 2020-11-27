# Developer Installation

Considering you already fetched the source code and you are located inside the root folder:

1. Within [Microsoft Excel], `Trust access to the VBA project object model` should be enabled.
   > File > Options > Trust Center > Trust Center Settings > Macro Settings
2. Build the add-in C# solution using [Microsoft Visual Studio](https://visualstudio.microsoft.com):
    1. [Office Developer Tools for Visual Studio](https://visualstudio.microsoft.com/vs/features/office-tools/) needs to be installed.
        <p align="center">
            <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/visual_studio_office_option.png" alt='Select office development additional package'>  
            <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/visual_studio_office_option_vsto.png" alt='VSTO must be checked'>  
        </p>
    
    2. Open `addin`/`PyxelRestAddIn.sln`.
    3. Create a test certificate
       > Project > PyxelRestAddIn > Signing

3. Install all `pyxelrest` python module dependencies:
    ```batch
    python -m pip install .[testing]
    ```
4. [Microsoft Excel] must be closed while executing the following script:
    ```batch
    python pyxelrest/install_addin.py --source addin/PyxelRestAddIn/bin/Release
    ```

[Microsoft Excel]: https://products.office.com/en-us/excel

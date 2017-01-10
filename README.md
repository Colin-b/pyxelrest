Access REST APIs from Excel using User Defined Functions (UDF)
==============================================================
PyxelRest allow you to query [Swagger 2.0/OpenAPI](https://www.openapis.org) REST APIs using Excel User Defined Functions.

How to use
----------

Once installed, open Microsoft Excel and add services within PyxelRest configuration.

![Microsoft Excel add-in](addin/AutoLoadPyxelRestAddIn/resources/screenshot_pyxelrest_auto_load_ribbon.PNG)

![Configuration screen](addin/AutoLoadPyxelRestAddIn/resources/screenshot_configure_pyxelrest_services.PNG)

User Installation
------------

1. This step will certainly be removed in the future, but in the meantime: Within Excel, ``Trust access to the VBA project object model`` should be enabled.
> File > Options > Trust Center > Trust Center Settings > Macro Settings
2. Excel must be closed while executing the following step.

        pip install pypiwin32 --trusted-host rms.gdfsuez.net --index http://rms.gdfsuez.net:8310/artifactory/api/pypi/python/simple
        pip install pyxelrest --trusted-host rms.gdfsuez.net --index http://rms.gdfsuez.net:8310/artifactory/api/pypi/python/simple

Upgrade
-------

1. Go to ``Control Panel/Programs and Features`` and uninstall AutoLoadPyxelRestAddIn (in case version changed).
2. Follow installation but add ``--upgrade`` option on ``pip install`` commands.

Uninstall
---------

1. Go to ``Control Panel/Programs and Features`` and uninstall AutoLoadPyxelRestAddIn.
2. Execute the following command:

        pip uninstall pyxelrest
3. Remove ``%APPDATA%\pyxelrest`` folder.
4. Remove ``%APPDATA%\Microsoft\Excel\XLSTART\pyxelrest.xlam`` file.

Logging
-------
Should you need to investigate what went wrong, logs can be found within your ``%APPDATA%\pyxelrest`` folder.

Developer Installation/Upgrade
----------------------

1. This step will certainly be removed in the future, but in the meantime: Within Excel, ``Trust access to the VBA project object model`` should be enabled.
> File > Options > Trust Center > Trust Center Settings > Macro Settings
2. Build the addin C# solution:
In order to do so, you need to add a test certificate.
> Project > AutoLoadPyxelRestAddIn > Signing
3. Excel must be closed while executing the following script from within pyxelrest root folder:

        developer_install.bat

Enhancements TODO list
----------------------

- Handle streaming of data back to Excel (reduce memory consumption).
- Handle structure with dictionaries nested in dictionaries.
- Full Swagger 2.0 specification support:
    - Handle multiple ways of sending arrays (for now arrays are sent as replication of the same parameter name).
    - etc...
- Add client logs to splunk? (it should be generic with default settings to file anyway)
- Handle filtering on Swagger tags
- Add test specific module requirements in setup.
- Do not package test module.
- Add more test cases actually performing calls to functions.
- Get rid of xlwings bas file by including what is required in our own addin.

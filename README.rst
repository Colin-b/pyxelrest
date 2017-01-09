Access REST APIs from Excel using User Defined Functions (UDF)
==============================================================
PyxelRest allow you to query `Swagger 2.0/OpenAPI <https://www.openapis.org>`_ REST APIs using Excel User Defined Functions.

How to use
----------

Once installed, open Microsoft Excel and add services within PyxelRest configuration.

.. figure:: addin/AutoLoadPyxelRestAddIn/resources/screenshot_pyxelrest_auto_load_ribbon.PNG
   :align: center

   Microsoft Excel add-in

.. figure:: addin/AutoLoadPyxelRestAddIn/resources/screenshot_configure_pyxelrest_services.PNG
   :align: center

   Configuration screen

Installation
------------

#. This step will certainly be removed in the future, but in the meantime: Within Excel, ``Trust access to the VBA project object model`` should be enabled.
> File > Options > Trust Center > Trust Center Settings > Macro Settings
#. Excel must be closed while executing the following step.
        >>> pip install pypiwin32 --trusted-host rms.gdfsuez.net --index http://rms.gdfsuez.net:8310/artifactory/api/pypi/python/simple
        >>> pip install pyxelrest --trusted-host rms.gdfsuez.net --index http://rms.gdfsuez.net:8310/artifactory/api/pypi/python/simple

Upgrade
-------

1. Uninstall AutoLoadPyxelRestAddIn (in case version changed).
2. Follow installation but add ``--upgrade`` option on ``pip install`` commands.

Uninstall
---------

1. Uninstall AutoLoadPyxelRestAddIn.
2. Execute the following command:
        >>> pip uninstall pyxelrest
3. Remove ``%APPDATA%\pyxelrest`` folder.
4. Remove ``%APPDATA%\Microsoft\Excel\XLSTART\pyxelrest.xlam`` file.

Logging
-------
Should you need to investigate what went wrong, logs can be found within your ``%APPDATA%\pyxelrest`` folder.

Developer Installation
----------------------

1. This step will certainly be removed in the future, but in the meantime: Within Excel, ``Trust access to the VBA project object model`` should be enabled.
> File > Options > Trust Center > Trust Center Settings > Macro Settings
2. Excel must be closed while executing the following step from within pyxelrest root folder (Note that for the moment you still need to build the addin C# solution by yourself):
        >>> pip install pypiwin32 --trusted-host rms.gdfsuez.net --index http://rms.gdfsuez.net:8310/artifactory/api/pypi/python/simple
        >>> pip install -e . --trusted-host rms.gdfsuez.net --index http://rms.gdfsuez.net:8310/artifactory/api/pypi/python/simple
        >>> python pyxelrest_post_install.py --addindirectory addin/AutoLoadPyxelRestAddIn/bin/Release --vbaddindirectory addin

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
- Clean up list of addin files that are packaged (App.config is useless).
- Add more test cases actually performing calls to functions.
- Get rid of xlwings bas file by including what is required in our own addin.

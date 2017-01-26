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

#. Within Excel, ``Trust access to the VBA project object model`` should be enabled.
> File > Options > Trust Center > Trust Center Settings > Macro Settings
#. Excel must be closed while executing the following commands:
        >>> pip install pypiwin32
        >>> pip install pyxelrest

Upgrade
-------

#. Excel must be closed while executing the following command:
        >>> pip install pyxelrest --upgrade

Uninstall
---------

1. Uninstall AutoLoadPyxelRestAddIn.
2. Execute the following command:
        >>> pip uninstall pyxelrest
3. Remove ``%APPDATA%\pyxelrest`` folder.
4. Remove ``%APPDATA%\Microsoft\Excel\XLSTART\pyxelrest.xlam`` file.

Logging
-------
Default log files can be found in your ``%APPDATA%\pyxelrest`` folder.
Logging configuration can be updated thanks to ``%APPDATA%\pyxelrest\logging_configuration.ini`` file.

Developer Installation/Upgrade
------------------------------

1. Within Excel, ``Trust access to the VBA project object model`` should be enabled.
> File > Options > Trust Center > Trust Center Settings > Macro Settings
2. Build the addin C# solution:
In order to do so, you need to add a test certificate.
> Project > AutoLoadPyxelRestAddIn > Signing
3. Excel must be closed while executing the following script from within pyxelrest root folder:
        >>> developer_install.bat

Known issues
------------

- Excel needs to be restarted for UDFs not to be displayed anymore in function wizard. (Even if calling them does not work)

Enhancements TODO list
----------------------

- Handle streaming of data back to Excel (reduce memory consumption).
- Handle structure with dictionaries nested in dictionaries.
- Full Swagger 2.0 specification support:
    - Handle multiple ways of sending arrays (for now arrays are sent as replication of the same parameter name).
    - etc...
- Handle filtering on Swagger tags
- Get rid of xlwings bas file by including what is required in our own addin.

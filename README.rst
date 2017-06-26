Access REST APIs from Microsoft Excel using User Defined Functions (UDF)
========================================================================
PyxelRest allow you to query `Swagger 2.0/OpenAPI <https://www.openapis.org>`_ REST APIs using Microsoft Excel User Defined Functions.

Usage
-----

Once installed, open Microsoft Excel and UDFs from configured services will be available.

.. figure:: addin/AutoLoadPyxelRestAddIn/resources/screenshot_udfs_category.PNG
   :align: center

   Selecting UDF

.. figure:: addin/AutoLoadPyxelRestAddIn/resources/screenshot_udf_arguments.PNG
   :align: center

   Filling in UDF parameters

UDFs are automatically updated on Microsoft Excel start and on Configuration update.

Updating UDFs without restarting Microsoft Excel or updating configuration can be done thanks to the ``Update Functions`` button within ``PyxelRest`` tab.

.. figure:: addin/AutoLoadPyxelRestAddIn/resources/screenshot_pyxelrest_auto_load_ribbon.PNG
   :align: center

   Microsoft Excel add-in

Installation
------------
Pre requisites
--------------

- [Python](https://www.python.org/downloads/) must be installed.
- [Microsoft Excel](https://products.office.com/en-us/excel) must be installed.
- [Microsoft .NET Framework 4.5.2](http://go.microsoft.com/fwlink/?linkid=328856) must be installed.

User Installation (using PIP)
-----------------------------

#. Within Microsoft Excel, ``Trust access to the VBA project object model`` should be enabled.
> File > Options > Trust Center > Trust Center Settings > Macro Settings
#. Microsoft Excel must be closed while executing the following command:
        >>> pip install pyxelrest

User Uninstall (using PIP)
--------------------------

1. Uninstall AutoLoadPyxelRestAddIn.
2. Execute the following command:
        >>> pip uninstall pyxelrest
3. Remove ``%APPDATA%\pyxelrest`` folder.
4. Remove ``%APPDATA%\Microsoft\Excel\XLSTART\pyxelrest.xlam`` file.

Developer Installation (using PIP)
----------------------------------

1. Within Microsoft Excel, ``Trust access to the VBA project object model`` should be enabled.
> File > Options > Trust Center > Trust Center Settings > Macro Settings
2. Build the add-in C# solution:
In order to do so, you need to add a test certificate.
> Project > AutoLoadPyxelRestAddIn > Signing
3. Microsoft Excel must be closed while executing the following script from within pyxelrest root folder:
        >>> developer_install.bat

Optional Dependencies
---------------------

- Support for ``application/msgpackpandas``
    - Pandas encoded msgpack will be used if ``pandas`` and ``msgpack-python`` modules are available.

- Support for ``ujson``
    - JSON responses deserialization (when rely_on_definitions is set to True) will rely on ``ujson`` in case ``ujson`` module is available.

- Support for ``requests_ntlm``
    - ``requests_ntlm`` is required in case auth=ntlm is set in ``security_details`` property and custom credentials are provided.

- Support for ``requests_negotiate_sspi``
    - ``requests_negotiate_sspi`` is required in case auth=ntlm is set in ``security_details`` property and logged in user credentials should be used..

Configuration
-------------

Services Configuration
----------------------

Services configuration can be done within Microsoft Excel thanks to the ``Configure Services`` button within ``PyxelRest`` tab.

.. figure:: addin/AutoLoadPyxelRestAddIn/resources/screenshot_pyxelrest_auto_load_ribbon.PNG
   :align: center

   Microsoft Excel add-in

.. figure:: addin/AutoLoadPyxelRestAddIn/resources/screenshot_configure_pyxelrest_services.PNG
   :align: center

   Configuration screen

Configuration can also be manually updated thanks to ``%APPDATA%\pyxelrest\configuration\services.ini`` file.

Each section name will be used as the UDFs category.

Each UDF will be prefixed by the section name (only [a-zA-Z0-9_] characters will be kept).

The following options are available for each section:

+------------------------+--------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------------+
|                        | Description                                                                                                  | Mandatory | Possible values                           |
+========================+==============================================================================================================+===========+===========================================+
| swagger_url            | Complete URL to the Swagger definition. It can also be a system file path if specified using file:// prefix. | Mandatory |                                           |
+------------------------+--------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------------+
| proxy_url              | Proxy that should be used to reach service.                                                                  | Optional  |                                           |
+------------------------+--------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------------+
| service_host           | Service host in case your service is behind a reverse proxy.                                                 | Optional  |                                           |
+------------------------+--------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------------+
| methods                | List of services methods to be exposed as UDFs.                                                              | Optional  | get, post, put, delete                    |
+------------------------+--------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------------+
| tags                   | Swagger tags that should be retrieved. If not specified, no filtering is applied.                            | Optional  | any value separated by ','                |
+------------------------+--------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------------+
| connect_timeout        | Maximum amount of time, in seconds, to wait when trying to reach the service. Wait for 1 second by default.  | Optional  | any float value (decimal separator is .)  |
+------------------------+--------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------------+
| read_timeout           | Maximum amount of time, in seconds, to wait when requesting a service. Infinite wait by default.             | Optional  | any float value (decimal separator is .)  |
+------------------------+--------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------------+
| security_details       | Extra security information not provided by swagger.                                                          | Optional  | port=XX,timeout=YY                        |
+------------------------+--------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------------+
| advanced_configuration | Additional configuration details                                                                             | Optional  | udf_return_type=XX,rely_on_definitions=YY |
+------------------------+--------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------------+

Security Details
----------------

Additional security details can be provided thanks to ``security_details`` property.

This property is supposed to contains key=value information. Separator is ',' (comma).

Values cannot contains "," character.
Values can be environment variables if provided in the form %MY_ENV_VARIABLE% (for MY_ENV_VARIABLE environment variable).

Depending on the type of authentication, the following keys are available:

Common
------

+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                      | Description                                                                                                                                                                                     |
+======================+=================================================================================================================================================================================================+
| auth                 | Custom authentication mechanism. Valid value is ntlm (requiring ``requests_ntlm`` or ``requests_negotiate_sspi``).                                                                              |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

OAuth 2
-------

If response_type is not provided in authorization_url, token is expected to be received in "token" field.

+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
|                      | Description                                                                                                                                                      | Mandatory |
+======================+==================================================================================================================================================================+===========+
| port                 | Port on which the authentication response is supposed to be received. Default value is 5000.                                                                     | Optional  |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| timeout              | Maximum number of seconds to wait for the authentication response to be received. Default value is 20 seconds.                                                   | Optional  |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| oauth2.XXXX          | Where XXXX is the name of the parameter in the authorization URL. You can find more details on https://tools.ietf.org/html/rfc6749#section-4.2.1                 | Optional  |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| success_display_time | Amount of milliseconds to wait before closing the authentication response page on success and returning back to Microsoft Excel. Default value is 1 millisecond. | Optional  |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| failure_display_time | Amount of milliseconds to wait before closing the authentication response page on failure and returning back to Microsoft Excel. Default value is 5 seconds.     | Optional  |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

API Key
-------

+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
|                      | Description                                                                                                                                                      | Mandatory |
+======================+==================================================================================================================================================================+===========+
| api_key              | User API Key.                                                                                                                                                    | Mandatory |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Basic
-----

+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
|                      | Description                                                                                                                                                      | Mandatory |
+======================+==================================================================================================================================================================+===========+
| username             | User name.                                                                                                                                                       | Mandatory |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| password             | User password.                                                                                                                                                   | Mandatory |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

NTLM
----

+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
|                      | Description                                                                                                                                                      | Mandatory |
+======================+==================================================================================================================================================================+===========+
| username             | User name. Should be of the form domain\\user. Default value is the logged in user name.                                                                         | Optional  |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| password             | User password. Default value is the logged in user password.                                                                                                     | Optional  |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Advanced Configuration
----------------------

Additional configuration details can be provided thanks to ``advanced_configuration`` property.

This property is supposed to contains key=value information. Separator is ',' (comma).

Values cannot contains "," character.

+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+
|                     | Description                                                                                                                                                                           | Possible values             |
+=====================+=======================================================================================================================================================================================+=============================+
| udf_return_type     | synchronous if you want your UDF to return the final result immediately. It means that you will have to specify all the cells that will contains the result. asynchronous by default. | asynchronous or synchronous |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+
| rely_on_definitions | Rely on swagger definitions to re-order fields received in JSON response. Deactivated by default.                                                                                     | True or False               |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+

Logging Configuration
---------------------

PyxelRest logging configuration can be updated thanks to ``%APPDATA%\pyxelrest\configuration\logging.ini`` file.

PyxelRest auto-update logging configuration can be updated thanks to ``%APPDATA%\pyxelrest\configuration\auto_update_logging.ini`` file.

Microsoft Excel Auto-Load add-in logging configuration can be updated thanks to ``%APPDATA%\pyxelrest\configuration\addin.config`` file.

Default log files can be found in your ``%APPDATA%\pyxelrest\logs`` folder.

This folder can easily be accessed thanks to the ``Open Logs`` button within ``PyxelRest`` tab.

.. figure:: addin/AutoLoadPyxelRestAddIn/resources/screenshot_pyxelrest_auto_load_ribbon.PNG
   :align: center

   Microsoft Excel add-in

Microsoft Excel Auto-Load add-in Configuration
----------------------------------------------

Auto check for update can be activated/deactivated within Microsoft Excel thanks to the ``Check for update on close`` button within ``PyxelRest`` tab.

.. figure:: addin/AutoLoadPyxelRestAddIn/resources/screenshot_pyxelrest_auto_load_ribbon.PNG
   :align: center

   Microsoft Excel add-in

Configuration can also be manually updated thanks to ``%APPDATA%\pyxelrest\configuration\addin.config`` file.

The following application settings are available:

+----------------------+------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------+
|                      | Description                                                                                    | Mandatory | Possible values                                             |
+======================+================================================================================================+===========+=============================================================+
| PathToPIP            | Path to the pip.exe (including) executable that should be used to update PyxelRest.            | Mandatory | Installation script is already setting this value properly. |
+----------------------+------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------+
| PathToPython         | Path to the python.exe (including) executable that should be used to launch the update script. | Mandatory | Installation script is already setting this value properly. |
+----------------------+------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------+
| PathToUpdateScript   | Path to the Python script used to update PyxelRest.                                            | Mandatory | Installation script is already setting this value properly. |
+----------------------+------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------+
| AutoCheckForUpdates  | Activate or Deactivate automatic check for PyxelRest update on Microsoft Excel closing.        | Optional  | True (default), False                                       |
+----------------------+------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------+
| PathToXlWingsBasFile | Path to the Python script used to update PyxelRest.                                            | Mandatory | Default value is already set.                               |
+----------------------+------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------+

Using as a module
-----------------

You can use pyxelrest as a python module as well.

Generating user defined functions
---------------------------------

When GENERATE_UDF_ON_IMPORT is set to True (default behavior), UDFs are generated by  loading (e.g. on first import)
pyxelrestgenerator.py.

You can manually regenerate UDFs by calling pyxelrestgenerator.generate_user_defined_functions().

All UDFs can be found within user_defined_functions.py.

Caching results
---------------

For testing purposes mainly, you can cache UDFs calls by using caching.py.
This serves as an automatic mocking feature.

The call to caching init method must be done prior to generating UDFs.

On disk
-------

init_disk_cache(<filename>) must be called to initialize the disk cache file.

In memory
---------

This cache has an expiry in second and a maximum size.
init_memory_cache(<maxsize>,<expiry>) must be called to initialize the mamory cache.
The cachetools module is required.

Frequently Asked Question
-------------------------

Microsoft Excel Wizard does not show any parameter
--------------------------------------------------

In case your UDF has a lot of parameters, then Microsoft Excel is unable to display them all in the function wizard.

Try reducing the number of parameters in your service.

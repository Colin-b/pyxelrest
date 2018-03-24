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

- [Python >= 2.7](https://www.python.org/downloads/) must be installed.
- [Microsoft Excel >= 2010](https://products.office.com/en-us/excel) must be installed.
- [Microsoft .NET Framework >= 4.5.2](http://go.microsoft.com/fwlink/?linkid=328856) must be installed.

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
    - ``requests_negotiate_sspi`` is required in case auth=ntlm is set in ``security_details`` property and logged in user credentials should be used.

- Support for ``cachetool``
    - ``cachetool`` is required to be able to use in-memory caching.

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

+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------------------------------+
|                        | Description                                                                                                                                                    | Mandatory | Possible values                              |
+========================+================================================================================================================================================================+===========+==============================================+
| swagger_url            | URL to the Swagger definition. http, https and file scheme are supported. For more details on what is a URL, please refer to https://en.wikipedia.org/wiki/URL | Mandatory |                                              |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------------------------------+
| proxy_url              | Proxy that should be used to reach service. If this is an URL, then this proxy will be used for the swagger_url scheme only.                                   | Optional  |                                              |
|                        | If you want to specify a proxy for a different scheme, then this value should be scheme=proxy_url_for_this_scheme.                                             |           |                                              |
|                        | You can specify multiple schemes by using comma as a separator. You can also use no_proxy as a scheme for a no_proxy url.                                      |           |                                              |
|                        | For more details refer to http://docs.python-requests.org/en/master/user/advanced/#proxies                                                                     |           |                                              |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------------------------------+
| service_host           | Service host in case your service is behind a reverse proxy.                                                                                                   | Optional  |                                              |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------------------------------+
| methods                | List of services methods to be exposed as UDFs. Retrieve all standards HTTP methods by default (get, post, put, delete, patch, options, head).                 | Optional  | get, post, put, delete, patch, options, head |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------------------------------+
| security_details       | Extra security information not provided by swagger. Refer to Security Details section for more information.                                                    | Optional  | port=XX,timeout=YY                           |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------------------------------+
| advanced_configuration | Additional configuration details. Refer to Advanced Configuration section for more information.                                                                | Optional  | udf_return_type=XX,rely_on_definitions=YY    |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------------------------------+

Security Details
----------------

Additional security details can be provided thanks to ``security_details`` property.

This property is supposed to contains key=value information. Separator is ',' (comma).

Values cannot contains "," character.
Values can be environment variables if provided in the form %MY_ENV_VARIABLE% (for MY_ENV_VARIABLE environment variable).

Depending on the type of authentication, the following keys are available:

Common
------

+------+--------------------------------------------------------------------------------------------------------------------+
|      | Description                                                                                                        |
+======+====================================================================================================================+
| auth | Custom authentication mechanism. Valid value is ntlm (requiring ``requests_ntlm`` or ``requests_negotiate_sspi``). |
+------+--------------------------------------------------------------------------------------------------------------------+

OAuth 2
-------

If response_type is not provided in authorization_url, token is expected to be received in "token" field.

+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
|                      | Description                                                                                                                                                      | Mandatory |
+======================+==================================================================================================================================================================+===========+
| port                 | Port on which the authentication response is supposed to be received. Default value is 5000.                                                                     | Optional  |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| timeout              | Maximum number of seconds to wait for the authentication response to be received. Default value is 1 minute.                                                     | Optional  |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| oauth2.XXXX          | Where XXXX is the name of the parameter in the authorization URL. You can find more details on https://tools.ietf.org/html/rfc6749#section-4.2.1                 | Optional  |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| success_display_time | Amount of milliseconds to wait before closing the authentication response page on success and returning back to Microsoft Excel. Default value is 1 millisecond. | Optional  |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| failure_display_time | Amount of milliseconds to wait before closing the authentication response page on failure and returning back to Microsoft Excel. Default value is 5 seconds.     | Optional  |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

API Key
-------

+---------+---------------+-----------+
|         | Description   | Mandatory |
+=========+===============+===========+
| api_key | User API Key. | Mandatory |
+---------+---------------+-----------+

Basic
-----

+----------+----------------+-----------+
|          | Description    | Mandatory |
+==========+================+===========+
| username | User name.     | Mandatory |
+----------+----------------+-----------+
| password | User password. | Mandatory |
+----------+----------------+-----------+

NTLM
----

+----------+------------------------------------------------------------------------------------------+-----------+
|          | Description                                                                              | Mandatory |
+==========+==========================================================================================+===========+
| username | User name. Should be of the form domain\\user. Default value is the logged in user name. | Optional  |
+----------+------------------------------------------------------------------------------------------+-----------+
| password | User password. Default value is the logged in user password.                             | Optional  |
+----------+------------------------------------------------------------------------------------------+-----------+

Advanced Configuration
----------------------

Additional configuration details can be provided thanks to ``advanced_configuration`` property.

This property is supposed to contains key=value information. Separator is ',' (comma).

Values cannot contains "," character.
Values can be environment variables if provided in the form %MY_ENV_VARIABLE% (for MY_ENV_VARIABLE environment variable).

+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
|                      | Description                                                                                                                                                                                                  | Possible values                                                                       |
+======================+==============================================================================================================================================================================================================+=======================================================================================+
| udf_return_type      | synchronous if you want your UDF to return the final result immediately. It means that you will have to specify all the cells that will contains the result. asynchronous by default.                        | asynchronous or synchronous. Both values can be provided separated by ';' (semicolon) |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| rely_on_definitions  | Rely on swagger definitions to re-order fields received in JSON response. Deactivated by default.                                                                                                            | True or False                                                                         |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| max_retries          | Maximum number of time a request should be retried before considered as failed. 5 by default.                                                                                                                | Any positive integer value                                                            |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| header.XXXX          | Where XXXX is the name of the header that should be sent with every request sent to this service.                                                                                                            |                                                                                       |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| connect_timeout      | Maximum amount of time, in seconds, to wait when trying to reach the service. Wait for 1 second by default. For more details refer to http://docs.python-requests.org/en/master/user/advanced/#timeouts      | any float value (decimal separator is .)                                              |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| read_timeout         | Maximum amount of time, in seconds, to wait when requesting a service. Infinite wait by default. For more details refer to http://docs.python-requests.org/en/master/user/advanced/#timeouts                 | any float value (decimal separator is .)                                              |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| swagger_read_timeout | Maximum amount of time, in seconds, to wait when requesting a swagger definition. Wait for 5 seconds by default. For more details refer to http://docs.python-requests.org/en/master/user/advanced/#timeouts | any float value (decimal separator is .)                                              |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| tags                 | Swagger tags that should be retrieved. If not specified, no filtering is applied. For more details refer to https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md                         | any value separated by ';' (semicolon)                                                |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

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

+------------------------------+------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------+
|                              | Description                                                                                    | Mandatory | Possible values                                             |
+==============================+================================================================================================+===========+=============================================================+
| PathToPython                 | Path to the python.exe (including) executable that should be used to launch the update script. | Mandatory | Installation script is already setting this value properly. |
+------------------------------+------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------+
| PathToUpdateScript           | Path to the Python script used to update PyxelRest.                                            | Mandatory | Installation script is already setting this value properly. |
+------------------------------+------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------+
| AutoCheckForUpdates          | Activate or Deactivate automatic check for PyxelRest update on Microsoft Excel closing.        | Optional  | True (default), False                                       |
+------------------------------+------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------+
| GenerateUDFAtStartup         | Activate or Deactivate generation of user defined functions at Microsoft Excel startup.        | Optional  | True (default), False                                       |
+------------------------------+------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------+
| PathToXlWingsBasFile         | Path to the Python script used to update PyxelRest.                                            | Mandatory | Default value is already set.                               |
+------------------------------+------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------+
| PathToUpToDateConfigurations | Path to the file or directory containing up to date services configuration.                    | Optional  |                                                             |
+------------------------------+------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------+

Using as a module
-----------------

You can use pyxelrest as a python module as well::

   import pyxelrest

   # Avoid the following import statement to generate UDFs
   pyxelrest.GENERATE_UDF_ON_IMPORT = False

   from pyxelrest import pyxelrestgenerator

   # Generate UDFs for the following import
   pyxelrestgenerator.generate_user_defined_functions()

   from pyxelrest import user_defined_functions

   # UDFs are available as python functions within user_defined_functions and can be used as such

Generating user defined functions
---------------------------------

When ::GENERATE_UDF_ON_IMPORT:: is set to ::True:: (default behavior), UDFs are generated by loading (e.g. on first import) pyxelrest.pyxelrestgenerator.py.

You can manually regenerate UDFs by calling ::pyxelrest.pyxelrestgenerator.generate_user_defined_functions()

All UDFs can be found within pyxelrest.user_defined_functions.py.

Caching results
---------------

For testing purposes mainly, you can cache UDFs calls by using pyxelrest.caching.py.
This serves as an automatic mocking feature.

The call to caching init method must be done prior to generating UDFs.

On disk
-------

::init_disk_cache(<filename>):: must be called to initialize the disk cache file.

In memory
---------

This cache has an expiry in second and a maximum size.
::init_memory_cache(<maxsize>,<expiry>):: must be called to initialize the memory cache.

The cachetools module is required for this feature to be available.

Frequently Asked Question
-------------------------

Microsoft Excel Wizard does not show any parameter
--------------------------------------------------

In case your UDF has a lot of parameters, then Microsoft Excel is unable to display them all in the function wizard.

Try reducing the number of parameters in your service.

No command specified in the configuration, cannot autostart server
------------------------------------------------------------------

This error will happen in case you manually specified in your xlwings.bas file to use debug server but did not uncomment the main function starting the server on pyxelrest module side.

Microsoft Excel Add-In cannot be installed
------------------------------------------

Check that all requirements are met:
- [Microsoft .NET Framework >= 4.5.2](http://go.microsoft.com/fwlink/?linkid=328856) must be installed.
- [Microsoft Visual Studio 2010 Tools for Office Runtime](https://www.microsoft.com/en-us/download/details.aspx?id=48217) must be installed.

In case you encounter an issue like `Could not load file or assembly 'Microsoft.Office.BusinessApplications.Fba...` anyway, you then need to remove `C:\Program Files\Common Files\Microsoft Shared\VSTO\10.0\VSTOInstaller.exe.config` file.

Dates with a year higher than 3000 are not converted to local timezone
----------------------------------------------------------------------

Due to timestamp limitation, dates after `3000-12-31` and date time after `3001-01-01T07:59:59+00:00` cannot be converted to local timezone.

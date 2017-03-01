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
User Installation
-----------------

#. Within Microsoft Excel, ``Trust access to the VBA project object model`` should be enabled.
> File > Options > Trust Center > Trust Center Settings > Macro Settings
#. Microsoft Excel must be closed while executing the following command:
        >>> pip install pyxelrest

User Upgrade
------------

#. Microsoft Excel must be closed while executing the following command:
        >>> pip install pyxelrest --upgrade

User Uninstall
--------------

1. Uninstall AutoLoadPyxelRestAddIn.
2. Execute the following command:
        >>> pip uninstall pyxelrest
3. Remove ``%APPDATA%\pyxelrest`` folder.
4. Remove ``%APPDATA%\Microsoft\Excel\XLSTART\pyxelrest.xlam`` file.

Developer Installation/Upgrade
------------------------------

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

+--------------+-----------------------------------------------------------------------------------+-----------+----------------------------+
|              | Description                                                                       | Mandatory | Possible values            |
+==============+===================================================================================+===========+============================+
| swagger_url  | Complete URL to the Swagger definition.                                           | Mandatory |                            |
+--------------+-----------------------------------------------------------------------------------+-----------+----------------------------+
| proxy_url    | Proxy that should be used to reach service.                                       | Optional  |                            |
+--------------+-----------------------------------------------------------------------------------+-----------+----------------------------+
| service_host | Service host in case your service is behind a reverse proxy.                      | Optional  |                            |
+--------------+-----------------------------------------------------------------------------------+-----------+----------------------------+
| methods      | List of services methods to be exposed as UDFs.                                   | Optional  | get, post, put, delete     |
+--------------+-----------------------------------------------------------------------------------+-----------+----------------------------+
| tags         | Swagger tags that should be retrieved. If not specified, no filtering is applied. | Optional  | any value separated by ',' |
+--------------+-----------------------------------------------------------------------------------+-----------+----------------------------+

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

+---------------------+------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------+
|                     | Description                                                                                    | Mandatory | Possible values                                             |
+=====================+================================================================================================+===========+=============================================================+
| PathToPIP           | Path to the pip.exe (including) executable that should be used to update PyxelRest.            | Mandatory | Installation script is already setting this value properly. |
+---------------------+------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------+
| PathToPython        | Path to the python.exe (including) executable that should be used to launch the update script. | Mandatory | Installation script is already setting this value properly. |
+---------------------+------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------+
| PathToUpdateScript  | Path to the Python script used to update PyxelRest.                                            | Mandatory | Installation script is already setting this value properly. |
+---------------------+------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------+
| AutoCheckForUpdates | Activate or Deactivate automatic check for PyxelRest update on Microsoft Excel closing.        | Optional  | True (default), False                                       |
+---------------------+------------------------------------------------------------------------------------------------+-----------+-------------------------------------------------------------+

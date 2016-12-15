Access REST APIs from Excel using User Defined Functions (UDF)
==============================================================
PyxelRest allow you to query `Swagger 2.0/OpenAPI <https://www.openapis.org>`_ REST APIs using Excel User Defined Functions.

How to use
----------

#. Update the configuration so that it contains the required services.
#. Launch Excel.

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

Configuration
-------------
Services to be exposed can be configured thanks to ``%APPDATA%\pyxelrest\pixelrest_config.ini`` file.

Each section corresponds to a service.

The following mandatory properties are available:

- **host**: URI to the service base path.

The following optional properties are available:

- **swaggerBasePath**: URI to retrieve the Swagger JSON. Default value is */*.
- **methods**: List (separator is ",") of service methods to be exposed, all by default, amongst:

    - *get*
    - *post*
    - *put*
    - *delete*


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
        >>> python pyxelrest_post_install.py --addindirectory addin/AutoLoadPyxelRestAddIn/bin/Release

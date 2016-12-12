Access REST APIs from Excel using User Defined Functions (UDF)
==============================================================
PyxelRest allow you to query Swagger/OpenAPI REST APIs using Excel User Defined Functions.

How to use
----------

1. Update the configuration so that it contains the required services.
2. Launch an existing Excel file or create a new one.
3. Hit ``Import Python UDFs`` button within xlwings tab
4. Enjoy

Installation
------------

1. This step will certainly be removed in the future, but in the meantime: Within Excel, ``Trust access to the VBA project object model`` should be enabled.
> File > Options > Trust Center > Trust Center Settings > Macro Settings
2. Excel must be closed while executing the following step.

    - For *Python 2* users, from an elevated command prompt, execute the following commands:
    
            pip install pypiwin32 --trusted-host rms.gdfsuez.net --index http://rms.gdfsuez.net:8310/artifactory/api/pypi/python/simple
            pip install --egg pyxelrest --trusted-host rms.gdfsuez.net --index http://rms.gdfsuez.net:8310/artifactory/api/pypi/python/simple
    - For *Python 3* users the following steps must be performed:

        1. *PyWin32* should be [downloaded](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pywin32).
        2. And installed thanks to the following command:
        
                pip install pywin32-220.1-cp36-cp36m-win_amd64.whl
        3. Finally, from an elevated command prompt, execute the following command from your python directory:
        
                python.exe Scripts\pywin32_postinstall.py -install
        4. Project must be installed. From an elevated command prompt, execute the following command:
        
                pip install --egg pyxelrest --trusted-host rms.gdfsuez.net --index http://rms.gdfsuez.net:8310/artifactory/api/pypi/python3/simple


Configuration
-------------
Services to be exposed can be configured thanks to ``pixelrest_config.ini`` file located in your user folder.

Each section corresponds to a service.

The following mandatory properties are available:

- **host**: URI to the service base path

The following optional properties are available:

- **swaggerBasePath**: URI to retrieve the Swagger JSON. Default value is */*
- **methods**: List (separator is ",") of service methods to be exposed, all by default, amongst:

    - *get*
    - *post*
    - *put*
    - *delete*


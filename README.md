# Access REST APIs from Excel using User Defined Functions (UDF)

## Requirements

1. This step will certainly be removed in the future, but in the meantime: Within Excel, `Trust access to the VBA project object model` should be enabled.
    > File > Options > Trust Center > Trust Center Settings > Macro Settings
2. Python dependencies must be installed.
    * For _Python 2_ users execute the following commands from within `src\main\python` folder:
    
            pip install pypiwin32
            pip install -e . --trusted-host rms.gdfsuez.net --index http://rms.gdfsuez.net:8310/artifactory/api/pypi/python/simple
    * For _Python 3_ users the following steps must be performed:
        1. _PyWin32_ should be [downloaded](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pywin32)
        2. And installed thanks to the following command:
        
                pip install pywin32-220.1-cp36-cp36m-win_amd64.whl
        3. Finally, from an elevated command prompt, execute the following command from your python directory:
        
                python.exe Scripts\pywin32_postinstall.py -install
        4. Project dependencies must be installed. Execute the following command from within `src\main\python` folder:
    
                pip install -e . --trusted-host rms.gdfsuez.net --index http://rms.gdfsuez.net:8310/artifactory/api/pypi/python3/simple
3. This step will be included in previous step, but in the meantime: XLWings default configuration for PixelRest must be installed. Execute the following command from within `src\main\python` folder:

        python pyxelrest_post_install.py

## Configuration

Services to be exposed can be configured thanks to `pixelrest_config.ini` file located in your user folder.

Each section corresponds to a service.

The following mandatory properties are available:
* __host__: URI to the service base path

The following optional properties are available:
* __swaggerBasePath__: URI to retrieve the Swagger JSON. Default value is _/_
* __methods__: List (separator is ",") of service methods to be exposed, all by default, amongst:
    * _get_
    * _post_
    * _put_
    * _delete_

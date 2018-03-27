# Access REST APIs from Microsoft Excel using User Defined Functions (UDF) #

PyxelRest allow you to query [Swagger 2.0/OpenAPI](https://www.openapis.org) REST APIs using Microsoft Excel User Defined Functions.

1. [Usage](#Usage)
2. [Installation](#Installation)
3. [Configuration](#Configuration)

## Usage ##

Once installed, open Microsoft Excel and UDFs from configured services will be available.

![Selecting UDF](addin/AutoLoadPyxelRestAddIn/resources/screenshot_udfs_category.PNG)

![Filling in UDF parameters](addin/AutoLoadPyxelRestAddIn/resources/screenshot_udf_arguments.PNG)

UDFs are automatically updated on Microsoft Excel start and on Configuration update.

Updating UDFs without restarting Microsoft Excel or updating configuration can be done thanks to the ``Update Functions`` button within ``PyxelRest`` tab.

![Microsoft Excel add-in](addin/AutoLoadPyxelRestAddIn/resources/screenshot_pyxelrest_auto_load_ribbon.PNG)

PyxelRest itself can automatically stay up to date. 
The updater make sure that the python module, the Microsoft Excel add-in and the services configuration stays up to date.

![Update steps](addin/AutoLoadPyxelRestAddIn/resources/update_gui.gif)

## Installation ##

### Pre requisites ###

* [Python >= 2.7](https://www.python.org/downloads/) must be installed.
* [Microsoft Excel >= 2010](https://products.office.com/en-us/excel) must be installed.
* [Microsoft .NET Framework >= 4.5.2](http://go.microsoft.com/fwlink/?linkid=328856) must be installed.

### User installation (using PIP) ###

1. Within Microsoft Excel, `Trust access to the VBA project object model` should be enabled.
> File > Options > Trust Center > Trust Center Settings > Macro Settings
2. Microsoft Excel must be closed while executing the following command:

```bash
pip install pyxelrest
```

#### User add-in installation ####

One python module is installed, a script is available to install the Microsoft Excel add-in.

The add-in is not installed at the same time as the module because:
    * It may prompt the user for installation.
    * pyxelrest can be used as a python module without the need for the add-in.

Considering %script_dir% as the directory containing python scripts (Scripts folder within your virtual environment).

Considering %data_dir% as the directory containing python data (root folder within your virtual environment).

Install Microsoft Excel add-in by executing the following command:

```bash
python %script_dir%\pyxelrest_install_addin.py %data_dir%\pyxelrest_addin %data_dir%\pyxelrest_vb_addin
```

The following options are available when launching this script:

<table>
    <th>
        <td><em>Description</em></td>
        <td><em>Mandatory</em></td>
        <td><em>Possible values</em></td>
    </th>
    <tr>
        <td><strong>add_in_directory</strong></td>
        <td>Directory containing PyxelRest Microsoft Excel auto load add-in.</td>
        <td>Mandatory</td>
        <td>Must be the first positional argument.</td>
    </tr>
    <tr>
        <td><strong>vb_add_in_directory</strong></td>
        <td>Directory containing PyxelRest Microsoft Visual Basic add-in.</td>
        <td>Mandatory</td>
        <td>Must be the second positional argument.</td>
    </tr>
    <tr>
        <td><strong>--scripts_directory</strong></td>
        <td>Directory containing installed Python scripts.</td>
        <td>Optional</td>
        <td>Default to the folder containing this script.</td>
    </tr>
    <tr>
        <td><strong>--path_to_up_to_date_configuration</strong></td>
        <td>Path to up to date configuration file(s). This path will be used in case of auto update to keep services configuration up to date.</td>
        <td>Optional</td>
        <td>Can be file, folder paths or an URL to a file.</td>
    </tr>
</table>

### User uninstall (using PIP) ###

1. Go to `Control Panel/Programs and Features` and uninstall AutoLoadPyxelRestAddIn.
2. Execute the following command:

        pip uninstall pyxelrest
3. Remove `%APPDATA%\pyxelrest` folder.
4. Remove `%APPDATA%\Microsoft\Excel\XLSTART\pyxelrest.xlam` file.

### Developer Installation (using PIP) ###

1. Within Microsoft Excel, `Trust access to the VBA project object model` should be enabled.
> File > Options > Trust Center > Trust Center Settings > Macro Settings
2. Build the add-in C# solution:
In order to do so, you need to add a test certificate.
> Project > AutoLoadPyxelRestAddIn > Signing
3. Microsoft Excel must be closed while executing the following script from within pyxelrest root folder:

        developer_install.bat

### Optional Dependencies ###

- Support for `application/msgpackpandas`
    - Pandas encoded msgpack will be used if `pandas` and `msgpack-python` modules are available.

- Support for ``ujson``
    - JSON responses deserialization (when rely_on_definitions is set to True) will rely on ``ujson`` in case ``ujson`` module is available.

- Support for ``requests_ntlm``
    - ``requests_ntlm`` is required in case auth=ntlm is set in ``security_details`` property and custom credentials are provided.

- Support for ``requests_negotiate_sspi``
    - ``requests_negotiate_sspi`` is required in case auth=ntlm is set in ``security_details`` property and logged in user credentials should be used.

- Support for ``cachetool``
    - ``cachetool`` is required to be able to use in-memory caching.

## Configuration ##

### Services Configuration ###

Services configuration can be done within Microsoft Excel thanks to the `Configure Services` button within `PyxelRest` tab.

![Microsoft Excel add-in](addin/AutoLoadPyxelRestAddIn/resources/screenshot_pyxelrest_auto_load_ribbon.PNG)

![Configuration screen](addin/AutoLoadPyxelRestAddIn/resources/screenshot_configure_pyxelrest_services.PNG)

Configuration can also be manually updated thanks to `%APPDATA%\pyxelrest\configuration\services.ini` file.

Each section name will be used as the UDFs category.

Each UDF will be prefixed by the section name (only [a-zA-Z0-9_] characters will be kept).

The following options are available for each section:

<table>
    <th>
        <td><em>Description</em></td>
        <td><em>Mandatory</em></td>
        <td><em>Possible values</em></td>
    </th>
    <tr>
        <td><strong>swagger_url</strong></td>
        <td>URL to the Swagger definition. http, https and file scheme are supported. For more details on what is a URL, please refer to https://en.wikipedia.org/wiki/URL</td>
        <td>Mandatory</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>proxy_url</strong></td>
        <td>Proxy that should be used to reach service. If this is an URL, then this proxy will be used for the swagger_url scheme only. If you want to specify a proxy for a different scheme, then this value should be scheme=proxy_url_for_this_scheme. You can specify multiple schemes by using comma as a separator. You can also use no_proxy as a scheme for a no_proxy url. For more details refer to http://docs.python-requests.org/en/master/user/advanced/#proxies</td>
        <td>Optional</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>service_host</strong></td>
        <td>Service host in case your service is behind a reverse proxy.</td>
        <td>Optional</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>methods</strong></td>
        <td>List of services methods to be exposed as UDFs. Retrieve all standards HTTP methods by default (get, post, put, delete, patch, options, head).</td>
        <td>Optional</td>
        <td>get, post, put, delete, patch, options, head</td>
    </tr>
    <tr>
        <td><strong>security_details</strong></td>
        <td>Extra security information not provided by swagger. Refer to Security Details section for more information.</td>
        <td>Optional</td>
        <td>port=XX,timeout=YY</td>
    </tr>
    <tr>
        <td><strong>advanced_configuration</strong></td>
        <td>Additional configuration details. Refer to Advanced Configuration section for more information.</td>
        <td>Optional</td>
        <td>udf_return_type=XX,rely_on_definitions=YY</td>
    </tr>
</table>

#### Security Details ####

Additional security details can be provided thanks to `security_details` property.

This property is supposed to contains key=value information. Separator is ',' (comma).

Values cannot contains "," character.
Values can be environment variables if provided in the form %MY_ENV_VARIABLE% (for MY_ENV_VARIABLE environment variable).

Depending on the type of authentication, the following keys are available:

##### Common #####

<table>
    <th>
        <td><em>Description</em></td>
    </th>
    <tr>
        <td><strong>auth</strong></td>
        <td>Custom authentication mechanism. Valid value is ntlm (requiring requests_ntlm or requests_negotiate_sspi).</td>
    </tr>
</table>

##### OAuth 2 #####

If response_type is not provided in authorization_url, token is expected to be received in "token" field.

<table>
    <th>
        <td><em>Description</em></td>
        <td><em>Mandatory</em></td>
    </th>
    <tr>
        <td><strong>port</strong></td>
        <td>Port on which the authentication response is supposed to be received. Default value is 5000.</td>
        <td>Optional</td>
    </tr>
    <tr>
        <td><strong>timeout</strong></td>
        <td>Maximum number of seconds to wait for the authentication response to be received. Default value is 1 minute.</td>
        <td>Optional</td>
    </tr>
    <tr>
        <td><strong>oauth2.XXXX</strong></td>
        <td>Where XXXX is the name of the parameter in the authorization URL. You can find more details on https://tools.ietf.org/html/rfc6749#section-4.2.1</td>
        <td>Optional</td>
    </tr>
    <tr>
        <td><strong>success_display_time</strong></td>
        <td>Amount of milliseconds to wait before closing the authentication response page on success and returning back to Microsoft Excel. Default value is 1 millisecond.</td>
        <td>Optional</td>
    </tr>
    <tr>
        <td><strong>failure_display_time</strong></td>
        <td>Amount of milliseconds to wait before closing the authentication response page on failure and returning back to Microsoft Excel. Default value is 5 seconds.</td>
        <td>Optional</td>
    </tr>
</table>

##### API Key #####

<table>
    <th>
        <td><em>Description</em></td>
        <td><em>Mandatory</em></td>
    </th>
    <tr>
        <td><strong>api_key</strong></td>
        <td>User API Key.</td>
        <td>Mandatory</td>
    </tr>
</table>

##### Basic #####

<table>
    <th>
        <td><em>Description</em></td>
        <td><em>Mandatory</em></td>
    </th>
    <tr>
        <td><strong>username</strong></td>
        <td>User name.</td>
        <td>Mandatory</td>
    </tr>
    <tr>
        <td><strong>password</strong></td>
        <td>User password.</td>
        <td>Mandatory</td>
    </tr>
</table>

##### NTLM #####

<table>
    <th>
        <td><em>Description</em></td>
        <td><em>Mandatory</em></td>
    </th>
    <tr>
        <td><strong>username</strong></td>
        <td>User name. Should be of the form domain\\user. Default value is the logged in user name.</td>
        <td>Optional</td>
    </tr>
    <tr>
        <td><strong>password</strong></td>
        <td>User password. Default value is the logged in user password.</td>
        <td>Optional</td>
    </tr>
</table>

#### Advanced Configuration ####

Additional configuration details can be provided thanks to `advanced_configuration` property.

This property is supposed to contains key=value information. Separator is ',' (comma).

Values cannot contains "," character.
Values can be environment variables if provided in the form %MY_ENV_VARIABLE% (for MY_ENV_VARIABLE environment variable).

<table>
    <th>
        <td><em>Description</em></td>
        <td><em>Possible values</em></td>
    </th>
    <tr>
        <td><strong>udf_return_type</strong></td>
        <td>synchronous if you want your UDF to return the final result immediately. It means that you will have to specify all the cells that will contains the result. asynchronous by default.</td>
        <td>asynchronous or synchronous. Both values can be provided separated by ';' (semicolon)</td>
    </tr>
    <tr>
        <td><strong>rely_on_definitions</strong></td>
        <td>Rely on swagger definitions to re-order fields received in JSON response. Deactivated by default.</td>
        <td>True or False</td>
    </tr>
    <tr>
        <td><strong>max_retries</strong></td>
        <td>Maximum number of time a request should be retried before considered as failed. 5 by default.</td>
        <td>Any positive integer value</td>
    </tr>
    <tr>
        <td><strong>header.XXXX</strong></td>
        <td>Where XXXX is the name of the header that should be sent with every request sent to this service.</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>connect_timeout</strong></td>
        <td>Maximum amount of time, in seconds, to wait when trying to reach the service. Wait for 1 second by default. For more details refer to http://docs.python-requests.org/en/master/user/advanced/#timeouts</td>
        <td>any float value (decimal separator is .)</td>
    </tr>
    <tr>
        <td><strong>read_timeout</strong></td>
        <td>Maximum amount of time, in seconds, to wait when requesting a service. Infinite wait by default. For more details refer to http://docs.python-requests.org/en/master/user/advanced/#timeouts</td>
        <td>any float value (decimal separator is .)</td>
    </tr>
    <tr>
        <td><strong>swagger_read_timeout</strong></td>
        <td>Maximum amount of time, in seconds, to wait when requesting a swagger definition. Wait for 5 seconds by default. For more details refer to http://docs.python-requests.org/en/master/user/advanced/#timeouts</td>
        <td>any float value (decimal separator is .)</td>
    </tr>
    <tr>
        <td><strong>tags</strong></td>
        <td>Swagger tags that should be retrieved. If not specified, no filtering is applied. For more details refer to https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md</td>
        <td>any value separated by ';' (semicolon)</td>
    </tr>
</table>

#### PyxelRest Service Configuration ####

You can also use the "pyxelrest" service name to activate [Postman](https://www.getpostman.com)-like UDFs.

![Configuration screen](addin/AutoLoadPyxelRestAddIn/resources/screenshot_configure_pyxelrest_service.PNG)

![Selecting UDF](addin/AutoLoadPyxelRestAddIn/resources/screenshot_udfs_pyxelrest_category.PNG)

It can be configured the same way than a usual service, except you cannot provide the following options as they do not make sense anymore:

<table>
    <tr>
        <td><strong>swagger_url</strong></td>
    </tr>
    <tr>
        <td><strong>service_host</strong></td>
    </tr>
</table>

Also the following advanced configuration options will not be taken into account:

<table>
    <tr>
        <td><strong>rely_on_definitions</strong></td>
    </tr>
    <tr>
        <td><strong>swagger_read_timeout</strong></td>
    </tr>
    <tr>
        <td><strong>tags</strong></td>
    </tr>
</table>

### Logging Configuration ###

PyxelRest logging configuration can be updated thanks to `%APPDATA%\pyxelrest\configuration\logging.ini` file.

PyxelRest auto-update logging configuration can be updated thanks to `%APPDATA%\pyxelrest\configuration\auto_update_logging.ini` file.

Microsoft Excel Auto-Load add-in logging configuration can be updated thanks to `%APPDATA%\pyxelrest\configuration\addin.config` file.

Default log files can be found in your `%APPDATA%\pyxelrest\logs` folder.

This folder can easily be accessed thanks to the `Open Logs` button within `PyxelRest` tab.

![Microsoft Excel add-in](addin/AutoLoadPyxelRestAddIn/resources/screenshot_pyxelrest_auto_load_ribbon.PNG)

### Microsoft Excel Auto-Load add-in Configuration ###

Auto check for update can be activated/deactivated within Microsoft Excel thanks to the `Check for update on close` button within `PyxelRest` tab.

![Microsoft Excel add-in](addin/AutoLoadPyxelRestAddIn/resources/screenshot_pyxelrest_auto_load_ribbon.PNG)

Configuration can also be manually updated thanks to `%APPDATA%\pyxelrest\configuration\addin.config` file.

The following application settings are available:

<table>
    <th>
        <td><em>Description</em></td>
        <td><em>Mandatory</em></td>
        <td><em>Possible values</em></td>
    </th>
    <tr>
        <td><strong>PathToPython</strong></td>
        <td>Path to the python.exe (including) executable that should be used to launch the update script.</td>
        <td>Mandatory</td>
        <td>Installation script is already setting this value properly.</td>
    </tr>
    <tr>
        <td><strong>PathToUpdateScript</strong></td>
        <td>Path to the Python script used to update PyxelRest.</td>
        <td>Mandatory</td>
        <td>Installation script is already setting this value properly.</td>
    </tr>
    <tr>
        <td><strong>AutoCheckForUpdates</strong></td>
        <td>Activate or Deactivate automatic check for PyxelRest update on Microsoft Excel closing.</td>
        <td>Optional</td>
        <td>True (default), False</td>
    </tr>
    <tr>
        <td><strong>GenerateUDFAtStartup</strong></td>
        <td>Activate or Deactivate generation of user defined functions at Microsoft Excel startup.</td>
        <td>Optional</td>
        <td>True (default), False</td>
    </tr>
    <tr>
        <td><strong>PathToXlWingsBasFile</strong></td>
        <td>Path to the Python script used to update PyxelRest.</td>
        <td>Mandatory</td>
        <td>Default value is already set.</td>
    </tr>
    <tr>
        <td><strong>PathToUpToDateConfigurations</strong></td>
        <td>Path to the file or directory containing up to date services configuration.</td>
        <td>Optional</td>
        <td>Installation script is already setting this value properly.</td>
    </tr>
</table>

## Using as a module ##

You can use pyxelrest as a python module as well.

```python
import pyxelrest

# Avoid the following import statement to generate UDFs
pyxelrest.GENERATE_UDF_ON_IMPORT = False

from pyxelrest import pyxelrestgenerator

# Generate UDFs for the following import
services = pyxelrestgenerator.generate_user_defined_functions()
pyxelrestgenerator.reload_user_defined_functions(services)

from pyxelrest import user_defined_functions

# UDFs are available as python functions within user_defined_functions and can be used as such
```

### Generating user defined functions ###

When `pyxelrest.GENERATE_UDF_ON_IMPORT` is set to `True` (default behavior), UDFs are generated by loading (e.g. on first import) pyxelrest.pyxelrestgenerator.py.

You can manually regenerate UDFs by calling `pyxelrest.pyxelrestgenerator.generate_user_defined_functions()`

All UDFs can be found within pyxelrest.user_defined_functions.py.

### Caching results ###

For testing purposes mainly, you can cache UDFs calls by using pyxelrest.caching.py.
This serves as an automatic mocking feature.

The call to caching init method must be done prior to generating UDFs.
 
#### On disk ####

`init_disk_cache(<filename>)` must be called to initialize the disk cache file.

#### In memory ####

This cache has an expiry in second and a maximum size.
`init_memory_cache(<maxsize>,<expiry>)` must be called to initialize the memory cache.

The cachetools module is required for this feature to be available.

## Frequently Asked Question ##

### Microsoft Excel Wizard does not show any parameter ###

In case your UDF has a lot of parameters (or parameters with long names), then Microsoft Excel is unable to display them all in the function wizard.

Try reducing the number of parameters in your service (or the length of your parameter names).

### No command specified in the configuration, cannot autostart server ###

This error will happen in case you manually specified in your xlwings.bas file to use debug server but did not uncomment the main function starting the server on pyxelrest module side.

### Microsoft Excel Add-In cannot be installed ###

Check that all requirements are met:
 * [Microsoft .NET Framework >= 4.5.2](http://go.microsoft.com/fwlink/?linkid=328856) must be installed.
 * [Microsoft Visual Studio 2010 Tools for Office Runtime](https://www.microsoft.com/en-us/download/details.aspx?id=48217) must be installed.

In case you encounter an issue like `Could not load file or assembly 'Microsoft.Office.BusinessApplications.Fba...` anyway, you then need to remove `C:\Program Files\Common Files\Microsoft Shared\VSTO\10.0\VSTOInstaller.exe.config` file.

### Dates with a year higher than 3000 are not converted to local timezone ###

Due to timestamp limitation, dates after 3000-12-31 and date time after 3001-01-01T07:59:59+00:00 cannot be converted to local timezone.

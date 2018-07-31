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

Considering %scripts_dir% as the directory containing python scripts (Scripts folder within your virtual environment).

Install Microsoft Excel add-in by executing the following command:

```bash
python %scripts_dir%\pyxelrest_install_addin.py
```

The following options are available when launching this script:

<table>
    <th>
        <td><em>Description</em></td>
        <td><em>Possible values</em></td>
    </th>
    <tr>
        <td><strong>--add_in_directory</strong></td>
        <td>Directory containing PyxelRest Microsoft Excel auto load add-in.</td>
        <td>Default to ..\pyxelrest_addin relatively to the scripts directory.</td>
    </tr>
    <tr>
        <td><strong>--scripts_directory</strong></td>
        <td>Directory containing installed Python scripts.</td>
        <td>Default to the folder containing this script.</td>
    </tr>
    <tr>
        <td><strong>--path_to_up_to_date_configuration</strong></td>
        <td>Path to up to date configuration file(s). This path will be used in case of auto update to keep services configuration up to date.</td>
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

- Support for ``application/msgpackpandas`` encoded data.
    - Pandas encoded msgpack will be used if ``pandas`` and ``msgpack-python`` modules are available.
    - ``pandas_msgpack`` extra requires can be used to install those dependencies.

- Support for faster JSON handling.
    - JSON responses deserialization (when rely_on_definitions is set to True) will rely on ``ujson`` in case ``ujson`` module is available.
    - ``ujson`` extra requires can be used to install those dependencies.

- Support for NTLM authentication (with user credentials provided),
    - ``requests_ntlm`` module is required in case auth=ntlm is set in ``security_details`` property and custom credentials are provided.
    - ``ntlm`` extra requires can be used to install those dependencies.

- Support for automatic NTLM authentication.
    - ``requests_negotiate_sspi`` module is required in case auth=ntlm is set in ``security_details`` property and logged in user credentials should be used.
    - ``ntlm`` extra requires can be used to install those dependencies.

- Support for in-memory caching.
    - ``cachetool`` module is required to be able to use in-memory caching.
    - ``cachetool`` extra requires can be used to install those dependencies.

## Configuration ##

### Services Configuration ###

Services configuration can be done within Microsoft Excel thanks to the `Configure Services` button within `PyxelRest` tab.

![Microsoft Excel add-in](addin/AutoLoadPyxelRestAddIn/resources/screenshot_pyxelrest_auto_load_ribbon.PNG)

![Configuration screen](addin/AutoLoadPyxelRestAddIn/resources/screenshot_configure_services.PNG)

![Advanced configuration screen](addin/AutoLoadPyxelRestAddIn/resources/screenshot_configure_service.PNG)

Configuration can also be manually updated thanks to `%APPDATA%\pyxelrest\configuration\services.yml` file.

File is following [YAML](http://yaml.org/start.html) formatting.

Each section name will be used as the UDFs category.

Each UDF will be prefixed by the section name (only [a-zA-Z0-9_] characters will be kept).

The following options are available for each section:

Values can be environment variables if provided in the form %MY_ENV_VARIABLE% (for MY_ENV_VARIABLE environment variable).

<table>
    <th>
        <td><em>Description</em></td>
        <td><em>Mandatory</em></td>
        <td><em>Possible values</em></td>
    </th>
    <tr>
        <td><strong>open_api</strong></td>
        <td>Dictionary describing the OpenAPI definition. Refer to OpenAPI section for more information.</td>
        <td>Mandatory</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>description</strong></td>
        <td>A small description of this service. To be displayed within Microsoft Excel add-in services configuration screen.</td>
        <td>Optional</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>proxies</strong></td>
        <td>Proxies that should be used to reach service. This is a dictionary where keys are the scheme (http or https) and/or no_proxy. If the key is a scheme then the value should be the proxy URL. Otherwise the value should be the URL for which proxies should be ignored. For more details refer to http://docs.python-requests.org/en/master/user/advanced/#proxies</td>
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
        <td><strong>oauth2</strong></td>
        <td>Dictionary containing OAuth2 related settings. Refer to OAuth 2 section for more information.</td>
        <td>Optional</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>api_key</strong></td>
        <td>User API Key.</td>
        <td>Optional</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>basic</strong></td>
        <td>Dictionary containing Basic authentication related settings. Refer to Basic section for more information.</td>
        <td>Optional</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>ntlm</strong></td>
        <td>Dictionary containing NTLM related settings. Refer to NTLM section for more information.</td>
        <td>Optional</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>udf</strong></td>
        <td>Dictionary containing user defined function related settings. Refer to User Defined Function section for more information.</td>
        <td>Optional</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>max_retries</strong></td>
        <td>Maximum number of time a request should be retried before considered as failed. 5 by default.</td>
        <td>Optional</td>
        <td>Any positive integer value</td>
    </tr>
    <tr>
        <td><strong>headers</strong></td>
        <td>Dictionary containing headers were key is the name of the header that should be sent with every request sent to this service.</td>
        <td>Optional</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>connect_timeout</strong></td>
        <td>Maximum amount of time, in seconds, to wait when trying to reach the service. Wait for 1 second by default. For more details refer to http://docs.python-requests.org/en/master/user/advanced/#timeouts</td>
        <td>Optional</td>
        <td>any float value</td>
    </tr>
    <tr>
        <td><strong>read_timeout</strong></td>
        <td>Maximum amount of time, in seconds, to wait when requesting a service. Infinite wait by default. For more details refer to http://docs.python-requests.org/en/master/user/advanced/#timeouts</td>
        <td>Optional</td>
        <td>any float value</td>
    </tr>
    <tr>
        <td><strong>skip_update_for</strong></td>
        <td>List of section names that should not be auto-updated.</td>
        <td>Optional</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>python_modules</strong></td>
        <td>List of extra python module names that should be installed.</td>
        <td>Optional</td>
        <td></td>
    </tr>
</table>

#### OpenAPI ####

<table>
    <th>
        <td><em>Description</em></td>
        <td><em>Mandatory</em></td>
        <td><em>Possible values</em></td>
    </th>
    <tr>
        <td><strong>definition</strong></td>
        <td>URL to the OpenAPI definition. http, https and file scheme are supported. For more details on what is a URL, please refer to https://en.wikipedia.org/wiki/URL</td>
        <td>Mandatory</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>definition_read_timeout</strong></td>
        <td>Maximum amount of time, in seconds, to wait when requesting an OpenAPI definition. Wait for 5 seconds by default. For more details refer to http://docs.python-requests.org/en/master/user/advanced/#timeouts</td>
        <td>Optional</td>
        <td>any float value</td>
    </tr>
    <tr>
        <td><strong>excluded_tags</strong></td>
        <td>List of tags within OpenAPI definition that should not be retrieved. If not specified, no filtering is applied. For more details refer to https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md</td>
        <td>Optional</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>selected_tags</strong></td>
        <td>List of tags within OpenAPI definition that should be retrieved (if not within excluded tags already). If not specified, no filtering is applied. For more details refer to https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md</td>
        <td>Optional</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>excluded_operation_ids</strong></td>
        <td>List of operation_id (or regular expressions) within OpenAPI definition that should not be retrieved. If not specified, no filtering is applied. For more details refer to https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md</td>
        <td>Optional</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>selected_operation_ids</strong></td>
        <td>List of operation_id (or regular expressions) within OpenAPI definition that should be retrieved (if not within excluded operation_ids already). If not specified, no filtering is applied. For more details refer to https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md</td>
        <td>Optional</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>excluded_parameters</strong></td>
        <td>List of parameter names (or regular expressions) within OpenAPI definition that should not be exposed. If not specified, no filtering is applied. For more details refer to https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md</td>
        <td>Optional</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>selected_parameters</strong></td>
        <td>List of parameter names (or regular expressions) within OpenAPI definition that should be exposed (if not within excluded parameters already). If not specified, no filtering is applied. For more details refer to https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md</td>
        <td>Optional</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>rely_on_definitions</strong></td>
        <td>Rely on OpenAPI definitions to re-order fields received in JSON response. Deactivated by default.</td>
        <td>Optional</td>
        <td>true or false</td>
    </tr>
    <tr>
        <td><strong>service_host</strong></td>
        <td>Service host in case your service is behind a reverse proxy.</td>
        <td>Optional</td>
        <td></td>
    </tr>
</table>

#### User Defined Function ####

<table>
    <th>
        <td><em>Description</em></td>
        <td><em>Mandatory</em></td>
        <td><em>Possible values</em></td>
    </th>
    <tr>
        <td><strong>return_types</strong></td>
        <td>List of user defined function return types. vba_compatible if you want your UDF to return the final result immediately. It means that you will have to specify all the cells that will contains the result. Use sync_auto_expand so that UDF call will be a synchronous call auto expanding the result. async_auto_expand (asynchronous call auto expanding the result) by default.</td>
        <td>Optional</td>
        <td>async_auto_expand, sync_auto_expand or vba_compatible.</td>
    </tr>
    <tr>
        <td><strong>shift_result</strong></td>
        <td>Shift auto expand result by one column to the right. True by default.</td>
        <td>Optional</td>
        <td>true or false.</td>
    </tr>
</table>

#### OAuth 2 ####

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
        <td><strong>success_display_time</strong></td>
        <td>Amount of milliseconds to wait before closing the authentication response page on success and returning back to Microsoft Excel. Default value is 1 millisecond.</td>
        <td>Optional</td>
    </tr>
    <tr>
        <td><strong>failure_display_time</strong></td>
        <td>Amount of milliseconds to wait before closing the authentication response page on failure and returning back to Microsoft Excel. Default value is 5 seconds.</td>
        <td>Optional</td>
    </tr>
    <tr>
        <td><strong>XXXX</strong></td>
        <td>Where XXXX is the name of the parameter in the authorization URL. You can find more details on https://tools.ietf.org/html/rfc6749#section-4.2.1</td>
        <td>Optional</td>
    </tr>
</table>

#### Basic ####

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

#### NTLM ####

Requiring requests_ntlm or requests_negotiate_sspi python modules.

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

#### PyxelRest Service Configuration ####

You can also use the "pyxelrest" service name to activate [Postman](https://www.getpostman.com)-like UDFs.

![Configuration screen](addin/AutoLoadPyxelRestAddIn/resources/screenshot_configure_services_pyxelrest.PNG)

![Advanced configuration screen](addin/AutoLoadPyxelRestAddIn/resources/screenshot_configure_service_pyxelrest.PNG)

![Selecting UDF](addin/AutoLoadPyxelRestAddIn/resources/screenshot_udfs_pyxelrest_category.PNG)

It can be configured the same way than a usual service, except that open_api section is not used anymore.

### Logging Configuration ###

PyxelRest logging configuration can be updated thanks to `%APPDATA%\pyxelrest\configuration\logging.yml` file.

PyxelRest auto-update logging configuration can be updated thanks to `%APPDATA%\pyxelrest\configuration\auto_update_logging.yml` file.

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
        <td><strong>PathToXlWingsConfiguration</strong></td>
        <td>Path to the XlWings configuration file used to configure XlWings for PyxelRest.</td>
        <td>Mandatory</td>
        <td>Installation script is already setting this value properly.</td>
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

![Microsoft Excel Wizard bug](addin/AutoLoadPyxelRestAddIn/resources/screenshot_udf_wizard_parameters_limit.PNG)

Microsoft Excel function wizard is not able to handle functions with a long definition.

The total length of parameter names (and commas to separate them) should not exceed 253 characters,

In case it does (your UDF has a lot of parameters or parameters with long names), then Microsoft Excel is unable to display them all in the function wizard.

To overcome this Microsoft Excel limitation you can try the following:
 * Exclude some parameters (refer to Open API configuration section for more information).
 * Remove some parameters in your service.
 * Reduce the length of your service parameter names.

### Microsoft Excel Wizard only list some functions ###

Microsoft Excel function wizard is not able to list more than a certain amount of functions per category.

However all functions can be directly accessed in cells.

To overcome this Microsoft Excel limitation you can try the following:
 * Exclude some functions in your service (refer to Open API configuration section for more information).

### No command specified in the configuration, cannot autostart server ###

This error will happen in case you manually specified in your xlwings.bas file to use debug server but did not uncomment the main function starting the server on pyxelrest module side.

### Microsoft Excel Add-In cannot be installed ###

Check that all requirements are met:
 * [Microsoft .NET Framework >= 4.5.2](http://go.microsoft.com/fwlink/?linkid=328856) must be installed.
 * [Microsoft Visual Studio 2010 Tools for Office Runtime](https://www.microsoft.com/en-us/download/details.aspx?id=48217) must be installed.

In case you encounter an issue like `Could not load file or assembly 'Microsoft.Office.BusinessApplications.Fba...` anyway, you then need to remove `C:\Program Files\Common Files\Microsoft Shared\VSTO\10.0\VSTOInstaller.exe.config` file.

In case you encounter an issue like `...An application with the same identity is already installed...`, you then need to manually remove all folders within `%USERPROFILE%\AppData\Local\Apps\2.0` and restart your computer.

### Dates with a year higher than 3000 are not converted to local timezone ###

Due to timestamp limitation, dates after 3000-12-31 and date time after 3001-01-01T07:59:59+00:00 cannot be converted to local timezone.

### Python process exited before it was possible to create the interface object ###

You need to check log files to identify the underlying issue.

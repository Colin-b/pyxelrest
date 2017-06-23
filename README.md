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

## Installation ##

### Pre requisites ###

* [Python](https://www.python.org/downloads/) must be installed.
* [Microsoft Excel](https://products.office.com/en-us/excel) must be installed.
* [Microsoft .NET Framework 4.5.2](http://go.microsoft.com/fwlink/?linkid=328856) must be installed.

### User installation (using PIP) ###

1. Within Microsoft Excel, `Trust access to the VBA project object model` should be enabled.
> File > Options > Trust Center > Trust Center Settings > Macro Settings
2. Microsoft Excel must be closed while executing the following command:

        pip install pyxelrest

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
        <td>Complete URL to the Swagger definition. It can also be a system file path if specified using file:// prefix.</td>
        <td>Mandatory</td>
        <td></td>
    </tr>
    <tr>
        <td><strong>proxy_url</strong></td>
        <td>Proxy that should be used to reach service.</td>
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
        <td>List of services methods to be exposed as UDFs.</td>
        <td>Optional</td>
        <td>get, post, put, delete</td>
    </tr>
    <tr>
        <td><strong>tags</strong></td>
        <td>Swagger tags that should be retrieved. If not specified, no filtering is applied.</td>
        <td>Optional</td>
        <td>any value separated by ','</td>
    </tr>
    <tr>
        <td><strong>connect_timeout</strong></td>
        <td>Maximum amount of time, in seconds, to wait when trying to reach the service. Wait for 1 second by default.</td>
        <td>Optional</td>
        <td>any float value (decimal separator is .)</td>
    </tr>
    <tr>
        <td><strong>read_timeout</strong></td>
        <td>Maximum amount of time, in seconds, to wait when requesting a service. Infinite wait by default.</td>
        <td>Optional</td>
        <td>any float value (decimal separator is .)</td>
    </tr>
    <tr>
        <td><strong>security_details</strong></td>
        <td>Extra security information not provided by swagger.</td>
        <td>Optional</td>
        <td>port=XX,timeout=YY</td>
    </tr>
    <tr>
        <td><strong>rely_on_definitions</strong></td>
        <td>Rely on swagger definitions to re-order fields received in JSON response. Deactivated by default.</td>
        <td>Optional</td>
        <td>True or False</td>
    </tr>
</table>

#### Security Details ####

Additional security details can be provided thanks to `security_details` property.

This property is supposed to contains key=value information. Separator is ',' (comma).

Depending on the type of authentication, the following keys are available:

##### Common #####

<table>
    <th>
        <td><em>Description</em></td>
        <td><em>Mandatory</em></td>
    </th>
    <tr>
        <td><strong>auth</strong></td>
        <td>Custom authentication mechanism. Valid value is ntlm (requiring requests_ntlm or requests_negotiate_sspi).</td>
        <td></td>
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
        <td>Maximum number of seconds to wait for the authentication response to be received. Default value is 20 seconds.</td>
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
        <td><strong>PathToPIP</strong></td>
        <td>Path to the pip.exe (including) executable that should be used to update PyxelRest.</td>
        <td>Mandatory</td>
        <td>Installation script is already setting this value properly.</td>
    </tr>
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
        <td><strong>PathToXlWingsBasFile</strong></td>
        <td>Path to the Python script used to update PyxelRest.</td>
        <td>Mandatory</td>
        <td>Default value is already set.</td>
    </tr>
</table>

## Using as a module ##

You can code using PyxelRest as well, all user defined functions are within user_defined_functions.py.
This file is generated by loading (e.g. on first import) pyxelrestgenerator.py.

### Caching results ###

For testing purposes mainly, you can cache UDFs calls by using caching.py.
This serves as an automatic mocking feature.

The call to caching init method must be done prior to generating UDFs.
 
#### On disk ####

init_disk_cache(<filename>) must be called to initialize the disk cache file.

#### In memory ####

This cache has an expiry in second and a maximum size.
init_memory_cache(<maxsize>,<expiry>) must be called to initialize the mamory cache.
The cachetools module is required.

## Frequently Asked Question ##

### Microsoft Excel Wizard does not show any parameter ###

In case your UDF has a lot of parameters, then Microsoft Excel is unable to display them all in the function wizard.

Try reducing the number of parameters in your service.

### Some UDFs are not updated when an update triggered multiple UDFs at once ###

Microsoft Excel is waiting for all UDFs to return prior to accepting value update.
PyxelRest is retrying up to 1000 times before considering that the value update failed but sometimes, 
depending on your Microsoft Excel book, all your UDFs might take more than 1000 retry to be performed.

<h2 align="center">Query REST APIs using functions (Microsoft Excel formulas or python functions)</h2>

<p align="center">
<a href="https://pypi.org/project/pyxelrest/"><img alt="pypi version" src="https://img.shields.io/pypi/v/pyxelrest"></a>
<a href="https://github.com/Colin-b/pyxelrest/actions"><img alt="Build status" src="https://github.com/Colin-b/pyxelrest/workflows/Release/badge.svg"></a>
<a href="https://github.com/Colin-b/pyxelrest/actions"><img alt="Coverage" src="https://img.shields.io/badge/coverage-65%25-orange"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/Colin-b/pyxelrest/actions"><img alt="Number of tests" src="https://img.shields.io/badge/tests-393 passed-blue"></a>
<a href="https://pypi.org/project/pyxelrest/"><img alt="Number of downloads" src="https://img.shields.io/pypi/dm/pyxelrest"></a>
</p>

PyxelRest allows you to query [Swagger 2.0/OpenAPI](https://www.openapis.org) REST APIs (or any HTTP/HTTPS URL) using:
* [Microsoft Excel]:
  * Dynamic array formulas
  * Legacy array formulas
  * Visual Basic for Applications functions

<p align="center">
  <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/dynamic_array_formula.gif" alt='Using dynamic array formulas to query petstore REST API'>
  
</p>
<p align="center"><em>Example with <a href="https://petstore.swagger.io/#/">petstore</a> REST API using formulas generated based on the OpenAPI definition.</em></p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/postman_in_excel.gif" alt='Using dynamic array formulas to query a URL'>
</p>
<p align="center"><em>Example using pyxelrest formulas to query any URL (as in Postman).</em></p>

* [Python](https://www.python.org) functions

```python
import pyxelrest

configuration = {'petstore': {'open_api': {'definition': 'http://petstore.swagger.io/v2/swagger.json'}}}
pyxelrest.load(configuration)

from pyxelrest.user_defined_functions import petstore

# Functions are available as python functions within petstore (in this case) and can be used as such
user = petstore.petstore_getUserByName("test")

# {'id': 9999, 'username': 'test', 'firstName': 'test', 'lastName': 'test', 'email': 'test@test.com', 'password': 'test', 'userStatus': 0}
print(user)
```
<p align="center"><em>Example with <a href="https://petstore.swagger.io/#/">petstore</a> REST API using functions generated based on the OpenAPI definition.</em></p>

## Table of Contents

* [Features](#features)
* [Installation](#how-to-install)
* [Configuration](#configuration)
  * [Services](#services-configuration)
  * [Logging](#logging-configuration)
  * [Microsoft Excel add-in](#microsoft-excel-com-add-in-configuration)
* [Using as a python module](#using-as-a-module)
* [Migration guide](#migration-guide)
* [FAQ](#frequently-asked-question)

## Features

### Automatic function (re)generation

Functions are automatically re-generated on [Microsoft Excel] startup and on Configuration update.

<p align="center">
  <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/update_functions_generate_startup.gif" alt='Formula generation'>
</p>
<p align="center"><em>Even if you should not need it, you can manually update functions without restarting Microsoft Excel or updating configuration by clicking on the <span style="color: #1382CE">Update Functions</span> button within <span style="color: #1E1E1F">PyxelRest</span> tab.</em></p>

### Automatic update

<p align="center">
  <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/update_gui.gif" alt='Update steps'>
</p>
<p align="center"><em>Check for update is performed when closing Microsoft Excel (it can be deactivated) and you will be prompted in case one is available.</em></p>

## How to install

1. [Python >= 3.7](https://www.python.org/downloads/) must be installed (with `pip` and `tkinter` for auto update to work).
2. Use pip to install module:
```bash
python -m pip install pyxelrest
```

### Optional Dependencies

- Support for NTLM authentication (with user credentials provided),
    - [`requests_ntlm`](https://pypi.org/project/requests_ntlm/) module is required in case auth=ntlm is set in `security_details` property and custom credentials are provided.
    - `ntlm` extra requires can be used to install those dependencies.
```bash
python -m pip install pyxelrest[ntlm]
```

- Support for automatic NTLM authentication.
    - [`requests_negotiate_sspi`](https://pypi.org/project/requests-negotiate-sspi/) module is required in case auth=ntlm is set in `security_details` property and logged in user credentials should be used.
    - `ntlm` extra requires can be used to install those dependencies.
```bash
python -m pip install pyxelrest[ntlm]
```

- Support for in-memory caching.
    - [`cachetool`](https://pypi.org/project/cachetools/) module is required to be able to use in-memory caching.
    - `cachetool` extra requires can be used to install those dependencies.
```bash
python -m pip install pyxelrest[cachetool]
```

### Microsoft Excel add-in installation

Once python module is installed, `pyxelrest_install_addin` script is available to install the [Microsoft Excel] COM add-in.

1. [Microsoft Excel >= 2010](https://products.office.com/en-us/excel) must be installed (Office 365 is supported).
2. [Microsoft .NET Framework >= 4.5.2](http://go.microsoft.com/fwlink/?linkid=328856) must be installed.
3. Within [Microsoft Excel], `Trust access to the VBA project object model` should be enabled.
   > File > Options > Trust Center > Trust Center Settings > Macro Settings
4. [Microsoft Excel] must be closed while executing the following command:
```bash
pyxelrest_install_addin
```

Note: The add-in is not required if you only want to use the `pyxelrest` python module.

#### Microsoft Excel add-in installer options

| Name | Description | Possible values |
|------|-------------|-----------------|
| --path_to_up_to_date_configuration | Path to up to date configuration file(s). This path will be used to keep services configuration up to date and provide a list of available services within the [Microsoft Excel] add-in. | file path, folder path or an URL returning a file content. |
| --check_pre_releases | Also fetch pre-releases when checking for updates. | No value is required, providing the option is enough. No pre-release check by default. |
| --add_in_directory | Directory containing PyxelRest [Microsoft Excel] COM add-in. | Default to `..\pyxelrest_addin` relatively to the python executable directory. |

## How to uninstall

1. Go to `Control Panel/Programs and Features` and uninstall `AutoLoadPyxelRestAddIn`.
2. Execute the following command:

        python -m pip uninstall pyxelrest
3. Remove `%APPDATA%\pyxelrest` folder.
4. Remove `%APPDATA%\Microsoft\Excel\XLSTART\pyxelrest.xlam` file.

## Configuration

### Services Configuration

<p align="center">
  <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/configure_service.gif" alt='Configuring services'>
</p>
<p align="center"><em>Services configuration can be done within Microsoft Excel thanks to the <span style="color: #1382CE">Configure Services</span> button within <span style="color: #1E1E1F">PyxelRest</span> tab.</em></p>

You can also update the [YAML](http://yaml.org/start.html) configuration file (`%APPDATA%\pyxelrest\configuration\services.yml`) yourself.

Each section name will be used as the related formulas category within [Microsoft Excel].

Each formula will be prefixed by the section name (only [a-zA-Z0-9_] characters will be kept).

#### Mandatory settings

| Name | Description |
|------|-------------|
| open_api | Dictionary describing the OpenAPI definition. Refer to [OpenAPI](#openapi) section for more information. |

Values can be environment variables if provided in the `%MY_ENV_VARIABLE%` form (where `MY_ENV_VARIABLE` is an environment variable).

#### Options

Values can be environment variables if provided in the `%MY_ENV_VARIABLE%` form (where `MY_ENV_VARIABLE` is an environment variable).

| Name | Description | Possible values |
|------|-------------|-----------------|
| description | A small description of this service. To be displayed within [Microsoft Excel] add-in services configuration screen. | |
| proxies | Proxies that should be used to reach service. This is a dictionary where keys are the scheme (http or https) and/or no_proxy. If the key is a scheme then the value should be the proxy URL. Otherwise the value should be the URL for which proxies should be ignored. For more details refer to [requests documentation](http://docs.python-requests.org/en/master/user/advanced/#proxies) | |
| methods | List of services methods to be exposed as UDFs. Retrieve all standards HTTP methods by default (get, post, put, delete, patch, options, head). | get, post, put, delete, patch, options, head |
| oauth2 | Dictionary containing OAuth2 related settings. Refer to [OAuth 2](#oauth-2) section for more information. | |
| api_key | User API Key. | |
| basic | Dictionary containing Basic authentication related settings. Refer to [Basic](#basic) section for more information. | |
| ntlm | Dictionary containing NTLM related settings. Refer to [NTLM](#ntlm) section for more information. | |
| formulas | Dictionary containing user defined function (formulas) related settings. Refer to [Formulas](#formulas) section for more information. | |
| max_retries | Maximum number of time a request should be retried before considered as failed. 5 by default. | Any positive integer value |
| headers | Dictionary containing headers were key is the name of the header that should be sent with every request sent to this service. | |
| connect_timeout | Maximum amount of time, in seconds, to wait when trying to reach the service. Wait for 1 second by default. For more details refer to [requests documentation](http://docs.python-requests.org/en/master/user/advanced/#timeouts) | any float value |
| read_timeout | Maximum amount of time, in seconds, to wait when requesting a service. Infinite wait by default. For more details refer to [requests documentation](http://docs.python-requests.org/en/master/user/advanced/#timeouts) | any float value |
| skip_update_for | List of section names that should not be auto-updated. | |
| python_modules | List of extra python module names that should be installed. | |
| caching | Dictionary containing caching related settings. Refer to [Caching](#caching) section for more information. | |
| result | Dictionary containing result related settings. Refer to [Result](#result) section for more information. | |
| udf_name_prefix | Prefix to be used in front of UDf name. | {service_name}_ |

#### OpenAPI

<table>
    <th>
        <td><em>Description</em></td>
        <td><em>Mandatory</em></td>
        <td><em>Possible values</em></td>
    </th>
    <tr>
        <td><strong>definition</strong></td>
        <td>URL to the OpenAPI definition. http, https and file scheme are supported. For more details on what is a URL, please refer to https://en.wikipedia.org/wiki/URL. If you would like to point to a static file such as C:\swagger.json, the value should be file:///C:\swagger.json</td>
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
        <td><strong>definition_retrieval_auths</strong></td>
        <td>List all authentication that should be used when retrieving the OpenAPI definition. Use no authentication by default.</td>
        <td>Optional</td>
        <td>oauth2_implicit, oauth2_access_code, oauth2_password, oauth2_application, api_key, basic, ntlm</td>
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

#### Formulas

##### Dynamic array formulas

Identified by the `dynamic_array` key within `formulas` section.

<table>
    <th>
        <td><em>Description</em></td>
        <td><em>Mandatory</em></td>
        <td><em>Possible values</em></td>
    </th>
    <tr>
        <td><strong>lock_excel</strong></td>
        <td>Should Microsoft Excel be locked (no other action can be performed) until the results are received.</td>
        <td>Optional</td>
        <td>true or false (default).</td>
    </tr>
</table>

##### Legacy array formulas

Identified by the `legacy_array` key within `formulas` section.

<table>
    <th>
        <td><em>Description</em></td>
        <td><em>Mandatory</em></td>
        <td><em>Possible values</em></td>
    </th>
    <tr>
        <td><strong>lock_excel</strong></td>
        <td>Should Microsoft Excel be locked (no other action can be performed) until the results are received.</td>
        <td>Optional</td>
        <td>true or false (default).</td>
    </tr>
</table>

##### Visual Basic for Applications (VBA) formulas

Identified by the `vba_compatible` key within `formulas` section.

#### OAuth 2

Depending on the flow, every parameter described in [requests-auth documentation](https://colin-b.github.io/requests_auth/) can be provided.

Note that token_url and authorization_url are extracted from OpenAPI documentation, thus they do not need to be provided.

#### Basic

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

#### NTLM

Requiring [`requests_ntlm`](https://pypi.org/project/requests_ntlm/) or [`requests_negotiate_sspi`](https://pypi.org/project/requests-negotiate-sspi/) python modules.

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

#### Caching

Requiring [`cachetools`](https://pypi.org/project/cachetools/) python module.

<table>
    <th>
        <td><em>Description</em></td>
        <td><em>Mandatory</em></td>
    </th>
    <tr>
        <td><strong>result_caching_time</strong></td>
        <td>Number of seconds during which a GET request will return previous result. Always send a new request by default.</td>
        <td>Optional</td>
    </tr>
    <tr>
        <td><strong>max_nb_results</strong></td>
        <td>Maximum number of results to store in cache. 100 by default.</td>
        <td>Optional</td>
    </tr>
</table>

#### Result

<table>
    <th>
        <td><em>Description</em></td>
        <td><em>Mandatory</em></td>
    </th>
    <tr>
        <td><strong>flatten</strong></td>
        <td>Flatten received JSON to a 2-Dimension array. Default to True.</td>
        <td>Optional</td>
    </tr>
    <tr>
        <td><strong>raise_exception</strong></td>
        <td>Raise received exceptions to client. False by default.</td>
        <td>Optional</td>
    </tr>
</table>


#### PyxelRest service configuration

You can query any URL, as long as you know everything that is required to perform the query.

To do so, you can use the `pyxelrest` service name to activate [Postman](https://www.getpostman.com)-like UDFs.

<p align="center">
  <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/configure_pyxelrest_service.gif" alt='Configuring pyxelrest service'>
</p>
<p align="center"><em>It can be configured the same way than a usual service, except that <i>open_api</i> section is not needed anymore.</em></p>

### Logging configuration

`pyxelrest` module logging configuration can be updated thanks to `%APPDATA%\pyxelrest\configuration\logging.yml` file.

[Microsoft Excel] COM add-in logging configuration can be updated thanks to `%APPDATA%\pyxelrest\configuration\addin.config` file.

By default, log files can be found in your `%APPDATA%\pyxelrest\logs` folder.

<p align="center">
  <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/open_logs.gif" alt='How to open logs'>
</p>
<p align="center"><em>This folder can be accessed from Microsoft Excel thanks to the <span style="color: #1382CE">Open Logs</span> button within <span style="color: #1E1E1F">PyxelRest</span> tab.</em></p>

### Microsoft Excel COM add-in configuration

<p align="center">
  <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/check_for_update_on_close.gif" alt='Managing auto update'>
</p>
<p align="center"><em>Auto update can be (de)activated from Microsoft Excel thanks to the <span style="color: #1382CE">Check for update on close</span> button within <span style="color: #1E1E1F">PyxelRest</span> tab.</em></p>

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
        <td>Path to the python.exe (including) executable where pyxelrest python module was installed.</td>
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
        <td>Installation script is already setting this value if provided.</td>
    </tr>
    <tr>
        <td><strong>CheckPreReleases</strong></td>
        <td>Should auto update fetch pre-releases.</td>
        <td>Optional</td>
        <td>True, False (default).</td>
    </tr>
</table>

## Using as a module

You can use `pyxelrest` as a python module as well.

```python
import pyxelrest

configuration = {'petstore': {'open_api': {'definition': 'http://petstore.swagger.io/v2/swagger.json'}}}
pyxelrest.load(configuration)

# Import statement MUST be after the call to pyxelrest.load as the modules are generated by this call
from pyxelrest.user_defined_functions import petstore

# Functions are available as python functions within petstore (in this case) and can be used as such
user = petstore.petstore_getUserByName("test")

# {'id': 9999, 'username': 'test', 'firstName': 'test', 'lastName': 'test', 'email': 'test@test.com', 'password': 'test', 'userStatus': 0}
print(user)
```

Refer to [configuration](#services-configuration) section for more details on the available options.

### Generating functions

You can manually (re)generate functions by calling `pyxelrest.load()` and providing your own services configuration.

All functions can be found within `pyxelrest.user_defined_functions` module. 
But you can also access the functions available for a single REST API by using the specific `pyxelrest.user_defined_functions.{my_api}` module where `{my_api}` is the name of the configuration section as shown in the example.

## Migration guide

### 0.69.0 to 1.0.0

#### Configuration changes

`udf` section has been replaced by a `formulas` section.

We __strongly__ advise to check out the new `dynamic_array` formulas if your [Microsoft Excel] version supports it.
Otherwise:

 * `sync_auto_expand` `return_type` corresponds to `legacy_array` sub-section with `lock_excel` set to `true`
 * `async_auto_expand` `return_type` corresponds to `legacy_array` sub-section with `lock_excel` set to `false`
 * `vba_compatible` `return_type` (in case there was another `return_type` as well) corresponds to `vba_compatible` sub-section with `lock_excel` set to `true`
 * `vba_compatible` `return_type` (in case it was the only `return_type`) corresponds to `legacy_array` sub-section with `lock_excel` set to `true`

`shift_result` is not an option anymore. As a result, formulas results will start from the first cell.

##### Previous (0.69.0)

```yaml
udf:
    return_types:
        - sync_auto_expand
```

##### New (1.0.0)

```yaml
formulas:
    legacy_array:
        lock_excel: true
```

## Developer Installation

1. Within [Microsoft Excel], `Trust access to the VBA project object model` should be enabled.
   > File > Options > Trust Center > Trust Center Settings > Macro Settings
2. Build the add-in C# solution using [Microsoft Visual Studio](https://visualstudio.microsoft.com):

   In order to do so, you need [Microsoft Office tools](https://visualstudio.microsoft.com/vs/features/office-tools/) to be installed and to add a test certificate.
   > Project > AutoLoadPyxelRestAddIn > Signing
3. [Microsoft Excel] must be closed while executing the following script from within `pyxelrest` root folder:

        developer_install.bat

## Frequently Asked Question

### Microsoft Excel Wizard does not show any parameter

<p align="center">
  <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/screenshot_udf_wizard_parameters_limit.PNG" alt='Microsoft Excel Wizard bug'>
</p>

[Microsoft Excel] function wizard is not able to handle functions with a long definition.

The total length of parameter names (and commas to separate them) should not exceed 253 characters,

In case it does (your UDF has a lot of parameters or parameters with long names), then [Microsoft Excel] is unable to display them all in the function wizard.

To overcome this [Microsoft Excel] limitation you can try the following:
 * Exclude some parameters (refer to [Open API](#openapi) configuration section for more information).
 * Remove some parameters in your service.
 * Reduce the length of your service parameter names.

### Microsoft Excel Wizard only list some functions

[Microsoft Excel] function wizard is not able to list more than a certain amount of functions per category.

However all functions can be directly accessed in cells.

To overcome this [Microsoft Excel] limitation you can try the following:
 * Exclude some functions in your service (refer to [Open API](#openapi) configuration section for more information).

### No command specified in the configuration, cannot autostart server

This error will happen in case you manually specified in your `xlwings.bas` file to use debug server but did not uncomment the main function starting the server on `pyxelrest` module side.

### Microsoft Excel COM Add-In cannot be installed

Check that all requirements are met:
 * [Microsoft .NET Framework >= 4.5.2](http://go.microsoft.com/fwlink/?linkid=328856) must be installed.
 * [Microsoft Visual Studio 2010 Tools for Office Runtime](https://www.microsoft.com/en-us/download/details.aspx?id=48217) must be installed.

In case you encounter an issue like `Could not load file or assembly 'Microsoft.Office.BusinessApplications.Fba...` anyway, you then need to remove `C:\Program Files\Common Files\Microsoft Shared\VSTO\10.0\VSTOInstaller.exe.config` file.

In case you encounter an issue like `...An application with the same identity is already installed...`, you then need to manually remove all folders within `%USERPROFILE%\AppData\Local\Apps\2.0` and restart your computer.

### Dates with a year higher than 3000 are not converted to local timezone

Due to timestamp limitation, dates after `3000-12-31` and date time after `3001-01-01T07:59:59+00:00` cannot be converted to local timezone.

### Python process exited before it was possible to create the interface object

You need to check [log files](#logging-configuration) to identify the underlying issue.

### pyxelrest.xlam is not available

The add-in might be disabled.

Within [Microsoft Excel], go to `File/Option/addin` and check disabled items (`Manage: Disabled Items`)

[Microsoft Excel]: https://products.office.com/en-us/excel
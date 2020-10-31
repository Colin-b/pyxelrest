<h2 align="center">Query REST APIs using Microsoft Excel formulas or python functions</h2>

<p align="center">
<a href="https://pypi.org/project/pyxelrest/"><img alt="pypi version" src="https://img.shields.io/pypi/v/pyxelrest"></a>
<a href="https://github.com/Colin-b/pyxelrest/actions"><img alt="Build status" src="https://github.com/Colin-b/pyxelrest/workflows/Release/badge.svg"></a>
<a href="https://github.com/Colin-b/pyxelrest/actions"><img alt="Coverage" src="https://img.shields.io/badge/coverage-71%25-orange"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/Colin-b/pyxelrest/actions"><img alt="Number of tests" src="https://img.shields.io/badge/tests-395 passed-blue"></a>
<a href="https://pypi.org/project/pyxelrest/"><img alt="Number of downloads" src="https://img.shields.io/pypi/dm/pyxelrest"></a>
</p>

PyxelRest allows you to query [Swagger 2.0/OpenAPI](https://www.openapis.org) REST APIs (or any HTTP/HTTPS URL) using:
* [Microsoft Excel] [array formulas](https://support.office.com/en-us/article/Create-an-array-formula-E43E12E0-AFC6-4A12-BC7F-48361075954D) ([dynamic](https://support.office.com/en-us/article/dynamic-array-formulas-and-spilled-array-behavior-205c6b06-03ba-4151-89a1-87a7eb36e531?ns=EXCEL&version=90&ui=en-US&rs=en-US&ad=US) and legacy) and Visual Basic for Applications functions:

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

Functions are automatically re-generated on [Microsoft Excel] startup and on configuration update.

<p align="center">
  <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/update_functions_generate_startup.gif" alt='Formula generation'>
</p>
<p align="center"><em>Even if you should not need it, you can manually update functions by clicking on the <span style="color: #1382CE">Update Functions</span> button within <span style="color: #1E1E1F">PyxelRest</span> tab.</em></p>

### Automatic update

<p align="center">
  <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/update_gui.gif" alt='Update steps'>
</p>
<p align="center"><em>Check for update is performed when closing Microsoft Excel (it can be deactivated), you will be prompted in case one is available.</em></p>

## How to install

1. [Python >= 3.7](https://www.python.org/downloads/) must be installed (with [`pip`](https://pip.pypa.io/en/stable/) and [`tkinter`](https://docs.python.org/3/library/tkinter.html) for auto update to work).
2. Use [`pip`](https://pip.pypa.io/en/stable/) to install module:
```bash
python -m pip install pyxelrest
```

### Microsoft Excel add-in installation (optional)

Once `pyxelrest` python module is installed, `pyxelrest_install_addin` executable is available to install the [Microsoft Excel] COM add-in.

1. [Microsoft Excel >= 2010](https://products.office.com/en-us/excel) must be installed (Office 365 is supported).
2. [Microsoft .NET Framework >= 4.5.2](http://go.microsoft.com/fwlink/?linkid=328856) must be installed (Chances are that it is already installed).
3. Within [Microsoft Excel], `Trust access to the VBA project object model` should be enabled.
   > File > Options > Trust Center > Trust Center Settings > Macro Settings
4. [Microsoft Excel] must be closed while executing the following command:
```bash
pyxelrest_install_addin
```

Note: The add-in is not required if you only want to use `pyxelrest` [as a python module](#using-as-a-module).

#### Microsoft Excel add-in installer options

| Name | Description | Possible values |
|------|-------------|-----------------|
| path_to_up_to_date_configuration | Path to up to date configuration file(s). This path will be used to keep services configuration up to date and provide a list of available services within the [Microsoft Excel] add-in. | file path, folder path or an URL returning a file content. |
| check_pre_releases | Also fetch pre-releases when checking for updates. | No value is required, providing the option is enough. No pre-release check by default. |
| add_in_directory | Directory containing PyxelRest [Microsoft Excel] COM add-in. | Default to `..\pyxelrest_addin` relatively to the python executable directory. |

Note: option name must be prefixed with `--` such as:
```bash
pyxelrest_install_addin --check_pre_releases
```

## How to uninstall

1. Go to `Control Panel/Programs and Features` and uninstall `PyxelRestAddIn`.
2. Execute the following command:
```bash
python -m pip uninstall pyxelrest
```
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

Sample configuration files can be found in the [samples repository](https://github.com/Colin-b/pyxelrest/tree/develop/samples).

#### Service mandatory settings

| Name | Description |
|------|-------------|
| open_api | Dictionary describing the OpenAPI definition. Refer to [OpenAPI](#openapi) section for more information. |

Values can be environment variables if provided in the `%MY_ENV_VARIABLE%` form (where `MY_ENV_VARIABLE` is an environment variable).

#### Service options

Values can be environment variables if provided in the `%MY_ENV_VARIABLE%` form (where `MY_ENV_VARIABLE` is an environment variable).

| Name | Description | Possible values |
|------|-------------|-----------------|
| description | A small description of this service. To be displayed within [Microsoft Excel] add-in services configuration screen. | |
| methods | List of services methods to be exposed as UDFs. Retrieve all standards HTTP methods by default (get, post, put, delete, patch, options, head). | get, post, put, delete, patch, options, head |
| formulas | Dictionary containing user defined function (formulas) related settings. Refer to [Formulas](#formulas) section for more information. Generate dynamic array formulas by default. | |
| headers | Dictionary containing headers were key is the name of the header that should be sent with every request sent to this service. | |
| auth | Dictionary containing authentication related settings. Refer to [Authentication](#authentication) section for more information. | |
| network | Dictionary containing network related settings. Refer to [Network](#network) section for more information. | |
| skip_update_for | List of section names that should not be auto-updated. | |
| python_modules | List of extra python module names that should be installed. | |
| caching | Caching results in-memory to avoid sending the same queries too often. Dictionary containing caching related settings. Refer to [Caching](#caching) section for more information. | |
| result | Dictionary containing result related settings. Refer to [Result](#result) section for more information. | |
| udf_name_prefix | Prefix to be used in front of UDf name. `{service_name}` will be replaced by the actual service name. | {service_name}_ |

#### OpenAPI

| Name | Description | Mandatory | Possible values |
|------|-------------|-----------|-----------------|
| definition | [URL](https://en.wikipedia.org/wiki/URL) to the OpenAPI definition. `http://`, `https://` and `file:///` (such as `file:///C:\swagger.json`) schemes are supported. | Mandatory | |
| definition_read_timeout | Maximum amount of time, in seconds, to wait when requesting an [OpenAPI 2.0 definition]. Wait for 5 seconds by default. For more details refer to [`requests` timeouts] | Optional | any float value |
| definition_retrieval_auths | List all authentication that should be used when retrieving the [OpenAPI 2.0 definition]. Use no authentication by default. | Optional | oauth2_implicit, oauth2_access_code, oauth2_password, oauth2_application, api_key, basic, ntlm (see [NTLM](#ntlm) to provide details) |
| excluded_tags | List of tags within [OpenAPI 2.0 definition] that should not be retrieved. If not specified, no filtering is applied. | Optional | |
| selected_tags | List of tags within [OpenAPI 2.0 definition] that should be retrieved (if not within excluded tags already). If not specified, no filtering is applied. | Optional | |
| excluded_operation_ids | List of operation_id (or regular expressions) within [OpenAPI 2.0 definition] that should not be retrieved. If not specified, no filtering is applied. | Optional | |
| selected_operation_ids | List of operation_id (or regular expressions) within [OpenAPI 2.0 definition] that should be retrieved (if not within excluded operation_ids already). If not specified, no filtering is applied. | Optional | |
| excluded_parameters | List of parameter names (or regular expressions) within [OpenAPI 2.0 definition] that should not be exposed. If not specified, no filtering is applied. | Optional | |
| selected_parameters | List of parameter names (or regular expressions) within [OpenAPI 2.0 definition] that should be exposed (if not within excluded parameters already). If not specified, no filtering is applied. | Optional | |
| rely_on_definitions | Rely on [OpenAPI 2.0 definitions](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#definitionsObject) to re-order fields received in response. Deactivated by default. | Optional | `true` or `false` |
| service_host | Service host in case your service is behind a reverse proxy and `basePath` is not properly set in [OpenAPI 2.0 definition]. | Optional | |

#### Formulas

Specify what kind of [formulas](https://support.office.com/en-us/article/Create-an-array-formula-E43E12E0-AFC6-4A12-BC7F-48361075954D) will be generated for every REST API endpoint.

##### Dynamic array formulas

Identified by the `dynamic_array` key within `formulas` section.

| Name | Description | Possible values |
|------|-------------|-----------------|
| lock_excel | Should [Microsoft Excel] be locked (no other action can be performed) until the results are received. | `true` or `false` (default) |

##### Legacy array formulas

Identified by the `legacy_array` key within `formulas` section.

| Name | Description | Possible values |
|------|-------------|-----------------|
| lock_excel | Should [Microsoft Excel] be locked (no other action can be performed) until the results are received. | `true` or `false` (default) |

##### Visual Basic for Applications (VBA) formulas

Identified by the `vba_compatible` key within `formulas` section.

#### Authentication

Contains authentication related settings.

| Name | Description | Possible values |
|------|-------------|-----------------|
| oauth2 | Dictionary containing OAuth2 authentication related settings. Refer to [OAuth 2](#oauth-2) section for more information. |
| api_key | User API Key. Can be an environment variable surrounded by `%` as in `%MY_API_KEY_ENV_VAR%`. |
| basic | Dictionary containing Basic authentication related settings. Refer to [Basic](#basic) section for more information. |
| ntlm | Dictionary containing NTLM authentication related settings. Refer to [NTLM](#ntlm) section for more information. |

##### OAuth 2

Depending on the flow, every parameter supported by [requests-auth](https://colin-b.github.io/requests_auth/) can be provided.

Note that `token_url` and `authorization_url` are extracted from [OpenAPI 2.0 definition], thus they do not need to be provided.

##### Basic

| Name | Description | Mandatory |
|------|-------------|-----------|
| username | User name | Mandatory |
| password | User password | Mandatory |

##### NTLM

| Name | Description |
|------|-------------|
| username | User name. Should be of the form `domain\\user`. Default value is the logged in user name. |
| password | User password. Default value is the logged in user password. |

In case user credentials are provided, [`requests_ntlm==1.*`](https://pypi.org/project/requests_ntlm/) module is required.
```bash
python -m pip install requests_ntlm==1.*
```

In case user credentials are not provided (using logged in user credentials), [`requests_negotiate_sspi==0.5.*`](https://pypi.org/project/requests-negotiate-sspi/) module is required.
```bash
python -m pip install requests_negotiate_sspi==0.5.*
```

#### Network

Contains network related settings such as HTTP timeouts or proxies configuration.

| Name | Description | Possible values |
|------|-------------|-----------------|
| max_retries | Maximum number of time a request should be retried before considered as failed. 5 by default. | Any positive integer value |
| connect_timeout | Maximum amount of time, in seconds, to wait when trying to reach the service. Wait for 1 second by default. For more details refer to [`requests` timeouts] | any float value |
| read_timeout | Maximum amount of time, in seconds, to wait when requesting a service. Wait for 5 seconds by default. For more details refer to [`requests` timeouts] | any float value |
| proxies | Proxies that should be used to reach service. This is a dictionary where keys are the scheme (http or https) and/or no_proxy. If the key is a scheme then the value should be the proxy URL. Otherwise the value should be the URL for which proxies should be ignored. For more details refer to [`requests` documentation](https://requests.readthedocs.io/en/master/user/advanced/#proxies) | |
| verify | Verify SSL certificate for HTTPS requests. Default to `true`. For more details refer to [`requests` documentation](https://2.python-requests.org/en/master/user/advanced/#ssl-cert-verification) | |

#### Caching

| Name | Description |
|------|-------------|
| result_caching_time | Number of seconds during which a GET request will return previous result. Always send a new request by default. |
| max_nb_results | Maximum number of results to store in cache. 100 by default. |

[`cachetools==4.*`](https://pypi.org/project/cachetools/) module is required.
```bash
python -m pip install cachetools==4.*
```

#### Result

| Name | Description |
|------|-------------|
| flatten | Flatten received JSON to a 2-Dimension array. Default to `true` |
| raise_exception | Raise received exceptions to client. `false` by default. |

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

| Name | Description | Mandatory | Possible values |
|------|-------------|-----------|-----------------|
| PathToPython | Path to the python.exe (including) executable where pyxelrest python module was installed. | Mandatory | Installation script is already setting this value properly. |
| AutoCheckForUpdates | Activate or Deactivate automatic check for PyxelRest update on Microsoft Excel closing. | Optional | True (default), False |
| GenerateUDFAtStartup | Activate or Deactivate generation of user defined functions at Microsoft Excel startup. | Optional | True (default), False |
| PathToXlWingsBasFile | Path to the XlWings modified BAS file used to configure XlWings for PyxelRest. | Mandatory | Installation script is already setting this value properly. |
| PathToUpToDateConfigurations | Path to the file or directory containing up to date services configuration. | Optional | Installation script is already setting this value if provided. |
| CheckPreReleases | Should auto update fetch pre-releases. | Optional | True, False (default). |

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

   In order to do so, you need [Microsoft Office tools](https://visualstudio.microsoft.com/vs/features/office-tools/) to be installed.
   You also need to create a test certificate.
   > Project > PyxelRestAddIn > Signing
3. [Microsoft Excel] must be closed while executing the following script from within `pyxelrest` root folder:
```batch
developer_install.bat
```

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

### Can I install xlwings and pyxelrest?

Yes.

We advise to install [`pyxelrest`] in its own virtual environment.
As [`pyxelrest`] relies on [`xlwings`], if you want to use [`xlwings`] you can, but if you rely on some specific [`xlwings`] configuration, you should use a separate environment.

The [`pyxelrest`] add-in and [`xlwings`] add-in can be installed for the same user as long as [`pyxelrest`] is installed in a separate virtual environment.

[Microsoft Excel]: https://products.office.com/en-us/excel
[OpenAPI 2.0 definition]: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md
[`requests` timeouts]: https://2.python-requests.org/en/master/user/advanced/#timeouts
[`xlwings`]: https://www.xlwings.org
[`pyxelrest`]: https://pypi.org/project/pyxelrest/
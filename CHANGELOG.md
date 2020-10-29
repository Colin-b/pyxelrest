# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Log number of received results.
- Log error in case caller cell cannot be retrieved.
- Add more information on VBA caller.
- Support for [Dynamic array formulas](https://support.office.com/en-us/article/dynamic-array-formulas-and-spilled-array-behavior-205c6b06-03ba-4151-89a1-87a7eb36e531?ns=EXCEL&version=90&ui=en-US&rs=en-US&ad=US)
- Allow to `verify` SSL certificate (or not).

### Fixed
- Do not use a fixed dependency version.
- Compatibility with `python` `3.8` and `3.9`.
- Ability to change the configuration and impact loaded functions within module without restarting python.
- file URl are now properly handled, they must start with `file:///` instead of `file://`
- Updater do not rely on yaml anymore. Instead, a basic configuration for logging is used. This should prevent random yaml upgrade issues.
- Do not request VBA caller in threading context (as it cannot be retrieved and result in COM call failure).
- The `PyxelRestAddIn` does not read default `xlwings` configuration anymore. Allowing to run in addition of the `xlwings` add-in.

### Removed
- Drop support for `python` < `3.8`.
- Drop support for `application/msgpackpandas` as `msgpack` support has been dropped from `pandas` and this is not a standardized content type.
- Drop support for `ujson`.
- Drop support for `ini` configuration files.
- Drop support for shifted results as there is no need for it anymore, first cell is always filled with an up to date value.
- Python update script path is now guessed by addin, no need to provide the path in configuration anymore.
- Drop `ntlm` and `cachetools` extra. As documentation clearly state what is supported and that there is no added value.

### Changed
- Auto update does not request pre-releases by default anymore. It must be explicitly requested via `--check_pre_releases`.
- Use HTTPS scheme whenever possible.
- Generate one python file with UDFs per service.
- Most of the python modules and functions are now private. If you need access to some internals, please open an issue.
- Most of the scripts are now inside the `pyxelrest` package.
- Update all dependencies to the latest major release.
- `read_timeout` now default to `5s` instead of waiting indefinitely.
- Network related settings (`max_retries`, `connect_timeout`, `read_timeout`, `proxies`) are now supposed to be provided within `network` configuration section.
- SSL certificate is now verified by default. You can change this by setting `network` `verify` to `false`.
- Authentication related settings (`oauth2`, `api_key`, `basic`, `ntlm`) are now supposed to be provided within `auth` configuration section.
- Display default values for OAuth2 settings in configuration UI.
- Renamed Microsoft Excel add-in to `PyxelRestAddIn`.

## [0.69.0] - 2018-12-03
### Changed
- OAuth2 parameters should now match the one handled by requests_auth.

### Added
- Provide UDF book name, sheet name and cell address within X-Pxl-Cell header.
- Send OAuth2 token within Authorization header by default.
- Allow to specify header name and header value for the non-standard OAuth2 services.
- Logs are now identifying the Book, Sheet and Cell performing the call.
- Document value 303 in wait_for_status pyxelrest_get_url parameter.
- Rely on latest official xlwings release (0.14.1).
- Allow to cache GET requests results.
- Support all authentication mechanism.
- Ease up usage of pyxelrest as a python module.
- Add parameter to configure result flatten, raising of exceptions and udf name prefix.

### Fixed
- Do not truncate logs in case of error reception from REST api call.
- Do not limit values of NumericUpDown within add-in configuration form.
- Update dependencies to latest version.
- Handle . (dot) in parameter name.
- Properly check that logs folder does not exists (warning was always issued).
- Previous results are now cleared when using asynchronous UDFs with shifted results.
- Make sure null values are sent in array only if swagger explicitly state that null values are allowed.
- Handle date and date-time prior or equal to 1970-01-01T01:00:00+00:00
- Support for pip > 9 (shipped with recent Python versions).
- Handle more than one leading underscore in field name.
- Send date as ISO Format instead of a datetime.

## [0.68.4] - 2018-08-07
### Fixed
- First cell in case of an asynchronous call will now contains "Formula" instead of being blank. To help users in case of non-shifted results.

## [0.68.3] - 2018-08-05
### Added
- Allow to authenticate for OpenAPI definition retrieval.
- "Save configuration" button is now grey when deactivated (instead of a lighter green).
- Allow to select a file when providing an OpenAPI definition.
- Disable the "Save configuration" button by default. Only activate when an actual modification occurred.

### Fixed
- Handle object parameter without ref in schema but properties instead.
- Add a ClickOnce version number for the add-in.
- Handle enum on numbers.
- Update now longer considered as ongoing if process is killed while updating. This was preventing automatic upgrade.
- Services configuration file is now created by add-in if needed. Previously generating an error.
- Logs folder is now created by add-in if needed. Previously generating an error.
- Default logs folder is now created by pyxelrest if needed. Previously generating an error in case default logging should be used.
- In case asynchronous calls are not shifted and result is on a single cell, result was not displayed. It is now shifted in this case.

## [0.68.2] - 2018-07-26
### Fixed
- Convert array parameters to the proper type whenever possible (integers, float, date and date-time).
- Allow to load UDFs even if UDFs are not loaded at startup.
- Update requests dependency to latest version (2.19.1)
- Fix PyYaml version (as it is not fixed by Pyaml) and update it to latest stable one (3.13)

## [0.68.1] - 2018-06-21
### Fixed
- XlWings users using RunPython were not able to access the workbook.

## [0.68.0] - 2018-06-08
### Added
- Update the usage of xlwings to be able to switch to the official version (possible since 0.11.8).
- Allow to provide extra python modules in configuration.
- Increment python-dateutil dependency to latest version (2.7.3)

### Fixed
- Environment variables were not interpreted anymore for headers and api_key since 0.67.0
- Minimum length of arrays were not properly checked, leading to invalid rejection.
- Prompt user only once per update.
- Return a proper error message in case asynchronous method is called by VBA.
- Allow to switch a configuration to VBA compatible only using add-in.
- Use xlwings ndim option to convert arrays
- Look for more than one location to ensure that "Programmatic Access to VBA Project" is enabled.
- Error message is now displayed in case results should be shifted.

## [0.67.0] - 2018-05-07
### Changed
- Previous services configuration files are not compatible anymore but convert is performed when updating.
- XlWings fork updated to latest xlwings version (0.11.7)

### Added
- Microsoft Excel add-in allows to select services from within a list as well as manually.
- Services configuration are kept up to date on Microsoft Excel start.
- Services configuration are kept up to date with latest version when editing configurations.
- Use YAML format for configuration (remove restriction on the content of values).
- Services are now loaded even if a service name is duplicated.
- Allow to avoid auto update of some fields within configuration.
- Allow to select services affected by an action during auto update.
- Allow to exclude OpenAPI tags.
- Allow to include or exclude OpenAPI operation_ids.
- Experimental support for Asynchronous UDFs.
- Allow to shift results by one column to the right.
- Additional dependencies can be installed via extra_requires.
- Optional UDF parameters can be hidden.

### Fixed
- If UDFs are not generated at startup according to user configuration. checkbox is now reflecting it.
- Microsoft Excel only allows 3 lines of UDF parameter description. Avoid one line per restricted values.
- UDF Parameter description now contains default value.
- Handle more parameter checks (maximum, exclusiveMaximum, minimum, exclusiveMinimum, maxLength, minLength, maxItems, minItems, uniqueItems, multipleOf)
- collectionFormat was ignored and considered as multi. It is now properly handled.
- Return a list with one string item in case response from server is not JSON but JSON was expected.
- Exceptions were not properly handled on workbook activation event.
- PyxelRest service now allows to specify authentication.
- Update Notification window will now be raised on forefront to prevent user missing it.
- Consider float value sent for a string field as an integer string value if there is no decimal (send 1.0 as '1').
- When receiving a single row and an array of array is expected, an array containing this single row (as one array) should now be sent.
- Allow to send non-described body.

## [0.66.0] - 2018-03-30
### Added
- Add field type and restricted values to UDF parameter documentation.
- Depends on the brand new official pywin32 package (pipywin32 is now only a proxy to pywin32).
- add-in installation script no longer have mandatory parameters.

## [0.65.0] - 2018-03-28
### Changed
- tags property do not exists anymore. Instead it is now available as key within advanced_configuration property (value separator is now semicolon).

### Added
- Allow to prevent generation of user defined functions at Microsoft Excel startup (see README for more information).
- Handle asynchronous REST APIs (HTTP 202 status code response).
- Provide ability to send custom GET/POST/PUT/DELETE requests thanks to definition of a pyxelrest service.
- Reduce code duplication in generated user defined function python file. Should result in a faster loading.
- Allow to post/put dictionaries and lists easily.
- Allow to post/put files by specifying content or file path.
- Display PyxelRest python module version in Microsoft Excel add-in.
- Auto update is not semi silent anymore and is providing information on every updating step.
- Less verbose error message in case a configuration file provided as a URL cannot be reached.
- Ability to generate both synchronous and asynchronous user defined functions.
- Allow same parameter name within different location.
- Python module users can now use a different logging and/or services configuration file path.

### Fixed
- Auto update settings were not saved.
- Array parameters are now always sent as array (was not the case for length 1 arrays).
- boolean and date-time arrays of length > 1 were not sent properly (not as boolean and not as ISO8601 formatted date-time)
- Update logs will now contains information about the whole upgrade process.
- Reject with a user friendly error message in case a date or date time is sent instead of a string.
- Send number formatted values as string if required by the OpenAPI definition.
- Avoid a configuration update script failure in case file do not exists.
- Excel boolean values were not handled.
- None values are now allowed within body.

## [0.64.1] - 2018-02-14
### Fixed
- Avoid uninstalling Microsoft Excel Add-in in case it cannot be installed back.
- Make sure Microsoft Excel Add-in can be installed in case 32 bits VSTO installer is the only one available.
- Use latest log4net version and latest version of python dependencies.
- Handle VBA reserved keywords within uri (eg. /resource/{name}/child/{attribute}).
- Add compatibility with Python 2.7 back.
- Handle date and date time after year 3000.
- Handle application/msgpackpandas with Python 3.

## [0.64.0] - 2017-12-20
### Added
- Introduce a new advanced configuration property: swagger_read_timeout. Allows to provide a read timeout for swagger retrieval (to avoid being stuck when service is not available behind an available reverse proxy).
- PyxelRest is now installed without the Microsoft Excel Add-In (to be used as an external module).

### Fixed
- Date Time are now sent following ISO format.
- Handle "attribute" VBA keyword.

## [0.63.1] - 2017-11-14
### Fixed
- Handle basePath ending with slash.

## [0.63.0] - 2017-10-10
### Changed
- connect_timeout and read_timeout properties do not exists anymore. Instead they are now available as keys within advanced_configuration property.

### Added
- Introduce new max_retries key for advanced_configuration property. Refer to documentation for more details. Previous behavior was "never retry", it will now retry 5 times by default.
- Update script no longer removes logs folder on update, the whole update process can now be logged.
- It is now possible to specify custom headers in advanced_configuration property. Refer to documentation for more details.
- Default OAuth2 authentication timeout was increased from 20 seconds to 1 minute.
- methods property now have a default value, meaning that by default all standards HTTP methods will be retrieved.
- It is now possible to specify more than one proxy per service (in case both http and https schemes are required). It is also possible to specify a no_proxy url as well.
- Authentication is now mostly handled in a separate `requests_auth` module, this module was refactored to get rid of the `flask` dependency.
- ClickOnce application cache will now be cleared after Microsoft Excel add-in uninstallation to ensure that next installation succeed. Installing add-in will now be possible even if Microsoft Excel is launched.
- Services configuration can now be auto-updated as part of the auto-update process.
- Updater now display the new version of PyxelRest and is faster to detect update.
- PathToPIP add-in property is not used anymore.

### Fixed
- application/msgpackpandas was always requested (if supported by server) even when pandas was not supported on client side
- PyxelRest is now properly set as a python package and can be used outside Microsoft Excel.
- file:// OpenAPI definition URL are now properly analyzed by Microsoft Excel Add-In
- Only HTTP GET results can now be cached as it does not make sense for other HTTP methods.
- Do not prompt anymore for one update per closed Microsoft Excel instance. Only prompt the user once.
- operationId was considered as mandatory in OpenAPI definition while it is not, leading to services without operationId not being able to be loaded.
- operationId was considered as unique within an OpenAPI definition, leading to missing UDFs if it was not the case.

## [0.62] - 2017-06-27
### Changed
- security_details OAuth2 response_type key is now oauth2.response_type
- rely_on_definitions property should now be set using the newly introduced advanced_configuration property.

### Added
- It is now possible to override and specify new parameters for OAuth2 authentication URL by using "oauth2." prefix in security_details key name.
- Security details values can be loaded from environment variables.
- UDFs can now be synchronous, meaning you will need to specify the result array within Microsoft Excel before the call. Refer to documentation for more details.
- It is now possible to request more methods than the usual get, post, put or delete.
- Microsoft Excel Auto-Load add-in now also allows to select patch, options and head HTTP methods.

## [0.61] - 2017-06-22
### Added
- Generated UDFs can now be called from VBA (Using RunPython).
- response_type can be provided in security_details property in case it is not provided in authorization_url and it is not default value (token).
- You can now cache the results of an UDF call in order to avoid calling the service once again.

### Fixed
- In case a huge number of UDFs are relying on the same cell value, some UDFs might have not returned a value. This issue should be fixed in xlwings-0.10.4.2.

## [0.60] - 2017-06-19
### Added
- API Key Security definition support. You should specify your API Key thanks to api_key keyword in security_details property.
- Basic security definition support. You should specify your username and password thanks to username and password keywords in security_details property.
- Slight performance improvement on UDFs loading.
- If more than one supported authentication step is required, all steps are now performed.
- OpenAPI definition URI can now contains a path to an OpenAPI definition on the file system using file:// prefix.
- Services requiring NTLM authentication are now accessible thanks to auth=ntlm within security_details property.
- Dependencies are now up-to-date (jinja2, requests, xlwings and flask upgraded to latest version)
- Oauth2 authentication response display time can be tweaked thanks to success_display_time and failure_display_time keys within security_details property.

### Fixed
- content-type header was sent instead of accept.
- content-type header is now set to the proper value according to OpenAPI "consumes" field.
- produces, consumes, parameters and security are now handled even if defined at root or methods level.
- Microsoft Internet Explorer should now be properly opened and closed to perform authentication.
- rely_on_definitions property was not working on Python 2.7

## [0.59] - 2017-05-31
### Added
- Add support for HTTPS services (do not validate certificate though).
- Focus will come back to Microsoft Excel after successful authentication (now performed using Microsoft Internet Explorer by default).

### Fixed
- security_details invalid value cannot be set anymore using Microsoft Excel Auto-Load add-in.
- Regression since 0.58, PyxelRest was not compatible with Python < 3.6
- Handle all restricted VBA Keywords described here: https://msdn.microsoft.com/en-us/library/ksh7h19t(v=vs.90).aspx?f=255&MSPPError=-2147217396
- Handle "type" restricted VBA keyword.
- All date times fields were still displayed as string in Microsoft Excel for Python 2.7 users.
- Handle produces section defined at OpenAPI definition root level instead (or in addition) of operation level.

## [0.58] - 2017-05-11
### Changed
- As OpenAPI definition responses sections is now read, content is validated. Meaning non compliant OpenAPI files (not providing any response) are now rejected.

### Added
- OAuth 2 Security definition support.
- It is possible to force the port and the timeout used by server to retrieve the OAuth 2 authentication token using security_details property.
- JSON deserialization can now be performed using uJSON following OpenAPI definitions field ordering. This can be activated thanks to rely_on_definitions property.

### Fixed
- Results were not provided in case a cell value was expected to contains more than 255 characters (Only first 255 characters are now provided).
- All date times fields are now displayed as local date times within Microsoft Excel (some were still interpreted as text).

## [0.56] - 2017-03-24
### Added
- Connection timeout can now be specified per service (1 second by default).
- Read timeout can now be specified per service (no timeout by default).
- Path to XlWings module can be configured by user.

### Fixed
- "0" and "False" where converted to an empty string before sent to Microsoft Excel.
- Post installation script was not setting PathToUpdateScript property. Leading to update not being performed.

## [0.55] - 2017-03-06
### Changed
- Log more client deserialization details.
- Installer is not assuming anymore that provided paths are valid to avoid failures afterwards and ease debugging.

### Fixed
- Path to PIP was wrong in case the user is not using a Python virtual environment, leading to updates not being performed.

## [0.54] - 2017-03-02
### Added
- Logging is not performed in DEBUG anymore by default. Consider PyxelRest as stable enough.
- It is now possible to deactivate the "Auto Check for Update" feature by removing the property from the configuration file.
- Microsoft Excel Auto-Load add-in is now always generating files prefixed with the date.
- Default logging configuration now keep only the last 10 files (others are dropped to save disk space).

### Fixed
- Auto updater was not working as he was logging the update result in a log file we are trying to remove.

## [0.53] - 2017-03-01
### Changed
- Microsoft Excel Auto-Load add-in uninstall is not silent anymore on PyxelRest update.

### Added
- Microsoft Excel Auto-Load add-in is now able to check for PyxelRest update on close and ask for an auto update if available.
- Logs now also contains requested URL in case of a valid response.
- Microsoft Excel Auto-Load add-in configuration can now be user specific and is located in configuration folder.

### Fixed
- Update will now fail in case of Microsoft Excel Auto-Load add-in uninstall failure.
- Avoid trying to uninstall add-in that was not installed previously because of previous failure at add-in installation step.

## [0.52] - 2017-02-24
### Changed
- Default configuration is now using the official OpenAPI example.
- Configuration files are now located in a specific configuration folder.

### Added
- Logs are now cleared on each PyxelRest update.

## [0.51] - 2017-02-23
### Added
- Ability to filter by tags.

## 0.50 - 2017-02-22
### Changed
- This version breaks compatibility with previous ones.
- To ensure that you update properly please follow uninstall procedure first.

### Added
- PyxelRest version is now displayed in Microsoft Excel.
- PyxelRest folder can now be opened from within Microsoft Excel (to ease investigation).

### Fixed
- Python for Windows extension was not listed in dependencies, thus not installed automatically.
- In case add-in version changed, the previous version was not automatically uninstalled.

## [0.49] - 2017-02-09
### Fixed
- Structure with more than 1 nested level are now handled (Structure with multiple dictionaries on a same level might not be handled properly).

## [0.48] - 2017-02-08
### Added
- Help on function is now provided for each UDF when available (first link to be present in provided description will be used).
- Microsoft Excel add-in now assert that '''Trust access to the the VBA object model''' is activated before trying to perform an action that would fail.

### Fixed
- XlWings module was loaded twice on Microsoft Excel startup in case it was already loaded.

[Unreleased]: https://github.com/Colin-b/pyxelrest/compare/v0.69.0...HEAD
[0.69.0]: https://github.com/Colin-b/pyxelrest/compare/v0.68.4...v0.69.0

# PyxelRest Changelog #

List all changes in various categories:
* Release notes: Contains all worth noting changes (breaking changes mainly)
* Enhancements
* Bug fixes
* Known issues

## 0.64.1 (2018-02-08) ##

### Bug fixes ###

- Avoid uninstalling Microsoft Excel Add-in in case it cannot be installed back.
- Make sure Microsoft Excel Add-in can be installed in case 32 bits VSTO installer is the only one available.
- Use latest log4net version and latest version of python dependencies.
- Handle VBA reserved keywords within uri (eg. /resource/{name}/child/{attribute}).
- Add compatibility with Python 2.7 back.
- Handle date and date time after year 3000.

## 0.64.0 (2017-12-20) ##

### Enhancements ###

- Introduce a new advanced configuration property: swagger_read_timeout. Allows to provide a read timeout for swagger retrieval (to avoid being stuck when service is not available behind an available reverse proxy).
- PyxelRest is now installed without the Microsoft Excel Add-In (to be used as an external module).

### Bug fixes ###

- Date Time are now sent following ISO format.
- Handle "attribute" VBA keyword.

## 0.63.1 (2017-11-14) ##

### Bug fixes ###

- Handle basePath ending with slash.

## 0.63.0 (2017-10-10) ##

### Release notes ###

- connect_timeout and read_timeout properties do not exists anymore. Instead they are now available as keys within advanced_configuration property.

### Enhancements ###

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

### Bug fixes ###

- application/msgpackpandas was always requested (if supported by server) even when pandas was not supported on client side
- PyxelRest is now properly set as a python package and can be used outside Microsoft Excel.
- file:// swagger URL are now properly analyzed by Microsoft Excel Add-In
- Only HTTP GET results can now be cached as it does not make sense for other HTTP methods.
- Do not prompt anymore for one update per closed Microsoft Excel instance. Only prompt the user once.
- operationId was considered as mandatory in swagger while it is not, leading to services without operationId not being able to be loaded.
- operationId was considered as unique within a swagger file, leading to missing UDFs if it was not the case.

## 0.62 (2017-06-27) ##

### Release notes ###

- security_details OAuth2 response_type key is now oauth2.response_type
- rely_on_definitions property should now be set using the newly introduced advanced_configuration property.

### Enhancements ###

- It is now possible to override and specify new parameters for OAuth2 authentication URL by using "oauth2." prefix in security_details key name.
- Security details values can be loaded from environment variables.
- UDFs can now be synchronous, meaning you will need to specify the result array within Microsoft Excel before the call. Refer to documentation for more details.
- It is now possible to request more methods than the usual get, post, put or delete.
- Microsoft Excel Auto-Load add-in now also allows to select patch, options and head HTTP methods.

## 0.61 (2017-06-22) ##

### Enhancements ###

- Generated UDFs can now be called from VBA (Using RunPython).
- response_type can be provided in security_details property in case it is not provided in authorization_url and it is not default value (token).
- You can now cache the results of an UDF call in order to avoid calling the service once again.

### Bug fixes ###

- In case a huge number of UDFs are relying on the same cell value, some UDFs might have not returned a value. This issue should be fixed in xlwings-0.10.4.2.

## 0.60 (2017-06-19) ##

### Enhancements ###

- API Key Security definition support. You should specify your API Key thanks to api_key keyword in security_details property.
- Basic security definition support. You should specify your username and password thanks to username and password keywords in security_details property.
- Slight performance improvement on UDFs loading.
- If more than one supported authentication step is required, all steps are now performed.
- Swagger URI can now contains a path to a swagger file on the file system using file:// prefix.
- Services requiring NTLM authentication are now accessible thanks to auth=ntlm within security_details property.
- Dependencies are now up-to-date (jinja2, requests, xlwings and flask upgraded to latest version)
- Oauth2 authentication response display time can be tweaked thanks to success_display_time and failure_display_time keys within security_details property.

### Bug fixes ###

- content-type header was sent instead of accept.
- content-type header is now set to the proper value according to Swagger "consumes" field.
- produces, consumes, parameters and security are now handled even if defined at root or methods level.
- Microsoft Internet Explorer should now be properly opened and closed to perform authentication.
- rely_on_definitions property was not working on Python 2.7

## 0.59 (2017-05-31) ##

### Enhancements ###

- Add support for HTTPS services (do not validate certificate though).
- Focus will come back to Microsoft Excel after successful authentication (now performed using Microsoft Internet Explorer by default).

### Bug fixes ###

- security_details invalid value cannot be set anymore using Microsoft Excel Auto-Load add-in.
- Regression since 0.58, PyxelRest was not compatible with Python < 3.6
- Handle all restricted VBA Keywords described here: https://msdn.microsoft.com/en-us/library/ksh7h19t(v=vs.90).aspx?f=255&MSPPError=-2147217396
- Handle "type" restricted VBA keyword.
- All date times fields were still displayed as string in Microsoft Excel for Python 2.7 users.
- Handle produces section defined at Swagger root level instead (or in addition) of operation level.

## 0.58 (2017-05-11) ##

### Release notes ###

- As Swagger responses sections is now read, content is validated. Meaning non compliant Swagger files (not providing any response) are now rejected.

### Enhancements ###

- OAuth 2 Security definition support.
- It is possible to force the port and the timeout used by server to retrieve the OAuth 2 authentication token using security_details property.
- JSON deserialization can now be performed using uJSON following swagger definitions field ordering. This can be activated thanks to rely_on_definitions property.

### Bug fixes ###

- Results were not provided in case a cell value was expected to contains more than 255 characters (Only first 255 characters are now provided).
- All date times fields are now displayed as local date times within Microsoft Excel (some were still interpreted as text).

## 0.56 (2017-03-24) ##

### Enhancements ###

- Connection timeout can now be specified per service (1 second by default).
- Read timeout can now be specified per service (no timeout by default).
- Path to XlWings module can be configured by user.

### Bug fixes ###

- "0" and "False" where converted to an empty string before sent to Microsoft Excel.
- Post installation script was not setting PathToUpdateScript property. Leading to update not being performed.

## 0.55 (2017-03-06) ##

### Release notes ###

- Log more client deserialization details.
- Installer is not assuming anymore that provided paths are valid to avoid failures afterwards and ease debugging.

### Bug fixes ###

- Path to PIP was wrong in case the user is not using a Python virtual environment, leading to updates not being performed.

## 0.54 (2017-03-02) ##

### Enhancements ###

- Logging is not performed in DEBUG anymore by default. Consider PyxelRest as stable enough.
- It is now possible to deactivate the "Auto Check for Update" feature by removing the property from the configuration file.
- Microsoft Excel Auto-Load add-in is now always generating files prefixed with the date.
- Default logging configuration now keep only the last 10 files (others are dropped to save disk space).

### Bug fixes ###

- Auto updater was not working as he was logging the update result in a log file we are trying to remove.

## 0.53 (2017-03-01) ##

### Release Notes ###

- Microsoft Excel Auto-Load add-in uninstall is not silent anymore on PyxelRest update.

### Enhancements ###

- Microsoft Excel Auto-Load add-in is now able to check for PyxelRest update on close and ask for an auto update if available.
- Logs now also contains requested URL in case of a valid response.
- Microsoft Excel Auto-Load add-in configuration can now be user specific and is located in configuration folder.

### Bug fixes ###

- Update will now fail in case of Microsoft Excel Auto-Load add-in uninstall failure.
- Avoid trying to uninstall add-in that was not installed previously because of previous failure at add-in installation step.

## 0.52 (2017-02-24) ##

### Release notes ###

Default configuration is now using the official OpenAPI example.
Configuration files are now located in a specific configuration folder.

### Enhancements ###

- Logs are now cleared on each PyxelRest update.

## 0.51 (2017-02-23) ##

### Enhancements ###

- Ability to filter by tags.

## 0.50 (2017-02-22) ##

### Release notes ###

This version breaks compatibility with previous ones.
To ensure that you update properly please follow uninstall procedure first.

### Enhancements ###

- PyxelRest version is now displayed in Microsoft Excel.
- PyxelRest folder can now be opened from within Microsoft Excel (to ease investigation).

### Bug fixes ###

- Python for Windows extension was not listed in dependencies, thus not installed automatically.
- In case add-in version changed, the previous version was not automatically uninstalled.

## 0.49 (2017-02-09) ##

### Bug fixes ###

- Structure with more than 1 nested level are now handled.

### Known issues ###

- Structure with multiple dictionaries on a same level might not be handled properly.

## 0.48 (2017-02-08) ##

### Enhancements ###

- Help on function is now provided for each UDF when available (first link to be present in provided description will be used).
- Microsoft Excel add-in now assert that '''Trust access to the the VBA object model''' is activated before trying to perform an action that would fail.

### Bug fixes ###

- XlWings module was loaded twice on Microsoft Excel startup in case it was already loaded.

### Known issues ###

- Help on function is always linking to the same URL.

## 0.47 (2017-01-31) ##

### Known issues ###

- Microsoft Excel needs to be restarted for UDFs not to be displayed anymore in function wizard. (Even if calling them does not work).

# PyxelRest Changelog #

## 0.60 (next) ##

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

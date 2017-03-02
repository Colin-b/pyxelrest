# PyxelRest Changelog #

## 0.55 (upcoming) ##

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

### Release Notes ###

Default configuration is now using the official OpenAPI example.
Configuration files are now located in a specific configuration folder.

### Enhancements ###

- Logs are now cleared on each PyxelRest update.

## 0.51 (2017-02-23) ##

### Enhancements ###

- Ability to filter by tags.

## 0.50 (2017-02-22) ##

### Release Notes ###

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

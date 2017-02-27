# PyxelRest Changelog #

## 0.53 (upcoming) ##

### Release Notes ###

- Microsoft Excel Auto-Load add-in uninstall is not silent anymore on PyxelRest update.

### Enhancements ###

- Logs now also contains requested URL in case of a valid response.

### Bug fixes ###

- Update will now fail in case of Microsoft Excel Auto-Load add-in uninstall failure.

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

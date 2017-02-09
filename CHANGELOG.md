# PyxelRest Changelog #

## 0.50 (upcoming) ##

## 0.49 (2017-02-09) ##

### Bug fixes ###

- Structure with more than 1 nested level are now handled

### Known issues ###

- Structure with multiple dictionaries on a same level might not be handled properly

## 0.48 (2017-02-08) ##

### Enhancements ###

- Help on function is now provided for each UDF when available (first link to be present in provided description will be used)
- Excel add-in now assert that '''Trust access to the the VBA object model''' is activated before trying to perform an action that would fail.

### Bug fixes ###

- XlWings module was loaded twice on Excel Startup in case it was already loaded.

### Known issues ###

- Help on function is always linking to the same URL

## 0.47 (2017-01-31) ##

### Known issues ###

- Excel needs to be restarted for UDFs not to be displayed anymore in function wizard. (Even if calling them does not work)

# Frequently Asked Question

* [Microsoft Excel Wizard does not show any parameter](#microsoft-excel-wizard-does-not-show-any-parameter)
* [Microsoft Excel Wizard only list some functions](#microsoft-excel-wizard-only-list-some-functions)
* [No command specified in the configuration, cannot autostart server](#no-command-specified-in-the-configuration-cannot-autostart-server)
* [Microsoft Excel COM Add-In cannot be installed](#microsoft-excel-com-add-in-cannot-be-installed)
* [Dates with a year higher than 3000 are not converted to local timezone](#dates-with-a-year-higher-than-3000-are-not-converted-to-local-timezone)
* [Python process exited before it was possible to create the interface object](#python-process-exited-before-it-was-possible-to-create-the-interface-object)
* [pyxelrest.xlam is not available](#pyxelrestxlam-is-not-available)
* [Can I install xlwings and pyxelrest?](#can-i-install-xlwings-and-pyxelrest)

## Microsoft Excel Wizard does not show any parameter

<p align="center">
  <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/screenshot_udf_wizard_parameters_limit.PNG" alt='Microsoft Excel Wizard bug'>
</p>

[Microsoft Excel] function wizard is not able to handle functions with a long definition.

The total length of parameter names (and commas to separate them) should not exceed 253 characters,

In case it does (your UDF has a lot of parameters or parameters with long names), then [Microsoft Excel] is unable to display them all in the function wizard.

To overcome this [Microsoft Excel] limitation you can try the following:
 * [Exclude some parameters](configuration/rest_api.md#selecting-parameters-to-include-or-exclude).
 * Remove some parameters in your service (in case you manage the service yourself).
 * Reduce the length of your service parameter names (in case you manage the service yourself).

## Microsoft Excel Wizard only list some functions

[Microsoft Excel] function wizard is not able to list more than a certain amount of functions per category.

However, all functions can be directly accessed in cells.

To overcome this [Microsoft Excel] limitation you can try the following:
 * [Exclude some functions in your service](configuration/rest_api.md#do-not-expose-everything-the-rest-api-offers).

## No command specified in the configuration, cannot autostart server

This error will happen in case you manually specified in your `xlwings.bas` file to use debug server but did not uncomment the main function starting the server on `pyxelrest` module side.

## Microsoft Excel COM Add-In cannot be installed

Check that all requirements are met:
 * [Microsoft .NET Framework >= 4.5.2](http://go.microsoft.com/fwlink/?linkid=328856) must be installed.
 * [Microsoft Visual Studio 2010 Tools for Office Runtime](https://www.microsoft.com/en-us/download/details.aspx?id=48217) must be installed.

In case you encounter an issue like `Could not load file or assembly 'Microsoft.Office.BusinessApplications.Fba...` anyway, you then need to remove `C:\Program Files\Common Files\Microsoft Shared\VSTO\10.0\VSTOInstaller.exe.config` file.

In case you encounter an issue like `...An application with the same identity is already installed...`, you then need to manually remove all folders within `%USERPROFILE%\AppData\Local\Apps\2.0` and restart your computer.

## Dates with a year higher than 3000 are not converted to local timezone

Due to timestamp limitation, dates after `3000-12-31` and date time after `3001-01-01T07:59:59+00:00` cannot be converted to local timezone.

## Python process exited before it was possible to create the interface object

You need to check [log files](configuration/advanced.md#logging-configuration) to identify the underlying issue.

## pyxelrest.xlam is not available

The add-in might be disabled.

Within [Microsoft Excel], go to `File/Option/addin` and check disabled items (`Manage: Disabled Items`)

## Can I install xlwings and pyxelrest?

Yes.

We advise installing [`pyxelrest`] in its own virtual environment.
As [`pyxelrest`] relies on [`xlwings`], if you want to use [`xlwings`] you can, but if you rely on some specific [`xlwings`] configuration, you should use a separate environment.

The [`pyxelrest`] add-in and [`xlwings`] add-in can be installed for the same user as long as [`pyxelrest`] is installed in a separate virtual environment.

## Where are the icons from the Microsoft Excel add-in coming from?

Those icons come from [iconsdb](https://www.iconsdb.com).

The blue color set is `#00AAFF`, the grey color set is `#CDCACD` and the orange one is the orange set from iconsdb.

[Microsoft Excel]: https://products.office.com/en-us/excel
[`xlwings`]: https://www.xlwings.org
[`pyxelrest`]: https://pypi.org/project/pyxelrest/

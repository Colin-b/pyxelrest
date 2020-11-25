# Installing pyxelrest

The preferred way to install `PyxelRest` is to use the provided [executable installer](#download).

## Download

### Download the latest version

[Download PyxelRest 1.0.0](https://raw.githubusercontent.com/Colin-b/pyxelrest/master/pyxelrest_installer.exe)

### Looking for a specific release?

`PyxelRest` releases by version number:

| Version | Release date | | Click for more |
|------|-------------|-------------|-------------|
| [1.0.0](https://raw.githubusercontent.com/Colin-b/pyxelrest/v1.0.0/pyxelrest_installer.exe) | YYYY-MM-DD | [Download](https://raw.githubusercontent.com/Colin-b/pyxelrest/v1.0.0/pyxelrest_installer.exe) | [Changelog](../../CHANGELOG.md#100---YYYY-MM-DD) |

Want to help test development versions of `PyxelRest`?
[Download the latest development version](https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/pyxelrest_installer.exe).

## Features

The installer allows you to:
 * Chose the installation directory.
 * Download and install python if required.
 * Provide a path to up to date services configuration (optional).
 * Install optional dependencies.
 * Add sample services.

This installer will also list `PyxelRest` as installed, so that you can uninstall it the same way you usually uninstall your other applications.

## Using a custom installer

If you don't trust the provided executable, you can re-build it yourself by downloading [NSIS](https://nsis.sourceforge.io/Main_Page) and using the [`pyxelrest_installer.nsi`](https://raw.githubusercontent.com/Colin-b/pyxelrest/master/pyxelrest_installer.nsi) file.

Note that the [NSIS](https://nsis.sourceforge.io/Main_Page) script expect the [ExecDos plugin](https://nsis.sourceforge.io/ExecDos_plug-in) to be available in nsis folder.

If you want even more control on what is installed and how, you can still [perform a manual installation yourself](/docs/installation/custom.md).

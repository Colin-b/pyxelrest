<h2 align="center">Query REST APIs using Microsoft Excel formulas or python functions</h2>

<p align="center">
<a href="https://pypi.org/project/pyxelrest/"><img alt="pypi version" src="https://img.shields.io/pypi/v/pyxelrest"></a>
<a href="https://github.com/Colin-b/pyxelrest/actions"><img alt="Build status" src="https://github.com/Colin-b/pyxelrest/workflows/Release/badge.svg"></a>
<a href="https://github.com/Colin-b/pyxelrest/actions"><img alt="Coverage" src="https://img.shields.io/badge/coverage-70%25-orange"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/Colin-b/pyxelrest/actions"><img alt="Number of tests" src="https://img.shields.io/badge/tests-401 passed-blue"></a>
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
* Installation
  * [Using the installer](/docs/installation/installer.md)
  * [Custom](/docs/installation/custom.md)
  * [Developer](/docs/installation/developer.md)
* Configuration
  * [Services](/docs/configuration/services.md)
  * [Logging](/docs/configuration/logging.md)
  * [Microsoft Excel add-in](/docs/configuration/addin.md)
* [Using as a python module](/docs/python_module.md)
* [Migration guide](/docs/migration_guide.md)
* [FAQ](/docs/faq.md)

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


[Microsoft Excel]: https://products.office.com/en-us/excel

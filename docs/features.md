# Features

PyxelRest allows you to query [Swagger 2.0/OpenAPI](https://www.openapis.org) REST APIs (or any HTTP/HTTPS URL).

You can do it using Microsoft Excel or python.

## Microsoft Excel

PyxelRest will expose formulas within Microsoft Excel, each formula can be used to query a REST API.

Once at least one REST API has been configured, you will have access to [Microsoft Excel] [array formulas](https://support.office.com/en-us/article/Create-an-array-formula-E43E12E0-AFC6-4A12-BC7F-48361075954D) ([dynamic](https://support.office.com/en-us/article/dynamic-array-formulas-and-spilled-array-behavior-205c6b06-03ba-4151-89a1-87a7eb36e531?ns=EXCEL&version=90&ui=en-US&rs=en-US&ad=US) and legacy) and Visual Basic for Applications functions:

<p align="center">
  <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/dynamic_array_formula.gif" alt='Using dynamic array formulas to query petstore REST API'>
  
</p>
<p align="center"><em>Example with <a href="https://petstore.swagger.io/#/">petstore</a> REST API using formulas generated based on the OpenAPI definition.</em></p>


If you want to query a URL yourself, you can use the pyxelrest service, acting like postman, within Microsoft Excel:

<p align="center">
  <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/postman_in_excel.gif" alt='Using dynamic array formulas to query a URL'>
</p>
<p align="center"><em>Example using pyxelrest formulas to query any URL (as in Postman).</em></p>

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
<p align="center"><em>Update check is only performed while Microsoft Excel is running. You will be prompted in case one is available (it can be deactivated).</em></p>


## Python

PyxelRest will expose [Python](https://www.python.org) functions, each function can be used to query a REST API.

Once at least one REST API has been configured, you will have access to functions:

```python
import pyxelrest

configuration = {'petstore': {'open_api': {'definition': 'https://petstore.swagger.io/v2/swagger.json'}}}
pyxelrest.load(configuration)

from pyxelrest.user_defined_functions import petstore

# Functions are available as python functions within petstore (in this case) and can be used as such
user = petstore.getUserByName("test")

# {'id': 9999, 'username': 'test', 'firstName': 'test', 'lastName': 'test', 'email': 'test@test.com', 'password': 'test', 'userStatus': 0}
print(user)
```
<p align="center"><em>Example with <a href="https://petstore.swagger.io/#/">petstore</a> REST API using functions generated based on the OpenAPI definition.</em></p>

[Microsoft Excel]: https://products.office.com/en-us/excel

Access REST APIs from Excel using User Defined Functions (UDF)
==============================================================
PyxelRest allow you to query [Swagger 2.0/OpenAPI](https://www.openapis.org) REST APIs using Excel User Defined Functions.

How to use
----------

Once installed, open Microsoft Excel and add services within PyxelRest configuration.

![Microsoft Excel add-in](addin/AutoLoadPyxelRestAddIn/resources/screenshot_pyxelrest_auto_load_ribbon.PNG)

![Configuration screen](addin/AutoLoadPyxelRestAddIn/resources/screenshot_configure_pyxelrest_services.PNG)

User Installation
------------

1. Within Excel, ``Trust access to the VBA project object model`` should be enabled.
> File > Options > Trust Center > Trust Center Settings > Macro Settings
2. Excel must be closed while executing the following commands:

        pip install pypiwin32
        pip install pyxelrest

Upgrade
-------

1. Excel must be closed while executing the following command:

        pip install pyxelrest --upgrade

Uninstall
---------

1. Go to ``Control Panel/Programs and Features`` and uninstall AutoLoadPyxelRestAddIn.
2. Execute the following command:

        pip uninstall pyxelrest
3. Remove ``%APPDATA%\pyxelrest`` folder.
4. Remove ``%APPDATA%\Microsoft\Excel\XLSTART\pyxelrest.xlam`` file.

Services Configuration
----------------------

Services configuration can also be manually updated thanks to ``%APPDATA%\pyxelrest\services_configuration.ini`` file.

The following options are available for each section:

<table>
    <th>
        <td>Property</td>
        <td>Description</td>
        <td>Mandatory</td>
        <td>Possible values</td>
    </th>
    <tr>
        <td>swagger_url</td>
        <td>Complete URL to the Swagger definition.</td>
        <td>Mandatory</td>
        <td></td>
    </tr>
    <tr>
        <td>proxy_url</td>
        <td>Proxy that should be used to reach service.</td>
        <td>Optional</td>
        <td></td>
    </tr>
    <tr>
        <td>service_host</td>
        <td>Service host in case your service is behind a reverse proxy.</td>
        <td>Optional</td>
        <td></td>
    </tr>
    <tr>
        <td>methods</td>
        <td>List of services methods to be exposed as UDFs.</td>
        <td>Optional</td>
        <td>get, post, put, delete</td>
    </tr>
</table>

Logging Configuration
---------------------

Logging configuration can be updated thanks to ``%APPDATA%\pyxelrest\logging_configuration.ini`` file.

Default log files can be found in your ``%APPDATA%\pyxelrest`` folder.

Developer Installation/Upgrade
----------------------

1. Within Excel, ``Trust access to the VBA project object model`` should be enabled.
> File > Options > Trust Center > Trust Center Settings > Macro Settings
2. Build the addin C# solution:
In order to do so, you need to add a test certificate.
> Project > AutoLoadPyxelRestAddIn > Signing
3. Excel must be closed while executing the following script from within pyxelrest root folder:

        developer_install.bat

Known issues
------------

- Excel needs to be restarted for UDFs not to be displayed anymore in function wizard. (Even if calling them does not work)

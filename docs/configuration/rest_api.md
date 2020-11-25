# REST API Configuration

You can configure access to as many REST API as you want.

<p align="center">
  <img src="https://raw.githubusercontent.com/Colin-b/pyxelrest/develop/resources/doc/configure_service.gif" alt='Configuring services'>
</p>
<p align="center"><em>Services configuration can be done within Microsoft Excel thanks to the <span style="color: #1382CE">Configure Services</span> button within <span style="color: #1E1E1F">PyxelRest</span> tab.</em></p>

You can also update the [YAML](http://yaml.org/start.html) configuration file (`configuration\services.yml` within the installation folder) yourself.

Each section name will be used as the related formulas category within [Microsoft Excel].

Each formula will be prefixed by the section name (only [a-zA-Z0-9_] characters will be kept).

Sample configuration files can be found in the [samples repository](https://github.com/Colin-b/pyxelrest/tree/develop/samples).

## Service mandatory settings

| Name | Description |
|------|-------------|
| open_api | Dictionary describing the OpenAPI definition. Refer to [OpenAPI](#openapi) section for more information. |

Values can be environment variables if provided in the `%MY_ENV_VARIABLE%` form (where `MY_ENV_VARIABLE` is an environment variable).

## Service options

Values can be environment variables if provided in the `%MY_ENV_VARIABLE%` form (where `MY_ENV_VARIABLE` is an environment variable).

| Name | Description | Possible values |
|------|-------------|-----------------|
| description | A small description of this service. To be displayed within [Microsoft Excel] add-in services configuration screen. | |
| formulas | Dictionary containing user defined function (formulas) related settings. Refer to [Formulas](#formulas) section for more information. Generate dynamic array formulas by default. | |
| auth | Dictionary containing authentication related settings. Refer to [Authentication](#authentication) section for more information. | |
| network | Dictionary containing network related settings. Refer to [Network](#network) section for more information. | |
| skip_update_for | List of section names that should not be auto-updated. | |
| caching | Caching results in-memory to avoid sending the same queries too often. Dictionary containing caching related settings. Refer to [Caching](#caching) section for more information. | |
| result | Dictionary containing result related settings. Refer to [Result](#result) section for more information. | |
| udf_name_prefix | Prefix to be used in front of UDf name. `{service_name}` will be replaced by the actual service name. | {service_name}_ |

## OpenAPI

| Name | Description | Mandatory | Possible values |
|------|-------------|-----------|-----------------|
| definition | [URL](https://en.wikipedia.org/wiki/URL) to the OpenAPI definition. `http://`, `https://` and `file:///` (such as `file:///C:\swagger.json`) schemes are supported. It can even be a YAML representation of the definition. | Mandatory | |
| definition_read_timeout | Maximum amount of time, in seconds, to wait when requesting an [OpenAPI 2.0 definition]. Wait for 5 seconds by default. For more details refer to [`requests` timeouts] | Optional | any float value |
| definition_retrieval_auths | List all authentication that should be used when retrieving the [OpenAPI 2.0 definition]. Use no authentication by default. | Optional | oauth2_implicit, oauth2_access_code, oauth2_password, oauth2_application, api_key, basic, ntlm (see [NTLM](#ntlm) to provide details) |
| selected_methods | List of `methods` within [OpenAPI 2.0 definition] that should be retrieved. If not specified, retrieve all standards HTTP methods (get, post, put, delete, patch, options, head). | Optional | get, post, put, delete, patch, options, head |
| excluded_tags | List of `tags` within [OpenAPI 2.0 definition] that should not be retrieved. If not specified, no filtering is applied. | Optional | |
| selected_tags | List of `tags` within [OpenAPI 2.0 definition] that should be retrieved (if not within excluded tags already). If not specified, no filtering is applied. | Optional | |
| excluded_operation_ids | List of `operation_id` (or regular expressions) within [OpenAPI 2.0 definition] that should not be retrieved. If not specified, no filtering is applied. | Optional | |
| selected_operation_ids | List of `operation_id` (or regular expressions) within [OpenAPI 2.0 definition] that should be retrieved (if not within excluded operation_ids already). If not specified, no filtering is applied. | Optional | |
| excluded_parameters | List of `parameter` names (or regular expressions) within [OpenAPI 2.0 definition] that should not be exposed. If not specified, no filtering is applied. | Optional | |
| selected_parameters | List of `parameter` names (or regular expressions) within [OpenAPI 2.0 definition] that should be exposed (if not within excluded parameters already). If not specified, no filtering is applied. | Optional | |
| rely_on_definitions | Rely on [OpenAPI 2.0 definitions](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#definitionsObject) to re-order fields received in response. Deactivated by default. | Optional | `true` or `false` |
| service_host | Service host in case your service is behind a reverse proxy and `basePath` is not properly set in [OpenAPI 2.0 definition]. | Optional | |

## Formulas

Specify what kind of [formulas](https://support.office.com/en-us/article/Create-an-array-formula-E43E12E0-AFC6-4A12-BC7F-48361075954D) will be generated for every REST API endpoint.

### Dynamic array formulas

Identified by the `dynamic_array` key within `formulas` section.

| Name | Description | Possible values |
|------|-------------|-----------------|
| lock_excel | Should [Microsoft Excel] be locked (no other action can be performed) until the results are received. | `true` or `false` (default) |

### Legacy array formulas

Identified by the `legacy_array` key within `formulas` section.

| Name | Description | Possible values |
|------|-------------|-----------------|
| lock_excel | Should [Microsoft Excel] be locked (no other action can be performed) until the results are received. | `true` or `false` (default) |

### Visual Basic for Applications (VBA) formulas

Identified by the `vba_compatible` key within `formulas` section.

## Authentication

Contains authentication related settings.

| Name | Description | Possible values |
|------|-------------|-----------------|
| oauth2 | Dictionary containing OAuth2 authentication related settings. Refer to [OAuth 2](#oauth-2) section for more information. |
| api_key | User API Key. Can be an environment variable surrounded by `%` as in `%MY_API_KEY_ENV_VAR%`. |
| basic | Dictionary containing Basic authentication related settings. Refer to [Basic](#basic) section for more information. |
| ntlm | Dictionary containing NTLM authentication related settings. Refer to [NTLM](#ntlm) section for more information. |

### OAuth 2

Depending on the flow, every parameter supported by [requests-auth](https://colin-b.github.io/requests_auth/) can be provided.

Note that `token_url` and `authorization_url` are extracted from [OpenAPI 2.0 definition], thus they do not need to be provided.

### Basic

| Name | Description | Mandatory |
|------|-------------|-----------|
| username | User name | Mandatory |
| password | User password | Mandatory |

### NTLM

| Name | Description |
|------|-------------|
| username | User name. Should be of the form `domain\\user`. Default value is the logged in user name. |
| password | User password. Default value is the logged in user password. |

In case user credentials are provided, [`requests_ntlm==1.*`](https://pypi.org/project/requests_ntlm/) module is required.
```bash
python -m pip install requests_ntlm==1.*
```

In case user credentials are not provided (using logged in user credentials), [`requests_negotiate_sspi==0.5.*`](https://pypi.org/project/requests-negotiate-sspi/) module is required.
```bash
python -m pip install requests_negotiate_sspi==0.5.*
```

## Network

Contains network related settings such as HTTP timeouts or proxies configuration.

| Name | Description | Possible values |
|------|-------------|-----------------|
| max_retries | Maximum number of time a request should be retried before considered as failed. 5 by default. | Any positive integer value |
| connect_timeout | Maximum amount of time, in seconds, to wait when trying to reach the service. Wait for 1 second by default. For more details refer to [`requests` timeouts] | any float value |
| read_timeout | Maximum amount of time, in seconds, to wait when requesting a service. Wait for 5 seconds by default. For more details refer to [`requests` timeouts] | any float value |
| proxies | Proxies that should be used to reach service. This is a dictionary where keys are the scheme (http or https) and/or no_proxy. If the key is a scheme then the value should be the proxy URL. Otherwise the value should be the URL for which proxies should be ignored. For more details refer to [`requests` documentation](https://requests.readthedocs.io/en/master/user/advanced/#proxies) | |
| verify | Verify SSL certificate for HTTPS requests. Default to `true`. For more details refer to [`requests` documentation](https://2.python-requests.org/en/master/user/advanced/#ssl-cert-verification). If you are using an internal certificate store (company certificates), you will most likely need to install `python-certifi-win32` | |
| headers | Dictionary containing headers were key is the name of the header that should be sent with every request sent to this service. | |

## Caching

| Name | Description |
|------|-------------|
| result_caching_time | Number of seconds during which a GET request will return previous result. 0 seconds (always send a new request) by default. |
| max_nb_results | Maximum number of results to store in cache. The last 100 results will be stored in cache by default. |

[`cachetools==4.*`](https://pypi.org/project/cachetools/) module is required.
```bash
python -m pip install cachetools==4.*
```

## Result

| Name | Description |
|------|-------------|
| flatten | Flatten received JSON to a 2-Dimension array. Default to `true` |
| raise_exception | Raise received exceptions to client. `false` by default. |

[Microsoft Excel]: https://products.office.com/en-us/excel
[OpenAPI 2.0 definition]: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md
[`requests` timeouts]: https://2.python-requests.org/en/master/user/advanced/#timeouts

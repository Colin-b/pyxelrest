# REST API Configuration

You can configure access to as many REST API as you want.

The configuration is stored in a [YAML](http://yaml.org/start.html) configuration file (`configuration\services.yml` within the installation folder).

Each REST API name will be used as the related formulas category within [Microsoft Excel].

For example, the following configuration file will create `my_first_rest_api` and `my_2nd_rest_api` formulas categories.
```yaml
my_first_rest_api:
  open_api:
    definition: "https://my_first_rest_api.com/swagger.json"

my_2nd_rest_api:
  open_api:
    definition: "https://my_second_rest_api.com/swagger.json"
```

Each formula will be prefixed by the REST API name provided in the configuration (only [a-zA-Z0-9_] characters will be kept).

If both REST API defined in the previous example were to expose the same endpoint named `users`, the following formulas would then be available:
`my_first_rest_api_users` and `my_2nd_rest_api_users`.

If you are looking for more example of configuration files, sample configuration files can be found in the [samples repository](/samples).

For each REST API, you at least have to provide the [OpenAPI definition](#openapi-definition).

## OpenAPI definition

The OpenAPI definition MUST be provided as `definition` under the `open_api` section.

You can provide the OpenAPI definition in 3 different ways:
1. [If you have the URL](#the-definition-is-accessible-via-url)
2. [If you have it in a file](#the-definition-is-stored-in-a-file)
3. [If you want to write it](#the-definition-cannot-be-accessed-via-file-path-or-url)

If none of the above options works for you, you can still use the [pyxelrest service](pyxelrest_service.md) to access a specific URL.

### The definition is accessible via URL

You can provide a [URL](https://en.wikipedia.org/wiki/URL) (starting with `http://` or `https://`) to a JSON definition, as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
```

#### Retrieving the definition on slow network

In case the OpenAPI definition might take more than 5 seconds to be retrieved (on slow network for example), you can tweak the timeout value.

The OpenAPI definition retrieval timeout can be provided as `definition_read_timeout` under the `open_api` section as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
    definition_read_timeout: 10
```

The value that will be provided is the maximum amount of time, in seconds, to wait when requesting an [OpenAPI 2.0 definition] via an URL.

The default value is set to `5`, meaning that if the OpenAPI definition cannot be retrieved within 5 seconds, the REST API will not be exposed.

For more technical details refer to [`requests` timeouts].

#### Retrieving a definition requiring authentication

In case the OpenAPI definition cannot be accessed anonymously (server requiring NTLM authentication for example), you can specify the list of required authentication mechanisms.

The list of authentication can be provided as `definition_retrieval_auths` under the `open_api` section as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
    definition_retrieval_auths:
      - ntlm
```

The value that will be provided is the list of all authentication that should be used when requesting an [OpenAPI 2.0 definition] via an URL.

The default value is an empty list, meaning that no authentication will be performed to retrieve the OpenAPI definition.

Below is the list of supported authentication mechanism (if your authentication mechanism is not in this list, please open an issue):
* oauth2_implicit
* oauth2_access_code
* oauth2_password
* oauth2_application
* api_key
* basic
* ntlm (see [NTLM](#ntlm) to provide details)

### The definition is stored in a file

You can provide a file path (starting with `file:///`) to a JSON definition, as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "file:///C:\path\to\swagger.json"
```

### The definition cannot be accessed via file path or URL

You can provide a [YAML](http://yaml.org/start.html) representation of the OpenAPI definition, as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition:
      swagger: "2.0"
      paths:
        "/endpoint":
          "get":
            "operationId": "get_endpoint"
            "responses":
              "200":
                "description": "OK"
```

## Formulas

Specify what kind of [formulas](https://support.office.com/en-us/article/Create-an-array-formula-E43E12E0-AFC6-4A12-BC7F-48361075954D) will be generated for every REST API endpoint.

Generate [dynamic array formulas](#dynamic-array-formulas) by default.

You can generate up to 3 kind of formulas per REST API:
* [Dynamic array](#dynamic-array-formulas)
* [Legacy array](#legacy-array-formulas)
* [VBA](#visual-basic-for-applications-vba-formulas)

### Dynamic array formulas

You can generate dynamic array formulas, as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  formulas:
    dynamic_array:
      lock_excel: false
```

#### Lock Microsoft Excel while formula is being called

By default, dynamic array formulas will allow you to continue using Microsoft Excel during computation.

But, if, for some reason, you want to ensure that nothing is performed during the formula computation, you can set `lock_excel` as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  formulas:
    dynamic_array:
      lock_excel: true
```

#### Change the prefix in front on formulas

By default, dynamic array formulas will be prefixed by the REST API name.

If you want to change this prefix (or even remove it), you can use `prefix` as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  formulas:
    dynamic_array:
      prefix: "{service_name}_"
```

Note that `{service_name}` will be replaced by the actual REST API name when generating the formulas.
In this case, `my_rest_api` will be used as `{service_name}` value, resulting in `my_rest_api_` prefix.

To disable the prefix, you can use a blank value as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  formulas:
    dynamic_array:
      prefix: ""
```

### Legacy array formulas

You can generate legacy array formulas, as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  formulas:
    legacy_array:
      lock_excel: false
```

#### Lock Microsoft Excel while formula is being called

By default, legacy array formulas will allow you to continue using Microsoft Excel during computation.

But, if, for some reason, you want to ensure that nothing is performed during the formula computation, you can set `lock_excel` as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  formulas:
    legacy_array:
      lock_excel: true
```

#### Change the prefix in front on formulas

By default, legacy array formulas will be prefixed by `legacy_` followed by the REST API name.

If you want to change this prefix (or even remove it), you can use `prefix` as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  formulas:
    legacy_array:
      prefix: "legacy_{service_name}_"
```

Note that `{service_name}` will be replaced by the actual REST API name when generating the formulas.
In this case, `my_rest_api` will be used as `{service_name}` value, resulting in `legacy_my_rest_api_` prefix.

To disable the prefix, you can use a blank value as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  formulas:
    legacy_array:
      prefix: ""
```

### Visual Basic for Applications (VBA) formulas

You can generate formulas that can be called in VBA, as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  formulas:
    vba_compatible:
      prefix: "vba_{service_name}_"
```

#### Change the prefix in front on formulas

By default, VBA formulas will be prefixed by `vba_` followed by the REST API name.

If you want to change this prefix (or even remove it), you can use `prefix` as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  formulas:
    vba_compatible:
      prefix: "vba_{service_name}_"
```

Note that `{service_name}` will be replaced by the actual REST API name when generating the formulas.
In this case, `my_rest_api` will be used as `{service_name}` value, resulting in `vba_my_rest_api_` prefix.

To disable the prefix, you can use a blank value as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  formulas:
    vba_compatible:
      prefix: ""
```

## Do not expose everything the REST API offers

The default behavior is to expose every endpoint as defined in the OpenAPI definition.

You can change this behavior by:
* [Selecting HTTP methods to expose](#selecting-http-methods-to-expose)
* [Selecting tags to include or exclude](#selecting-tags-to-include-or-exclude)
* [Selecting operation_id to include or exclude](#selecting-operation_id-to-include-or-exclude)
* [Selecting parameters to include or exclude](#selecting-parameters-to-include-or-exclude)

### Selecting HTTP methods to expose

The HTTP methods to expose can be provided as `selected_methods` under the `open_api` section as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
    selected_methods:
      - "get"
```

The default value is a list containing all standards HTTP methods as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
    selected_methods:
      - "get"
      - "post"
      - "put"
      - "delete"
      - "patch"
      - "options"
      - "head"
```

As you will have one formula per endpoint per HTTP method, OpenAPI definition endpoints with HTTP methods not in the provided list will not be exposed.

Note that if an endpoint is defined with both (methods that should be exposed, and methods that should be skipped), then only the methods that should be exposed will be available on this endpoint.

### Selecting tags to include or exclude

OpenAPI definition endpoints are often grouped by `tags`.

You can filter (in or out) endpoints by filtering on related `tags`.

Filtered-out `tags` can be provided as `excluded_tags` under the `open_api` section as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
    excluded_tags:
      - "sample tag"
```

The default value is an empty list, meaning that no filtering is performed.

Filtered-in `tags` can be provided as `selected_tags` under the `open_api` section as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
    selected_tags:
      - "sample tag"
```

The default value is an empty list, meaning that no filtering is performed.

Note that if a tag is provided in both `excluded_tags` and `selected_tags`. It will be considered as excluded.

### Selecting operation_id to include or exclude

OpenAPI definition endpoints are uniquely identified by an `operation_id`.

If an operation_id is not provided in the OpenAPI definition, pyxelrest will create one based on the following logic:
`{http_method}{underscored_endpoint}`. 

Meaning an HTTP `GET` method on `/path/resource` will have the `get_path_resource` `operation_id`.

You can filter (in or out) endpoints by filtering on related `operation_id`.

Filtered-out `operation_id` can be provided as `excluded_operation_ids` under the `open_api` section as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
    excluded_operation_ids:
      - "get_endpoint"
```

The default value is an empty list, meaning that no filtering is performed.

Note that Python regular expression can be provided as value. But you can also write *simple* regular expression by only using the `*` character to match anything.

Filtered-in `operation_id` can be provided as `selected_operation_ids` under the `open_api` section as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
    selected_operation_ids:
      - "get_endpoint"
```

The default value is an empty list, meaning that no filtering is performed.

Note that Python regular expression can be provided as value. But you can also write *simple* regular expression by only using the `*` character to match anything.

Note that if an `operation_id` is provided in both `excluded_operation_ids` and `selected_operation_ids`. It will be considered as excluded.

### Selecting parameters to include or exclude

Even if an endpoint is supposed to be exposed, you might not need every parameter in your resulting formula.

Filtered-out `parameters` can be provided as `excluded_parameters` under the `open_api` section as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
    excluded_parameters:
      - "secret"
```

The default value is an empty list, meaning that no filtering is performed.

Note that Python regular expression can be provided as value. But you can also write *simple* regular expression by only using the `*` character to match anything.

Filtered-in `parameters` can be provided as `selected_parameters` under the `open_api` section as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
    selected_parameters:
      - "secret"
```

The default value is an empty list, meaning that no filtering is performed.

Note that Python regular expression can be provided as value. But you can also write *simple* regular expression by only using the `*` character to match anything.

Note that if a `parameter` is provided in both `excluded_parameters` and `selected_parameters`. It will be considered as excluded.

## Microsoft Excel add-in specific settings

### Add a description to the service in the configuration screen

You can provide a description of the REST API, to be displayed within [Microsoft Excel] add-in services configuration screen.

The description can be provided as `description` as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  description: "This is the purpose of the REST API"
```

It will default to blank, meaning no description will be provided by default.

### Keep client specific configuration when updating the configuration

The Microsoft Excel add-in will ensure that every configured REST API stays up to date.

You might however want to avoid update to overwrite some client custom configuration (such as a custom API key or a client specific formulas configuration).

The configuration options to skip when updating can be provided as `skip_update_for` as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  skip_update_for:
    - "formulas"
    - "auth.api_key"
```

You can use dot notation to specify a specific option within a section.

## Authentication

Contains authentication related settings.

| Name | Description | Possible values |
|------|-------------|-----------------|
| oauth2 | Dictionary containing OAuth2 authentication related settings. Refer to [OAuth 2](#oauth-2) section for more information. |
| api_key | User API Key. Can be an environment variable surrounded by `%` as in `%MY_API_KEY_ENV_VAR%`. |
| basic | Dictionary containing Basic authentication related settings. Refer to [Basic](#basic) section for more information. |
| ntlm | Dictionary containing NTLM authentication related settings. Refer to [NTLM](#ntlm) section for more information. |

api_key value can be environment variables if provided in the `%MY_ENV_VARIABLE%` form (where `MY_ENV_VARIABLE` is an environment variable).

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

Header values can be environment variables if provided in the `%MY_ENV_VARIABLE%` form (where `MY_ENV_VARIABLE` is an environment variable).

OpenAPI
| host | Service host in case your service is behind a reverse proxy and `basePath` is not properly set in [OpenAPI 2.0 definition]. | Optional | |

## Caching

Caching results in-memory to avoid sending the same queries too often.

| Name | Description |
|------|-------------|
| result_caching_time | Number of seconds during which a GET request will return previous result. 0 seconds (always send a new request) by default. |
| max_nb_results | Maximum number of results to store in cache. The last 100 results will be stored in cache by default. |

[`cachetools==4.*`](https://pypi.org/project/cachetools/) module is required.
```bash
python -m pip install cachetools==4.*
```

## Result

Result related settings.

| Name | Description |
|------|-------------|
| flatten | Flatten received JSON to a 2-Dimension array. Default to `true` |
| raise_exception | Raise received exceptions to client. `false` by default. |

## OpenAPI

TODO Move this setting to Result

| Name | Description | Mandatory | Possible values |
|------|-------------|-----------|-----------------|
| rely_on_definitions | Rely on [OpenAPI 2.0 definitions](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#definitionsObject) to re-order fields received in response. Deactivated by default. | Optional | `true` or `false` |


[Microsoft Excel]: https://products.office.com/en-us/excel
[OpenAPI 2.0 definition]: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md
[`requests` timeouts]: https://2.python-requests.org/en/master/user/advanced/#timeouts

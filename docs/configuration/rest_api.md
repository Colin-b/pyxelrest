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

#### Cache results

To avoid sending queries too often and retrieve results faster, you can cache results in memory.

The default behavior is to always send a new query, even if the exact same one was send a few milliseconds ago.

To cache results, you can use `cache` section as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  formulas:
    dynamic_array:
      cache:
        duration: 1
        size: 100
```

The `duration` is the number of seconds during which a GET request will return previous result for the same query.

The `size` is the maximum number of results to store in cache. The last 100 results will be stored in cache by default.

[`cachetools==4.*`](https://pypi.org/project/cachetools/) module is required for cache to be created.
```bash
python -m pip install cachetools==4.*
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

## Authentication

Access to REST API may require authentication.

In such case, the required authentication will be selected according to the OpenAPI definition.

However additional information will be required to be able to perform authentication properly.

The following authentication mechanisms are supported:
 * [API key](#api-key)
 * [OAuth2](#oauth-2)
 * [Basic (name and password)](#basic-name-and-password)
 * [NTLM (Microsoft Windows)](#ntlm-microsoft-windows)

### API key

If accessing the REST API requires to authenticate using an API key, the value can be provided as `api_key` under the `auth` section, as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  auth:
    api_key: "value"
```

The value can contains environment variables if provided in the `%MY_ENV_VARIABLE%` form (where `MY_ENV_VARIABLE` is an environment variable).

The following sample will use the value of `REST_API_KEY` environment variable as the API key:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  auth:
    api_key: "%REST_API_KEY%"
```

### OAuth 2

If accessing the REST API requires to authenticate using an OAuth2 grant flow, the authentication will be performed using [requests-auth](https://colin-b.github.io/requests_auth/).

Every supported parameter can be provided, as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  auth:
    oauth2:
      client_id: "A-B-C-D-E"
```

Note that `token_url` and `authorization_url` are extracted from [OpenAPI 2.0 definition], thus they do not need to be provided.

### Basic (name and password)

If accessing the REST API requires to authenticate using a username and a password, the values can be provided, as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  auth:
    basic:
      username: "user"
      password: "pwd"
```

### NTLM (Microsoft Windows)

If accessing the REST API requires to authenticate using Microsoft Windows, the values can be provided, as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  auth:
    ntlm:
      username: "domain\\user"
      password: "pwd"
```

Note that [`requests_ntlm==1.*`](https://pypi.org/project/requests_ntlm/) module MUST be installed for this to work.
```bash
python -m pip install requests_ntlm==1.*
```

You can also authenticate using the currently logged in Microsoft Windows user, as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  auth:
    ntlm:
      username: ""
      password: ""
```

Note that [`requests_negotiate_sspi==0.5.*`](https://pypi.org/project/requests-negotiate-sspi/) module MUST be installed for this to work.
```bash
python -m pip install requests_negotiate_sspi==0.5.*
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

## Network

### Automatic retry in case of network failure or timeout

By default, pyxelrest will resend a HTTP query 5 times until reporting a failure.

To change this behavior, you can set `max_retries` within `network` section as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  network:
    max_retries: 0
```

### Establishing an HTTP connection on slow network

By default, pyxelrest will wait for 1 second for a connection to be established.

To change this behavior, you can set `connect_timeout` within `network` section as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  network:
    connect_timeout: 5
```

This will be the maximum amount of time, in seconds, to wait when trying to reach the REST API.
For more details refer to [`requests` timeouts].

### Performing long HTTP queries

By default, pyxelrest will wait for 5 seconds for a response to be received.

To change this behavior, you can set `read_timeout` within `network` section as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  network:
    read_timeout: 60
```

This will be the maximum amount of time, in seconds, to wait when requesting the REST API.
For more details refer to [`requests` timeouts].

### Trusting HTTPS certificate

By default, pyxelrest will verify SSL certificate for HTTPS requests.

If you are using an internal certificate store (company certificates), you will most likely need to install `python-certifi-win32`

For more details refer to [`requests` documentation](https://2.python-requests.org/en/master/user/advanced/#ssl-cert-verification). 

To disable this check (not advised), you can set `verify` within `network` section to `false` as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "https://my_rest_api.com/swagger.json"
  network:
    verify: false
```

### Providing custom proxying rules

By default, pyxelrest will use the proxies defined on `HTTP_PROXY` (for `http://` REST API) and `HTTPS_PROXY` (for `https://` REST API) environment variables.

To change this behavior, you can set `proxies` within `network` section to a dictionary as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "http://my_rest_api.com/swagger.json"
  network:
    proxies:
      http://my_rest_api.com: "http://custom_proxy"
      https://my_rest_api.com: "http://custom_proxy"
      no_proxy: "http://my_other_rest_api.com"
```

For more details refer to [`requests` documentation](https://requests.readthedocs.io/en/master/user/advanced/#proxies)

### Sending headers with every request

The only header pyxelrest will send is `User-Agent` with value set to `pyxelrest/` followed by the version number.
eg. `pyxelrest/1.0.0` for pyxelrest version `1.0.0`.

You can add more headers to outgoing requests by setting `headers` within `network` section to a dictionary as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "http://my_rest_api.com/swagger.json"
  network:
    headers:
      X-PXL-USERNAME: "%USERNAME%"
      X-PXL-CUSTOM: "a custom value"
```

Header values can be environment variables if provided in the `%MY_ENV_VARIABLE%` form (where `MY_ENV_VARIABLE` is an environment variable).

### Overriding host for REST API behind a reverse proxy

In case your REST API definition is behind a reverse proxy, and `basePath` is not properly set in the [OpenAPI 2.0 definition].

You can overcome this by setting `host` within `network` section to the path of the service as in the following sample:
```yaml
my_rest_api:
  open_api:
    definition: "http://my_rest_api.com/swagger.json"
  network:
    host: "my_reverse_proxy_host/my_api"
```

Note: This setting does not apply to `pyxelrest` configuration section, as it is not a REST API.

[Microsoft Excel]: https://products.office.com/en-us/excel
[OpenAPI 2.0 definition]: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md
[`requests` timeouts]: https://2.python-requests.org/en/master/user/advanced/#timeouts

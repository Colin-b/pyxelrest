# Migration guide

For a list of enhancements and bugfixes, refer to [changelog](../CHANGELOG.md).

## From version `0.69.0` to version `1.*`

### Breaking changes

#### Python module usage

If you were using `pyxelrest` as a python module, you will now have to import your functions via the submodule corresponding to your REST API configuration.
The name of the function is not prefixed by the REST API configuration name anymore, requiring to remove the prefix from your function calls in your code.

Previous (0.69.0)

```python
import pyxelrest

configuration = {'petstore': {'open_api': {'definition': 'https://petstore.swagger.io/v2/swagger.json'}}}
pyxelrest.load(configuration)

import pyxelrest.user_defined_functions

user = pyxelrest.user_defined_functions.petstore_getUserByName("test")
```

New (1.0.0)

```python
import pyxelrest

configuration = {'petstore': {'open_api': {'definition': 'https://petstore.swagger.io/v2/swagger.json'}}}
pyxelrest.load(configuration)

from pyxelrest.generated import petstore

user = petstore.getUserByName("test")
```

#### Services configuration changes

REST API configuration will most likely not be compatible anymore due to the changes in the following section:

##### udf

`udf` section has been replaced by a `formulas` section.

We __strongly__ advise to check out the new `dynamic_array` formulas if your [Microsoft Excel] version supports it.
Otherwise:

 * `sync_auto_expand` `return_type` corresponds to `legacy_array` sub-section with `lock_excel` set to `true` and prefix set to `{name}_`
 
    Previous (0.69.0)
    
    ```yaml
    udf:
        return_types:
            - sync_auto_expand
    ```
    
    New (1.0.0)
    
    ```yaml
    formulas:
        legacy_array:
            lock_excel: true
            prefix: "{name}_"
    ```

 * `async_auto_expand` `return_type` corresponds to `legacy_array` sub-section with `lock_excel` set to `false` and prefix set to `{name}_`
 
    Previous (0.69.0)
    
    ```yaml
    udf:
        return_types:
            - async_auto_expand
    ```
    
    New (1.0.0)
    
    ```yaml
    formulas:
        legacy_array:
            lock_excel: false
            prefix: "{name}_"
    ```

 * `vba_compatible` `return_type` (in case there was another `return_type` as well) corresponds to `vba_compatible` sub-section with `lock_excel` set to `true`
 
    Previous (0.69.0)
    
    ```yaml
    udf:
        return_types:
            - ...
            - vba_compatible
    ```
    
    New (1.0.0)
    
    ```yaml
    formulas:
        vba_compatible:
            lock_excel: true
    ```

 * `vba_compatible` `return_type` (in case it was the only `return_type`) corresponds to `vba_compatible` sub-section with `lock_excel` set to `true` and prefix set to `{name}_`
 
    Previous (0.69.0)
    
    ```yaml
    udf:
        return_types:
            - vba_compatible
    ```
    
    New (1.0.0)
    
    ```yaml
    formulas:
        vba_compatible:
            lock_excel: true
            prefix: "{name}_"
    ```

##### shift_result

`shift_result` is not an option anymore. 

As a result, formulas results will start from the first cell (results will not be shifted from one column to the right).

If you were using `shift_result: true`, __this change will impact your existing Microsoft Excel workbooks__

##### methods

`methods` option is now `selected_methods` option within `open_api` section.

Previous (0.69.0)

```yaml
methods:
    - get
```

New (1.0.0)

```yaml
open_api:
    selected_methods:
        - get
```

##### headers

`headers` section is now expected as a sub-section within `network` section.

Previous (0.69.0)

```yaml
headers:
    X-Custom: "This is a value"
```

New (1.0.0)

```yaml
network:
    headers:
        X-Custom: "This is a value"
```

##### service_host

`service_host` option within `open_api` section is now `host` option within `network` section.

Previous (0.69.0)

```yaml
open_api:
    service_host: "my_reverse_proxy/api"
```

New (1.0.0)

```yaml
network:
    host: "my_reverse_proxy/api"
```

##### udf_name_prefix

`udf_name_prefix` option was replaced by `prefix` option per formula type.

Previous (0.69.0)

```yaml
udf_name_prefix: "my_prefix"
```

New (1.0.0)

```yaml
formulas:
    dynamic_array:
        prefix: "my_prefix"
```

##### caching

`caching` option was replaced by `cache` option per formula type.
`max_nb_results` has been renamed to `size` and `result_caching_time` to `duration`.

Previous (0.69.0)

```yaml
caching:
    max_nb_results: 100
    result_caching_time: 1
```

New (1.0.0)

```yaml
formulas:
    dynamic_array:
        cache:
            size: 100
            duration: 1
```

##### definition_retrieval_auths

 * `oauth2_implicit` `oauth2_auth_url` is now `authorization_url` within `oauth2` `implicit` section
 
    Previous (0.69.0)
    
    ```yaml
    open_api:
        definition_retrieval_auths:
            oauth2_implicit:
                oauth2_auth_url: "https://authorization_url"
    ```
    
    New (1.0.0)
    
    ```yaml
    open_api:
        definition_retrieval_auths:
            oauth2:
                implicit:
                    authorization_url: "https://authorization_url"
    ```

 * `oauth2_access_code` `oauth2_auth_url` is now `authorization_url` and `oauth2_token_url` is now `token_url` within `oauth2` `access_code` section
 
    Previous (0.69.0)
    
    ```yaml
    open_api:
        definition_retrieval_auths:
            oauth2_access_code:
                oauth2_auth_url: "https://authorization_url"
                oauth2_token_url: "https://token_url"
    ```
    
    New (1.0.0)
    
    ```yaml
    open_api:
        definition_retrieval_auths:
            oauth2:
                access_code:
                    authorization_url: "https://authorization_url"
                    token_url: "https://token_url"
    ```

 * `oauth2_password` `oauth2_token_url` is now `token_url` within `oauth2` `password` section
 
    Previous (0.69.0)
    
    ```yaml
    open_api:
        definition_retrieval_auths:
            oauth2_password:
                oauth2_token_url: "https://token_url"
    ```
    
    New (1.0.0)
    
    ```yaml
    open_api:
        definition_retrieval_auths:
            oauth2:
                password:
                    token_url: "https://token_url"
    ```

 * `oauth2_application` `oauth2_token_url` is now `token_url` within `oauth2` `application` section
 
    Previous (0.69.0)
    
    ```yaml
    open_api:
        definition_retrieval_auths:
            oauth2_application:
                oauth2_token_url: "https://token_url"
    ```
    
    New (1.0.0)
    
    ```yaml
    open_api:
        definition_retrieval_auths:
            oauth2:
                application:
                    token_url: "https://token_url"
    ```

 * `api_key` `name` is now `query_parameter_name` if `in` was `query`
 
    Previous (0.69.0)
    
    ```yaml
    open_api:
        definition_retrieval_auths:
            api_key:
                in: "query"
                name: "param_name"
    ```
    
    New (1.0.0)
    
    ```yaml
    open_api:
        definition_retrieval_auths:
            api_key:
                query_parameter_name: "param_name"
    ```

 * `api_key` `name` is now `header_name` if `in` was `header`
 
    Previous (0.69.0)
    
    ```yaml
    open_api:
        definition_retrieval_auths:
            api_key:
                in: "header"
                name: "x-api-key"
    ```
    
    New (1.0.0)
    
    ```yaml
    open_api:
        definition_retrieval_auths:
            api_key:
                header_name: "x-api-key"
    ```

#### Add-in installation script

* `--path_to_up_to_date_configuration` parameter does not exists anymore. [Use the registry key](configuration/advanced.md) to provide it instead.
* `--scripts_directory` parameter does not exist anymore.

Previous (0.69.0)

```shell
python pyxelrest_install_addin.py --add_in_directory ADD_IN_DIR --scripts_directory SCRIPTS_DIR --path_to_up_to_date_configuration PATH_TO_CONFS
```

New (1.0.0)

```shell
pyxelrest_install_addin.exe --source ADD_IN_DIR
```

For more information on what the new script has to offer, refer to [the custom installation documentation](installation/custom.md#microsoft-excel-add-in-installer-options)

[Microsoft Excel]: https://products.office.com/en-us/excel

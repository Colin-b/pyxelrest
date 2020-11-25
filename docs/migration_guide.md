# Migration guide

For a list of enhancements and bugfixes, refer to [changelog](../CHANGELOG.md).

## From version `0.69.0` to version `1.*`

### Breaking changes

If you were expecting your formulas to shift results from one column to the right, 
then you will have to update your Microsoft Excel workbooks due to [this change](#shift_result) as this will not be the case anymore.

REST API configuration will most likely not be compatible anymore due to the changes in the following section:

#### udf

`udf` section has been replaced by a `formulas` section.

We __strongly__ advise to check out the new `dynamic_array` formulas if your [Microsoft Excel] version supports it.
Otherwise:

 * `sync_auto_expand` `return_type` corresponds to `legacy_array` sub-section with `lock_excel` set to `true`
 
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
    ```

 * `async_auto_expand` `return_type` corresponds to `legacy_array` sub-section with `lock_excel` set to `false`
 
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

 * `vba_compatible` `return_type` (in case it was the only `return_type`) corresponds to `legacy_array` sub-section with `lock_excel` set to `true`
 
    Previous (0.69.0)
    
    ```yaml
    udf:
        return_types:
            - vba_compatible
    ```
    
    New (1.0.0)
    
    ```yaml
    formulas:
        legacy_array:
            lock_excel: true
    ```

#### shift_result

`shift_result` is not an option anymore. 

As a result, formulas results will start from the first cell.

If you were using `shift_result: true`, __this change will impact your existing Microsoft Excel workbooks__

#### methods

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

#### headers

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

[Microsoft Excel]: https://products.office.com/en-us/excel

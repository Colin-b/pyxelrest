# Migration guide

## 0.69.0 to 1.0.0

### Configuration changes

`udf` section has been replaced by a `formulas` section.

We __strongly__ advise to check out the new `dynamic_array` formulas if your [Microsoft Excel] version supports it.
Otherwise:

 * `sync_auto_expand` `return_type` corresponds to `legacy_array` sub-section with `lock_excel` set to `true`
 * `async_auto_expand` `return_type` corresponds to `legacy_array` sub-section with `lock_excel` set to `false`
 * `vba_compatible` `return_type` (in case there was another `return_type` as well) corresponds to `vba_compatible` sub-section with `lock_excel` set to `true`
 * `vba_compatible` `return_type` (in case it was the only `return_type`) corresponds to `legacy_array` sub-section with `lock_excel` set to `true`

`shift_result` is not an option anymore. As a result, formulas results will start from the first cell.

`methods` option is now `selected_methods` option within `open_api` section.

`headers` section is now expected as a sub-section within `network` section.

#### Previous (0.69.0)

```yaml
udf:
    return_types:
        - sync_auto_expand
```

#### New (1.0.0)

```yaml
formulas:
    legacy_array:
        lock_excel: true
```

[Microsoft Excel]: https://products.office.com/en-us/excel

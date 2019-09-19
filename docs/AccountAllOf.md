# AccountAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_status** | **str** | The status of the account. Currently the only possible value is \&quot;active\&quot;, but more values may be added in the future. | [optional] 
**created_on** | **datetime** |  | [optional] 
**display_name** | **str** |  | [optional] 
**has_2fa_enabled** | **bool** |  | [optional] 
**links** | [**AccountAllOfLinks**](AccountAllOfLinks.md) |  | [optional] 
**nickname** | **str** | Account name defined by the owner. Should be used instead of the \&quot;username\&quot; field. Note that \&quot;nickname\&quot; cannot be used in place of \&quot;username\&quot; in URLs and queries, as \&quot;nickname\&quot; is not guaranteed to be unique. | [optional] 
**username** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**website** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



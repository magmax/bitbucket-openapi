# PullrequestMergeParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close_source_branch** | **bool** | Whether the source branch should be deleted. If this is not provided, we fallback to the value used when the pull request was created, which defaults to False | [optional] 
**merge_strategy** | **str** | The merge strategy that will be used to merge the pull request. | [optional] [default to 'merge_commit']
**message** | **str** | The commit message that will be used on the resulting commit. | [optional] 
**type** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



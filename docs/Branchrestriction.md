# Branchrestriction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_match_kind** | **str** | Indicates how the restriction is matched against a branch. The default is &#x60;glob&#x60;. | 
**branch_type** | **str** | Apply the restriction to branches of this type. Active when &#x60;branch_match_kind&#x60; is &#x60;branching_model&#x60;. The branch type will be calculated using the branching model configured for the repository. | [optional] 
**groups** | [**list[Group]**](Group.md) |  | [optional] 
**id** | **int** | The branch restriction status&#39; id. | [optional] 
**kind** | **str** | The type of restriction that is being applied. | 
**links** | [**BranchingModelSettingsAllOfLinks**](BranchingModelSettingsAllOfLinks.md) |  | [optional] 
**pattern** | **str** | Apply the restriction to branches that match this pattern. Active when &#x60;branch_match_kind&#x60; is &#x60;glob&#x60;. Will be empty when &#x60;branch_match_kind&#x60; is &#x60;branching_model&#x60;. | 
**users** | [**list[Account]**](Account.md) |  | [optional] 
**value** | **int** | Value with kind-specific semantics: \&quot;require_approvals_to_merge\&quot; uses it to require a minimum number of approvals on a PR; \&quot;require_passing_builds_to_merge\&quot; uses it to require a minimum number of passing builds. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RepositoryAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**fork_policy** | **str** |  Controls the rules for forking this repository.  * **allow_forks**: unrestricted forking * **no_public_forks**: restrict forking to private forks (forks cannot   be made public later) * **no_forks**: deny all forking  | [optional] 
**full_name** | **str** | The concatenation of the repository owner&#39;s username and the slugified name, e.g. \&quot;evzijst/interruptingcow\&quot;. This is the same string used in Bitbucket URLs. | [optional] 
**has_issues** | **bool** |  | [optional] 
**has_wiki** | **bool** |  | [optional] 
**is_private** | **bool** |  | [optional] 
**language** | **str** |  | [optional] 
**links** | [**RepositoryAllOfLinks**](RepositoryAllOfLinks.md) |  | [optional] 
**mainbranch** | [**Branch**](Branch.md) |  | [optional] 
**name** | **str** |  | [optional] 
**owner** | [**Account**](Account.md) |  | [optional] 
**parent** | [**Repository**](Repository.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**scm** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**updated_on** | **datetime** |  | [optional] 
**uuid** | **str** | The repository&#39;s immutable id. This can be used as a substitute for the slug segment in URLs. Doing this guarantees your URLs will survive renaming of the repository by its owner, or even transfer of the repository to a different user. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



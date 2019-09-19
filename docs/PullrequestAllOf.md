# PullrequestAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**Account**](Account.md) |  | [optional] 
**close_source_branch** | **bool** | A boolean flag indicating if merging the pull request closes the source branch. | [optional] 
**closed_by** | [**Account**](Account.md) |  | [optional] 
**comment_count** | **int** | The number of comments for a specific pull request. | [optional] 
**created_on** | **datetime** | The ISO8601 timestamp the request was created. | [optional] 
**destination** | [**PullrequestEndpoint**](PullrequestEndpoint.md) |  | [optional] 
**id** | **int** | The pull request&#39;s unique ID. Note that pull request IDs are only unique within their associated repository. | [optional] 
**links** | [**PullrequestAllOfLinks**](PullrequestAllOfLinks.md) |  | [optional] 
**merge_commit** | [**PullrequestAllOfMergeCommit**](PullrequestAllOfMergeCommit.md) |  | [optional] 
**participants** | [**list[Participant]**](Participant.md) |         The list of users that are collaborating on this pull request.         Collaborators are user that:          * are added to the pull request as a reviewer (part of the reviewers           list)         * are not explicit reviewers, but have commented on the pull request         * are not explicit reviewers, but have approved the pull request          Each user is wrapped in an object that indicates the user&#39;s role and         whether they have approved the pull request. For performance reasons,         the API only returns this list when an API requests a pull request by         id.          | [optional] 
**reason** | **str** | Explains why a pull request was declined. This field is only applicable to pull requests in rejected state. | [optional] 
**rendered** | [**PullrequestAllOfRendered**](PullrequestAllOfRendered.md) |  | [optional] 
**reviewers** | [**list[Account]**](Account.md) | The list of users that were added as reviewers on this pull request when it was created. For performance reasons, the API only includes this list on a pull request&#39;s &#x60;self&#x60; URL. | [optional] 
**source** | [**PullrequestEndpoint**](PullrequestEndpoint.md) |  | [optional] 
**state** | **str** | The pull request&#39;s current status. | [optional] 
**summary** | [**BaseCommitAllOfSummary**](BaseCommitAllOfSummary.md) |  | [optional] 
**task_count** | **int** | The number of open tasks for a specific pull request. | [optional] 
**title** | **str** | Title of the pull request. | [optional] 
**updated_on** | **datetime** | The ISO8601 timestamp the request was last updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Pipeline

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_number** | **int** | The build number of the pipeline. | [optional] 
**build_seconds_used** | **int** | The number of build seconds used by this pipeline. | [optional] 
**completed_on** | **datetime** | The timestamp when the Pipeline was completed. This is not set if the pipeline is still in progress. | [optional] 
**created_on** | **datetime** | The timestamp when the pipeline was created. | [optional] 
**creator** | [**Account**](Account.md) |  | [optional] 
**repository** | [**Repository**](Repository.md) |  | [optional] 
**state** | [**PipelineState**](PipelineState.md) |  | [optional] 
**target** | [**PipelineTarget**](PipelineTarget.md) |  | [optional] 
**trigger** | [**PipelineTrigger**](PipelineTrigger.md) |  | [optional] 
**uuid** | **str** | The UUID identifying the pipeline. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



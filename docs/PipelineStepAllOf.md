# PipelineStepAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_on** | **datetime** | The timestamp when the step execution was completed. This is not set if the step is still in progress. | [optional] 
**image** | [**PipelineImage**](PipelineImage.md) |  | [optional] 
**script_commands** | [**list[PipelineCommand]**](PipelineCommand.md) | The list of build commands. These commands are executed in the build container. | [optional] 
**setup_commands** | [**list[PipelineCommand]**](PipelineCommand.md) | The list of commands that are executed as part of the setup phase of the build. These commands are executed outside the build container. | [optional] 
**started_on** | **datetime** | The timestamp when the step execution was started. This is not set when the step hasn&#39;t executed yet. | [optional] 
**state** | [**PipelineStepState**](PipelineStepState.md) |  | [optional] 
**uuid** | **str** | The UUID identifying the step. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



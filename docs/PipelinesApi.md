# bitbucketopenapi.PipelinesApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pipeline_for_repository**](PipelinesApi.md#create_pipeline_for_repository) | **POST** /repositories/{workspace}/{repo_slug}/pipelines/ | 
[**create_pipeline_variable_for_team**](PipelinesApi.md#create_pipeline_variable_for_team) | **POST** /teams/{username}/pipelines_config/variables/ | 
[**create_pipeline_variable_for_user**](PipelinesApi.md#create_pipeline_variable_for_user) | **POST** /users/{username}/pipelines_config/variables/ | 
[**create_repository_pipeline_known_host**](PipelinesApi.md#create_repository_pipeline_known_host) | **POST** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/ | 
[**create_repository_pipeline_schedule**](PipelinesApi.md#create_repository_pipeline_schedule) | **POST** /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/ | 
[**create_repository_pipeline_variable**](PipelinesApi.md#create_repository_pipeline_variable) | **POST** /repositories/{workspace}/{repo_slug}/pipelines_config/variables/ | 
[**delete_pipeline_variable_for_team**](PipelinesApi.md#delete_pipeline_variable_for_team) | **DELETE** /teams/{username}/pipelines_config/variables/{variable_uuid} | 
[**delete_pipeline_variable_for_user**](PipelinesApi.md#delete_pipeline_variable_for_user) | **DELETE** /users/{username}/pipelines_config/variables/{variable_uuid} | 
[**delete_repository_pipeline_key_pair**](PipelinesApi.md#delete_repository_pipeline_key_pair) | **DELETE** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair | 
[**delete_repository_pipeline_known_host**](PipelinesApi.md#delete_repository_pipeline_known_host) | **DELETE** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid} | 
[**delete_repository_pipeline_schedule**](PipelinesApi.md#delete_repository_pipeline_schedule) | **DELETE** /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid} | 
[**delete_repository_pipeline_variable**](PipelinesApi.md#delete_repository_pipeline_variable) | **DELETE** /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid} | 
[**get_pipeline_for_repository**](PipelinesApi.md#get_pipeline_for_repository) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid} | 
[**get_pipeline_step_for_repository**](PipelinesApi.md#get_pipeline_step_for_repository) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid} | 
[**get_pipeline_step_log_for_repository**](PipelinesApi.md#get_pipeline_step_log_for_repository) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/log | 
[**get_pipeline_steps_for_repository**](PipelinesApi.md#get_pipeline_steps_for_repository) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/ | 
[**get_pipeline_variable_for_team**](PipelinesApi.md#get_pipeline_variable_for_team) | **GET** /teams/{username}/pipelines_config/variables/{variable_uuid} | 
[**get_pipeline_variable_for_user**](PipelinesApi.md#get_pipeline_variable_for_user) | **GET** /users/{username}/pipelines_config/variables/{variable_uuid} | 
[**get_pipeline_variables_for_team**](PipelinesApi.md#get_pipeline_variables_for_team) | **GET** /teams/{username}/pipelines_config/variables/ | 
[**get_pipeline_variables_for_user**](PipelinesApi.md#get_pipeline_variables_for_user) | **GET** /users/{username}/pipelines_config/variables/ | 
[**get_pipelines_for_repository**](PipelinesApi.md#get_pipelines_for_repository) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/ | 
[**get_repository_pipeline_config**](PipelinesApi.md#get_repository_pipeline_config) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config | 
[**get_repository_pipeline_known_host**](PipelinesApi.md#get_repository_pipeline_known_host) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid} | 
[**get_repository_pipeline_known_hosts**](PipelinesApi.md#get_repository_pipeline_known_hosts) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/ | 
[**get_repository_pipeline_schedule**](PipelinesApi.md#get_repository_pipeline_schedule) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid} | 
[**get_repository_pipeline_schedule_executions**](PipelinesApi.md#get_repository_pipeline_schedule_executions) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}/executions/ | 
[**get_repository_pipeline_schedules**](PipelinesApi.md#get_repository_pipeline_schedules) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/ | 
[**get_repository_pipeline_ssh_key_pair**](PipelinesApi.md#get_repository_pipeline_ssh_key_pair) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair | 
[**get_repository_pipeline_variable**](PipelinesApi.md#get_repository_pipeline_variable) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid} | 
[**get_repository_pipeline_variables**](PipelinesApi.md#get_repository_pipeline_variables) | **GET** /repositories/{workspace}/{repo_slug}/pipelines_config/variables/ | 
[**stop_pipeline**](PipelinesApi.md#stop_pipeline) | **POST** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/stopPipeline | 
[**update_pipeline_variable_for_team**](PipelinesApi.md#update_pipeline_variable_for_team) | **PUT** /teams/{username}/pipelines_config/variables/{variable_uuid} | 
[**update_pipeline_variable_for_user**](PipelinesApi.md#update_pipeline_variable_for_user) | **PUT** /users/{username}/pipelines_config/variables/{variable_uuid} | 
[**update_repository_build_number**](PipelinesApi.md#update_repository_build_number) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines_config/build_number | 
[**update_repository_pipeline_config**](PipelinesApi.md#update_repository_pipeline_config) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines_config | 
[**update_repository_pipeline_key_pair**](PipelinesApi.md#update_repository_pipeline_key_pair) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair | 
[**update_repository_pipeline_known_host**](PipelinesApi.md#update_repository_pipeline_known_host) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid} | 
[**update_repository_pipeline_schedule**](PipelinesApi.md#update_repository_pipeline_schedule) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid} | 
[**update_repository_pipeline_variable**](PipelinesApi.md#update_repository_pipeline_variable) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid} | 


# **create_pipeline_for_repository**
> Pipeline create_pipeline_for_repository(username, repo_slug, body)



Endpoint to create and initiate a pipeline.  There are a couple of different options to initiate a pipeline, where the payload of the request will determine which type of pipeline will be instantiated. # Trigger a Pipeline for a branch One way to trigger pipelines is by specifying the branch for which you want to trigger a pipeline.  The specified branch will be used to determine which pipeline definition from the `bitbucket-pipelines.yml` file will be applied to initiate the pipeline. The pipeline will then do a clone of the repository and checkout the latest revision of the specified branch.  ### Example  ``` $ curl -X POST -is -u username:password \\   -H 'Content-Type: application/json' \\  https://api.bitbucket.org/2.0/repositories/jeroendr/meat-demo2/pipelines/ \\   -d '   {     \"target\": {       \"ref_type\": \"branch\",        \"type\": \"pipeline_ref_target\",        \"ref_name\": \"master\"     }   }' ``` # Trigger a Pipeline for a commit on a branch or tag You can initiate a pipeline for a specific commit and in the context of a specified reference (e.g. a branch, tag or bookmark). The specified reference will be used to determine which pipeline definition from the bitbucket-pipelines.yml file will be applied to initiate the pipeline. The pipeline will clone the repository and then do a checkout the specified reference.   The following reference types are supported:  * `branch`  * `named_branch` * `bookmark`   * `tag`  ### Example  ``` $ curl -X POST -is -u username:password \\   -H 'Content-Type: application/json' \\   https://api.bitbucket.org/2.0/repositories/jeroendr/meat-demo2/pipelines/ \\   -d '   {     \"target\": {       \"commit\": {         \"type\": \"commit\",          \"hash\": \"ce5b7431602f7cbba007062eeb55225c6e18e956\"       },        \"ref_type\": \"branch\",        \"type\": \"pipeline_ref_target\",        \"ref_name\": \"master\"     }   }' ``` # Trigger a specific pipeline definition for a commit You can trigger a specific pipeline that is defined in your `bitbucket-pipelines.yml` file for a specific commit.  In addition to the commit revision, you specify the type and pattern of the selector that identifies the pipeline definition. The resulting pipeline will then clone the repository and checkout the specified revision.  ### Example  ``` $ curl -X POST -is -u username:password \\   -H 'Content-Type: application/json' \\  https://api.bitbucket.org/2.0/repositories/jeroendr/meat-demo2/pipelines/ \\  -d '   {      \"target\": {       \"commit\": {          \"hash\":\"a3c4e02c9a3755eccdc3764e6ea13facdf30f923\",          \"type\":\"commit\"        },         \"selector\": {            \"type\":\"custom\",               \"pattern\":\"Deploy to production\"           },         \"type\":\"pipeline_commit_target\"    }   }' ``` # Trigger a specific pipeline definition for a commit on a branch or tag You can trigger a specific pipeline that is defined in your `bitbucket-pipelines.yml` file for a specific commit in the context of a specified reference.  In addition to the commit revision, you specify the type and pattern of the selector that identifies the pipeline definition, as well as the reference information. The resulting pipeline will then clone the repository a checkout the specified reference.  ### Example  ``` $ curl -X POST -is -u username:password \\   -H 'Content-Type: application/json' \\  https://api.bitbucket.org/2.0/repositories/jeroendr/meat-demo2/pipelines/ \\  -d '   {      \"target\": {       \"commit\": {          \"hash\":\"a3c4e02c9a3755eccdc3764e6ea13facdf30f923\",          \"type\":\"commit\"        },        \"selector\": {           \"type\": \"custom\",           \"pattern\": \"Deploy to production\"        },        \"type\": \"pipeline_ref_target\",        \"ref_name\": \"master\",        \"ref_type\": \"branch\"      }   }' ```   # Trigger a custom pipeline with variables In addition to triggering a custom pipeline that is defined in your `bitbucket-pipelines.yml` file as shown in the examples above, you can specify variables that will be available for your build. In the request, provide a list of variables, specifying the following for each variable: key, value, and whether it should be secured or not (this field is optional and defaults to not secured).  ### Example  ``` $ curl -X POST -is -u username:password \\   -H 'Content-Type: application/json' \\  https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \\  -d '   {     \"target\": {       \"type\": \"pipeline_ref_target\",       \"ref_type\": \"branch\",       \"ref_name\": \"master\",       \"selector\": {         \"type\": \"custom\",         \"pattern\": \"Deploy to production\"       }     },     \"variables\": [       {         \"key\": \"var1key\",         \"value\": \"var1value\",         \"secured\": true       },       {         \"key\": \"var2key\",         \"value\": \"var2value\"       }     ]   }' ``` 

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
body = bitbucketopenapi.Pipeline() # Pipeline | The pipeline to initiate.

try:
    api_response = api_instance.create_pipeline_for_repository(username, repo_slug, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->create_pipeline_for_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **body** | [**Pipeline**](Pipeline.md)| The pipeline to initiate. | 

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The initiated pipeline. |  * Location - The URL of the newly created pipeline. <br>  |
**400** | The account or repository is not enabled, the yml file does not exist in the repository for the given revision, or the request body contained invalid properties. |  -  |
**404** | The account or repository was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pipeline_variable_for_team**
> PipelineVariable create_pipeline_variable_for_team(username, body=body)



Create an account level variable.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
body = bitbucketopenapi.PipelineVariable() # PipelineVariable | The variable to create. (optional)

try:
    api_response = api_instance.create_pipeline_variable_for_team(username, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->create_pipeline_variable_for_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **body** | [**PipelineVariable**](PipelineVariable.md)| The variable to create. | [optional] 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created variable. |  * Location - The URL of the newly created pipeline variable. <br>  |
**404** | The account does not exist. |  -  |
**409** | A variable with the provided key already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pipeline_variable_for_user**
> PipelineVariable create_pipeline_variable_for_user(username, body=body)



Create a user level variable.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
body = bitbucketopenapi.PipelineVariable() # PipelineVariable | The variable to create. (optional)

try:
    api_response = api_instance.create_pipeline_variable_for_user(username, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->create_pipeline_variable_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **body** | [**PipelineVariable**](PipelineVariable.md)| The variable to create. | [optional] 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created variable. |  * Location - The URL of the newly created pipeline variable. <br>  |
**404** | The account does not exist. |  -  |
**409** | A variable with the provided key already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository_pipeline_known_host**
> PipelineKnownHost create_repository_pipeline_known_host(username, repo_slug, body)



Create a repository level known host.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
body = bitbucketopenapi.PipelineKnownHost() # PipelineKnownHost | The known host to create.

try:
    api_response = api_instance.create_repository_pipeline_known_host(username, repo_slug, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->create_repository_pipeline_known_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **body** | [**PipelineKnownHost**](PipelineKnownHost.md)| The known host to create. | 

### Return type

[**PipelineKnownHost**](PipelineKnownHost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The known host was created. |  * Location - The URL of the newly created pipeline known host. <br>  |
**404** | The account or repository does not exist. |  -  |
**409** | A known host with the provided hostname already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository_pipeline_schedule**
> PipelineSchedule create_repository_pipeline_schedule(username, repo_slug, body)



Create a schedule for the given repository.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
body = bitbucketopenapi.PipelineSchedule() # PipelineSchedule | The schedule to create.

try:
    api_response = api_instance.create_repository_pipeline_schedule(username, repo_slug, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->create_repository_pipeline_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **body** | [**PipelineSchedule**](PipelineSchedule.md)| The schedule to create. | 

### Return type

[**PipelineSchedule**](PipelineSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created schedule. |  -  |
**400** | There were errors validating the request. |  -  |
**401** | The maximum limit of schedules for this repository was reached. |  -  |
**404** | The account or repository was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository_pipeline_variable**
> PipelineVariable create_repository_pipeline_variable(username, repo_slug, body)



Create a repository level variable.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
body = bitbucketopenapi.PipelineVariable() # PipelineVariable | The variable to create.

try:
    api_response = api_instance.create_repository_pipeline_variable(username, repo_slug, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->create_repository_pipeline_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **body** | [**PipelineVariable**](PipelineVariable.md)| The variable to create. | 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The variable was created. |  * Location - The URL of the newly created pipeline variable. <br>  |
**404** | The account or repository does not exist. |  -  |
**409** | A variable with the provided key already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pipeline_variable_for_team**
> delete_pipeline_variable_for_team(username, variable_uuid)



Delete a team level variable.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
variable_uuid = 'variable_uuid_example' # str | The UUID of the variable to delete.

try:
    api_instance.delete_pipeline_variable_for_team(username, variable_uuid)
except ApiException as e:
    print("Exception when calling PipelinesApi->delete_pipeline_variable_for_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **variable_uuid** | **str**| The UUID of the variable to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The variable was deleted |  -  |
**404** | The account or the variable with the provided UUID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pipeline_variable_for_user**
> delete_pipeline_variable_for_user(username, variable_uuid)



Delete an account level variable.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
variable_uuid = 'variable_uuid_example' # str | The UUID of the variable to delete.

try:
    api_instance.delete_pipeline_variable_for_user(username, variable_uuid)
except ApiException as e:
    print("Exception when calling PipelinesApi->delete_pipeline_variable_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **variable_uuid** | **str**| The UUID of the variable to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The variable was deleted |  -  |
**404** | The account or the variable with the provided UUID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repository_pipeline_key_pair**
> delete_repository_pipeline_key_pair(username, repo_slug)



Delete the repository SSH key pair.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.

try:
    api_instance.delete_repository_pipeline_key_pair(username, repo_slug)
except ApiException as e:
    print("Exception when calling PipelinesApi->delete_repository_pipeline_key_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The SSH key pair was deleted. |  -  |
**404** | The account, repository or SSH key pair was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repository_pipeline_known_host**
> delete_repository_pipeline_known_host(username, repo_slug, known_host_uuid)



Delete a repository level known host.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
known_host_uuid = 'known_host_uuid_example' # str | The UUID of the known host to delete.

try:
    api_instance.delete_repository_pipeline_known_host(username, repo_slug, known_host_uuid)
except ApiException as e:
    print("Exception when calling PipelinesApi->delete_repository_pipeline_known_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **known_host_uuid** | **str**| The UUID of the known host to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The known host was deleted. |  -  |
**404** | The account, repository or known host with given UUID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repository_pipeline_schedule**
> delete_repository_pipeline_schedule(username, repo_slug, schedule_uuid)



Delete a schedule.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
schedule_uuid = 'schedule_uuid_example' # str | The uuid of the schedule.

try:
    api_instance.delete_repository_pipeline_schedule(username, repo_slug, schedule_uuid)
except ApiException as e:
    print("Exception when calling PipelinesApi->delete_repository_pipeline_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **schedule_uuid** | **str**| The uuid of the schedule. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The schedule was deleted. |  -  |
**404** | The account, repository or schedule was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repository_pipeline_variable**
> delete_repository_pipeline_variable(username, repo_slug, variable_uuid)



Delete a repository level variable.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
variable_uuid = 'variable_uuid_example' # str | The UUID of the variable to delete.

try:
    api_instance.delete_repository_pipeline_variable(username, repo_slug, variable_uuid)
except ApiException as e:
    print("Exception when calling PipelinesApi->delete_repository_pipeline_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **variable_uuid** | **str**| The UUID of the variable to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The variable was deleted. |  -  |
**404** | The account, repository or variable with given UUID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_for_repository**
> Pipeline get_pipeline_for_repository(username, repo_slug, pipeline_uuid)



Retrieve a specified pipeline

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
pipeline_uuid = 'pipeline_uuid_example' # str | The pipeline UUID.

try:
    api_response = api_instance.get_pipeline_for_repository(username, repo_slug, pipeline_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_pipeline_for_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **pipeline_uuid** | **str**| The pipeline UUID. | 

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The pipeline. |  -  |
**404** | No account, repository or pipeline with the UUID provided exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_step_for_repository**
> PipelineStep get_pipeline_step_for_repository(username, repo_slug, pipeline_uuid, step_uuid)



Retrieve a given step of a pipeline.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
pipeline_uuid = 'pipeline_uuid_example' # str | The UUID of the pipeline.
step_uuid = 'step_uuid_example' # str | The UUID of the step.

try:
    api_response = api_instance.get_pipeline_step_for_repository(username, repo_slug, pipeline_uuid, step_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_pipeline_step_for_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **pipeline_uuid** | **str**| The UUID of the pipeline. | 
 **step_uuid** | **str**| The UUID of the step. | 

### Return type

[**PipelineStep**](PipelineStep.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The step. |  -  |
**404** | No account, repository, pipeline or step with the UUID provided exists for the pipeline with the UUID provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_step_log_for_repository**
> get_pipeline_step_log_for_repository(username, repo_slug, pipeline_uuid, step_uuid)



Retrieve the log file for a given step of a pipeline.  This endpoint supports (and encourages!) the use of [HTTP Range requests](https://tools.ietf.org/html/rfc7233) to deal with potentially very large log files.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
pipeline_uuid = 'pipeline_uuid_example' # str | The UUID of the pipeline.
step_uuid = 'step_uuid_example' # str | The UUID of the step.

try:
    api_instance.get_pipeline_step_log_for_repository(username, repo_slug, pipeline_uuid, step_uuid)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_pipeline_step_log_for_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **pipeline_uuid** | **str**| The UUID of the pipeline. | 
 **step_uuid** | **str**| The UUID of the step. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The raw log file for this pipeline step. |  -  |
**304** | The log has the same etag as the provided If-None-Match header. |  -  |
**404** | A pipeline with the given UUID does not exist, a step with the given UUID does not exist in the pipeline or a log file does not exist for the given step. |  -  |
**416** | The requested range does not exist for requests that specified the [HTTP Range header](https://tools.ietf.org/html/rfc7233#section-3.1). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_steps_for_repository**
> PaginatedPipelineSteps get_pipeline_steps_for_repository(username, repo_slug, pipeline_uuid)



Find steps for the given pipeline.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
pipeline_uuid = 'pipeline_uuid_example' # str | The UUID of the pipeline.

try:
    api_response = api_instance.get_pipeline_steps_for_repository(username, repo_slug, pipeline_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_pipeline_steps_for_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **pipeline_uuid** | **str**| The UUID of the pipeline. | 

### Return type

[**PaginatedPipelineSteps**](PaginatedPipelineSteps.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The steps. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_variable_for_team**
> PipelineVariable get_pipeline_variable_for_team(username, variable_uuid)



Retrieve a team level variable.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
variable_uuid = 'variable_uuid_example' # str | The UUID of the variable to retrieve.

try:
    api_response = api_instance.get_pipeline_variable_for_team(username, variable_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_pipeline_variable_for_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **variable_uuid** | **str**| The UUID of the variable to retrieve. | 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The variable. |  -  |
**404** | The account or variable with the given UUID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_variable_for_user**
> PipelineVariable get_pipeline_variable_for_user(username, variable_uuid)



Retrieve a user level variable.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
variable_uuid = 'variable_uuid_example' # str | The UUID of the variable to retrieve.

try:
    api_response = api_instance.get_pipeline_variable_for_user(username, variable_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_pipeline_variable_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **variable_uuid** | **str**| The UUID of the variable to retrieve. | 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The variable. |  -  |
**404** | The account or variable with the given UUID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_variables_for_team**
> PaginatedPipelineVariables get_pipeline_variables_for_team(username)



Find account level variables.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.

try:
    api_response = api_instance.get_pipeline_variables_for_team(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_pipeline_variables_for_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 

### Return type

[**PaginatedPipelineVariables**](PaginatedPipelineVariables.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The found account level variables. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_variables_for_user**
> PaginatedPipelineVariables get_pipeline_variables_for_user(username)



Find user level variables.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.

try:
    api_response = api_instance.get_pipeline_variables_for_user(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_pipeline_variables_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 

### Return type

[**PaginatedPipelineVariables**](PaginatedPipelineVariables.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The found user level variables. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipelines_for_repository**
> PaginatedPipelines get_pipelines_for_repository(username, repo_slug)



Find pipelines

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.

try:
    api_response = api_instance.get_pipelines_for_repository(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_pipelines_for_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 

### Return type

[**PaginatedPipelines**](PaginatedPipelines.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching pipelines. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository_pipeline_config**
> PipelinesConfig get_repository_pipeline_config(username, repo_slug)



Retrieve the repository pipelines configuration.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.

try:
    api_response = api_instance.get_repository_pipeline_config(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_repository_pipeline_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 

### Return type

[**PipelinesConfig**](PipelinesConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The repository pipelines configuration. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository_pipeline_known_host**
> PipelineKnownHost get_repository_pipeline_known_host(username, repo_slug, known_host_uuid)



Retrieve a repository level known host.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
known_host_uuid = 'known_host_uuid_example' # str | The UUID of the known host to retrieve.

try:
    api_response = api_instance.get_repository_pipeline_known_host(username, repo_slug, known_host_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_repository_pipeline_known_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **known_host_uuid** | **str**| The UUID of the known host to retrieve. | 

### Return type

[**PipelineKnownHost**](PipelineKnownHost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The known host. |  -  |
**404** | The account, repository or known host with the specified UUID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository_pipeline_known_hosts**
> PaginatedPipelineKnownHosts get_repository_pipeline_known_hosts(username, repo_slug)



Find repository level known hosts.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.

try:
    api_response = api_instance.get_repository_pipeline_known_hosts(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_repository_pipeline_known_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 

### Return type

[**PaginatedPipelineKnownHosts**](PaginatedPipelineKnownHosts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The retrieved known hosts. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository_pipeline_schedule**
> PipelineSchedule get_repository_pipeline_schedule(username, repo_slug, schedule_uuid)



Retrieve a schedule by its UUID.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
schedule_uuid = 'schedule_uuid_example' # str | The uuid of the schedule.

try:
    api_response = api_instance.get_repository_pipeline_schedule(username, repo_slug, schedule_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_repository_pipeline_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **schedule_uuid** | **str**| The uuid of the schedule. | 

### Return type

[**PipelineSchedule**](PipelineSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested schedule. |  -  |
**404** | The account, repository or schedule was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository_pipeline_schedule_executions**
> PaginatedPipelineScheduleExecutions get_repository_pipeline_schedule_executions(username, repo_slug)



Retrieve the executions of a given schedule.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.

try:
    api_response = api_instance.get_repository_pipeline_schedule_executions(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_repository_pipeline_schedule_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 

### Return type

[**PaginatedPipelineScheduleExecutions**](PaginatedPipelineScheduleExecutions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of executions of a schedule. |  -  |
**404** | The account or repository was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository_pipeline_schedules**
> PaginatedPipelineSchedules get_repository_pipeline_schedules(username, repo_slug)



Retrieve the configured schedules for the given repository.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.

try:
    api_response = api_instance.get_repository_pipeline_schedules(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_repository_pipeline_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 

### Return type

[**PaginatedPipelineSchedules**](PaginatedPipelineSchedules.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of schedules. |  -  |
**404** | The account or repository was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository_pipeline_ssh_key_pair**
> PipelineSshKeyPair get_repository_pipeline_ssh_key_pair(username, repo_slug)



Retrieve the repository SSH key pair excluding the SSH private key. The private key is a write only field and will never be exposed in the logs or the REST API.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.

try:
    api_response = api_instance.get_repository_pipeline_ssh_key_pair(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_repository_pipeline_ssh_key_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 

### Return type

[**PipelineSshKeyPair**](PipelineSshKeyPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SSH key pair. |  -  |
**404** | The account, repository or SSH key pair was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository_pipeline_variable**
> PipelineVariable get_repository_pipeline_variable(username, repo_slug, variable_uuid)



Retrieve a repository level variable.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
variable_uuid = 'variable_uuid_example' # str | The UUID of the variable to retrieve.

try:
    api_response = api_instance.get_repository_pipeline_variable(username, repo_slug, variable_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_repository_pipeline_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **variable_uuid** | **str**| The UUID of the variable to retrieve. | 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The variable. |  -  |
**404** | The account, repository or variable with the specified UUID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository_pipeline_variables**
> PaginatedPipelineVariables get_repository_pipeline_variables(username, repo_slug)



Find repository level variables.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.

try:
    api_response = api_instance.get_repository_pipeline_variables(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_repository_pipeline_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 

### Return type

[**PaginatedPipelineVariables**](PaginatedPipelineVariables.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The retrieved variables. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_pipeline**
> stop_pipeline(username, repo_slug, pipeline_uuid)



Signal the stop of a pipeline and all of its steps that not have completed yet.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
pipeline_uuid = 'pipeline_uuid_example' # str | The UUID of the pipeline.

try:
    api_instance.stop_pipeline(username, repo_slug, pipeline_uuid)
except ApiException as e:
    print("Exception when calling PipelinesApi->stop_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **pipeline_uuid** | **str**| The UUID of the pipeline. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The pipeline has been signaled to stop. |  -  |
**400** | The specified pipeline has already completed. |  -  |
**404** | Either the account, repository or pipeline with the given UUID does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pipeline_variable_for_team**
> PipelineVariable update_pipeline_variable_for_team(username, variable_uuid, body)



Update a team level variable.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
variable_uuid = 'variable_uuid_example' # str | The UUID of the variable.
body = bitbucketopenapi.PipelineVariable() # PipelineVariable | The updated variable.

try:
    api_response = api_instance.update_pipeline_variable_for_team(username, variable_uuid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->update_pipeline_variable_for_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **variable_uuid** | **str**| The UUID of the variable. | 
 **body** | [**PipelineVariable**](PipelineVariable.md)| The updated variable. | 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The variable was updated. |  -  |
**404** | The account or the variable was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pipeline_variable_for_user**
> PipelineVariable update_pipeline_variable_for_user(username, variable_uuid, body)



Update a user level variable.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
variable_uuid = 'variable_uuid_example' # str | The UUID of the variable.
body = bitbucketopenapi.PipelineVariable() # PipelineVariable | The updated variable.

try:
    api_response = api_instance.update_pipeline_variable_for_user(username, variable_uuid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->update_pipeline_variable_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **variable_uuid** | **str**| The UUID of the variable. | 
 **body** | [**PipelineVariable**](PipelineVariable.md)| The updated variable. | 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The variable was updated. |  -  |
**404** | The account or the variable was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository_build_number**
> PipelineBuildNumber update_repository_build_number(username, repo_slug, body)



Update the next build number that should be assigned to a pipeline. The next build number that will be configured has to be strictly higher than the current latest build number for this repository.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
body = bitbucketopenapi.PipelineBuildNumber() # PipelineBuildNumber | The build number to update.

try:
    api_response = api_instance.update_repository_build_number(username, repo_slug, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->update_repository_build_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **body** | [**PipelineBuildNumber**](PipelineBuildNumber.md)| The build number to update. | 

### Return type

[**PipelineBuildNumber**](PipelineBuildNumber.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The build number has been configured. |  -  |
**400** | The update failed because the next number was invalid (it should be higher than the current number). |  -  |
**404** | The account or repository was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository_pipeline_config**
> PipelinesConfig update_repository_pipeline_config(username, repo_slug, body)



Update the pipelines configuration for a repository.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
body = bitbucketopenapi.PipelinesConfig() # PipelinesConfig | The updated repository pipelines configuration.

try:
    api_response = api_instance.update_repository_pipeline_config(username, repo_slug, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->update_repository_pipeline_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **body** | [**PipelinesConfig**](PipelinesConfig.md)| The updated repository pipelines configuration. | 

### Return type

[**PipelinesConfig**](PipelinesConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The repository pipelines configuration was updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository_pipeline_key_pair**
> PipelineSshKeyPair update_repository_pipeline_key_pair(username, repo_slug, body)



Create or update the repository SSH key pair. The private key will be set as a default SSH identity in your build container.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
body = bitbucketopenapi.PipelineSshKeyPair() # PipelineSshKeyPair | The created or updated SSH key pair.

try:
    api_response = api_instance.update_repository_pipeline_key_pair(username, repo_slug, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->update_repository_pipeline_key_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **body** | [**PipelineSshKeyPair**](PipelineSshKeyPair.md)| The created or updated SSH key pair. | 

### Return type

[**PipelineSshKeyPair**](PipelineSshKeyPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SSH key pair was created or updated. |  -  |
**404** | The account, repository or SSH key pair was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository_pipeline_known_host**
> PipelineKnownHost update_repository_pipeline_known_host(username, repo_slug, known_host_uuid, body)



Update a repository level known host.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
known_host_uuid = 'known_host_uuid_example' # str | The UUID of the known host to update.
body = bitbucketopenapi.PipelineKnownHost() # PipelineKnownHost | The updated known host.

try:
    api_response = api_instance.update_repository_pipeline_known_host(username, repo_slug, known_host_uuid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->update_repository_pipeline_known_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **known_host_uuid** | **str**| The UUID of the known host to update. | 
 **body** | [**PipelineKnownHost**](PipelineKnownHost.md)| The updated known host. | 

### Return type

[**PipelineKnownHost**](PipelineKnownHost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The known host was updated. |  -  |
**404** | The account, repository or known host with the given UUID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository_pipeline_schedule**
> PipelineSchedule update_repository_pipeline_schedule(username, repo_slug, schedule_uuid, body)



Update a schedule.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
schedule_uuid = 'schedule_uuid_example' # str | The uuid of the schedule.
body = bitbucketopenapi.PipelineSchedule() # PipelineSchedule | The schedule to update.

try:
    api_response = api_instance.update_repository_pipeline_schedule(username, repo_slug, schedule_uuid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->update_repository_pipeline_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **schedule_uuid** | **str**| The uuid of the schedule. | 
 **body** | [**PipelineSchedule**](PipelineSchedule.md)| The schedule to update. | 

### Return type

[**PipelineSchedule**](PipelineSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The schedule is updated. |  -  |
**404** | The account, repository or schedule was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository_pipeline_variable**
> PipelineVariable update_repository_pipeline_variable(username, repo_slug, variable_uuid, body)



Update a repository level variable.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PipelinesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
variable_uuid = 'variable_uuid_example' # str | The UUID of the variable to update.
body = bitbucketopenapi.PipelineVariable() # PipelineVariable | The updated variable

try:
    api_response = api_instance.update_repository_pipeline_variable(username, repo_slug, variable_uuid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->update_repository_pipeline_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **variable_uuid** | **str**| The UUID of the variable to update. | 
 **body** | [**PipelineVariable**](PipelineVariable.md)| The updated variable | 

### Return type

[**PipelineVariable**](PipelineVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The variable was updated. |  -  |
**404** | The account, repository or variable with the given UUID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


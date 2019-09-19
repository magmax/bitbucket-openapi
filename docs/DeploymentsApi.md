# bitbucketopenapi.DeploymentsApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_environment**](DeploymentsApi.md#create_environment) | **POST** /repositories/{workspace}/{repo_slug}/environments/ | 
[**delete_environment_for_repository**](DeploymentsApi.md#delete_environment_for_repository) | **DELETE** /repositories/{workspace}/{repo_slug}/environments/{environment_uuid} | 
[**get_deployment_for_repository**](DeploymentsApi.md#get_deployment_for_repository) | **GET** /repositories/{workspace}/{repo_slug}/deployments/{deployment_uuid} | 
[**get_deployments_for_repository**](DeploymentsApi.md#get_deployments_for_repository) | **GET** /repositories/{workspace}/{repo_slug}/deployments/ | 
[**get_environment_for_repository**](DeploymentsApi.md#get_environment_for_repository) | **GET** /repositories/{workspace}/{repo_slug}/environments/{environment_uuid} | 
[**get_environments_for_repository**](DeploymentsApi.md#get_environments_for_repository) | **GET** /repositories/{workspace}/{repo_slug}/environments/ | 
[**update_environment_for_repository**](DeploymentsApi.md#update_environment_for_repository) | **POST** /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes/ | 


# **create_environment**
> DeploymentEnvironment create_environment(username, repo_slug, body)



Create an environment.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.DeploymentsApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
body = bitbucketopenapi.DeploymentEnvironment() # DeploymentEnvironment | The environment to create.

try:
    api_response = api_instance.create_environment(username, repo_slug, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->create_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **body** | [**DeploymentEnvironment**](DeploymentEnvironment.md)| The environment to create. | 

### Return type

[**DeploymentEnvironment**](DeploymentEnvironment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The environment was created. |  * Location - The URL of the newly created environment. <br>  |
**404** | The account or repository does not exist. |  -  |
**409** | An environment host with the provided name already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_environment_for_repository**
> delete_environment_for_repository(username, repo_slug, environment_uuid)



Delete an environment

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.DeploymentsApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
environment_uuid = 'environment_uuid_example' # str | The environment UUID.

try:
    api_instance.delete_environment_for_repository(username, repo_slug, environment_uuid)
except ApiException as e:
    print("Exception when calling DeploymentsApi->delete_environment_for_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **environment_uuid** | **str**| The environment UUID. | 

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
**204** | The environment was deleted. |  -  |
**404** | No account or repository with the UUID provided exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_for_repository**
> Deployment get_deployment_for_repository(username, repo_slug, deployment_uuid)



Retrieve a deployment

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.DeploymentsApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
deployment_uuid = 'deployment_uuid_example' # str | The deployment UUID.

try:
    api_response = api_instance.get_deployment_for_repository(username, repo_slug, deployment_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_deployment_for_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **deployment_uuid** | **str**| The deployment UUID. | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deployment. |  -  |
**404** | No account, repository or deployment with the UUID provided exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployments_for_repository**
> PaginatedDeployments get_deployments_for_repository(username, repo_slug)



Find deployments

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.DeploymentsApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.

try:
    api_response = api_instance.get_deployments_for_repository(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_deployments_for_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 

### Return type

[**PaginatedDeployments**](PaginatedDeployments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching deployments. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_for_repository**
> DeploymentEnvironment get_environment_for_repository(username, repo_slug, environment_uuid)



Retrieve an environment

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.DeploymentsApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
environment_uuid = 'environment_uuid_example' # str | The environment UUID.

try:
    api_response = api_instance.get_environment_for_repository(username, repo_slug, environment_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_environment_for_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **environment_uuid** | **str**| The environment UUID. | 

### Return type

[**DeploymentEnvironment**](DeploymentEnvironment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The environment. |  -  |
**404** | No account, repository or environment with the UUID provided exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environments_for_repository**
> PaginatedEnvironments get_environments_for_repository(username, repo_slug)



Find environments

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.DeploymentsApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.

try:
    api_response = api_instance.get_environments_for_repository(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_environments_for_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 

### Return type

[**PaginatedEnvironments**](PaginatedEnvironments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matching environments. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_environment_for_repository**
> update_environment_for_repository(username, repo_slug, environment_uuid)



Update an environment

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.DeploymentsApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
environment_uuid = 'environment_uuid_example' # str | The environment UUID.

try:
    api_instance.update_environment_for_repository(username, repo_slug, environment_uuid)
except ApiException as e:
    print("Exception when calling DeploymentsApi->update_environment_for_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **environment_uuid** | **str**| The environment UUID. | 

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
**202** | The environment update request was accepted. |  -  |
**404** | No account, repository or environment with the UUID provided exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


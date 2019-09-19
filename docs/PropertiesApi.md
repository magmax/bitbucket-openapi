# bitbucketopenapi.PropertiesApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_commit_hosted_property_value**](PropertiesApi.md#delete_commit_hosted_property_value) | **DELETE** /repositories/{workspace}/{repo_slug}/commit/{commit}/properties/{app_key}/{property_name} | 
[**delete_pull_request_hosted_property_value**](PropertiesApi.md#delete_pull_request_hosted_property_value) | **DELETE** /repositories/{workspace}/{repo_slug}/pullrequests/{pullrequest_id}/properties/{app_key}/{property_name} | 
[**delete_repository_hosted_property_value**](PropertiesApi.md#delete_repository_hosted_property_value) | **DELETE** /repositories/{workspace}/{repo_slug}/properties/{app_key}/{property_name} | 
[**delete_user_hosted_property_value**](PropertiesApi.md#delete_user_hosted_property_value) | **DELETE** /users/{username}/properties/{app_key}/{property_name} | 
[**get_commit_hosted_property_value**](PropertiesApi.md#get_commit_hosted_property_value) | **GET** /repositories/{workspace}/{repo_slug}/commit/{commit}/properties/{app_key}/{property_name} | 
[**get_pull_request_hosted_property_value**](PropertiesApi.md#get_pull_request_hosted_property_value) | **GET** /repositories/{workspace}/{repo_slug}/pullrequests/{pullrequest_id}/properties/{app_key}/{property_name} | 
[**get_repository_hosted_property_value**](PropertiesApi.md#get_repository_hosted_property_value) | **GET** /repositories/{workspace}/{repo_slug}/properties/{app_key}/{property_name} | 
[**retrieve_user_hosted_property_value**](PropertiesApi.md#retrieve_user_hosted_property_value) | **GET** /users/{username}/properties/{app_key}/{property_name} | 
[**update_commit_hosted_property_value**](PropertiesApi.md#update_commit_hosted_property_value) | **PUT** /repositories/{workspace}/{repo_slug}/commit/{commit}/properties/{app_key}/{property_name} | 
[**update_pull_request_hosted_property_value**](PropertiesApi.md#update_pull_request_hosted_property_value) | **PUT** /repositories/{workspace}/{repo_slug}/pullrequests/{pullrequest_id}/properties/{app_key}/{property_name} | 
[**update_repository_hosted_property_value**](PropertiesApi.md#update_repository_hosted_property_value) | **PUT** /repositories/{workspace}/{repo_slug}/properties/{app_key}/{property_name} | 
[**update_user_hosted_property_value**](PropertiesApi.md#update_user_hosted_property_value) | **PUT** /users/{username}/properties/{app_key}/{property_name} | 


# **delete_commit_hosted_property_value**
> delete_commit_hosted_property_value(username, repo_slug, commit, app_key, property_name)



Delete an application property value stored against a commit.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PropertiesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
commit = 'commit_example' # str | The commit.
app_key = 'app_key_example' # str | The key of the Connect app.
property_name = 'property_name_example' # str | The name of the property.

try:
    api_instance.delete_commit_hosted_property_value(username, repo_slug, commit, app_key, property_name)
except ApiException as e:
    print("Exception when calling PropertiesApi->delete_commit_hosted_property_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **commit** | **str**| The commit. | 
 **app_key** | **str**| The key of the Connect app. | 
 **property_name** | **str**| The name of the property. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | An empty response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pull_request_hosted_property_value**
> delete_pull_request_hosted_property_value(username, repo_slug, pullrequest_id, app_key, property_name)



Delete an application property value stored against a pull request.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PropertiesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
pullrequest_id = 'pullrequest_id_example' # str | The pull request ID.
app_key = 'app_key_example' # str | The key of the Connect app.
property_name = 'property_name_example' # str | The name of the property.

try:
    api_instance.delete_pull_request_hosted_property_value(username, repo_slug, pullrequest_id, app_key, property_name)
except ApiException as e:
    print("Exception when calling PropertiesApi->delete_pull_request_hosted_property_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **pullrequest_id** | **str**| The pull request ID. | 
 **app_key** | **str**| The key of the Connect app. | 
 **property_name** | **str**| The name of the property. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | An empty response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repository_hosted_property_value**
> delete_repository_hosted_property_value(username, repo_slug, app_key, property_name)



Delete an application property value stored against a repository.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PropertiesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
app_key = 'app_key_example' # str | The key of the Connect app.
property_name = 'property_name_example' # str | The name of the property.

try:
    api_instance.delete_repository_hosted_property_value(username, repo_slug, app_key, property_name)
except ApiException as e:
    print("Exception when calling PropertiesApi->delete_repository_hosted_property_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **app_key** | **str**| The key of the Connect app. | 
 **property_name** | **str**| The name of the property. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | An empty response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_hosted_property_value**
> delete_user_hosted_property_value(username, app_key, property_name)



Delete an application property value stored against a user.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PropertiesApi()
username = 'username_example' # str | The user.
app_key = 'app_key_example' # str | The key of the Connect app.
property_name = 'property_name_example' # str | The name of the property.

try:
    api_instance.delete_user_hosted_property_value(username, app_key, property_name)
except ApiException as e:
    print("Exception when calling PropertiesApi->delete_user_hosted_property_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The user. | 
 **app_key** | **str**| The key of the Connect app. | 
 **property_name** | **str**| The name of the property. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | An empty response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commit_hosted_property_value**
> get_commit_hosted_property_value(username, repo_slug, commit, app_key, property_name)



Retrieve an application property value stored against a commit.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PropertiesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
commit = 'commit_example' # str | The commit.
app_key = 'app_key_example' # str | The key of the Connect app.
property_name = 'property_name_example' # str | The name of the property.

try:
    api_instance.get_commit_hosted_property_value(username, repo_slug, commit, app_key, property_name)
except ApiException as e:
    print("Exception when calling PropertiesApi->get_commit_hosted_property_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **commit** | **str**| The commit. | 
 **app_key** | **str**| The key of the Connect app. | 
 **property_name** | **str**| The name of the property. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The value of the property. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pull_request_hosted_property_value**
> get_pull_request_hosted_property_value(username, repo_slug, pullrequest_id, app_key, property_name)



Retrieve an application property value stored against a pull request.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PropertiesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
pullrequest_id = 'pullrequest_id_example' # str | The pull request ID.
app_key = 'app_key_example' # str | The key of the Connect app.
property_name = 'property_name_example' # str | The name of the property.

try:
    api_instance.get_pull_request_hosted_property_value(username, repo_slug, pullrequest_id, app_key, property_name)
except ApiException as e:
    print("Exception when calling PropertiesApi->get_pull_request_hosted_property_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **pullrequest_id** | **str**| The pull request ID. | 
 **app_key** | **str**| The key of the Connect app. | 
 **property_name** | **str**| The name of the property. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The value of the property. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository_hosted_property_value**
> get_repository_hosted_property_value(username, repo_slug, app_key, property_name)



Retrieve an application property value stored against a repository.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PropertiesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
app_key = 'app_key_example' # str | The key of the Connect app.
property_name = 'property_name_example' # str | The name of the property.

try:
    api_instance.get_repository_hosted_property_value(username, repo_slug, app_key, property_name)
except ApiException as e:
    print("Exception when calling PropertiesApi->get_repository_hosted_property_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **app_key** | **str**| The key of the Connect app. | 
 **property_name** | **str**| The name of the property. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The value of the property. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_user_hosted_property_value**
> retrieve_user_hosted_property_value(username, app_key, property_name)



Retrieve an application property value stored against a user.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PropertiesApi()
username = 'username_example' # str | The user.
app_key = 'app_key_example' # str | The key of the Connect app.
property_name = 'property_name_example' # str | The name of the property.

try:
    api_instance.retrieve_user_hosted_property_value(username, app_key, property_name)
except ApiException as e:
    print("Exception when calling PropertiesApi->retrieve_user_hosted_property_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The user. | 
 **app_key** | **str**| The key of the Connect app. | 
 **property_name** | **str**| The name of the property. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The value of the property. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_commit_hosted_property_value**
> update_commit_hosted_property_value(username, repo_slug, commit, app_key, property_name)



Update an application property value stored against a commit.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PropertiesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
commit = 'commit_example' # str | The commit.
app_key = 'app_key_example' # str | The key of the Connect app.
property_name = 'property_name_example' # str | The name of the property.

try:
    api_instance.update_commit_hosted_property_value(username, repo_slug, commit, app_key, property_name)
except ApiException as e:
    print("Exception when calling PropertiesApi->update_commit_hosted_property_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **commit** | **str**| The commit. | 
 **app_key** | **str**| The key of the Connect app. | 
 **property_name** | **str**| The name of the property. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | An empty response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pull_request_hosted_property_value**
> update_pull_request_hosted_property_value(username, repo_slug, pullrequest_id, app_key, property_name)



Update an application property value stored against a pull request.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PropertiesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
pullrequest_id = 'pullrequest_id_example' # str | The pull request ID.
app_key = 'app_key_example' # str | The key of the Connect app.
property_name = 'property_name_example' # str | The name of the property.

try:
    api_instance.update_pull_request_hosted_property_value(username, repo_slug, pullrequest_id, app_key, property_name)
except ApiException as e:
    print("Exception when calling PropertiesApi->update_pull_request_hosted_property_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **pullrequest_id** | **str**| The pull request ID. | 
 **app_key** | **str**| The key of the Connect app. | 
 **property_name** | **str**| The name of the property. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | An empty response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository_hosted_property_value**
> update_repository_hosted_property_value(username, repo_slug, app_key, property_name)



Update an application property value stored against a repository.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PropertiesApi()
username = 'username_example' # str | The account.
repo_slug = 'repo_slug_example' # str | The repository.
app_key = 'app_key_example' # str | The key of the Connect app.
property_name = 'property_name_example' # str | The name of the property.

try:
    api_instance.update_repository_hosted_property_value(username, repo_slug, app_key, property_name)
except ApiException as e:
    print("Exception when calling PropertiesApi->update_repository_hosted_property_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account. | 
 **repo_slug** | **str**| The repository. | 
 **app_key** | **str**| The key of the Connect app. | 
 **property_name** | **str**| The name of the property. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | An empty response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_hosted_property_value**
> update_user_hosted_property_value(username, app_key, property_name)



Update an application property value stored against a user.

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.PropertiesApi()
username = 'username_example' # str | The user.
app_key = 'app_key_example' # str | The key of the Connect app.
property_name = 'property_name_example' # str | The name of the property.

try:
    api_instance.update_user_hosted_property_value(username, app_key, property_name)
except ApiException as e:
    print("Exception when calling PropertiesApi->update_user_hosted_property_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The user. | 
 **app_key** | **str**| The key of the Connect app. | 
 **property_name** | **str**| The name of the property. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | An empty response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


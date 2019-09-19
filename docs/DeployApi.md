# bitbucketopenapi.DeployApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_repositories_by_username_by_repo_slug_deploykeys**](DeployApi.md#create_repositories_by_username_by_repo_slug_deploykeys) | **POST** /repositories/{username}/{repo_slug}/deploy-keys | 
[**delete_repositories_by_username_by_repo_slug_deploykeys_by_key_id**](DeployApi.md#delete_repositories_by_username_by_repo_slug_deploykeys_by_key_id) | **DELETE** /repositories/{username}/{repo_slug}/deploy-keys/{key_id} | 
[**get_repositories_by_username_by_repo_slug_deploykeys**](DeployApi.md#get_repositories_by_username_by_repo_slug_deploykeys) | **GET** /repositories/{username}/{repo_slug}/deploy-keys | 
[**get_repositories_by_username_by_repo_slug_deploykeys_by_key_id**](DeployApi.md#get_repositories_by_username_by_repo_slug_deploykeys_by_key_id) | **GET** /repositories/{username}/{repo_slug}/deploy-keys/{key_id} | 
[**update_repositories_by_username_by_repo_slug_deploykeys_by_key_id**](DeployApi.md#update_repositories_by_username_by_repo_slug_deploykeys_by_key_id) | **PUT** /repositories/{username}/{repo_slug}/deploy-keys/{key_id} | 


# **create_repositories_by_username_by_repo_slug_deploykeys**
> DeployKey create_repositories_by_username_by_repo_slug_deploykeys(username, repo_slug)



Create a new deploy key in a repository.  Example: ``` $ curl -XPOST \\ -H \"Authorization <auth header>\" \\ -H \"Content-type: application/json\" \\ https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys -d \\ '{     \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5 mleu@C02W454JHTD8\",     \"label\": \"mydeploykey\" }'  Output: {     \"id\": 123,     \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5\",     \"label\": \"mydeploykey\",     \"type\": \"deploy_key\",     \"created_on\": \"2018-08-15T23:50:59.993890+00:00\",     \"repository\": {         \"full_name\": \"mleu/test\",         \"name\": \"test\",         \"type\": \"repository\",         \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"     },     \"links\":{         \"self\":{             \"href\": \"https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys/123\"         }     }     \"last_used\": null,     \"comment\": \"mleu@C02W454JHTD8\" } ```

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint
configuration = bitbucketopenapi.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bitbucketopenapi.Configuration()
# Configure HTTP basic authorization: basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = bitbucketopenapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bitbucket.org/2.0
configuration.host = "https://api.bitbucket.org/2.0"
# Create an instance of the API class
api_instance = bitbucketopenapi.DeployApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.create_repositories_by_username_by_repo_slug_deploykeys(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->create_repositories_by_username_by_repo_slug_deploykeys: %s\n" % e)
```

* Basic Authentication (basic):
```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint
configuration = bitbucketopenapi.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bitbucketopenapi.Configuration()
# Configure HTTP basic authorization: basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = bitbucketopenapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bitbucket.org/2.0
configuration.host = "https://api.bitbucket.org/2.0"
# Create an instance of the API class
api_instance = bitbucketopenapi.DeployApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.create_repositories_by_username_by_repo_slug_deploykeys(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->create_repositories_by_username_by_repo_slug_deploykeys: %s\n" % e)
```

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint
configuration = bitbucketopenapi.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bitbucketopenapi.Configuration()
# Configure HTTP basic authorization: basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = bitbucketopenapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bitbucket.org/2.0
configuration.host = "https://api.bitbucket.org/2.0"
# Create an instance of the API class
api_instance = bitbucketopenapi.DeployApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.create_repositories_by_username_by_repo_slug_deploykeys(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->create_repositories_by_username_by_repo_slug_deploykeys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deploy key that was created |  -  |
**400** | Invalid deploy key inputs |  -  |
**403** | If the specified user or repository is not accessible to the current user |  -  |
**404** | If the specified user or repository does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repositories_by_username_by_repo_slug_deploykeys_by_key_id**
> delete_repositories_by_username_by_repo_slug_deploykeys_by_key_id(username, key_id, repo_slug)



This deletes a deploy key from a repository.  Example: ``` $ curl -XDELETE \\ -H \"Authorization <auth header>\" \\ https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys/1234 ```

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint
configuration = bitbucketopenapi.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bitbucketopenapi.Configuration()
# Configure HTTP basic authorization: basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = bitbucketopenapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bitbucket.org/2.0
configuration.host = "https://api.bitbucket.org/2.0"
# Create an instance of the API class
api_instance = bitbucketopenapi.DeployApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
key_id = 'key_id_example' # str | The key ID matching the deploy key.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_instance.delete_repositories_by_username_by_repo_slug_deploykeys_by_key_id(username, key_id, repo_slug)
except ApiException as e:
    print("Exception when calling DeployApi->delete_repositories_by_username_by_repo_slug_deploykeys_by_key_id: %s\n" % e)
```

* Basic Authentication (basic):
```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint
configuration = bitbucketopenapi.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bitbucketopenapi.Configuration()
# Configure HTTP basic authorization: basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = bitbucketopenapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bitbucket.org/2.0
configuration.host = "https://api.bitbucket.org/2.0"
# Create an instance of the API class
api_instance = bitbucketopenapi.DeployApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
key_id = 'key_id_example' # str | The key ID matching the deploy key.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_instance.delete_repositories_by_username_by_repo_slug_deploykeys_by_key_id(username, key_id, repo_slug)
except ApiException as e:
    print("Exception when calling DeployApi->delete_repositories_by_username_by_repo_slug_deploykeys_by_key_id: %s\n" % e)
```

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint
configuration = bitbucketopenapi.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bitbucketopenapi.Configuration()
# Configure HTTP basic authorization: basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = bitbucketopenapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bitbucket.org/2.0
configuration.host = "https://api.bitbucket.org/2.0"
# Create an instance of the API class
api_instance = bitbucketopenapi.DeployApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
key_id = 'key_id_example' # str | The key ID matching the deploy key.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_instance.delete_repositories_by_username_by_repo_slug_deploykeys_by_key_id(username, key_id, repo_slug)
except ApiException as e:
    print("Exception when calling DeployApi->delete_repositories_by_username_by_repo_slug_deploykeys_by_key_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **key_id** | **str**| The key ID matching the deploy key. | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The key has been deleted |  -  |
**403** | If the current user does not have permission to delete a key for the specified user |  -  |
**404** | If the specified user, repository, or deploy key does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_deploykeys**
> PaginatedDeployKeys get_repositories_by_username_by_repo_slug_deploykeys(username, repo_slug)



Returns all deploy-keys belonging to a repository.  Example: ``` $ curl -H \"Authorization <auth header>\" \\ https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys  Output: {     \"pagelen\": 10,     \"values\": [         {             \"id\": 123,             \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5\",             \"label\": \"mykey\",             \"type\": \"deploy_key\",             \"created_on\": \"2018-08-15T23:50:59.993890+00:00\",             \"repository\": {                 \"full_name\": \"mleu/test\",                 \"name\": \"test\",                 \"type\": \"repository\",                 \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"             },             \"links\":{                 \"self\":{                     \"href\": \"https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys/123\"                 }             }             \"last_used\": null,             \"comment\": \"mleu@C02W454JHTD8\"         }     ],     \"page\": 1,     \"size\": 1 } ```

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint
configuration = bitbucketopenapi.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bitbucketopenapi.Configuration()
# Configure HTTP basic authorization: basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = bitbucketopenapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bitbucket.org/2.0
configuration.host = "https://api.bitbucket.org/2.0"
# Create an instance of the API class
api_instance = bitbucketopenapi.DeployApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_deploykeys(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_repositories_by_username_by_repo_slug_deploykeys: %s\n" % e)
```

* Basic Authentication (basic):
```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint
configuration = bitbucketopenapi.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bitbucketopenapi.Configuration()
# Configure HTTP basic authorization: basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = bitbucketopenapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bitbucket.org/2.0
configuration.host = "https://api.bitbucket.org/2.0"
# Create an instance of the API class
api_instance = bitbucketopenapi.DeployApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_deploykeys(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_repositories_by_username_by_repo_slug_deploykeys: %s\n" % e)
```

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint
configuration = bitbucketopenapi.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bitbucketopenapi.Configuration()
# Configure HTTP basic authorization: basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = bitbucketopenapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bitbucket.org/2.0
configuration.host = "https://api.bitbucket.org/2.0"
# Create an instance of the API class
api_instance = bitbucketopenapi.DeployApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_deploykeys(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_repositories_by_username_by_repo_slug_deploykeys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**PaginatedDeployKeys**](PaginatedDeployKeys.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deploy keys matching the repository |  -  |
**403** | If the specified user or repository is not accessible to the current user |  -  |
**404** | If the specified user or repository does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_deploykeys_by_key_id**
> DeployKey get_repositories_by_username_by_repo_slug_deploykeys_by_key_id(username, key_id, repo_slug)



Returns the deploy key belonging to a specific key.  Example: ``` $ curl -H \"Authorization <auth header>\" \\ https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-key/1234  Output: {     \"comment\": \"mleu@C02W454JHTD8\",     \"last_used\": null,     \"links\": {         \"self\": {             \"href\": https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-key/1234\"         }     },     \"repository\": {         \"full_name\": \"mleu/test\",         \"name\": \"test\",         \"type\": \"repository\",         \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"     },     \"label\": \"mykey\",     \"created_on\": \"2018-08-15T23:50:59.993890+00:00\",     \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5\",     \"id\": 1234,     \"type\": \"deploy_key\" } ```

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint
configuration = bitbucketopenapi.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bitbucketopenapi.Configuration()
# Configure HTTP basic authorization: basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = bitbucketopenapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bitbucket.org/2.0
configuration.host = "https://api.bitbucket.org/2.0"
# Create an instance of the API class
api_instance = bitbucketopenapi.DeployApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
key_id = 'key_id_example' # str | The key ID matching the deploy key.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_deploykeys_by_key_id(username, key_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_repositories_by_username_by_repo_slug_deploykeys_by_key_id: %s\n" % e)
```

* Basic Authentication (basic):
```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint
configuration = bitbucketopenapi.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bitbucketopenapi.Configuration()
# Configure HTTP basic authorization: basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = bitbucketopenapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bitbucket.org/2.0
configuration.host = "https://api.bitbucket.org/2.0"
# Create an instance of the API class
api_instance = bitbucketopenapi.DeployApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
key_id = 'key_id_example' # str | The key ID matching the deploy key.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_deploykeys_by_key_id(username, key_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_repositories_by_username_by_repo_slug_deploykeys_by_key_id: %s\n" % e)
```

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint
configuration = bitbucketopenapi.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bitbucketopenapi.Configuration()
# Configure HTTP basic authorization: basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = bitbucketopenapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bitbucket.org/2.0
configuration.host = "https://api.bitbucket.org/2.0"
# Create an instance of the API class
api_instance = bitbucketopenapi.DeployApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
key_id = 'key_id_example' # str | The key ID matching the deploy key.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_deploykeys_by_key_id(username, key_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_repositories_by_username_by_repo_slug_deploykeys_by_key_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **key_id** | **str**| The key ID matching the deploy key. | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deploy key matching the key ID |  -  |
**403** | If the specified user or repository is not accessible to the current user |  -  |
**404** | If the specified user or repository does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repositories_by_username_by_repo_slug_deploykeys_by_key_id**
> DeployKey update_repositories_by_username_by_repo_slug_deploykeys_by_key_id(username, key_id, repo_slug)



Create a new deploy key in a repository.  The same key needs to be passed in but the comment and label can change.  Example: ``` $ curl -XPUT \\ -H \"Authorization <auth header>\" \\ -H \"Content-type: application/json\" \\ https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys/1234 -d \\ '{     \"label\": \"newlabel\",     \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5 newcomment\", }'  Output: {     \"comment\": \"newcomment\",     \"last_used\": null,     \"links\": {         \"self\": {             \"href\": \"https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys/1234\"         }     },     \"repository\": {         \"full_name\": \"mleu/test\",         \"name\": \"test\",         \"type\": \"repository\",         \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"     },     \"label\": \"newlabel\",     \"created_on\": \"2018-08-15T23:50:59.993890+00:00\",     \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5\",     \"id\": 1234,     \"type\": \"deploy_key\" } ```

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint
configuration = bitbucketopenapi.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bitbucketopenapi.Configuration()
# Configure HTTP basic authorization: basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = bitbucketopenapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bitbucket.org/2.0
configuration.host = "https://api.bitbucket.org/2.0"
# Create an instance of the API class
api_instance = bitbucketopenapi.DeployApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
key_id = 'key_id_example' # str | The key ID matching the deploy key.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.update_repositories_by_username_by_repo_slug_deploykeys_by_key_id(username, key_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->update_repositories_by_username_by_repo_slug_deploykeys_by_key_id: %s\n" % e)
```

* Basic Authentication (basic):
```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint
configuration = bitbucketopenapi.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bitbucketopenapi.Configuration()
# Configure HTTP basic authorization: basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = bitbucketopenapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bitbucket.org/2.0
configuration.host = "https://api.bitbucket.org/2.0"
# Create an instance of the API class
api_instance = bitbucketopenapi.DeployApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
key_id = 'key_id_example' # str | The key ID matching the deploy key.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.update_repositories_by_username_by_repo_slug_deploykeys_by_key_id(username, key_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->update_repositories_by_username_by_repo_slug_deploykeys_by_key_id: %s\n" % e)
```

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint
configuration = bitbucketopenapi.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bitbucketopenapi.Configuration()
# Configure HTTP basic authorization: basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = bitbucketopenapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bitbucket.org/2.0
configuration.host = "https://api.bitbucket.org/2.0"
# Create an instance of the API class
api_instance = bitbucketopenapi.DeployApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
key_id = 'key_id_example' # str | The key ID matching the deploy key.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.update_repositories_by_username_by_repo_slug_deploykeys_by_key_id(username, key_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->update_repositories_by_username_by_repo_slug_deploykeys_by_key_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **key_id** | **str**| The key ID matching the deploy key. | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly updated deploy key. |  -  |
**400** | If the submitted key or related value is invalid |  -  |
**403** | If the current user does not have permission to add a key for the specified user |  -  |
**404** | If the specified user, repository, or deploy key does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


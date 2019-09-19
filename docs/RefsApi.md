# bitbucketopenapi.RefsApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_repositories_by_username_by_repo_slug_refs_branches**](RefsApi.md#create_repositories_by_username_by_repo_slug_refs_branches) | **POST** /repositories/{username}/{repo_slug}/refs/branches | 
[**create_repositories_by_username_by_repo_slug_refs_tags**](RefsApi.md#create_repositories_by_username_by_repo_slug_refs_tags) | **POST** /repositories/{username}/{repo_slug}/refs/tags | 
[**delete_repositories_by_username_by_repo_slug_refs_branches_by_name**](RefsApi.md#delete_repositories_by_username_by_repo_slug_refs_branches_by_name) | **DELETE** /repositories/{username}/{repo_slug}/refs/branches/{name} | 
[**delete_repositories_by_username_by_repo_slug_refs_tags_by_name**](RefsApi.md#delete_repositories_by_username_by_repo_slug_refs_tags_by_name) | **DELETE** /repositories/{username}/{repo_slug}/refs/tags/{name} | 
[**get_repositories_by_username_by_repo_slug_refs**](RefsApi.md#get_repositories_by_username_by_repo_slug_refs) | **GET** /repositories/{username}/{repo_slug}/refs | 
[**get_repositories_by_username_by_repo_slug_refs_branches**](RefsApi.md#get_repositories_by_username_by_repo_slug_refs_branches) | **GET** /repositories/{username}/{repo_slug}/refs/branches | 
[**get_repositories_by_username_by_repo_slug_refs_branches_by_name**](RefsApi.md#get_repositories_by_username_by_repo_slug_refs_branches_by_name) | **GET** /repositories/{username}/{repo_slug}/refs/branches/{name} | 
[**get_repositories_by_username_by_repo_slug_refs_tags**](RefsApi.md#get_repositories_by_username_by_repo_slug_refs_tags) | **GET** /repositories/{username}/{repo_slug}/refs/tags | 
[**get_repositories_by_username_by_repo_slug_refs_tags_by_name**](RefsApi.md#get_repositories_by_username_by_repo_slug_refs_tags_by_name) | **GET** /repositories/{username}/{repo_slug}/refs/tags/{name} | 


# **create_repositories_by_username_by_repo_slug_refs_branches**
> Branch create_repositories_by_username_by_repo_slug_refs_branches(username, repo_slug)



Creates a new branch in the specified repository.  The payload of the POST should consist of a JSON document that contains the name of the tag and the target hash.  ``` curl https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/branches \\ -s -u seanfarley -X POST -H \"Content-Type: application/json\" \\ -d '{     \"name\" : \"smf/create-feature\",     \"target\" : {         \"hash\" : \"default\",     } }' ```  This call requires authentication. Private repositories require the caller to authenticate with an account that has appropriate authorization.  For Git, the branch name should not include any prefixes (e.g. refs/heads). This endpoint does support using short hash prefixes for the commit hash, but it may return a 400 response if the provided prefix is ambiguous. Using a full commit hash is the preferred approach.  For Mercurial, the authenticated user making this call is the author of the new branch commit and the date is current datetime of the call.

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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.create_repositories_by_username_by_repo_slug_refs_branches(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->create_repositories_by_username_by_repo_slug_refs_branches: %s\n" % e)
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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.create_repositories_by_username_by_repo_slug_refs_branches(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->create_repositories_by_username_by_repo_slug_refs_branches: %s\n" % e)
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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.create_repositories_by_username_by_repo_slug_refs_branches(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->create_repositories_by_username_by_repo_slug_refs_branches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**Branch**](Branch.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created branch object. |  -  |
**403** | If the repository is private and the authenticated user does not have access to it.  |  -  |
**404** | The specified repository or branch does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repositories_by_username_by_repo_slug_refs_tags**
> Tag create_repositories_by_username_by_repo_slug_refs_tags(username, repo_slug, body)



Creates a new tag in the specified repository.  The payload of the POST should consist of a JSON document that contains the name of the tag and the target hash.  ``` curl https://api.bitbucket.org/2.0/repositories/jdoe/myrepo/refs/tags \\ -s -u jdoe -X POST -H \"Content-Type: application/json\" \\ -d '{     \"name\" : \"new-tag-name\",     \"target\" : {         \"hash\" : \"a1b2c3d4e5f6\",     } }' ```  This endpoint does support using short hash prefixes for the commit hash, but it may return a 400 response if the provided prefix is ambiguous. Using a full commit hash is the preferred approach.

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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
body = bitbucketopenapi.Tag() # Tag | 

try:
    api_response = api_instance.create_repositories_by_username_by_repo_slug_refs_tags(username, repo_slug, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->create_repositories_by_username_by_repo_slug_refs_tags: %s\n" % e)
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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
body = bitbucketopenapi.Tag() # Tag | 

try:
    api_response = api_instance.create_repositories_by_username_by_repo_slug_refs_tags(username, repo_slug, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->create_repositories_by_username_by_repo_slug_refs_tags: %s\n" % e)
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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
body = bitbucketopenapi.Tag() # Tag | 

try:
    api_response = api_instance.create_repositories_by_username_by_repo_slug_refs_tags(username, repo_slug, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->create_repositories_by_username_by_repo_slug_refs_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **body** | [**Tag**](Tag.md)|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created tag. |  -  |
**400** | If the target hash is missing, ambiguous, or invalid, or if the name is not provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repositories_by_username_by_repo_slug_refs_branches_by_name**
> delete_repositories_by_username_by_repo_slug_refs_branches_by_name(username, name, repo_slug)



Delete a branch in the specified repository.  The main branch is not allowed to be deleted and will return a 400 response.  For Git, the branch name should not include any prefixes (e.g. refs/heads). For Mercurial, this closes all open heads on the branch, sets the author of the commit to the authenticated caller, and changes the date to the datetime of the call.

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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
name = 'name_example' # str | The name of the branch.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_instance.delete_repositories_by_username_by_repo_slug_refs_branches_by_name(username, name, repo_slug)
except ApiException as e:
    print("Exception when calling RefsApi->delete_repositories_by_username_by_repo_slug_refs_branches_by_name: %s\n" % e)
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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
name = 'name_example' # str | The name of the branch.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_instance.delete_repositories_by_username_by_repo_slug_refs_branches_by_name(username, name, repo_slug)
except ApiException as e:
    print("Exception when calling RefsApi->delete_repositories_by_username_by_repo_slug_refs_branches_by_name: %s\n" % e)
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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
name = 'name_example' # str | The name of the branch.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_instance.delete_repositories_by_username_by_repo_slug_refs_branches_by_name(username, name, repo_slug)
except ApiException as e:
    print("Exception when calling RefsApi->delete_repositories_by_username_by_repo_slug_refs_branches_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **name** | **str**| The name of the branch. | 
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
**204** | Indicates that the specified branch was successfully deleted. |  -  |
**403** | If the repository is private and the authenticated user does not have access to it.  |  -  |
**404** | The specified repository or branch does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repositories_by_username_by_repo_slug_refs_tags_by_name**
> delete_repositories_by_username_by_repo_slug_refs_tags_by_name(username, name, repo_slug)



Delete a tag in the specified repository.  For Git, the tag name should not include any prefixes (e.g. refs/tags). For Mercurial, this adds a commit to the main branch that removes the specified tag.

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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
name = 'name_example' # str | The name of the tag.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_instance.delete_repositories_by_username_by_repo_slug_refs_tags_by_name(username, name, repo_slug)
except ApiException as e:
    print("Exception when calling RefsApi->delete_repositories_by_username_by_repo_slug_refs_tags_by_name: %s\n" % e)
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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
name = 'name_example' # str | The name of the tag.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_instance.delete_repositories_by_username_by_repo_slug_refs_tags_by_name(username, name, repo_slug)
except ApiException as e:
    print("Exception when calling RefsApi->delete_repositories_by_username_by_repo_slug_refs_tags_by_name: %s\n" % e)
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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
name = 'name_example' # str | The name of the tag.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_instance.delete_repositories_by_username_by_repo_slug_refs_tags_by_name(username, name, repo_slug)
except ApiException as e:
    print("Exception when calling RefsApi->delete_repositories_by_username_by_repo_slug_refs_tags_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **name** | **str**| The name of the tag. | 
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
**204** | Indicates the specified tag was successfully deleted. |  -  |
**403** | If the repository is private and the authenticated user does not have access to it.  |  -  |
**404** | The specified repository or tag does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_refs**
> PaginatedRefs get_repositories_by_username_by_repo_slug_refs(username, repo_slug, q=q, sort=sort)



Returns the branches and tags in the repository.  By default, results will be in the order the underlying source control system returns them and identical to the ordering one sees when running \"$ git show-ref\". Note that this follows simple lexical ordering of the ref names.  This can be undesirable as it does apply any natural sorting semantics, meaning for instance that refs are sorted [\"branch1\", \"branch10\", \"branch2\", \"v10\", \"v11\", \"v9\"] instead of [\"branch1\", \"branch2\", \"branch10\", \"v9\", \"v10\", \"v11\"].  Sorting can be changed using the ?sort= query parameter. When using ?sort=name to explicitly sort on ref name, Bitbucket will apply natural sorting and interpret numerical values as numbers instead of strings.

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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str |  This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str |  This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Field by which the results should be sorted as per [filtering and sorting](../../../../../../meta/filtering). The `name` field is handled specially for refs in that, if specified as the sort field, it uses a natural sort order instead of the default lexicographical sort order. For example, it will return ['1.1', '1.2', '1.10'] instead of ['1.1', '1.10', '1.2']. (optional)

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_refs(username, repo_slug, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->get_repositories_by_username_by_repo_slug_refs: %s\n" % e)
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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str |  This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str |  This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Field by which the results should be sorted as per [filtering and sorting](../../../../../../meta/filtering). The `name` field is handled specially for refs in that, if specified as the sort field, it uses a natural sort order instead of the default lexicographical sort order. For example, it will return ['1.1', '1.2', '1.10'] instead of ['1.1', '1.10', '1.2']. (optional)

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_refs(username, repo_slug, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->get_repositories_by_username_by_repo_slug_refs: %s\n" % e)
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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str |  This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str |  This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Field by which the results should be sorted as per [filtering and sorting](../../../../../../meta/filtering). The `name` field is handled specially for refs in that, if specified as the sort field, it uses a natural sort order instead of the default lexicographical sort order. For example, it will return ['1.1', '1.2', '1.10'] instead of ['1.1', '1.10', '1.2']. (optional)

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_refs(username, repo_slug, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->get_repositories_by_username_by_repo_slug_refs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  This can either be the username or the UUID of the user, surrounded by curly-braces, for example: &#x60;{user UUID}&#x60;.  | 
 **repo_slug** | **str**|  This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **q** | **str**|  Query string to narrow down the response as per [filtering and sorting](../../../../../../meta/filtering). | [optional] 
 **sort** | **str**|  Field by which the results should be sorted as per [filtering and sorting](../../../../../../meta/filtering). The &#x60;name&#x60; field is handled specially for refs in that, if specified as the sort field, it uses a natural sort order instead of the default lexicographical sort order. For example, it will return [&#39;1.1&#39;, &#39;1.2&#39;, &#39;1.10&#39;] instead of [&#39;1.1&#39;, &#39;1.10&#39;, &#39;1.2&#39;]. | [optional] 

### Return type

[**PaginatedRefs**](PaginatedRefs.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of refs matching any filter criteria that were provided. |  -  |
**403** | If the repository is private and the authenticated user does not have access to it.  |  -  |
**404** | The specified repository does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_refs_branches**
> PaginatedBranches get_repositories_by_username_by_repo_slug_refs_branches(username, repo_slug, q=q, sort=sort)



Returns a list of all open branches within the specified repository. Results will be in the order the source control manager returns them.  ``` $ curl -s https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/refs/branches | jq . {   \"pagelen\": 10,   \"values\": [     {       \"heads\": [         {           \"hash\": \"f1a0933ce59e809f190602655e22ae6ec107c397\",           \"type\": \"commit\",           \"links\": {             \"self\": {               \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commit/f1a0933ce59e809f190602655e22ae6ec107c397\"             },             \"html\": {               \"href\": \"https://bitbucket.org/seanfarley/mercurial/commits/f1a0933ce59e809f190602655e22ae6ec107c397\"             }           }         }       ],       \"type\": \"named_branch\",       \"name\": \"default\",       \"links\": {         \"commits\": {           \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commits/default\"         },         \"self\": {           \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/refs/branches/default\"         },         \"html\": {           \"href\": \"https://bitbucket.org/seanfarley/mercurial/branch/default\"         }       },       \"target\": {         \"hash\": \"f1a0933ce59e809f190602655e22ae6ec107c397\",         \"repository\": {           \"links\": {             \"self\": {               \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial\"             },             \"html\": {               \"href\": \"https://bitbucket.org/seanfarley/mercurial\"             },             \"avatar\": {               \"href\": \"https://bitbucket.org/seanfarley/mercurial/avatar/32/\"             }           },           \"type\": \"repository\",           \"name\": \"mercurial\",           \"full_name\": \"seanfarley/mercurial\",           \"uuid\": \"{73dcbd61-e506-4fc1-9ecd-31be2b6d6031}\"         },         \"links\": {           \"self\": {             \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commit/f1a0933ce59e809f190602655e22ae6ec107c397\"           },           \"comments\": {             \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commit/f1a0933ce59e809f190602655e22ae6ec107c397/comments\"           },           \"patch\": {             \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/patch/f1a0933ce59e809f190602655e22ae6ec107c397\"           },           \"html\": {             \"href\": \"https://bitbucket.org/seanfarley/mercurial/commits/f1a0933ce59e809f190602655e22ae6ec107c397\"           },           \"diff\": {             \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/diff/f1a0933ce59e809f190602655e22ae6ec107c397\"           },           \"approve\": {             \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commit/f1a0933ce59e809f190602655e22ae6ec107c397/approve\"           },           \"statuses\": {             \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commit/f1a0933ce59e809f190602655e22ae6ec107c397/statuses\"           }         },         \"author\": {           \"raw\": \"Martin von Zweigbergk <martinvonz@google.com>\",           \"type\": \"author\",           \"user\": {             \"username\": \"martinvonz\",             \"nickname\": \"martinvonz\",             \"display_name\": \"Martin von Zweigbergk\",             \"type\": \"user\",             \"uuid\": \"{fdb0e657-3ade-4fad-a136-95f1ffe4a5ac}\",             \"links\": {               \"self\": {                 \"href\": \"https://api.bitbucket.org/2.0/users/martinvonz\"               },               \"html\": {                 \"href\": \"https://bitbucket.org/martinvonz/\"               },               \"avatar\": {                 \"href\": \"https://bitbucket.org/account/martinvonz/avatar/32/\"               }             }           }         },         \"parents\": [           {             \"hash\": \"5523aabb85c30ebc2b8e29aadcaf5e13fa92b375\",             \"type\": \"commit\",             \"links\": {               \"self\": {                 \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commit/5523aabb85c30ebc2b8e29aadcaf5e13fa92b375\"               },               \"html\": {                 \"href\": \"https://bitbucket.org/seanfarley/mercurial/commits/5523aabb85c30ebc2b8e29aadcaf5e13fa92b375\"               }             }           }         ],         \"date\": \"2018-02-01T18:44:49+00:00\",         \"message\": \"config: replace a for-else by any()\",         \"type\": \"commit\"       }     },     {       \"heads\": [         {           \"hash\": \"1d60ad093792706e1dc7a52b20942593f2c19655\",           \"type\": \"commit\",           \"links\": {             \"self\": {               \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commit/1d60ad093792706e1dc7a52b20942593f2c19655\"             },             \"html\": {               \"href\": \"https://bitbucket.org/seanfarley/mercurial/commits/1d60ad093792706e1dc7a52b20942593f2c19655\"             }           }         }       ],       \"type\": \"named_branch\",       \"name\": \"stable\",       \"links\": {         \"commits\": {           \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commits/stable\"         },         \"self\": {           \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/refs/branches/stable\"         },         \"html\": {           \"href\": \"https://bitbucket.org/seanfarley/mercurial/branch/stable\"         }       },       \"target\": {         \"hash\": \"1d60ad093792706e1dc7a52b20942593f2c19655\",         \"repository\": {           \"links\": {             \"self\": {               \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial\"             },             \"html\": {               \"href\": \"https://bitbucket.org/seanfarley/mercurial\"             },             \"avatar\": {               \"href\": \"https://bitbucket.org/seanfarley/mercurial/avatar/32/\"             }           },           \"type\": \"repository\",           \"name\": \"mercurial\",           \"full_name\": \"seanfarley/mercurial\",           \"uuid\": \"{73dcbd61-e506-4fc1-9ecd-31be2b6d6031}\"         },         \"links\": {           \"self\": {             \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commit/1d60ad093792706e1dc7a52b20942593f2c19655\"           },           \"comments\": {             \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commit/1d60ad093792706e1dc7a52b20942593f2c19655/comments\"           },           \"patch\": {             \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/patch/1d60ad093792706e1dc7a52b20942593f2c19655\"           },           \"html\": {             \"href\": \"https://bitbucket.org/seanfarley/mercurial/commits/1d60ad093792706e1dc7a52b20942593f2c19655\"           },           \"diff\": {             \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/diff/1d60ad093792706e1dc7a52b20942593f2c19655\"           },           \"approve\": {             \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commit/1d60ad093792706e1dc7a52b20942593f2c19655/approve\"           },           \"statuses\": {             \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commit/1d60ad093792706e1dc7a52b20942593f2c19655/statuses\"           }         },         \"author\": {           \"raw\": \"Augie Fackler <raf@durin42.com>\",           \"type\": \"author\",           \"user\": {             \"username\": \"durin42\",             \"nickname\": \"durin42\",             \"display_name\": \"Augie Fackler\",             \"type\": \"user\",             \"uuid\": \"{e07dc61f-bb05-4218-b43a-d991f26be65a}\",             \"links\": {               \"self\": {                 \"href\": \"https://api.bitbucket.org/2.0/users/durin42\"               },               \"html\": {                 \"href\": \"https://bitbucket.org/durin42/\"               },               \"avatar\": {                 \"href\": \"https://bitbucket.org/account/durin42/avatar/32/\"               }             }           }         },         \"parents\": [           {             \"hash\": \"56a0da11bde519d79168e890df4bcf0da62f0a7b\",             \"type\": \"commit\",             \"links\": {               \"self\": {                 \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commit/56a0da11bde519d79168e890df4bcf0da62f0a7b\"               },               \"html\": {                 \"href\": \"https://bitbucket.org/seanfarley/mercurial/commits/56a0da11bde519d79168e890df4bcf0da62f0a7b\"               }             }           }         ],         \"date\": \"2018-02-01T19:13:41+00:00\",         \"message\": \"Added signature for changeset d334afc585e2\",         \"type\": \"commit\"       }     }   ],   \"page\": 1,   \"size\": 2 } ```  Branches support [filtering and sorting](../../../../../meta/filtering) that can be used to search for specific branches. For instance, to find all branches that have \"stab\" in their name:  ``` curl -s https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/refs/branches -G --data-urlencode 'q=name ~ \"stab\"' ```  By default, results will be in the order the underlying source control system returns them and identical to the ordering one sees when running \"$ hg branches\" or \"$ git branch --list\". Note that this follows simple lexical ordering of the ref names.  This can be undesirable as it does apply any natural sorting semantics, meaning for instance that tags are sorted [\"v10\", \"v11\", \"v9\"] instead of [\"v9\", \"v10\", \"v11\"].  Sorting can be changed using the ?q= query parameter. When using ?q=name to explicitly sort on ref name, Bitbucket will apply natural sorting and interpret numerical values as numbers instead of strings.

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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str |  This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str |  This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Field by which the results should be sorted as per [filtering and sorting](../../../../../../meta/filtering). The `name` field is handled specially for branches in that, if specified as the sort field, it uses a natural sort order instead of the default lexicographical sort order. For example, it will return ['branch1', 'branch2', 'branch10'] instead of ['branch1', 'branch10', 'branch2']. (optional)

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_refs_branches(username, repo_slug, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->get_repositories_by_username_by_repo_slug_refs_branches: %s\n" % e)
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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str |  This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str |  This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Field by which the results should be sorted as per [filtering and sorting](../../../../../../meta/filtering). The `name` field is handled specially for branches in that, if specified as the sort field, it uses a natural sort order instead of the default lexicographical sort order. For example, it will return ['branch1', 'branch2', 'branch10'] instead of ['branch1', 'branch10', 'branch2']. (optional)

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_refs_branches(username, repo_slug, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->get_repositories_by_username_by_repo_slug_refs_branches: %s\n" % e)
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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str |  This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str |  This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Field by which the results should be sorted as per [filtering and sorting](../../../../../../meta/filtering). The `name` field is handled specially for branches in that, if specified as the sort field, it uses a natural sort order instead of the default lexicographical sort order. For example, it will return ['branch1', 'branch2', 'branch10'] instead of ['branch1', 'branch10', 'branch2']. (optional)

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_refs_branches(username, repo_slug, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->get_repositories_by_username_by_repo_slug_refs_branches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  This can either be the username or the UUID of the user, surrounded by curly-braces, for example: &#x60;{user UUID}&#x60;.  | 
 **repo_slug** | **str**|  This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **q** | **str**|  Query string to narrow down the response as per [filtering and sorting](../../../../../../meta/filtering). | [optional] 
 **sort** | **str**|  Field by which the results should be sorted as per [filtering and sorting](../../../../../../meta/filtering). The &#x60;name&#x60; field is handled specially for branches in that, if specified as the sort field, it uses a natural sort order instead of the default lexicographical sort order. For example, it will return [&#39;branch1&#39;, &#39;branch2&#39;, &#39;branch10&#39;] instead of [&#39;branch1&#39;, &#39;branch10&#39;, &#39;branch2&#39;]. | [optional] 

### Return type

[**PaginatedBranches**](PaginatedBranches.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of branches matching any filter criteria that were provided. |  -  |
**403** | If the repository is private and the authenticated user does not have access to it.  |  -  |
**404** | The specified repository does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_refs_branches_by_name**
> Branch get_repositories_by_username_by_repo_slug_refs_branches_by_name(username, name, repo_slug)



Returns a branch object within the specified repository.  ``` $ curl -s https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/refs/branches/default | jq . {   \"heads\": [     {       \"hash\": \"f1a0933ce59e809f190602655e22ae6ec107c397\",       \"type\": \"commit\",       \"links\": {         \"self\": {           \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commit/f1a0933ce59e809f190602655e22ae6ec107c397\"         },         \"html\": {           \"href\": \"https://bitbucket.org/seanfarley/mercurial/commits/f1a0933ce59e809f190602655e22ae6ec107c397\"         }       }     }   ],   \"type\": \"named_branch\",   \"name\": \"default\",   \"links\": {     \"commits\": {       \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commits/default\"     },     \"self\": {       \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/refs/branches/default\"     },     \"html\": {       \"href\": \"https://bitbucket.org/seanfarley/mercurial/branch/default\"     }   },   \"target\": {     \"hash\": \"f1a0933ce59e809f190602655e22ae6ec107c397\",     \"repository\": {       \"links\": {         \"self\": {           \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial\"         },         \"html\": {           \"href\": \"https://bitbucket.org/seanfarley/mercurial\"         },         \"avatar\": {           \"href\": \"https://bitbucket.org/seanfarley/mercurial/avatar/32/\"         }       },       \"type\": \"repository\",       \"name\": \"mercurial\",       \"full_name\": \"seanfarley/mercurial\",       \"uuid\": \"{73dcbd61-e506-4fc1-9ecd-31be2b6d6031}\"     },     \"links\": {       \"self\": {         \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commit/f1a0933ce59e809f190602655e22ae6ec107c397\"       },       \"comments\": {         \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commit/f1a0933ce59e809f190602655e22ae6ec107c397/comments\"       },       \"patch\": {         \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/patch/f1a0933ce59e809f190602655e22ae6ec107c397\"       },       \"html\": {         \"href\": \"https://bitbucket.org/seanfarley/mercurial/commits/f1a0933ce59e809f190602655e22ae6ec107c397\"       },       \"diff\": {         \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/diff/f1a0933ce59e809f190602655e22ae6ec107c397\"       },       \"approve\": {         \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commit/f1a0933ce59e809f190602655e22ae6ec107c397/approve\"       },       \"statuses\": {         \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commit/f1a0933ce59e809f190602655e22ae6ec107c397/statuses\"       }     },     \"author\": {       \"raw\": \"Martin von Zweigbergk <martinvonz@google.com>\",       \"type\": \"author\",       \"user\": {         \"username\": \"martinvonz\",         \"nickname\": \"martinvonz\",         \"display_name\": \"Martin von Zweigbergk\",         \"type\": \"user\",         \"uuid\": \"{fdb0e657-3ade-4fad-a136-95f1ffe4a5ac}\",         \"links\": {           \"self\": {             \"href\": \"https://api.bitbucket.org/2.0/users/martinvonz\"           },           \"html\": {             \"href\": \"https://bitbucket.org/martinvonz/\"           },           \"avatar\": {             \"href\": \"https://bitbucket.org/account/martinvonz/avatar/32/\"           }         }       }     },     \"parents\": [       {         \"hash\": \"5523aabb85c30ebc2b8e29aadcaf5e13fa92b375\",         \"type\": \"commit\",         \"links\": {           \"self\": {             \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/mercurial/commit/5523aabb85c30ebc2b8e29aadcaf5e13fa92b375\"           },           \"html\": {             \"href\": \"https://bitbucket.org/seanfarley/mercurial/commits/5523aabb85c30ebc2b8e29aadcaf5e13fa92b375\"           }         }       }     ],     \"date\": \"2018-02-01T18:44:49+00:00\",     \"message\": \"config: replace a for-else by any()\",     \"type\": \"commit\"   } } ```  This call requires authentication. Private repositories require the caller to authenticate with an account that has appropriate authorization.  For Git, the branch name should not include any prefixes (e.g. refs/heads).  For Mercurial, the response will include an additional field that lists the open heads.

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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
name = 'name_example' # str | The name of the branch.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_refs_branches_by_name(username, name, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->get_repositories_by_username_by_repo_slug_refs_branches_by_name: %s\n" % e)
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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
name = 'name_example' # str | The name of the branch.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_refs_branches_by_name(username, name, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->get_repositories_by_username_by_repo_slug_refs_branches_by_name: %s\n" % e)
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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
name = 'name_example' # str | The name of the branch.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_refs_branches_by_name(username, name, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->get_repositories_by_username_by_repo_slug_refs_branches_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **name** | **str**| The name of the branch. | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**Branch**](Branch.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The branch object. |  -  |
**403** | If the repository is private and the authenticated user does not have access to it.  |  -  |
**404** | The specified repository or branch does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_refs_tags**
> PaginatedTags get_repositories_by_username_by_repo_slug_refs_tags(username, repo_slug, q=q, sort=sort)



Returns the tags in the repository.  By default, results will be in the order the underlying source control system returns them and identical to the ordering one sees when running \"$ hg tags\" or \"$ git tag --list\". Note that this follows simple lexical ordering of the ref names.  This can be undesirable as it does apply any natural sorting semantics, meaning for instance that tags are sorted [\"v10\", \"v11\", \"v9\"] instead of [\"v9\", \"v10\", \"v11\"].  Sorting can be changed using the ?sort= query parameter. When using ?sort=name to explicitly sort on ref name, Bitbucket will apply natural sorting and interpret numerical values as numbers instead of strings.

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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str |  This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str |  This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Field by which the results should be sorted as per [filtering and sorting](../../../../../../meta/filtering). The `name` field is handled specially for tags in that, if specified as the sort field, it uses a natural sort order instead of the default lexicographical sort order. For example, it will return ['1.1', '1.2', '1.10'] instead of ['1.1', '1.10', '1.2']. (optional)

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_refs_tags(username, repo_slug, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->get_repositories_by_username_by_repo_slug_refs_tags: %s\n" % e)
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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str |  This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str |  This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Field by which the results should be sorted as per [filtering and sorting](../../../../../../meta/filtering). The `name` field is handled specially for tags in that, if specified as the sort field, it uses a natural sort order instead of the default lexicographical sort order. For example, it will return ['1.1', '1.2', '1.10'] instead of ['1.1', '1.10', '1.2']. (optional)

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_refs_tags(username, repo_slug, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->get_repositories_by_username_by_repo_slug_refs_tags: %s\n" % e)
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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str |  This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str |  This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Field by which the results should be sorted as per [filtering and sorting](../../../../../../meta/filtering). The `name` field is handled specially for tags in that, if specified as the sort field, it uses a natural sort order instead of the default lexicographical sort order. For example, it will return ['1.1', '1.2', '1.10'] instead of ['1.1', '1.10', '1.2']. (optional)

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_refs_tags(username, repo_slug, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->get_repositories_by_username_by_repo_slug_refs_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  This can either be the username or the UUID of the user, surrounded by curly-braces, for example: &#x60;{user UUID}&#x60;.  | 
 **repo_slug** | **str**|  This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **q** | **str**|  Query string to narrow down the response as per [filtering and sorting](../../../../../../meta/filtering). | [optional] 
 **sort** | **str**|  Field by which the results should be sorted as per [filtering and sorting](../../../../../../meta/filtering). The &#x60;name&#x60; field is handled specially for tags in that, if specified as the sort field, it uses a natural sort order instead of the default lexicographical sort order. For example, it will return [&#39;1.1&#39;, &#39;1.2&#39;, &#39;1.10&#39;] instead of [&#39;1.1&#39;, &#39;1.10&#39;, &#39;1.2&#39;]. | [optional] 

### Return type

[**PaginatedTags**](PaginatedTags.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of tags matching any filter criteria that were provided. |  -  |
**403** | If the repository is private and the authenticated user does not have access to it.  |  -  |
**404** | The specified repository does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_refs_tags_by_name**
> Tag get_repositories_by_username_by_repo_slug_refs_tags_by_name(username, name, repo_slug)



Returns the specified tag.  ``` $ curl -s https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8 -G | jq . {   \"name\": \"3.8\",   \"links\": {     \"commits\": {       \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commits/3.8\"     },     \"self\": {       \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8\"     },     \"html\": {       \"href\": \"https://bitbucket.org/seanfarley/hg/commits/tag/3.8\"     }   },   \"tagger\": {     \"raw\": \"Matt Mackall <mpm@selenic.com>\",     \"type\": \"author\",     \"user\": {       \"username\": \"mpmselenic\",       \"nickname\": \"mpmselenic\",       \"display_name\": \"Matt Mackall\",       \"type\": \"user\",       \"uuid\": \"{a4934530-db4c-419c-a478-9ab4964c2ee7}\",       \"links\": {         \"self\": {           \"href\": \"https://api.bitbucket.org/2.0/users/mpmselenic\"         },         \"html\": {           \"href\": \"https://bitbucket.org/mpmselenic/\"         },         \"avatar\": {           \"href\": \"https://bitbucket.org/account/mpmselenic/avatar/32/\"         }       }     }   },   \"date\": \"2016-05-01T18:52:25+00:00\",   \"message\": \"Added tag 3.8 for changeset f85de28eae32\",   \"type\": \"tag\",   \"target\": {     \"hash\": \"f85de28eae32e7d3064b1a1321309071bbaaa069\",     \"repository\": {       \"links\": {         \"self\": {           \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg\"         },         \"html\": {           \"href\": \"https://bitbucket.org/seanfarley/hg\"         },         \"avatar\": {           \"href\": \"https://bitbucket.org/seanfarley/hg/avatar/32/\"         }       },       \"type\": \"repository\",       \"name\": \"hg\",       \"full_name\": \"seanfarley/hg\",       \"uuid\": \"{c75687fb-e99d-4579-9087-190dbd406d30}\"     },     \"links\": {       \"self\": {         \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3064b1a1321309071bbaaa069\"       },       \"comments\": {         \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3064b1a1321309071bbaaa069/comments\"       },       \"patch\": {         \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/patch/f85de28eae32e7d3064b1a1321309071bbaaa069\"       },       \"html\": {         \"href\": \"https://bitbucket.org/seanfarley/hg/commits/f85de28eae32e7d3064b1a1321309071bbaaa069\"       },       \"diff\": {         \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/diff/f85de28eae32e7d3064b1a1321309071bbaaa069\"       },       \"approve\": {         \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3064b1a1321309071bbaaa069/approve\"       },       \"statuses\": {         \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3064b1a1321309071bbaaa069/statuses\"       }     },     \"author\": {       \"raw\": \"Sean Farley <sean@farley.io>\",       \"type\": \"author\",       \"user\": {         \"username\": \"seanfarley\",         \"nickname\": \"seanfarley\",         \"display_name\": \"Sean Farley\",         \"type\": \"user\",         \"uuid\": \"{a295f8a8-5876-4d43-89b5-3ad8c6c3c51d}\",         \"links\": {           \"self\": {             \"href\": \"https://api.bitbucket.org/2.0/users/seanfarley\"           },           \"html\": {             \"href\": \"https://bitbucket.org/seanfarley/\"           },           \"avatar\": {             \"href\": \"https://bitbucket.org/account/seanfarley/avatar/32/\"           }         }       }     },     \"parents\": [       {         \"hash\": \"9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\",         \"type\": \"commit\",         \"links\": {           \"self\": {             \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\"           },           \"html\": {             \"href\": \"https://bitbucket.org/seanfarley/hg/commits/9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\"           }         }       }     ],     \"date\": \"2016-05-01T04:21:17+00:00\",     \"message\": \"debian: alphabetize build deps\",     \"type\": \"commit\"   } } ```

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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
name = 'name_example' # str | The name of the tag.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_refs_tags_by_name(username, name, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->get_repositories_by_username_by_repo_slug_refs_tags_by_name: %s\n" % e)
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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
name = 'name_example' # str | The name of the tag.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_refs_tags_by_name(username, name, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->get_repositories_by_username_by_repo_slug_refs_tags_by_name: %s\n" % e)
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
api_instance = bitbucketopenapi.RefsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
name = 'name_example' # str | The name of the tag.
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_refs_tags_by_name(username, name, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefsApi->get_repositories_by_username_by_repo_slug_refs_tags_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **name** | **str**| The name of the tag. | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tag object. |  -  |
**403** | If the repository is private and the authenticated user does not have access to it.  |  -  |
**404** | The specified repository or tag does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


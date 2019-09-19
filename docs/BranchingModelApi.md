# bitbucketopenapi.BranchingModelApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_repositories_by_username_by_repo_slug_branchingmodel**](BranchingModelApi.md#get_repositories_by_username_by_repo_slug_branchingmodel) | **GET** /repositories/{username}/{repo_slug}/branching-model | 
[**get_repositories_by_username_by_repo_slug_branchingmodel_settings**](BranchingModelApi.md#get_repositories_by_username_by_repo_slug_branchingmodel_settings) | **GET** /repositories/{username}/{repo_slug}/branching-model/settings | 
[**update_repositories_by_username_by_repo_slug_branchingmodel_settings**](BranchingModelApi.md#update_repositories_by_username_by_repo_slug_branchingmodel_settings) | **PUT** /repositories/{username}/{repo_slug}/branching-model/settings | 


# **get_repositories_by_username_by_repo_slug_branchingmodel**
> BranchingModel get_repositories_by_username_by_repo_slug_branchingmodel(username, repo_slug)



Return the branching model as applied to the repository. This view is read-only. The branching model settings can be changed using the [settings](branching-model/settings#get) API.  The returned object:  1. Always has a `development` property. `development.branch` contains    the actual repository branch object that is considered to be the    `development` branch. `development.branch` will not be present    if it does not exist. 2. Might have a `production` property. `production` will not    be present when `production` is disabled.    `production.branch` contains the actual branch object that is    considered to be the `production` branch. `production.branch` will    not be present if it does not exist. 3. Always has a `branch_types` array which contains all enabled branch    types.  Example body:  ``` {   \"development\": {     \"name\": \"master\",     \"branch\": {       \"type\": \"branch\",       \"name\": \"master\",       \"target\": {         \"hash\": \"16dffcb0de1b22e249db6799532074cf32efe80f\"       }     },     \"use_mainbranch\": true   },   \"production\": {     \"name\": \"production\",     \"branch\": {       \"type\": \"branch\",       \"name\": \"production\",       \"target\": {         \"hash\": \"16dffcb0de1b22e249db6799532074cf32efe80f\"       }     },     \"use_mainbranch\": false   },   \"branch_types\": [     {       \"kind\": \"release\",       \"prefix\": \"release/\"     },     {       \"kind\": \"hotfix\",       \"prefix\": \"hotfix/\"     },     {       \"kind\": \"feature\",       \"prefix\": \"feature/\"     },     {       \"kind\": \"bugfix\",       \"prefix\": \"bugfix/\"     }   ],   \"type\": \"branching_model\",   \"links\": {     \"self\": {       \"href\": \"https://api.bitbucket.org/.../branching-model\"     }   } } ```

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
api_instance = bitbucketopenapi.BranchingModelApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_branchingmodel(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BranchingModelApi->get_repositories_by_username_by_repo_slug_branchingmodel: %s\n" % e)
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
api_instance = bitbucketopenapi.BranchingModelApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_branchingmodel(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BranchingModelApi->get_repositories_by_username_by_repo_slug_branchingmodel: %s\n" % e)
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
api_instance = bitbucketopenapi.BranchingModelApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_branchingmodel(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BranchingModelApi->get_repositories_by_username_by_repo_slug_branchingmodel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**BranchingModel**](BranchingModel.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The branching model object |  -  |
**401** | If the request was not authenticated |  -  |
**403** | If the authenticated user does not have read access to the repository |  -  |
**404** | If the repository does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_branchingmodel_settings**
> BranchingModelSettings get_repositories_by_username_by_repo_slug_branchingmodel_settings(username, repo_slug)



Return the branching model configuration for a repository. The returned object:  1. Always has a `development` property for the development branch. 2. Always a `production` property for the production branch. The    production branch can be disabled. 3. The `branch_types` contains all the branch types.  This is the raw configuration for the branching model. A client wishing to see the branching model with its actual current branches may find the [active model API](../branching-model#get) more useful.  Example body:  ``` {   \"development\": {     \"is_valid\": true,     \"name\": null,     \"use_mainbranch\": true   },   \"production\": {     \"is_valid\": true,     \"name\": \"production\",     \"use_mainbranch\": false,     \"enabled\": false   },   \"branch_types\": [     {       \"kind\": \"release\",       \"enabled\": true,       \"prefix\": \"release/\"     },     {       \"kind\": \"hotfix\",       \"enabled\": true,       \"prefix\": \"hotfix/\"     },     {       \"kind\": \"feature\",       \"enabled\": true,       \"prefix\": \"feature/\"     },     {       \"kind\": \"bugfix\",       \"enabled\": false,       \"prefix\": \"bugfix/\"     }   ],   \"type\": \"branching_model_settings\",   \"links\": {     \"self\": {       \"href\": \"https://api.bitbucket.org/.../branching-model/settings\"     }   } } ```

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
api_instance = bitbucketopenapi.BranchingModelApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_branchingmodel_settings(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BranchingModelApi->get_repositories_by_username_by_repo_slug_branchingmodel_settings: %s\n" % e)
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
api_instance = bitbucketopenapi.BranchingModelApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_branchingmodel_settings(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BranchingModelApi->get_repositories_by_username_by_repo_slug_branchingmodel_settings: %s\n" % e)
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
api_instance = bitbucketopenapi.BranchingModelApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_branchingmodel_settings(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BranchingModelApi->get_repositories_by_username_by_repo_slug_branchingmodel_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**BranchingModelSettings**](BranchingModelSettings.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The branching model configuration |  -  |
**401** | If the request was not authenticated |  -  |
**403** | If the authenticated user does not have admin access to the repository |  -  |
**404** | If the repository does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repositories_by_username_by_repo_slug_branchingmodel_settings**
> BranchingModelSettings update_repositories_by_username_by_repo_slug_branchingmodel_settings(username, repo_slug)



Update the branching model configuration for a repository.  The `development` branch can be configured to a specific branch or to track the main branch. When set to a specific branch it must currently exist. Only the passed properties will be updated. The properties not passed will be left unchanged. A request without a `development` property will leave the development branch unchanged.  It is possible for the `development` branch to be invalid. This happens when it points at a specific branch that has been deleted. This is indicated in the `is_valid` field for the branch. It is not possible to update the settings for `development` if that would leave the branch in an invalid state. Such a request will be rejected.  The `production` branch can be a specific branch, the main branch or disabled. When set to a specific branch it must currently exist. The `enabled` property can be used to enable (`true`) or disable (`false`) it. Only the passed properties will be updated. The properties not passed will be left unchanged. A request without a `production` property will leave the production branch unchanged.  It is possible for the `production` branch to be invalid. This happens when it points at a specific branch that has been deleted. This is indicated in the `is_valid` field for the branch. A request that would leave `production` enabled and invalid will be rejected. It is possible to update `production` and make it invalid if it would also be left disabled.  The `branch_types` property contains the branch types to be updated. Only the branch types passed will be updated. All updates will be rejected if it would leave the branching model in an invalid state. For branch types this means that:  1. The prefixes for all enabled branch types are valid. For example,    it is not possible to use '*' inside a Git prefix. 2. A prefix of an enabled branch type must not be a prefix of another    enabled branch type. This is to ensure that a branch can be easily    classified by its prefix unambiguously.  It is possible to store an invalid prefix if that branch type would be left disabled. Only the passed properties will be updated. The properties not passed will be left unchanged. Each branch type must have a `kind` property to identify it.  Example Body:  ```     {       \"development\": {         \"use_mainbranch\": true       },       \"production\": {         \"enabled\": true,         \"use_mainbranch\": false,         \"name\": \"production\"       },       \"branch_types\": [         {           \"kind\": \"bugfix\",           \"enabled\": true,           \"prefix\": \"bugfix/\"         },         {           \"kind\": \"feature\",           \"enabled\": true,           \"prefix\": \"feature/\"         },         {           \"kind\": \"hotfix\",           \"prefix\": \"hotfix/\"         },         {           \"kind\": \"release\",           \"enabled\": false,         }       ]     } ```

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
api_instance = bitbucketopenapi.BranchingModelApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.update_repositories_by_username_by_repo_slug_branchingmodel_settings(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BranchingModelApi->update_repositories_by_username_by_repo_slug_branchingmodel_settings: %s\n" % e)
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
api_instance = bitbucketopenapi.BranchingModelApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.update_repositories_by_username_by_repo_slug_branchingmodel_settings(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BranchingModelApi->update_repositories_by_username_by_repo_slug_branchingmodel_settings: %s\n" % e)
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
api_instance = bitbucketopenapi.BranchingModelApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.update_repositories_by_username_by_repo_slug_branchingmodel_settings(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BranchingModelApi->update_repositories_by_username_by_repo_slug_branchingmodel_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**BranchingModelSettings**](BranchingModelSettings.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated branching model configuration |  -  |
**400** | If the request contains invalid branching model configuration |  -  |
**401** | If the request was not authenticated |  -  |
**403** | If the authenticated user does not have admin access to the repository |  -  |
**404** | If the repository does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


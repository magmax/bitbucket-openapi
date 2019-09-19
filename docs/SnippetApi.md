# bitbucketopenapi.SnippetApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_snippets_by_username_by_encoded_id_files_by_path**](SnippetApi.md#get_snippets_by_username_by_encoded_id_files_by_path) | **GET** /snippets/{username}/{encoded_id}/files/{path} | 


# **get_snippets_by_username_by_encoded_id_files_by_path**
> get_snippets_by_username_by_encoded_id_files_by_path(username, path, encoded_id)



Convenience resource for getting to a snippet's raw files without the need for first having to retrieve the snippet itself and having to pull out the versioned file links.

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
api_instance = bitbucketopenapi.SnippetApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
path = 'path_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_instance.get_snippets_by_username_by_encoded_id_files_by_path(username, path, encoded_id)
except ApiException as e:
    print("Exception when calling SnippetApi->get_snippets_by_username_by_encoded_id_files_by_path: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
path = 'path_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_instance.get_snippets_by_username_by_encoded_id_files_by_path(username, path, encoded_id)
except ApiException as e:
    print("Exception when calling SnippetApi->get_snippets_by_username_by_encoded_id_files_by_path: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
path = 'path_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_instance.get_snippets_by_username_by_encoded_id_files_by_path(username, path, encoded_id)
except ApiException as e:
    print("Exception when calling SnippetApi->get_snippets_by_username_by_encoded_id_files_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **path** | **str**|  | 
 **encoded_id** | **str**|  | 

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
**302** | A redirect to the most recent revision of the specified file. |  * Location - The URL of the most recent file revision. <br>  |
**403** | If the authenticated user does not have access to the snippet. |  -  |
**404** | If the snippet does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


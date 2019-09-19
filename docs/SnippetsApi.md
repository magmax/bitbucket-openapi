# bitbucketopenapi.SnippetsApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_snippets**](SnippetsApi.md#create_snippets) | **POST** /snippets | 
[**create_snippets_by_username**](SnippetsApi.md#create_snippets_by_username) | **POST** /snippets/{username} | 
[**create_snippets_by_username_by_encoded_id_comments**](SnippetsApi.md#create_snippets_by_username_by_encoded_id_comments) | **POST** /snippets/{username}/{encoded_id}/comments | 
[**delete_snippets_by_username_by_encoded_id**](SnippetsApi.md#delete_snippets_by_username_by_encoded_id) | **DELETE** /snippets/{username}/{encoded_id} | 
[**delete_snippets_by_username_by_encoded_id_by_node_id**](SnippetsApi.md#delete_snippets_by_username_by_encoded_id_by_node_id) | **DELETE** /snippets/{username}/{encoded_id}/{node_id} | 
[**delete_snippets_by_username_by_encoded_id_comments_by_comment_id**](SnippetsApi.md#delete_snippets_by_username_by_encoded_id_comments_by_comment_id) | **DELETE** /snippets/{username}/{encoded_id}/comments/{comment_id} | 
[**delete_snippets_by_username_by_encoded_id_watch**](SnippetsApi.md#delete_snippets_by_username_by_encoded_id_watch) | **DELETE** /snippets/{username}/{encoded_id}/watch | 
[**get_snippets**](SnippetsApi.md#get_snippets) | **GET** /snippets | 
[**get_snippets_by_username**](SnippetsApi.md#get_snippets_by_username) | **GET** /snippets/{username} | 
[**get_snippets_by_username_by_encoded_id**](SnippetsApi.md#get_snippets_by_username_by_encoded_id) | **GET** /snippets/{username}/{encoded_id} | 
[**get_snippets_by_username_by_encoded_id_by_node_id**](SnippetsApi.md#get_snippets_by_username_by_encoded_id_by_node_id) | **GET** /snippets/{username}/{encoded_id}/{node_id} | 
[**get_snippets_by_username_by_encoded_id_by_node_id_files_by_path**](SnippetsApi.md#get_snippets_by_username_by_encoded_id_by_node_id_files_by_path) | **GET** /snippets/{username}/{encoded_id}/{node_id}/files/{path} | 
[**get_snippets_by_username_by_encoded_id_by_revision_diff**](SnippetsApi.md#get_snippets_by_username_by_encoded_id_by_revision_diff) | **GET** /snippets/{username}/{encoded_id}/{revision}/diff | 
[**get_snippets_by_username_by_encoded_id_by_revision_patch**](SnippetsApi.md#get_snippets_by_username_by_encoded_id_by_revision_patch) | **GET** /snippets/{username}/{encoded_id}/{revision}/patch | 
[**get_snippets_by_username_by_encoded_id_comments**](SnippetsApi.md#get_snippets_by_username_by_encoded_id_comments) | **GET** /snippets/{username}/{encoded_id}/comments | 
[**get_snippets_by_username_by_encoded_id_comments_by_comment_id**](SnippetsApi.md#get_snippets_by_username_by_encoded_id_comments_by_comment_id) | **GET** /snippets/{username}/{encoded_id}/comments/{comment_id} | 
[**get_snippets_by_username_by_encoded_id_commits**](SnippetsApi.md#get_snippets_by_username_by_encoded_id_commits) | **GET** /snippets/{username}/{encoded_id}/commits | 
[**get_snippets_by_username_by_encoded_id_commits_by_revision**](SnippetsApi.md#get_snippets_by_username_by_encoded_id_commits_by_revision) | **GET** /snippets/{username}/{encoded_id}/commits/{revision} | 
[**get_snippets_by_username_by_encoded_id_watch**](SnippetsApi.md#get_snippets_by_username_by_encoded_id_watch) | **GET** /snippets/{username}/{encoded_id}/watch | 
[**get_snippets_by_username_by_encoded_id_watchers**](SnippetsApi.md#get_snippets_by_username_by_encoded_id_watchers) | **GET** /snippets/{username}/{encoded_id}/watchers | 
[**update_snippets_by_username_by_encoded_id**](SnippetsApi.md#update_snippets_by_username_by_encoded_id) | **PUT** /snippets/{username}/{encoded_id} | 
[**update_snippets_by_username_by_encoded_id_by_node_id**](SnippetsApi.md#update_snippets_by_username_by_encoded_id_by_node_id) | **PUT** /snippets/{username}/{encoded_id}/{node_id} | 
[**update_snippets_by_username_by_encoded_id_comments_by_comment_id**](SnippetsApi.md#update_snippets_by_username_by_encoded_id_comments_by_comment_id) | **PUT** /snippets/{username}/{encoded_id}/comments/{comment_id} | 
[**update_snippets_by_username_by_encoded_id_watch**](SnippetsApi.md#update_snippets_by_username_by_encoded_id_watch) | **PUT** /snippets/{username}/{encoded_id}/watch | 


# **create_snippets**
> Snippet create_snippets(body)



Creates a new snippet under the authenticated user's account.  Snippets can contain multiple files. Both text and binary files are supported.  The simplest way to create a new snippet from a local file:      $ curl -u username:password -X POST https://api.bitbucket.org/2.0/snippets               -F file=@image.png  Creating snippets through curl has a few limitations and so let's look at a more complicated scenario.  Snippets are created with a multipart POST. Both `multipart/form-data` and `multipart/related` are supported. Both allow the creation of snippets with both meta data (title, etc), as well as multiple text and binary files.  The main difference is that `multipart/related` can use rich encoding for the meta data (currently JSON).   multipart/related (RFC-2387) ----------------------------  This is the most advanced and efficient way to create a paste.      POST /2.0/snippets/evzijst HTTP/1.1     Content-Length: 1188     Content-Type: multipart/related; start=\"snippet\"; boundary=\"===============1438169132528273974==\"     MIME-Version: 1.0      --===============1438169132528273974==     Content-Type: application/json; charset=\"utf-8\"     MIME-Version: 1.0     Content-ID: snippet      {       \"title\": \"My snippet\",       \"is_private\": true,       \"scm\": \"hg\",       \"files\": {           \"foo.txt\": {},           \"image.png\": {}         }     }      --===============1438169132528273974==     Content-Type: text/plain; charset=\"us-ascii\"     MIME-Version: 1.0     Content-Transfer-Encoding: 7bit     Content-ID: \"foo.txt\"     Content-Disposition: attachment; filename=\"foo.txt\"      foo      --===============1438169132528273974==     Content-Type: image/png     MIME-Version: 1.0     Content-Transfer-Encoding: base64     Content-ID: \"image.png\"     Content-Disposition: attachment; filename=\"image.png\"      iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m     TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB     cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5     EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ     73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN     AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==     --===============1438169132528273974==--  The request contains multiple parts and is structured as follows.  The first part is the JSON document that describes the snippet's properties or meta data. It either has to be the first part, or the request's `Content-Type` header must contain the `start` parameter to point to it.  The remaining parts are the files of which there can be zero or more. Each file part should contain the `Content-ID` MIME header through which the JSON meta data's `files` element addresses it. The value should be the name of the file.  `Content-Disposition` is an optional MIME header. The header's optional `filename` parameter can be used to specify the file name that Bitbucket should use when writing the file to disk. When present, `filename` takes precedence over the value of `Content-ID`.  When the JSON body omits the `files` element, the remaining parts are not ignored. Instead, each file is added to the new snippet as if its name was explicitly linked (the use of the `files` elements is mandatory for some operations like deleting or renaming files).   multipart/form-data -------------------  The use of JSON for the snippet's meta data is optional. Meta data can also be supplied as regular form fields in a more conventional `multipart/form-data` request:      $ curl -X POST -u credentials https://api.bitbucket.org/2.0/snippets               -F title=\"My snippet\"               -F file=@foo.txt -F file=@image.png      POST /2.0/snippets HTTP/1.1     Content-Length: 951     Content-Type: multipart/form-data; boundary=----------------------------63a4b224c59f      ------------------------------63a4b224c59f     Content-Disposition: form-data; name=\"file\"; filename=\"foo.txt\"     Content-Type: text/plain      foo      ------------------------------63a4b224c59f     Content-Disposition: form-data; name=\"file\"; filename=\"image.png\"     Content-Type: application/octet-stream      ?PNG      IHDR?1??I.....     ------------------------------63a4b224c59f     Content-Disposition: form-data; name=\"title\"      My snippet     ------------------------------63a4b224c59f--  Here the meta data properties are included as flat, top-level form fields. The file attachments use the `file` field name. To attach multiple files, simply repeat the field.  The advantage of `multipart/form-data` over `multipart/related` is that it can be easier to build clients.  Essentially all properties are optional, `title` and `files` included.   Sharing and Visibility ----------------------  Snippets can be either public (visible to anyone on Bitbucket, as well as anonymous users), or private (visible only to the owner, creator and members of the team in case the snippet is owned by a team). This is controlled through the snippet's `is_private` element:  * **is_private=false** -- everyone, including anonymous users can view   the snippet * **is_private=true** -- only the owner and team members (for team   snippets) can view it  To create the snippet under a team account, just append the team name to the URL (see `/2.0/snippets/{username}`).

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
body = bitbucketopenapi.Snippet() # Snippet | The new snippet object.

try:
    api_response = api_instance.create_snippets(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->create_snippets: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
body = bitbucketopenapi.Snippet() # Snippet | The new snippet object.

try:
    api_response = api_instance.create_snippets(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->create_snippets: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
body = bitbucketopenapi.Snippet() # Snippet | The new snippet object.

try:
    api_response = api_instance.create_snippets(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->create_snippets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Snippet**](Snippet.md)| The new snippet object. | 

### Return type

[**Snippet**](Snippet.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created snippet object. |  * Location - The URL of the newly created snippet. <br>  |
**401** | If the request was not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snippets_by_username**
> Snippet create_snippets_by_username(username, body)



Identical to `/snippets`, except that the new snippet will be created under the account specified in the path parameter `{username}`.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
body = bitbucketopenapi.Snippet() # Snippet | The new snippet object.

try:
    api_response = api_instance.create_snippets_by_username(username, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->create_snippets_by_username: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
body = bitbucketopenapi.Snippet() # Snippet | The new snippet object.

try:
    api_response = api_instance.create_snippets_by_username(username, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->create_snippets_by_username: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
body = bitbucketopenapi.Snippet() # Snippet | The new snippet object.

try:
    api_response = api_instance.create_snippets_by_username(username, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->create_snippets_by_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **body** | [**Snippet**](Snippet.md)| The new snippet object. | 

### Return type

[**Snippet**](Snippet.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created snippet object. |  * Location - The URL of the newly created snippet. <br>  |
**401** | If the request was not authenticated |  -  |
**403** | If the authenticated user does not have permission to create snippets under the specified account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snippets_by_username_by_encoded_id_comments**
> Snippet create_snippets_by_username_by_encoded_id_comments(username, encoded_id, body)



Creates a new comment.  The only required field in the body is `content.raw`.  To create a threaded reply to an existing comment, include `parent.id`.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | 
body = bitbucketopenapi.Snippet() # Snippet | The contents of the new comment.

try:
    api_response = api_instance.create_snippets_by_username_by_encoded_id_comments(username, encoded_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->create_snippets_by_username_by_encoded_id_comments: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | 
body = bitbucketopenapi.Snippet() # Snippet | The contents of the new comment.

try:
    api_response = api_instance.create_snippets_by_username_by_encoded_id_comments(username, encoded_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->create_snippets_by_username_by_encoded_id_comments: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | 
body = bitbucketopenapi.Snippet() # Snippet | The contents of the new comment.

try:
    api_response = api_instance.create_snippets_by_username_by_encoded_id_comments(username, encoded_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->create_snippets_by_username_by_encoded_id_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **encoded_id** | **str**|  | 
 **body** | [**Snippet**](Snippet.md)| The contents of the new comment. | 

### Return type

[**Snippet**](Snippet.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created comment. |  * Location - The URL of the new comment <br>  |
**403** | If the authenticated user does not have access to the snippet. |  -  |
**404** | If the snippet does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snippets_by_username_by_encoded_id**
> delete_snippets_by_username_by_encoded_id(username, encoded_id)



Deletes a snippet and returns an empty response.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet's id.

try:
    api_instance.delete_snippets_by_username_by_encoded_id(username, encoded_id)
except ApiException as e:
    print("Exception when calling SnippetsApi->delete_snippets_by_username_by_encoded_id: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet's id.

try:
    api_instance.delete_snippets_by_username_by_encoded_id(username, encoded_id)
except ApiException as e:
    print("Exception when calling SnippetsApi->delete_snippets_by_username_by_encoded_id: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet's id.

try:
    api_instance.delete_snippets_by_username_by_encoded_id(username, encoded_id)
except ApiException as e:
    print("Exception when calling SnippetsApi->delete_snippets_by_username_by_encoded_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **encoded_id** | **str**| The snippet&#39;s id. | 

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
**204** | If the snippet was deleted successfully. |  -  |
**401** | If the snippet is private and the request was not authenticated. |  -  |
**403** | If authenticated user does not have permission to delete the private snippet. |  -  |
**404** | If the snippet does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snippets_by_username_by_encoded_id_by_node_id**
> delete_snippets_by_username_by_encoded_id_by_node_id(username, node_id, encoded_id)



Deletes the snippet.  Note that this only works for versioned URLs that point to the latest commit of the snippet. Pointing to an older commit results in a 405 status code.  To delete a snippet, regardless of whether or not concurrent changes are being made to it, use `DELETE /snippets/{encoded_id}` instead.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
node_id = 'node_id_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet's id.

try:
    api_instance.delete_snippets_by_username_by_encoded_id_by_node_id(username, node_id, encoded_id)
except ApiException as e:
    print("Exception when calling SnippetsApi->delete_snippets_by_username_by_encoded_id_by_node_id: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
node_id = 'node_id_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet's id.

try:
    api_instance.delete_snippets_by_username_by_encoded_id_by_node_id(username, node_id, encoded_id)
except ApiException as e:
    print("Exception when calling SnippetsApi->delete_snippets_by_username_by_encoded_id_by_node_id: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
node_id = 'node_id_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet's id.

try:
    api_instance.delete_snippets_by_username_by_encoded_id_by_node_id(username, node_id, encoded_id)
except ApiException as e:
    print("Exception when calling SnippetsApi->delete_snippets_by_username_by_encoded_id_by_node_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **node_id** | **str**|  | 
 **encoded_id** | **str**| The snippet&#39;s id. | 

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
**204** | If the snippet was deleted successfully. |  -  |
**401** | If the snippet is private and the request was not authenticated. |  -  |
**403** | If authenticated user does not have permission to delete the private snippet. |  -  |
**404** | If the snippet does not exist. |  -  |
**405** | If &#x60;{node_id}&#x60; is not the latest revision. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snippets_by_username_by_encoded_id_comments_by_comment_id**
> delete_snippets_by_username_by_encoded_id_comments_by_comment_id(username, comment_id, encoded_id)



Deletes a snippet comment.  Comments can only be removed by their author.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
comment_id = 'comment_id_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_instance.delete_snippets_by_username_by_encoded_id_comments_by_comment_id(username, comment_id, encoded_id)
except ApiException as e:
    print("Exception when calling SnippetsApi->delete_snippets_by_username_by_encoded_id_comments_by_comment_id: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
comment_id = 'comment_id_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_instance.delete_snippets_by_username_by_encoded_id_comments_by_comment_id(username, comment_id, encoded_id)
except ApiException as e:
    print("Exception when calling SnippetsApi->delete_snippets_by_username_by_encoded_id_comments_by_comment_id: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
comment_id = 'comment_id_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_instance.delete_snippets_by_username_by_encoded_id_comments_by_comment_id(username, comment_id, encoded_id)
except ApiException as e:
    print("Exception when calling SnippetsApi->delete_snippets_by_username_by_encoded_id_comments_by_comment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **comment_id** | **str**|  | 
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
**204** | Indicates the comment was deleted successfully. |  -  |
**403** | If the authenticated user is not the author of the comment. |  -  |
**404** | If the comment or the snippet does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snippets_by_username_by_encoded_id_watch**
> PaginatedUsers delete_snippets_by_username_by_encoded_id_watch(username, encoded_id)



Used to stop watching a specific snippet. Returns 204 (No Content) to indicate success.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet id.

try:
    api_response = api_instance.delete_snippets_by_username_by_encoded_id_watch(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->delete_snippets_by_username_by_encoded_id_watch: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet id.

try:
    api_response = api_instance.delete_snippets_by_username_by_encoded_id_watch(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->delete_snippets_by_username_by_encoded_id_watch: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet id.

try:
    api_response = api_instance.delete_snippets_by_username_by_encoded_id_watch(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->delete_snippets_by_username_by_encoded_id_watch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **encoded_id** | **str**| The snippet id. | 

### Return type

[**PaginatedUsers**](PaginatedUsers.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Indicates the user stopped watching the snippet successfully. |  -  |
**401** | If the request was not authenticated. |  -  |
**404** | If the snippet does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snippets**
> PaginatedSnippets get_snippets(role=role)



Returns all snippets. Like pull requests, repositories and teams, the full set of snippets is defined by what the current user has access to.  This includes all snippets owned by the current user, but also all snippets owned by any of the teams the user is a member of, or snippets by other users that the current user is either watching or has collaborated on (for instance by commenting on it).  To limit the set of returned snippets, apply the `?role=[owner|contributor|member]` query parameter where the roles are defined as follows:  * `owner`: all snippets owned by the current user * `contributor`: all snippets owned by, or watched by the current user * `member`: owned by the user, their teams, or watched by the current user  When no role is specified, all public snippets are returned, as well as all privately owned snippets watched or commented on.  The returned response is a normal paginated JSON list. This endpoint only supports `application/json` responses and no `multipart/form-data` or `multipart/related`. As a result, it is not possible to include the file contents.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
role = 'role_example' # str | Filter down the result based on the authenticated user's role (`owner`, `contributor`, or `member`). (optional)

try:
    api_response = api_instance.get_snippets(role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
role = 'role_example' # str | Filter down the result based on the authenticated user's role (`owner`, `contributor`, or `member`). (optional)

try:
    api_response = api_instance.get_snippets(role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
role = 'role_example' # str | Filter down the result based on the authenticated user's role (`owner`, `contributor`, or `member`). (optional)

try:
    api_response = api_instance.get_snippets(role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| Filter down the result based on the authenticated user&#39;s role (&#x60;owner&#x60;, &#x60;contributor&#x60;, or &#x60;member&#x60;). | [optional] 

### Return type

[**PaginatedSnippets**](PaginatedSnippets.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of snippets. |  -  |
**404** | If the snippet does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snippets_by_username**
> PaginatedSnippets get_snippets_by_username(username, role=role)



Identical to `/snippets`, except that the result is further filtered by the snippet owner and only those that are owned by `{username}` are returned.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | Limits the result to snippets owned by this user.
role = 'role_example' # str | Filter down the result based on the authenticated user's role (`owner`, `contributor`, or `member`). (optional)

try:
    api_response = api_instance.get_snippets_by_username(username, role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | Limits the result to snippets owned by this user.
role = 'role_example' # str | Filter down the result based on the authenticated user's role (`owner`, `contributor`, or `member`). (optional)

try:
    api_response = api_instance.get_snippets_by_username(username, role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | Limits the result to snippets owned by this user.
role = 'role_example' # str | Filter down the result based on the authenticated user's role (`owner`, `contributor`, or `member`). (optional)

try:
    api_response = api_instance.get_snippets_by_username(username, role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Limits the result to snippets owned by this user. | 
 **role** | **str**| Filter down the result based on the authenticated user&#39;s role (&#x60;owner&#x60;, &#x60;contributor&#x60;, or &#x60;member&#x60;). | [optional] 

### Return type

[**PaginatedSnippets**](PaginatedSnippets.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of snippets. |  -  |
**404** | If the user does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snippets_by_username_by_encoded_id**
> Snippet get_snippets_by_username_by_encoded_id(username, encoded_id)



Retrieves a single snippet.  Snippets support multiple content types:  * application/json * multipart/related * multipart/form-data   application/json ----------------  The default content type of the response is `application/json`. Since JSON is always `utf-8`, it cannot reliably contain file contents for files that are not text. Therefore, JSON snippet documents only contain the filename and links to the file contents.  This means that in order to retrieve all parts of a snippet, N+1 requests need to be made (where N is the number of files in the snippet).   multipart/related -----------------  To retrieve an entire snippet in a single response, use the `Accept: multipart/related` HTTP request header.      $ curl -H \"Accept: multipart/related\" https://api.bitbucket.org/2.0/snippets/evzijst/1  Response:      HTTP/1.1 200 OK     Content-Length: 2214     Content-Type: multipart/related; start=\"snippet\"; boundary=\"===============1438169132528273974==\"     MIME-Version: 1.0      --===============1438169132528273974==     Content-Type: application/json; charset=\"utf-8\"     MIME-Version: 1.0     Content-ID: snippet      {       \"links\": {         \"self\": {           \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj\"         },         \"html\": {           \"href\": \"https://bitbucket.org/snippets/evzijst/kypj\"         },         \"comments\": {           \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/comments\"         },         \"watchers\": {           \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/watchers\"         },         \"commits\": {           \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/commits\"         }       },       \"id\": kypj,       \"title\": \"My snippet\",       \"created_on\": \"2014-12-29T22:22:04.790331+00:00\",       \"updated_on\": \"2014-12-29T22:22:04.790331+00:00\",       \"is_private\": false,       \"files\": {         \"foo.txt\": {           \"links\": {             \"self\": {               \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/files/367ab19/foo.txt\"             },             \"html\": {               \"href\": \"https://bitbucket.org/snippets/evzijst/kypj#file-foo.txt\"             }           }         },         \"image.png\": {           \"links\": {             \"self\": {               \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/files/367ab19/image.png\"             },             \"html\": {               \"href\": \"https://bitbucket.org/snippets/evzijst/kypj#file-image.png\"             }           }         }       ],       \"owner\": {         \"username\": \"evzijst\",         \"nickname\": \"evzijst\",         \"display_name\": \"Erik van Zijst\",         \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\",         \"links\": {           \"self\": {             \"href\": \"https://api.bitbucket.org/2.0/users/evzijst\"           },           \"html\": {             \"href\": \"https://bitbucket.org/evzijst\"           },           \"avatar\": {             \"href\": \"https://bitbucket-staging-assetroot.s3.amazonaws.com/c/photos/2013/Jul/31/erik-avatar-725122544-0_avatar.png\"           }         }       },       \"creator\": {         \"username\": \"evzijst\",         \"nickname\": \"evzijst\",         \"display_name\": \"Erik van Zijst\",         \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\",         \"links\": {           \"self\": {             \"href\": \"https://api.bitbucket.org/2.0/users/evzijst\"           },           \"html\": {             \"href\": \"https://bitbucket.org/evzijst\"           },           \"avatar\": {             \"href\": \"https://bitbucket-staging-assetroot.s3.amazonaws.com/c/photos/2013/Jul/31/erik-avatar-725122544-0_avatar.png\"           }         }       }     }      --===============1438169132528273974==     Content-Type: text/plain; charset=\"us-ascii\"     MIME-Version: 1.0     Content-Transfer-Encoding: 7bit     Content-ID: \"foo.txt\"     Content-Disposition: attachment; filename=\"foo.txt\"      foo      --===============1438169132528273974==     Content-Type: image/png     MIME-Version: 1.0     Content-Transfer-Encoding: base64     Content-ID: \"image.png\"     Content-Disposition: attachment; filename=\"image.png\"      iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m     TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB     cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5     EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ     73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN     AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==     --===============1438169132528273974==--  multipart/form-data -------------------  As with creating new snippets, `multipart/form-data` can be used as an alternative to `multipart/related`. However, the inherently flat structure of form-data means that only basic, root-level properties can be returned, while nested elements like `links` are omitted:      $ curl -H \"Accept: multipart/form-data\" https://api.bitbucket.org/2.0/snippets/evzijst/kypj  Response:      HTTP/1.1 200 OK     Content-Length: 951     Content-Type: multipart/form-data; boundary=----------------------------63a4b224c59f      ------------------------------63a4b224c59f     Content-Disposition: form-data; name=\"title\"     Content-Type: text/plain; charset=\"utf-8\"      My snippet     ------------------------------63a4b224c59f--     Content-Disposition: attachment; name=\"file\"; filename=\"foo.txt\"     Content-Type: text/plain      foo      ------------------------------63a4b224c59f     Content-Disposition: attachment; name=\"file\"; filename=\"image.png\"     Content-Transfer-Encoding: base64     Content-Type: application/octet-stream      iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m     TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB     cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5     EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ     73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN     AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==     ------------------------------5957323a6b76--

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet's id.

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet's id.

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet's id.

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **encoded_id** | **str**| The snippet&#39;s id. | 

### Return type

[**Snippet**](Snippet.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, multipart/related, multipart/form-data

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The snippet object. |  -  |
**401** | If the snippet is private and the request was not authenticated. |  -  |
**403** | If authenticated user does not have access to the private snippet. |  -  |
**404** | If the snippet does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snippets_by_username_by_encoded_id_by_node_id**
> Snippet get_snippets_by_username_by_encoded_id_by_node_id(username, encoded_id, node_id)



Identical to `GET /snippets/encoded_id`, except that this endpoint can be used to retrieve the contents of the snippet as it was at an older revision, while `/snippets/encoded_id` always returns the snippet's current revision.  Note that only the snippet's file contents are versioned, not its meta data properties like the title.  Other than that, the two endpoints are identical in behavior.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet's id.
node_id = 'node_id_example' # str | A commit revision (SHA1).

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_by_node_id(username, encoded_id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_by_node_id: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet's id.
node_id = 'node_id_example' # str | A commit revision (SHA1).

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_by_node_id(username, encoded_id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_by_node_id: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet's id.
node_id = 'node_id_example' # str | A commit revision (SHA1).

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_by_node_id(username, encoded_id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_by_node_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **encoded_id** | **str**| The snippet&#39;s id. | 
 **node_id** | **str**| A commit revision (SHA1). | 

### Return type

[**Snippet**](Snippet.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, multipart/related, multipart/form-data

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The snippet object. |  -  |
**401** | If the snippet is private and the request was not authenticated. |  -  |
**403** | If authenticated user does not have access to the private snippet. |  -  |
**404** | If the snippet, or the revision does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snippets_by_username_by_encoded_id_by_node_id_files_by_path**
> get_snippets_by_username_by_encoded_id_by_node_id_files_by_path(username, path, node_id, encoded_id)



Retrieves the raw contents of a specific file in the snippet. The `Content-Disposition` header will be \"attachment\" to avoid issues with malevolent executable files.  The file's mime type is derived from its filename and returned in the `Content-Type` header.  Note that for text files, no character encoding is included as part of the content type.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
path = 'path_example' # str | 
node_id = 'node_id_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_instance.get_snippets_by_username_by_encoded_id_by_node_id_files_by_path(username, path, node_id, encoded_id)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_by_node_id_files_by_path: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
path = 'path_example' # str | 
node_id = 'node_id_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_instance.get_snippets_by_username_by_encoded_id_by_node_id_files_by_path(username, path, node_id, encoded_id)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_by_node_id_files_by_path: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
path = 'path_example' # str | 
node_id = 'node_id_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_instance.get_snippets_by_username_by_encoded_id_by_node_id_files_by_path(username, path, node_id, encoded_id)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_by_node_id_files_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **path** | **str**|  | 
 **node_id** | **str**|  | 
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
**200** | Returns the contents of the specified file. |  * Content-Disposition - attachment <br>  * Content-Type - The mime type as derived from the filename <br>  |
**403** | If the authenticated user does not have access to the snippet. |  -  |
**404** | If the file or snippet does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snippets_by_username_by_encoded_id_by_revision_diff**
> get_snippets_by_username_by_encoded_id_by_revision_diff(username, encoded_id, revision, path=path)



Returns the diff of the specified commit against its first parent.  Note that this resource is different in functionality from the `patch` resource.  The differences between a diff and a patch are:  * patches have a commit header with the username, message, etc * diffs support the optional `path=foo/bar.py` query param to filter the   diff to just that one file diff (not supported for patches) * for a merge, the diff will show the diff between the merge commit and   its first parent (identical to how PRs work), while patch returns a   response containing separate patches for each commit on the second   parent's ancestry, up to the oldest common ancestor (identical to   its reachability).  Note that the character encoding of the contents of the diff is unspecified as Git and Mercurial do not track this, making it hard for Bitbucket to reliably determine this.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet id.
revision = 'revision_example' # str | A revspec expression. This can simply be a commit SHA1, a ref name, or a compare expression like `staging..production`.
path = 'path_example' # str | When used, only one the diff of the specified file will be returned. (optional)

try:
    api_instance.get_snippets_by_username_by_encoded_id_by_revision_diff(username, encoded_id, revision, path=path)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_by_revision_diff: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet id.
revision = 'revision_example' # str | A revspec expression. This can simply be a commit SHA1, a ref name, or a compare expression like `staging..production`.
path = 'path_example' # str | When used, only one the diff of the specified file will be returned. (optional)

try:
    api_instance.get_snippets_by_username_by_encoded_id_by_revision_diff(username, encoded_id, revision, path=path)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_by_revision_diff: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet id.
revision = 'revision_example' # str | A revspec expression. This can simply be a commit SHA1, a ref name, or a compare expression like `staging..production`.
path = 'path_example' # str | When used, only one the diff of the specified file will be returned. (optional)

try:
    api_instance.get_snippets_by_username_by_encoded_id_by_revision_diff(username, encoded_id, revision, path=path)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_by_revision_diff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **encoded_id** | **str**| The snippet id. | 
 **revision** | **str**| A revspec expression. This can simply be a commit SHA1, a ref name, or a compare expression like &#x60;staging..production&#x60;. | 
 **path** | **str**| When used, only one the diff of the specified file will be returned. | [optional] 

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
**200** | The raw diff contents. |  -  |
**403** | If the authenticated user does not have access to the snippet. |  -  |
**404** | If the snippet does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snippets_by_username_by_encoded_id_by_revision_patch**
> get_snippets_by_username_by_encoded_id_by_revision_patch(username, encoded_id, revision)



Returns the patch of the specified commit against its first parent.  Note that this resource is different in functionality from the `diff` resource.  The differences between a diff and a patch are:  * patches have a commit header with the username, message, etc * diffs support the optional `path=foo/bar.py` query param to filter the   diff to just that one file diff (not supported for patches) * for a merge, the diff will show the diff between the merge commit and   its first parent (identical to how PRs work), while patch returns a   response containing separate patches for each commit on the second   parent's ancestry, up to the oldest common ancestor (identical to   its reachability).  Note that the character encoding of the contents of the patch is unspecified as Git and Mercurial do not track this, making it hard for Bitbucket to reliably determine this.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet id.
revision = 'revision_example' # str | A revspec expression. This can simply be a commit SHA1, a ref name, or a compare expression like `staging..production`.

try:
    api_instance.get_snippets_by_username_by_encoded_id_by_revision_patch(username, encoded_id, revision)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_by_revision_patch: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet id.
revision = 'revision_example' # str | A revspec expression. This can simply be a commit SHA1, a ref name, or a compare expression like `staging..production`.

try:
    api_instance.get_snippets_by_username_by_encoded_id_by_revision_patch(username, encoded_id, revision)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_by_revision_patch: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet id.
revision = 'revision_example' # str | A revspec expression. This can simply be a commit SHA1, a ref name, or a compare expression like `staging..production`.

try:
    api_instance.get_snippets_by_username_by_encoded_id_by_revision_patch(username, encoded_id, revision)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_by_revision_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **encoded_id** | **str**| The snippet id. | 
 **revision** | **str**| A revspec expression. This can simply be a commit SHA1, a ref name, or a compare expression like &#x60;staging..production&#x60;. | 

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
**200** | The raw patch contents. |  -  |
**403** | If the authenticated user does not have access to the snippet. |  -  |
**404** | If the snippet does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snippets_by_username_by_encoded_id_comments**
> PaginatedSnippetComments get_snippets_by_username_by_encoded_id_comments(username, encoded_id)



Used to retrieve a paginated list of all comments for a specific snippet.  This resource works identical to commit and pull request comments.  The default sorting is oldest to newest and can be overridden with the `sort` query parameter.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_comments(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_comments: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_comments(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_comments: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_comments(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **encoded_id** | **str**|  | 

### Return type

[**PaginatedSnippetComments**](PaginatedSnippetComments.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of snippet comments, ordered by creation date. |  -  |
**403** | If the authenticated user does not have access to the snippet. |  -  |
**404** | If the snippet does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snippets_by_username_by_encoded_id_comments_by_comment_id**
> SnippetComment get_snippets_by_username_by_encoded_id_comments_by_comment_id(username, comment_id, encoded_id)



Returns the specific snippet comment.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
comment_id = 'comment_id_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_comments_by_comment_id(username, comment_id, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_comments_by_comment_id: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
comment_id = 'comment_id_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_comments_by_comment_id(username, comment_id, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_comments_by_comment_id: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
comment_id = 'comment_id_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_comments_by_comment_id(username, comment_id, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_comments_by_comment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **comment_id** | **str**|  | 
 **encoded_id** | **str**|  | 

### Return type

[**SnippetComment**](SnippetComment.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The specified comment. |  -  |
**403** | If the authenticated user does not have access to the snippet. |  -  |
**404** | If the comment or snippet does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snippets_by_username_by_encoded_id_commits**
> PaginatedSnippetCommit get_snippets_by_username_by_encoded_id_commits(username, encoded_id)



Returns the changes (commits) made on this snippet.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_commits(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_commits: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_commits(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_commits: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_commits(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_commits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **encoded_id** | **str**|  | 

### Return type

[**PaginatedSnippetCommit**](PaginatedSnippetCommit.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The paginated list of snippet commits. |  -  |
**403** | If the authenticated user does not have access to the snippet. |  -  |
**404** | If the snippet does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snippets_by_username_by_encoded_id_commits_by_revision**
> SnippetCommit get_snippets_by_username_by_encoded_id_commits_by_revision(username, encoded_id, revision)



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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | 
revision = 'revision_example' # str | 

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_commits_by_revision(username, encoded_id, revision)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_commits_by_revision: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | 
revision = 'revision_example' # str | 

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_commits_by_revision(username, encoded_id, revision)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_commits_by_revision: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | 
revision = 'revision_example' # str | 

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_commits_by_revision(username, encoded_id, revision)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_commits_by_revision: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **encoded_id** | **str**|  | 
 **revision** | **str**|  | 

### Return type

[**SnippetCommit**](SnippetCommit.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The specified snippet commit. |  -  |
**403** | If the authenticated user does not have access to the snippet. |  -  |
**404** | If the commit or the snippet does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snippets_by_username_by_encoded_id_watch**
> PaginatedUsers get_snippets_by_username_by_encoded_id_watch(username, encoded_id)



Used to check if the current user is watching a specific snippet.  Returns 204 (No Content) if the user is watching the snippet and 404 if not.  Hitting this endpoint anonymously always returns a 404.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet id.

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_watch(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_watch: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet id.

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_watch(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_watch: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet id.

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_watch(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_watch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **encoded_id** | **str**| The snippet id. | 

### Return type

[**PaginatedUsers**](PaginatedUsers.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | If the authenticated user is watching the snippet. |  -  |
**404** | If the snippet does not exist, or if the authenticated user is not watching the snippet. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snippets_by_username_by_encoded_id_watchers**
> PaginatedUsers get_snippets_by_username_by_encoded_id_watchers(username, encoded_id)



Returns a paginated list of all users watching a specific snippet.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet id.

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_watchers(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_watchers: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet id.

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_watchers(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_watchers: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet id.

try:
    api_response = api_instance.get_snippets_by_username_by_encoded_id_watchers(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->get_snippets_by_username_by_encoded_id_watchers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **encoded_id** | **str**| The snippet id. | 

### Return type

[**PaginatedUsers**](PaginatedUsers.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The paginated list of users watching this snippet |  -  |
**404** | If the snippet does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snippets_by_username_by_encoded_id**
> Snippet update_snippets_by_username_by_encoded_id(username, encoded_id)



Used to update a snippet. Use this to add and delete files and to change a snippet's title.  To update a snippet, one can either PUT a full snapshot, or only the parts that need to be changed.  The contract for PUT on this API is that properties missing from the request remain untouched so that snippets can be efficiently manipulated with differential payloads.  To delete a property (e.g. the title, or a file), include its name in the request, but omit its value (use `null`).  As in Git, explicit renaming of files is not supported. Instead, to rename a file, delete it and add it again under another name. This can be done atomically in a single request. Rename detection is left to the SCM.  PUT supports three different content types for both request and response bodies:  * `application/json` * `multipart/related` * `multipart/form-data`  The content type used for the request body can be different than that used for the response. Content types are specified using standard HTTP headers.  Use the `Content-Type` and `Accept` headers to select the desired request and response format.   application/json ----------------  As with creation and retrieval, the content type determines what properties can be manipulated. `application/json` does not support file contents and is therefore limited to a snippet's meta data.  To update the title, without changing any of its files:      $ curl -X POST -H \"Content-Type: application/json\" https://api.bitbucket.org/2.0/snippets/evzijst/kypj             -d '{\"title\": \"Updated title\"}'   To delete the title:      $ curl -X POST -H \"Content-Type: application/json\" https://api.bitbucket.org/2.0/snippets/evzijst/kypj             -d '{\"title\": null}'  Not all parts of a snippet can be manipulated. The owner and creator for instance are immutable.   multipart/related -----------------  `multipart/related` can be used to manipulate all of a snippet's properties. The body is identical to a POST. properties omitted from the request are left unchanged. Since the `start` part contains JSON, the mechanism for manipulating the snippet's meta data is identical to `application/json` requests.  To update one of a snippet's file contents, while also changing its title:      PUT /2.0/snippets/evzijst/kypj HTTP/1.1     Content-Length: 288     Content-Type: multipart/related; start=\"snippet\"; boundary=\"===============1438169132528273974==\"     MIME-Version: 1.0      --===============1438169132528273974==     Content-Type: application/json; charset=\"utf-8\"     MIME-Version: 1.0     Content-ID: snippet      {       \"title\": \"My updated snippet\",       \"files\": {           \"foo.txt\": {}         }     }      --===============1438169132528273974==     Content-Type: text/plain; charset=\"us-ascii\"     MIME-Version: 1.0     Content-Transfer-Encoding: 7bit     Content-ID: \"foo.txt\"     Content-Disposition: attachment; filename=\"foo.txt\"      Updated file contents.      --===============1438169132528273974==--  Here only the parts that are changed are included in the body. The other files remain untouched.  Note the use of the `files` list in the JSON part. This list contains the files that are being manipulated. This list should have corresponding multiparts in the request that contain the new contents of these files.  If a filename in the `files` list does not have a corresponding part, it will be deleted from the snippet, as shown below:      PUT /2.0/snippets/evzijst/kypj HTTP/1.1     Content-Length: 188     Content-Type: multipart/related; start=\"snippet\"; boundary=\"===============1438169132528273974==\"     MIME-Version: 1.0      --===============1438169132528273974==     Content-Type: application/json; charset=\"utf-8\"     MIME-Version: 1.0     Content-ID: snippet      {       \"files\": {         \"image.png\": {}       }     }      --===============1438169132528273974==--  To simulate a rename, delete a file and add the same file under another name:      PUT /2.0/snippets/evzijst/kypj HTTP/1.1     Content-Length: 212     Content-Type: multipart/related; start=\"snippet\"; boundary=\"===============1438169132528273974==\"     MIME-Version: 1.0      --===============1438169132528273974==     Content-Type: application/json; charset=\"utf-8\"     MIME-Version: 1.0     Content-ID: snippet      {         \"files\": {           \"foo.txt\": {},           \"bar.txt\": {}         }     }      --===============1438169132528273974==     Content-Type: text/plain; charset=\"us-ascii\"     MIME-Version: 1.0     Content-Transfer-Encoding: 7bit     Content-ID: \"bar.txt\"     Content-Disposition: attachment; filename=\"bar.txt\"      foo      --===============1438169132528273974==--   multipart/form-data -----------------  Again, one can also use `multipart/form-data` to manipulate file contents and meta data atomically.      $ curl -X PUT http://localhost:12345/2.0/snippets/evzijst/kypj             -F title=\"My updated snippet\" -F file=@foo.txt      PUT /2.0/snippets/evzijst/kypj HTTP/1.1     Content-Length: 351     Content-Type: multipart/form-data; boundary=----------------------------63a4b224c59f      ------------------------------63a4b224c59f     Content-Disposition: form-data; name=\"file\"; filename=\"foo.txt\"     Content-Type: text/plain      foo      ------------------------------63a4b224c59f     Content-Disposition: form-data; name=\"title\"      My updated snippet     ------------------------------63a4b224c59f  To delete a file, omit its contents while including its name in the `files` field:      $ curl -X PUT https://api.bitbucket.org/2.0/snippets/evzijst/kypj -F files=image.png      PUT /2.0/snippets/evzijst/kypj HTTP/1.1     Content-Length: 149     Content-Type: multipart/form-data; boundary=----------------------------ef8871065a86      ------------------------------ef8871065a86     Content-Disposition: form-data; name=\"files\"      image.png     ------------------------------ef8871065a86--  The explicit use of the `files` element in `multipart/related` and `multipart/form-data` is only required when deleting files. The default mode of operation is for file parts to be processed, regardless of whether or not they are listed in `files`, as a convenience to the client.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet's id.

try:
    api_response = api_instance.update_snippets_by_username_by_encoded_id(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->update_snippets_by_username_by_encoded_id: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet's id.

try:
    api_response = api_instance.update_snippets_by_username_by_encoded_id(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->update_snippets_by_username_by_encoded_id: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet's id.

try:
    api_response = api_instance.update_snippets_by_username_by_encoded_id(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->update_snippets_by_username_by_encoded_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **encoded_id** | **str**| The snippet&#39;s id. | 

### Return type

[**Snippet**](Snippet.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, multipart/related, multipart/form-data

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated snippet object. |  -  |
**401** | If the snippet is private and the request was not authenticated. |  -  |
**403** | If authenticated user does not have permission to update the private snippet. |  -  |
**404** | If the snippet does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snippets_by_username_by_encoded_id_by_node_id**
> Snippet update_snippets_by_username_by_encoded_id_by_node_id(username, encoded_id, node_id)



Identical to `UPDATE /snippets/encoded_id`, except that this endpoint takes an explicit commit revision. Only the snippet's \"HEAD\"/\"tip\" (most recent) version can be updated and requests on all other, older revisions fail by returning a 405 status.  Usage of this endpoint over the unrestricted `/snippets/encoded_id` could be desired if the caller wants to be sure no concurrent modifications have taken place between the moment of the UPDATE request and the original GET.  This can be considered a so-called \"Compare And Swap\", or CAS operation.  Other than that, the two endpoints are identical in behavior.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet's id.
node_id = 'node_id_example' # str | A commit revision (SHA1).

try:
    api_response = api_instance.update_snippets_by_username_by_encoded_id_by_node_id(username, encoded_id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->update_snippets_by_username_by_encoded_id_by_node_id: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet's id.
node_id = 'node_id_example' # str | A commit revision (SHA1).

try:
    api_response = api_instance.update_snippets_by_username_by_encoded_id_by_node_id(username, encoded_id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->update_snippets_by_username_by_encoded_id_by_node_id: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet's id.
node_id = 'node_id_example' # str | A commit revision (SHA1).

try:
    api_response = api_instance.update_snippets_by_username_by_encoded_id_by_node_id(username, encoded_id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->update_snippets_by_username_by_encoded_id_by_node_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **encoded_id** | **str**| The snippet&#39;s id. | 
 **node_id** | **str**| A commit revision (SHA1). | 

### Return type

[**Snippet**](Snippet.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, multipart/related, multipart/form-data

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated snippet object. |  -  |
**401** | If the snippet is private and the request was not authenticated. |  -  |
**403** | If authenticated user does not have permission to update the private snippet. |  -  |
**404** | If the snippet or the revision does not exist. |  -  |
**405** | If &#x60;{node_id}&#x60; is not the latest revision. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snippets_by_username_by_encoded_id_comments_by_comment_id**
> update_snippets_by_username_by_encoded_id_comments_by_comment_id(username, comment_id, encoded_id)



Updates a comment.  Comments can only be updated by their author.

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
comment_id = 'comment_id_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_instance.update_snippets_by_username_by_encoded_id_comments_by_comment_id(username, comment_id, encoded_id)
except ApiException as e:
    print("Exception when calling SnippetsApi->update_snippets_by_username_by_encoded_id_comments_by_comment_id: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
comment_id = 'comment_id_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_instance.update_snippets_by_username_by_encoded_id_comments_by_comment_id(username, comment_id, encoded_id)
except ApiException as e:
    print("Exception when calling SnippetsApi->update_snippets_by_username_by_encoded_id_comments_by_comment_id: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
comment_id = 'comment_id_example' # str | 
encoded_id = 'encoded_id_example' # str | 

try:
    api_instance.update_snippets_by_username_by_encoded_id_comments_by_comment_id(username, comment_id, encoded_id)
except ApiException as e:
    print("Exception when calling SnippetsApi->update_snippets_by_username_by_encoded_id_comments_by_comment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **comment_id** | **str**|  | 
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
**200** | The updated comment object. |  -  |
**403** | If the authenticated user does not have access to the snippet. |  -  |
**404** | If the comment or snippet does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snippets_by_username_by_encoded_id_watch**
> PaginatedUsers update_snippets_by_username_by_encoded_id_watch(username, encoded_id)



Used to start watching a specific snippet. Returns 204 (No Content).

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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet id.

try:
    api_response = api_instance.update_snippets_by_username_by_encoded_id_watch(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->update_snippets_by_username_by_encoded_id_watch: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet id.

try:
    api_response = api_instance.update_snippets_by_username_by_encoded_id_watch(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->update_snippets_by_username_by_encoded_id_watch: %s\n" % e)
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
api_instance = bitbucketopenapi.SnippetsApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
encoded_id = 'encoded_id_example' # str | The snippet id.

try:
    api_response = api_instance.update_snippets_by_username_by_encoded_id_watch(username, encoded_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnippetsApi->update_snippets_by_username_by_encoded_id_watch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **encoded_id** | **str**| The snippet id. | 

### Return type

[**PaginatedUsers**](PaginatedUsers.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Indicates the authenticated user is now watching the snippet. |  -  |
**401** | If the request was not authenticated. |  -  |
**404** | If the snippet does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


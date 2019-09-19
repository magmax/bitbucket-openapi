# bitbucketopenapi.SearchApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_account**](SearchApi.md#search_account) | **GET** /teams/{username}/search/code | Search for code in the repositories of the specified team
[**search_account_0**](SearchApi.md#search_account_0) | **GET** /users/{username}/search/code | Search for code in the repositories of the specified user


# **search_account**
> SearchResultPage search_account(username, search_query, page=page, pagelen=pagelen)

Search for code in the repositories of the specified team

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.SearchApi()
username = 'username_example' # str | The account to search in; either the username or the UUID in curly braces
search_query = 'search_query_example' # str | The search query
page = 1 # int | Which page of the search results to retrieve (optional) (default to 1)
pagelen = 10 # int | How many search results to retrieve per page (optional) (default to 10)

try:
    # Search for code in the repositories of the specified team
    api_response = api_instance.search_account(username, search_query, page=page, pagelen=pagelen)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account to search in; either the username or the UUID in curly braces | 
 **search_query** | **str**| The search query | 
 **page** | **int**| Which page of the search results to retrieve | [optional] [default to 1]
 **pagelen** | **int**| How many search results to retrieve per page | [optional] [default to 10]

### Return type

[**SearchResultPage**](SearchResultPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful search |  -  |
**400** | If the search request was invalid due to one of the following reasons: * the specified type of target account doesn&#39;t match the actual account type; * malformed pagination properties; * missing or malformed search query, in the latter case an error key will be returned in &#x60;error.data.key&#x60; property. |  -  |
**404** | Search is not enabled for the requested team, navigate to [https://bitbucket.org/search](https://bitbucket.org/search) to turn it on |  -  |
**429** | Too many requests, try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_account_0**
> SearchResultPage search_account_0(username, search_query, page=page, pagelen=pagelen)

Search for code in the repositories of the specified user

### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.SearchApi()
username = 'username_example' # str | The account to search in; either the username or the UUID in curly braces
search_query = 'search_query_example' # str | The search query
page = 1 # int | Which page of the search results to retrieve (optional) (default to 1)
pagelen = 10 # int | How many search results to retrieve per page (optional) (default to 10)

try:
    # Search for code in the repositories of the specified user
    api_response = api_instance.search_account_0(username, search_query, page=page, pagelen=pagelen)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_account_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The account to search in; either the username or the UUID in curly braces | 
 **search_query** | **str**| The search query | 
 **page** | **int**| Which page of the search results to retrieve | [optional] [default to 1]
 **pagelen** | **int**| How many search results to retrieve per page | [optional] [default to 10]

### Return type

[**SearchResultPage**](SearchResultPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful search |  -  |
**400** | If the search request was invalid due to one of the following reasons: * the specified type of target account doesn&#39;t match the actual account type; * malformed pagination properties; * missing or malformed search query, in the latter case an error key will be returned in &#x60;error.data.key&#x60; property. |  -  |
**404** | Search is not enabled for the requested user, navigate to [https://bitbucket.org/search](https://bitbucket.org/search) to turn it on |  -  |
**429** | Too many requests, try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


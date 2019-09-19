# bitbucketopenapi.IssueTrackerApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_repositories_by_username_by_repo_slug_issues**](IssueTrackerApi.md#create_repositories_by_username_by_repo_slug_issues) | **POST** /repositories/{username}/{repo_slug}/issues | 
[**create_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments**](IssueTrackerApi.md#create_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments) | **POST** /repositories/{username}/{repo_slug}/issues/{issue_id}/attachments | 
[**create_repositories_by_username_by_repo_slug_issues_by_issue_id_changes**](IssueTrackerApi.md#create_repositories_by_username_by_repo_slug_issues_by_issue_id_changes) | **POST** /repositories/{username}/{repo_slug}/issues/{issue_id}/changes | 
[**create_repositories_by_username_by_repo_slug_issues_by_issue_id_comments**](IssueTrackerApi.md#create_repositories_by_username_by_repo_slug_issues_by_issue_id_comments) | **POST** /repositories/{username}/{repo_slug}/issues/{issue_id}/comments | 
[**delete_repositories_by_username_by_repo_slug_issues_by_issue_id**](IssueTrackerApi.md#delete_repositories_by_username_by_repo_slug_issues_by_issue_id) | **DELETE** /repositories/{username}/{repo_slug}/issues/{issue_id} | 
[**delete_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path**](IssueTrackerApi.md#delete_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path) | **DELETE** /repositories/{username}/{repo_slug}/issues/{issue_id}/attachments/{path} | 
[**delete_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id**](IssueTrackerApi.md#delete_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id) | **DELETE** /repositories/{username}/{repo_slug}/issues/{issue_id}/comments/{comment_id} | 
[**delete_repositories_by_username_by_repo_slug_issues_by_issue_id_vote**](IssueTrackerApi.md#delete_repositories_by_username_by_repo_slug_issues_by_issue_id_vote) | **DELETE** /repositories/{username}/{repo_slug}/issues/{issue_id}/vote | 
[**delete_repositories_by_username_by_repo_slug_issues_by_issue_id_watch**](IssueTrackerApi.md#delete_repositories_by_username_by_repo_slug_issues_by_issue_id_watch) | **DELETE** /repositories/{username}/{repo_slug}/issues/{issue_id}/watch | 
[**get_repositories_by_username_by_repo_slug_components**](IssueTrackerApi.md#get_repositories_by_username_by_repo_slug_components) | **GET** /repositories/{username}/{repo_slug}/components | 
[**get_repositories_by_username_by_repo_slug_components_by_component_id**](IssueTrackerApi.md#get_repositories_by_username_by_repo_slug_components_by_component_id) | **GET** /repositories/{username}/{repo_slug}/components/{component_id} | 
[**get_repositories_by_username_by_repo_slug_issues**](IssueTrackerApi.md#get_repositories_by_username_by_repo_slug_issues) | **GET** /repositories/{username}/{repo_slug}/issues | 
[**get_repositories_by_username_by_repo_slug_issues_by_issue_id**](IssueTrackerApi.md#get_repositories_by_username_by_repo_slug_issues_by_issue_id) | **GET** /repositories/{username}/{repo_slug}/issues/{issue_id} | 
[**get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments**](IssueTrackerApi.md#get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments) | **GET** /repositories/{username}/{repo_slug}/issues/{issue_id}/attachments | 
[**get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path**](IssueTrackerApi.md#get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path) | **GET** /repositories/{username}/{repo_slug}/issues/{issue_id}/attachments/{path} | 
[**get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes**](IssueTrackerApi.md#get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes) | **GET** /repositories/{username}/{repo_slug}/issues/{issue_id}/changes | 
[**get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes_by_change_id**](IssueTrackerApi.md#get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes_by_change_id) | **GET** /repositories/{username}/{repo_slug}/issues/{issue_id}/changes/{change_id} | 
[**get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments**](IssueTrackerApi.md#get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments) | **GET** /repositories/{username}/{repo_slug}/issues/{issue_id}/comments | 
[**get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id**](IssueTrackerApi.md#get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id) | **GET** /repositories/{username}/{repo_slug}/issues/{issue_id}/comments/{comment_id} | 
[**get_repositories_by_username_by_repo_slug_issues_by_issue_id_vote**](IssueTrackerApi.md#get_repositories_by_username_by_repo_slug_issues_by_issue_id_vote) | **GET** /repositories/{username}/{repo_slug}/issues/{issue_id}/vote | 
[**get_repositories_by_username_by_repo_slug_issues_by_issue_id_watch**](IssueTrackerApi.md#get_repositories_by_username_by_repo_slug_issues_by_issue_id_watch) | **GET** /repositories/{username}/{repo_slug}/issues/{issue_id}/watch | 
[**get_repositories_by_username_by_repo_slug_milestones**](IssueTrackerApi.md#get_repositories_by_username_by_repo_slug_milestones) | **GET** /repositories/{username}/{repo_slug}/milestones | 
[**get_repositories_by_username_by_repo_slug_milestones_by_milestone_id**](IssueTrackerApi.md#get_repositories_by_username_by_repo_slug_milestones_by_milestone_id) | **GET** /repositories/{username}/{repo_slug}/milestones/{milestone_id} | 
[**get_repositories_by_username_by_repo_slug_versions**](IssueTrackerApi.md#get_repositories_by_username_by_repo_slug_versions) | **GET** /repositories/{username}/{repo_slug}/versions | 
[**get_repositories_by_username_by_repo_slug_versions_by_version_id**](IssueTrackerApi.md#get_repositories_by_username_by_repo_slug_versions_by_version_id) | **GET** /repositories/{username}/{repo_slug}/versions/{version_id} | 
[**update_repositories_by_username_by_repo_slug_issues_by_issue_id**](IssueTrackerApi.md#update_repositories_by_username_by_repo_slug_issues_by_issue_id) | **PUT** /repositories/{username}/{repo_slug}/issues/{issue_id} | 
[**update_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id**](IssueTrackerApi.md#update_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id) | **PUT** /repositories/{username}/{repo_slug}/issues/{issue_id}/comments/{comment_id} | 
[**update_repositories_by_username_by_repo_slug_issues_by_issue_id_vote**](IssueTrackerApi.md#update_repositories_by_username_by_repo_slug_issues_by_issue_id_vote) | **PUT** /repositories/{username}/{repo_slug}/issues/{issue_id}/vote | 
[**update_repositories_by_username_by_repo_slug_issues_by_issue_id_watch**](IssueTrackerApi.md#update_repositories_by_username_by_repo_slug_issues_by_issue_id_watch) | **PUT** /repositories/{username}/{repo_slug}/issues/{issue_id}/watch | 


# **create_repositories_by_username_by_repo_slug_issues**
> Issue create_repositories_by_username_by_repo_slug_issues(username, repo_slug, body)



Creates a new issue.  This call requires authentication. Private repositories or private issue trackers require the caller to authenticate with an account that has appropriate authorization.  The authenticated user is used for the issue's `reporter` field.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
body = bitbucketopenapi.Issue() # Issue | The new issue. The only required element is `title`. All other elements can be omitted from the body.

try:
    api_response = api_instance.create_repositories_by_username_by_repo_slug_issues(username, repo_slug, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->create_repositories_by_username_by_repo_slug_issues: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
body = bitbucketopenapi.Issue() # Issue | The new issue. The only required element is `title`. All other elements can be omitted from the body.

try:
    api_response = api_instance.create_repositories_by_username_by_repo_slug_issues(username, repo_slug, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->create_repositories_by_username_by_repo_slug_issues: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
body = bitbucketopenapi.Issue() # Issue | The new issue. The only required element is `title`. All other elements can be omitted from the body.

try:
    api_response = api_instance.create_repositories_by_username_by_repo_slug_issues(username, repo_slug, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->create_repositories_by_username_by_repo_slug_issues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **body** | [**Issue**](Issue.md)| The new issue. The only required element is &#x60;title&#x60;. All other elements can be omitted from the body. | 

### Return type

[**Issue**](Issue.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created issue. |  * Location - The (absolute) URL of the newly created issue. <br>  |
**401** | When the request wasn&#39;t authenticated. |  -  |
**403** | When the authenticated user isn&#39;t authorized to create the issue. |  -  |
**404** | The specified repository does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments**
> create_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments(username, repo_slug, issue_id)



Upload new issue attachments.  To upload files, perform a `multipart/form-data` POST containing one or more file fields.  When a file is uploaded with the same name as an existing attachment, then the existing file will be replaced.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
repo_slug = 'repo_slug_example' # str | 
issue_id = 56 # int | The issue's id

try:
    api_instance.create_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments(username, repo_slug, issue_id)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->create_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
repo_slug = 'repo_slug_example' # str | 
issue_id = 56 # int | The issue's id

try:
    api_instance.create_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments(username, repo_slug, issue_id)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->create_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
repo_slug = 'repo_slug_example' # str | 
issue_id = 56 # int | The issue's id

try:
    api_instance.create_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments(username, repo_slug, issue_id)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->create_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **repo_slug** | **str**|  | 
 **issue_id** | **int**| The issue&#39;s id | 

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
**201** | An empty response document. |  * Location - The URL to the issue&#39;s collection of attachments. <br>  |
**400** | If no files were uploaded, or if the wrong &#x60;Content-Type&#x60; was used. |  -  |
**401** | If the issue tracker is private and the request was not authenticated. |  -  |
**404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repositories_by_username_by_repo_slug_issues_by_issue_id_changes**
> IssueChange create_repositories_by_username_by_repo_slug_issues_by_issue_id_changes(username, issue_id, repo_slug, body)



Makes a change to the specified issue.  For example, to change an issue's state and assignee, create a new change object that modifies these fields:  ``` curl https://api.bitbucket.org/2.0/site/master/issues/1234/changes \\   -s -u evzijst -X POST -H \"Content-Type: application/json\" \\   -d '{     \"changes\": {       \"assignee_account_id\": {         \"new\": \"557058:c0b72ad0-1cb5-4018-9cdc-0cde8492c443\"       },       \"state\": {         \"new\": 'resolved\"       }     }     \"message\": {       \"raw\": \"This is now resolved.\"     }   }' ```  The above example also includes a custom comment to go alongside the change. This comment will also be visible on the issue page in the UI.  The fields of the `changes` object are strings, not objects. This allows for immutable change log records, even after user accounts, milestones, or other objects recorded in a change entry, get renamed or deleted.  The `assignee_account_id` field stores the account id. When POSTing a new change and changing the assignee, the client should therefore use the user's account_id in the `changes.assignee_account_id.new` field.  This call requires authentication. Private repositories or private issue trackers require the caller to authenticate with an account that has appropriate authorization.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
body = bitbucketopenapi.IssueChange() # IssueChange | The new issue state change. The only required elements are `changes.[].new`. All other elements can be omitted from the body.

try:
    api_response = api_instance.create_repositories_by_username_by_repo_slug_issues_by_issue_id_changes(username, issue_id, repo_slug, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->create_repositories_by_username_by_repo_slug_issues_by_issue_id_changes: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
body = bitbucketopenapi.IssueChange() # IssueChange | The new issue state change. The only required elements are `changes.[].new`. All other elements can be omitted from the body.

try:
    api_response = api_instance.create_repositories_by_username_by_repo_slug_issues_by_issue_id_changes(username, issue_id, repo_slug, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->create_repositories_by_username_by_repo_slug_issues_by_issue_id_changes: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
body = bitbucketopenapi.IssueChange() # IssueChange | The new issue state change. The only required elements are `changes.[].new`. All other elements can be omitted from the body.

try:
    api_response = api_instance.create_repositories_by_username_by_repo_slug_issues_by_issue_id_changes(username, issue_id, repo_slug, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->create_repositories_by_username_by_repo_slug_issues_by_issue_id_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **issue_id** | **str**| The issue id | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **body** | [**IssueChange**](IssueChange.md)| The new issue state change. The only required elements are &#x60;changes.[].new&#x60;. All other elements can be omitted from the body. | 

### Return type

[**IssueChange**](IssueChange.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created issue change. |  * Location - The (absolute) URL of the newly created issue change. <br>  |
**401** | When the request wasn&#39;t authenticated. |  -  |
**403** | When the authenticated user isn&#39;t authorized to modify the issue. |  -  |
**404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repositories_by_username_by_repo_slug_issues_by_issue_id_comments**
> create_repositories_by_username_by_repo_slug_issues_by_issue_id_comments(issue_id, username, repo_slug, body)



Creates a new issue comment.  ``` $ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/issues/42/comments/ \\   -X POST -u evzijst \\   -H 'Content-Type: application/json' \\   -d '{\"content\": {\"raw\": \"Lorem ipsum.\"}}' ```

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
issue_id = 'issue_id_example' # str | 
username = 'username_example' # str | This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
body = bitbucketopenapi.IssueComment() # IssueComment | The new issue comment object.

try:
    api_instance.create_repositories_by_username_by_repo_slug_issues_by_issue_id_comments(issue_id, username, repo_slug, body)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->create_repositories_by_username_by_repo_slug_issues_by_issue_id_comments: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
issue_id = 'issue_id_example' # str | 
username = 'username_example' # str | This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
body = bitbucketopenapi.IssueComment() # IssueComment | The new issue comment object.

try:
    api_instance.create_repositories_by_username_by_repo_slug_issues_by_issue_id_comments(issue_id, username, repo_slug, body)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->create_repositories_by_username_by_repo_slug_issues_by_issue_id_comments: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
issue_id = 'issue_id_example' # str | 
username = 'username_example' # str | This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
body = bitbucketopenapi.IssueComment() # IssueComment | The new issue comment object.

try:
    api_instance.create_repositories_by_username_by_repo_slug_issues_by_issue_id_comments(issue_id, username, repo_slug, body)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->create_repositories_by_username_by_repo_slug_issues_by_issue_id_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id** | **str**|  | 
 **username** | **str**| This can either be the username or the UUID of the user, surrounded by curly-braces, for example: &#x60;{user UUID}&#x60;.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **body** | [**IssueComment**](IssueComment.md)| The new issue comment object. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created comment. |  * Location - The location of the newly issue comment. <br>  |
**400** | If the input was invalid, or if the comment being created is detected as spam  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repositories_by_username_by_repo_slug_issues_by_issue_id**
> Issue delete_repositories_by_username_by_repo_slug_issues_by_issue_id(username, issue_id, repo_slug)



Deletes the specified issue. This requires write access to the repository.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.delete_repositories_by_username_by_repo_slug_issues_by_issue_id(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->delete_repositories_by_username_by_repo_slug_issues_by_issue_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.delete_repositories_by_username_by_repo_slug_issues_by_issue_id(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->delete_repositories_by_username_by_repo_slug_issues_by_issue_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.delete_repositories_by_username_by_repo_slug_issues_by_issue_id(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->delete_repositories_by_username_by_repo_slug_issues_by_issue_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **issue_id** | **str**| The issue id | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**Issue**](Issue.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The issue object. |  -  |
**403** | When the authenticated user isn&#39;t authorized to delete the issue. |  -  |
**404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path**
> delete_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path(username, path, issue_id, repo_slug)



Deletes an attachment.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
path = 'path_example' # str | 
issue_id = 'issue_id_example' # str | 
repo_slug = 'repo_slug_example' # str | 

try:
    api_instance.delete_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path(username, path, issue_id, repo_slug)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->delete_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
path = 'path_example' # str | 
issue_id = 'issue_id_example' # str | 
repo_slug = 'repo_slug_example' # str | 

try:
    api_instance.delete_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path(username, path, issue_id, repo_slug)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->delete_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
path = 'path_example' # str | 
issue_id = 'issue_id_example' # str | 
repo_slug = 'repo_slug_example' # str | 

try:
    api_instance.delete_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path(username, path, issue_id, repo_slug)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->delete_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **path** | **str**|  | 
 **issue_id** | **str**|  | 
 **repo_slug** | **str**|  | 

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
**204** | Indicates that the deletion was successful |  -  |
**401** | If the issue tracker is private and the request was not authenticated. |  -  |
**404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id**
> delete_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id(comment_id, username, repo_slug, issue_id, body)



Deletes the specified comment.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
comment_id = 'comment_id_example' # str | 
username = 'username_example' # str | This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
issue_id = 'issue_id_example' # str | The ID of the issue that is being queried. 
body = bitbucketopenapi.IssueComment() # IssueComment | The updated comment.

try:
    api_instance.delete_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id(comment_id, username, repo_slug, issue_id, body)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->delete_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
comment_id = 'comment_id_example' # str | 
username = 'username_example' # str | This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
issue_id = 'issue_id_example' # str | The ID of the issue that is being queried. 
body = bitbucketopenapi.IssueComment() # IssueComment | The updated comment.

try:
    api_instance.delete_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id(comment_id, username, repo_slug, issue_id, body)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->delete_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
comment_id = 'comment_id_example' # str | 
username = 'username_example' # str | This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
issue_id = 'issue_id_example' # str | The ID of the issue that is being queried. 
body = bitbucketopenapi.IssueComment() # IssueComment | The updated comment.

try:
    api_instance.delete_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id(comment_id, username, repo_slug, issue_id, body)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->delete_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **username** | **str**| This can either be the username or the UUID of the user, surrounded by curly-braces, for example: &#x60;{user UUID}&#x60;.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **issue_id** | **str**| The ID of the issue that is being queried.  | 
 **body** | [**IssueComment**](IssueComment.md)| The updated comment. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Indicates successful deletion. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repositories_by_username_by_repo_slug_issues_by_issue_id_vote**
> Error delete_repositories_by_username_by_repo_slug_issues_by_issue_id_vote(username, issue_id, repo_slug)



Retract your vote.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.delete_repositories_by_username_by_repo_slug_issues_by_issue_id_vote(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->delete_repositories_by_username_by_repo_slug_issues_by_issue_id_vote: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.delete_repositories_by_username_by_repo_slug_issues_by_issue_id_vote(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->delete_repositories_by_username_by_repo_slug_issues_by_issue_id_vote: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.delete_repositories_by_username_by_repo_slug_issues_by_issue_id_vote(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->delete_repositories_by_username_by_repo_slug_issues_by_issue_id_vote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **issue_id** | **str**| The issue id | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**Error**](Error.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repositories_by_username_by_repo_slug_issues_by_issue_id_watch**
> Error delete_repositories_by_username_by_repo_slug_issues_by_issue_id_watch(username, issue_id, repo_slug)



Stop watching this issue.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.delete_repositories_by_username_by_repo_slug_issues_by_issue_id_watch(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->delete_repositories_by_username_by_repo_slug_issues_by_issue_id_watch: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.delete_repositories_by_username_by_repo_slug_issues_by_issue_id_watch(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->delete_repositories_by_username_by_repo_slug_issues_by_issue_id_watch: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.delete_repositories_by_username_by_repo_slug_issues_by_issue_id_watch(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->delete_repositories_by_username_by_repo_slug_issues_by_issue_id_watch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **issue_id** | **str**| The issue id | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**Error**](Error.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Indicates that the authenticated user successfully stopped watching this issue. |  -  |
**401** | When the request wasn&#39;t authenticated. |  -  |
**404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_components**
> PaginatedComponents get_repositories_by_username_by_repo_slug_components(username, repo_slug)



Returns the components that have been defined in the issue tracker.  This resource is only available on repositories that have the issue tracker enabled.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_components(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_components: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_components(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_components: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_components(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**PaginatedComponents**](PaginatedComponents.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The components that have been defined in the issue tracker. |  -  |
**404** | The specified repository does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_components_by_component_id**
> Component get_repositories_by_username_by_repo_slug_components_by_component_id(username, component_id, repo_slug)



Returns the specified issue tracker component object.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
component_id = 56 # int | The component's id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_components_by_component_id(username, component_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_components_by_component_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
component_id = 56 # int | The component's id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_components_by_component_id(username, component_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_components_by_component_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
component_id = 56 # int | The component's id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_components_by_component_id(username, component_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_components_by_component_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **component_id** | **int**| The component&#39;s id | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**Component**](Component.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The specified component object. |  -  |
**404** | The specified repository or component does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_issues**
> PaginatedIssues get_repositories_by_username_by_repo_slug_issues(username, repo_slug)



Returns the issues in the issue tracker.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**PaginatedIssues**](PaginatedIssues.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of the issues matching any filter criteria that were provided. |  -  |
**404** | The specified repository does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_issues_by_issue_id**
> Issue get_repositories_by_username_by_repo_slug_issues_by_issue_id(username, issue_id, repo_slug)



Returns the specified issue.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **issue_id** | **str**| The issue id | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**Issue**](Issue.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The issue object. |  -  |
**403** | When the authenticated user isn&#39;t authorized to access the issue. |  -  |
**404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments**
> PaginatedIssueAttachments get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments(username, repo_slug, issue_id)



Returns all attachments for this issue.  This returns the files' meta data. This does not return the files' actual contents.  The files are always ordered by their upload date.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
repo_slug = 'repo_slug_example' # str | 
issue_id = 56 # int | The issue's id

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments(username, repo_slug, issue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
repo_slug = 'repo_slug_example' # str | 
issue_id = 56 # int | The issue's id

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments(username, repo_slug, issue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
repo_slug = 'repo_slug_example' # str | 
issue_id = 56 # int | The issue's id

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments(username, repo_slug, issue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **repo_slug** | **str**|  | 
 **issue_id** | **int**| The issue&#39;s id | 

### Return type

[**PaginatedIssueAttachments**](PaginatedIssueAttachments.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of all attachments for this issue. |  -  |
**401** | If the issue tracker is private and the request was not authenticated. |  -  |
**404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path**
> get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path(username, path, issue_id, repo_slug)



Returns the contents of the specified file attachment.  Note that this endpoint does not return a JSON response, but instead returns a redirect pointing to the actual file that in turn will return the raw contents.  The redirect URL contains a one-time token that has a limited lifetime. As a result, the link should not be persisted, stored, or shared.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
path = 'path_example' # str | 
issue_id = 'issue_id_example' # str | 
repo_slug = 'repo_slug_example' # str | 

try:
    api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path(username, path, issue_id, repo_slug)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
path = 'path_example' # str | 
issue_id = 'issue_id_example' # str | 
repo_slug = 'repo_slug_example' # str | 

try:
    api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path(username, path, issue_id, repo_slug)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | 
path = 'path_example' # str | 
issue_id = 'issue_id_example' # str | 
repo_slug = 'repo_slug_example' # str | 

try:
    api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path(username, path, issue_id, repo_slug)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_attachments_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **path** | **str**|  | 
 **issue_id** | **str**|  | 
 **repo_slug** | **str**|  | 

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
**302** | A redirect to the file&#39;s contents |  * Location -  <br>  |
**401** | If the issue tracker is private and the request was not authenticated. |  -  |
**404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes**
> PaginatedLogEntries get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes(username, issue_id, repo_slug, q=q, sort=sort)



Returns the list of all changes that have been made to the specified issue. Changes are returned in chronological order with the oldest change first.  Each time an issue is edited in the UI or through the API, an immutable change record is created under the `/issues/123/changes` endpoint. It also has a comment associated with the change.  Note that this operation is changing significantly, due to privacy changes. See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-gdpr/#changes-to-the-issue-changes-api) for details.  ``` $ curl -s https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1/changes - | jq .  {   \"pagelen\": 20,   \"values\": [     {       \"changes\": {         \"priority\": {           \"new\": \"trivial\",           \"old\": \"major\"         },         \"assignee\": {           \"new\": \"\",           \"old\": \"evzijst\"         },         \"assignee_account_id\": {           \"new\": \"\",           \"old\": \"557058:c0b72ad0-1cb5-4018-9cdc-0cde8492c443\"         },         \"kind\": {           \"new\": \"enhancement\",           \"old\": \"bug\"         }       },       \"links\": {         \"self\": {           \"href\": \"https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1/changes/2\"         },         \"html\": {           \"href\": \"https://bitbucket.org/evzijst/dogslow/issues/1#comment-2\"         }       },       \"issue\": {         \"links\": {           \"self\": {             \"href\": \"https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1\"           }         },         \"type\": \"issue\",         \"id\": 1,         \"repository\": {           \"links\": {             \"self\": {               \"href\": \"https://api.bitbucket.org/2.0/repositories/evzijst/dogslow\"             },             \"html\": {               \"href\": \"https://bitbucket.org/evzijst/dogslow\"             },             \"avatar\": {               \"href\": \"https://bitbucket.org/evzijst/dogslow/avatar/32/\"             }           },           \"type\": \"repository\",           \"name\": \"dogslow\",           \"full_name\": \"evzijst/dogslow\",           \"uuid\": \"{988b17c6-1a47-4e70-84ee-854d5f012bf6}\"         },         \"title\": \"Updated title\"       },       \"created_on\": \"2018-03-03T00:35:28.353630+00:00\",       \"user\": {         \"username\": \"evzijst\",         \"nickname\": \"evzijst\",         \"display_name\": \"evzijst\",         \"type\": \"user\",         \"uuid\": \"{aaa7972b-38af-4fb1-802d-6e3854c95778}\",         \"links\": {           \"self\": {             \"href\": \"https://api.bitbucket.org/2.0/users/evzijst\"           },           \"html\": {             \"href\": \"https://bitbucket.org/evzijst/\"           },           \"avatar\": {             \"href\": \"https://bitbucket.org/account/evzijst/avatar/32/\"           }         }       },       \"message\": {         \"raw\": \"Removed assignee, changed kind and priority.\",         \"markup\": \"markdown\",         \"html\": \"<p>Removed assignee, changed kind and priority.</p>\",         \"type\": \"rendered\"       },       \"type\": \"issue_change\",       \"id\": 2     }   ],   \"page\": 1 } ```  Changes support [filtering and sorting](../../../meta/filtering) that can be used to search for specific changes. For instance, to see when an issue transitioned to \"resolved\":  ``` $ curl -s https://api.bitbucket.org/2.0/repositories/site/master/issues/1/changes \\    -G --data-urlencode='q=changes.state.new = \"resolved\"' ```  This resource is only available on repositories that have the issue tracker enabled.  N.B.  The `changes.assignee` and `changes.assignee_account_id` fields are not a `user` object. Instead, they contain the raw `username` and `account_id` of the user. This is to protect the integrity of the audit log even after a user account gets deleted.  The `changes.assignee` field is deprecated will disappear in the future. Use `changes.assignee_account_id` instead.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
q = 'q_example' # str |  Query string to narrow down the response. See [filtering and sorting](../../../meta/filtering) for details. (optional)
sort = 'sort_example' # str |  Name of a response property to sort results. See [filtering and sorting](../../../meta/filtering#query-sort) for details.  (optional)

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes(username, issue_id, repo_slug, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
q = 'q_example' # str |  Query string to narrow down the response. See [filtering and sorting](../../../meta/filtering) for details. (optional)
sort = 'sort_example' # str |  Name of a response property to sort results. See [filtering and sorting](../../../meta/filtering#query-sort) for details.  (optional)

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes(username, issue_id, repo_slug, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
q = 'q_example' # str |  Query string to narrow down the response. See [filtering and sorting](../../../meta/filtering) for details. (optional)
sort = 'sort_example' # str |  Name of a response property to sort results. See [filtering and sorting](../../../meta/filtering#query-sort) for details.  (optional)

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes(username, issue_id, repo_slug, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **issue_id** | **str**| The issue id | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **q** | **str**|  Query string to narrow down the response. See [filtering and sorting](../../../meta/filtering) for details. | [optional] 
 **sort** | **str**|  Name of a response property to sort results. See [filtering and sorting](../../../meta/filtering#query-sort) for details.  | [optional] 

### Return type

[**PaginatedLogEntries**](PaginatedLogEntries.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all the issue changes that were made on the specified issue. |  -  |
**404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes_by_change_id**
> IssueChange get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes_by_change_id(username, change_id, issue_id, repo_slug)



Returns the specified issue change object.  This resource is only available on repositories that have the issue tracker enabled.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
change_id = 'change_id_example' # str | The issue change id
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes_by_change_id(username, change_id, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes_by_change_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
change_id = 'change_id_example' # str | The issue change id
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes_by_change_id(username, change_id, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes_by_change_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
change_id = 'change_id_example' # str | The issue change id
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes_by_change_id(username, change_id, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_changes_by_change_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **change_id** | **str**| The issue change id | 
 **issue_id** | **str**| The issue id | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**IssueChange**](IssueChange.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The specified issue change object. |  -  |
**404** | The specified repository or issue change does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments**
> PaginatedIssueComments get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments(issue_id, username, repo_slug, q=q)



Returns a paginated list of all comments that were made on the specified issue.  The default sorting is oldest to newest and can be overridden with the `sort` query parameter.  This endpoint also supports filtering and sorting of the results. See [filtering and sorting](../../../../../../meta/filtering) for more details.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
issue_id = 'issue_id_example' # str | 
username = 'username_example' # str | This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../../../../meta/filtering). (optional)

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments(issue_id, username, repo_slug, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
issue_id = 'issue_id_example' # str | 
username = 'username_example' # str | This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../../../../meta/filtering). (optional)

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments(issue_id, username, repo_slug, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
issue_id = 'issue_id_example' # str | 
username = 'username_example' # str | This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../../../../meta/filtering). (optional)

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments(issue_id, username, repo_slug, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id** | **str**|  | 
 **username** | **str**| This can either be the username or the UUID of the user, surrounded by curly-braces, for example: &#x60;{user UUID}&#x60;.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **q** | **str**|  Query string to narrow down the response as per [filtering and sorting](../../../../../../meta/filtering). | [optional] 

### Return type

[**PaginatedIssueComments**](PaginatedIssueComments.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of issue comments. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id**
> IssueComment get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id(comment_id, username, repo_slug, issue_id)



Returns the specified issue comment object.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
comment_id = 'comment_id_example' # str | 
username = 'username_example' # str | This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
issue_id = 'issue_id_example' # str | The ID of the issue that is being queried. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id(comment_id, username, repo_slug, issue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
comment_id = 'comment_id_example' # str | 
username = 'username_example' # str | This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
issue_id = 'issue_id_example' # str | The ID of the issue that is being queried. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id(comment_id, username, repo_slug, issue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
comment_id = 'comment_id_example' # str | 
username = 'username_example' # str | This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
issue_id = 'issue_id_example' # str | The ID of the issue that is being queried. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id(comment_id, username, repo_slug, issue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **username** | **str**| This can either be the username or the UUID of the user, surrounded by curly-braces, for example: &#x60;{user UUID}&#x60;.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **issue_id** | **str**| The ID of the issue that is being queried.  | 

### Return type

[**IssueComment**](IssueComment.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The issue comment. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_issues_by_issue_id_vote**
> Error get_repositories_by_username_by_repo_slug_issues_by_issue_id_vote(username, issue_id, repo_slug)



Check whether the authenticated user has voted for this issue. A 204 status code indicates that the user has voted, while a 404 implies they haven't.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_vote(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_vote: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_vote(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_vote: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_vote(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_vote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **issue_id** | **str**| The issue id | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**Error**](Error.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | If the authenticated user has not voted for this issue. |  -  |
**401** | When the request wasn&#39;t authenticated. |  -  |
**404** | If the authenticated user has not voted for this issue, or when the repo does not exist, or does not have an issue tracker. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_issues_by_issue_id_watch**
> Error get_repositories_by_username_by_repo_slug_issues_by_issue_id_watch(username, issue_id, repo_slug)



Indicated whether or not the authenticated user is watching this issue.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_watch(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_watch: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_watch(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_watch: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_by_issue_id_watch(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_issues_by_issue_id_watch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **issue_id** | **str**| The issue id | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**Error**](Error.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | If the authenticated user is watching this issue. |  -  |
**401** | When the request wasn&#39;t authenticated. |  -  |
**404** | If the authenticated user is not watching this issue, or when the repo does not exist, or does not have an issue tracker. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_milestones**
> PaginatedMilestones get_repositories_by_username_by_repo_slug_milestones(username, repo_slug)



Returns the milestones that have been defined in the issue tracker.  This resource is only available on repositories that have the issue tracker enabled.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_milestones(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_milestones: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_milestones(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_milestones: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_milestones(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_milestones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**PaginatedMilestones**](PaginatedMilestones.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The milestones that have been defined in the issue tracker. |  -  |
**404** | The specified repository does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_milestones_by_milestone_id**
> Milestone get_repositories_by_username_by_repo_slug_milestones_by_milestone_id(username, milestone_id, repo_slug)



Returns the specified issue tracker milestone object.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
milestone_id = 56 # int | The milestone's id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_milestones_by_milestone_id(username, milestone_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_milestones_by_milestone_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
milestone_id = 56 # int | The milestone's id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_milestones_by_milestone_id(username, milestone_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_milestones_by_milestone_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
milestone_id = 56 # int | The milestone's id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_milestones_by_milestone_id(username, milestone_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_milestones_by_milestone_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **milestone_id** | **int**| The milestone&#39;s id | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**Milestone**](Milestone.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The specified milestone object. |  -  |
**404** | The specified repository or milestone does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_versions**
> PaginatedVersions get_repositories_by_username_by_repo_slug_versions(username, repo_slug)



Returns the versions that have been defined in the issue tracker.  This resource is only available on repositories that have the issue tracker enabled.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_versions(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_versions: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_versions(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_versions: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_versions(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**PaginatedVersions**](PaginatedVersions.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The versions that have been defined in the issue tracker. |  -  |
**404** | The specified repository does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_versions_by_version_id**
> Version get_repositories_by_username_by_repo_slug_versions_by_version_id(username, version_id, repo_slug)



Returns the specified issue tracker version object.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
version_id = 56 # int | The version's id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_versions_by_version_id(username, version_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_versions_by_version_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
version_id = 56 # int | The version's id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_versions_by_version_id(username, version_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_versions_by_version_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
version_id = 56 # int | The version's id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_versions_by_version_id(username, version_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->get_repositories_by_username_by_repo_slug_versions_by_version_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **version_id** | **int**| The version&#39;s id | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**Version**](Version.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The specified version object. |  -  |
**404** | The specified repository or version does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repositories_by_username_by_repo_slug_issues_by_issue_id**
> Issue update_repositories_by_username_by_repo_slug_issues_by_issue_id(username, issue_id, repo_slug)



Modifies the issue.  ``` $ curl https://api.bitbucket.org/2.0/repostories/evzijst/dogslow/issues/123 \\   -u evzijst -s -X PUT -H 'Content-Type: application/json' \\   -d '{   \"title\": \"Updated title\",   \"assignee\": {     \"username\": \"evzijst\"   },   \"priority\": \"minor\",   \"version\": {     \"name\": \"1.0\"   },   \"component\": null }' ```  This example changes the `title`, `assignee`, `priority` and the `version`. It also removes the value of the `component` from the issue by setting the field to `null`. Any field not present keeps its existing value.  Each time an issue is edited in the UI or through the API, an immutable change record is created under the `/issues/123/changes` endpoint. It also has a comment associated with the change.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.update_repositories_by_username_by_repo_slug_issues_by_issue_id(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->update_repositories_by_username_by_repo_slug_issues_by_issue_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.update_repositories_by_username_by_repo_slug_issues_by_issue_id(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->update_repositories_by_username_by_repo_slug_issues_by_issue_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.update_repositories_by_username_by_repo_slug_issues_by_issue_id(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->update_repositories_by_username_by_repo_slug_issues_by_issue_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **issue_id** | **str**| The issue id | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**Issue**](Issue.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated issue object. |  -  |
**403** | When the authenticated user isn&#39;t authorized to access the issue. |  -  |
**404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id**
> IssueComment update_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id(comment_id, username, repo_slug, issue_id, body)



Updates the content of the specified issue comment. Note that only the `content.raw` field can be modified.  ``` $ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/issues/42/comments/5728901 \\   -X PUT -u evzijst \\   -H 'Content-Type: application/json' \\   -d '{\"content\": {\"raw\": \"Lorem ipsum.\"}' ```

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
comment_id = 'comment_id_example' # str | 
username = 'username_example' # str | This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
issue_id = 'issue_id_example' # str | The ID of the issue that is being queried. 
body = bitbucketopenapi.IssueComment() # IssueComment | The updated comment.

try:
    api_response = api_instance.update_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id(comment_id, username, repo_slug, issue_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->update_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
comment_id = 'comment_id_example' # str | 
username = 'username_example' # str | This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
issue_id = 'issue_id_example' # str | The ID of the issue that is being queried. 
body = bitbucketopenapi.IssueComment() # IssueComment | The updated comment.

try:
    api_response = api_instance.update_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id(comment_id, username, repo_slug, issue_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->update_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
comment_id = 'comment_id_example' # str | 
username = 'username_example' # str | This can either be the username or the UUID of the user, surrounded by curly-braces, for example: `{user UUID}`. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
issue_id = 'issue_id_example' # str | The ID of the issue that is being queried. 
body = bitbucketopenapi.IssueComment() # IssueComment | The updated comment.

try:
    api_response = api_instance.update_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id(comment_id, username, repo_slug, issue_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->update_repositories_by_username_by_repo_slug_issues_by_issue_id_comments_by_comment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **username** | **str**| This can either be the username or the UUID of the user, surrounded by curly-braces, for example: &#x60;{user UUID}&#x60;.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **issue_id** | **str**| The ID of the issue that is being queried.  | 
 **body** | [**IssueComment**](IssueComment.md)| The updated comment. | 

### Return type

[**IssueComment**](IssueComment.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated issue comment. |  -  |
**400** | If the input was invalid, or if the update to the comment is detected as spam  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repositories_by_username_by_repo_slug_issues_by_issue_id_vote**
> Error update_repositories_by_username_by_repo_slug_issues_by_issue_id_vote(username, issue_id, repo_slug)



Vote for this issue.  To cast your vote, do an empty PUT. The 204 status code indicates that the operation was successful.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.update_repositories_by_username_by_repo_slug_issues_by_issue_id_vote(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->update_repositories_by_username_by_repo_slug_issues_by_issue_id_vote: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.update_repositories_by_username_by_repo_slug_issues_by_issue_id_vote(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->update_repositories_by_username_by_repo_slug_issues_by_issue_id_vote: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.update_repositories_by_username_by_repo_slug_issues_by_issue_id_vote(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->update_repositories_by_username_by_repo_slug_issues_by_issue_id_vote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **issue_id** | **str**| The issue id | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**Error**](Error.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Indicating the authenticated user has cast their vote successfully. |  -  |
**401** | When the request wasn&#39;t authenticated. |  -  |
**404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repositories_by_username_by_repo_slug_issues_by_issue_id_watch**
> Error update_repositories_by_username_by_repo_slug_issues_by_issue_id_watch(username, issue_id, repo_slug)



Start watching this issue.  To start watching this issue, do an empty PUT. The 204 status code indicates that the operation was successful.

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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.update_repositories_by_username_by_repo_slug_issues_by_issue_id_watch(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->update_repositories_by_username_by_repo_slug_issues_by_issue_id_watch: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.update_repositories_by_username_by_repo_slug_issues_by_issue_id_watch(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->update_repositories_by_username_by_repo_slug_issues_by_issue_id_watch: %s\n" % e)
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
api_instance = bitbucketopenapi.IssueTrackerApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
issue_id = 'issue_id_example' # str | The issue id
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.update_repositories_by_username_by_repo_slug_issues_by_issue_id_watch(username, issue_id, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueTrackerApi->update_repositories_by_username_by_repo_slug_issues_by_issue_id_watch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **issue_id** | **str**| The issue id | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**Error**](Error.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Indicates that the authenticated user successfully started watching this issue. |  -  |
**401** | When the request wasn&#39;t authenticated. |  -  |
**404** | If the authenticated user is not watching this issue, or when the repo does not exist, or does not have an issue tracker. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


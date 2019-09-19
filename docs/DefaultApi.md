# bitbucketopenapi.DefaultApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_repositories_by_username_by_repo_slug_issues_export**](DefaultApi.md#create_repositories_by_username_by_repo_slug_issues_export) | **POST** /repositories/{username}/{repo_slug}/issues/export | 
[**create_repositories_by_username_by_repo_slug_issues_import**](DefaultApi.md#create_repositories_by_username_by_repo_slug_issues_import) | **POST** /repositories/{username}/{repo_slug}/issues/import | 
[**get_repositories_by_username_by_repo_slug_diffstat_by_spec**](DefaultApi.md#get_repositories_by_username_by_repo_slug_diffstat_by_spec) | **GET** /repositories/{username}/{repo_slug}/diffstat/{spec} | 
[**get_repositories_by_username_by_repo_slug_issues_export_by_repo_nameissuesby_task_id_zip**](DefaultApi.md#get_repositories_by_username_by_repo_slug_issues_export_by_repo_nameissuesby_task_id_zip) | **GET** /repositories/{username}/{repo_slug}/issues/export/{repo_name}-issues-{task_id}.zip | 
[**get_repositories_by_username_by_repo_slug_issues_import**](DefaultApi.md#get_repositories_by_username_by_repo_slug_issues_import) | **GET** /repositories/{username}/{repo_slug}/issues/import | 
[**get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_logs_by_log_uuid**](DefaultApi.md#get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_logs_by_log_uuid) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/logs/{log_uuid} | 
[**get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_test_reports**](DefaultApi.md#get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_test_reports) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports | 
[**get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_test_reports_test_cases**](DefaultApi.md#get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_test_reports_test_cases) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports/test_cases | 
[**get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_test_reports_test_cases_by_test_case_uuid_test_case_reasons**](DefaultApi.md#get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_test_reports_test_cases_by_test_case_uuid_test_case_reasons) | **GET** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports/test_cases/{test_case_uuid}/test_case_reasons | 
[**get_teams_by_username_permissions**](DefaultApi.md#get_teams_by_username_permissions) | **GET** /teams/{username}/permissions | 
[**get_teams_by_username_permissions_repositories**](DefaultApi.md#get_teams_by_username_permissions_repositories) | **GET** /teams/{username}/permissions/repositories | 
[**get_teams_by_username_permissions_repositories_by_repo_slug**](DefaultApi.md#get_teams_by_username_permissions_repositories_by_repo_slug) | **GET** /teams/{username}/permissions/repositories/{repo_slug} | 
[**get_user_permissions_teams**](DefaultApi.md#get_user_permissions_teams) | **GET** /user/permissions/teams | 
[**update_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_remotetriggers_by_trigger_key**](DefaultApi.md#update_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_remotetriggers_by_trigger_key) | **PUT** /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/remote-triggers/{trigger_key} | 


# **create_repositories_by_username_by_repo_slug_issues_export**
> create_repositories_by_username_by_repo_slug_issues_export(username, repo_slug)



A POST request to this endpoint initiates a new background celery task that archives the repo's issues.  For example, you can run:  curl -u <username> -X POST http://api.bitbucket.org/2.0/repositories/<owner_username>/<repo_slug>/ issues/export  When the job has been accepted, it will return a 202 (Accepted) along with a unique url to this job in the 'Location' response header. This url is the endpoint for where the user can obtain their zip files.\"

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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_instance.create_repositories_by_username_by_repo_slug_issues_export(username, repo_slug)
except ApiException as e:
    print("Exception when calling DefaultApi->create_repositories_by_username_by_repo_slug_issues_export: %s\n" % e)
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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_instance.create_repositories_by_username_by_repo_slug_issues_export(username, repo_slug)
except ApiException as e:
    print("Exception when calling DefaultApi->create_repositories_by_username_by_repo_slug_issues_export: %s\n" % e)
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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_instance.create_repositories_by_username_by_repo_slug_issues_export(username, repo_slug)
except ApiException as e:
    print("Exception when calling DefaultApi->create_repositories_by_username_by_repo_slug_issues_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
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
**202** | The export job has been accepted |  -  |
**401** | The request wasn&#39;t authenticated properly |  -  |
**403** | When the authenticated user does not have admin permission on the repo |  -  |
**404** | The repo does not exist or does not have an issue tracker |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repositories_by_username_by_repo_slug_issues_import**
> IssueJobStatus create_repositories_by_username_by_repo_slug_issues_import(username, repo_slug)



A POST request to this endpoint will import the zip file given by the archive parameter into the repository. All existing issues will be deleted and replaced by the contents of the imported zip file.  Imports are done through a multipart/form-data POST. There is one valid and required form field, with the name \"archive,\" which needs to be a file field:  ``` $ curl -u <username> -X POST -F archive=@/path/to/file.zip https://api.bitbucket.org/2.0/repositories/<owner_username>/<repo_slug>/issues/import ```  When the import job is accepted, here is example output:  ``` < HTTP/1.1 202 Accepted  {     \"type\": \"issue_job_status\",     \"status\": \"ACCEPTED\",     \"phase\": \"Attachments\",     \"total\": 15,     \"count\": 0,     \"percent\": 0 } ```

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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.create_repositories_by_username_by_repo_slug_issues_import(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_repositories_by_username_by_repo_slug_issues_import: %s\n" % e)
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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.create_repositories_by_username_by_repo_slug_issues_import(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_repositories_by_username_by_repo_slug_issues_import: %s\n" % e)
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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.create_repositories_by_username_by_repo_slug_issues_import(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_repositories_by_username_by_repo_slug_issues_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**IssueJobStatus**](IssueJobStatus.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Import job accepted |  -  |
**401** | The request wasn&#39;t authenticated properly |  -  |
**403** | When the authenticated user does not have admin permission on the repo |  -  |
**404** | No export job has begun |  -  |
**409** | Import already running |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_diffstat_by_spec**
> PaginatedDiffstats get_repositories_by_username_by_repo_slug_diffstat_by_spec(username, spec, repo_slug, ignore_whitespace=ignore_whitespace)



Returns the diff stat for the specified commit.  Diff stat responses contain a record for every path modified by the commit and lists the number of lines added and removed for each file.   Example: ``` curl https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/diffstat/d222fa2..e174964 {     \"pagelen\": 500,     \"values\": [         {             \"type\": \"diffstat\",             \"status\": \"modified\",             \"lines_removed\": 1,             \"lines_added\": 2,             \"old\": {                 \"path\": \"setup.py\",                 \"type\": \"commit_file\",                 \"links\": {                     \"self\": {                         \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/src/e1749643d655d7c7014001a6c0f58abaf42ad850/setup.py\"                     }                 }             },             \"new\": {                 \"path\": \"setup.py\",                 \"type\": \"commit_file\",                 \"links\": {                     \"self\": {                         \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/src/d222fa235229c55dad20b190b0b571adf737d5a6/setup.py\"                     }                 }             }         }     ],     \"page\": 1,     \"size\": 1 } ```

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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
spec = 'spec_example' # str | A commit SHA (e.g. `3a8b42`) or a commit range using double dot notation (e.g. `3a8b42..9ff173`). 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
ignore_whitespace = True # bool | Generate diffs that ignore whitespace (optional)

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_diffstat_by_spec(username, spec, repo_slug, ignore_whitespace=ignore_whitespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_repositories_by_username_by_repo_slug_diffstat_by_spec: %s\n" % e)
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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
spec = 'spec_example' # str | A commit SHA (e.g. `3a8b42`) or a commit range using double dot notation (e.g. `3a8b42..9ff173`). 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
ignore_whitespace = True # bool | Generate diffs that ignore whitespace (optional)

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_diffstat_by_spec(username, spec, repo_slug, ignore_whitespace=ignore_whitespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_repositories_by_username_by_repo_slug_diffstat_by_spec: %s\n" % e)
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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
spec = 'spec_example' # str | A commit SHA (e.g. `3a8b42`) or a commit range using double dot notation (e.g. `3a8b42..9ff173`). 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
ignore_whitespace = True # bool | Generate diffs that ignore whitespace (optional)

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_diffstat_by_spec(username, spec, repo_slug, ignore_whitespace=ignore_whitespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_repositories_by_username_by_repo_slug_diffstat_by_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **spec** | **str**| A commit SHA (e.g. &#x60;3a8b42&#x60;) or a commit range using double dot notation (e.g. &#x60;3a8b42..9ff173&#x60;).  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **ignore_whitespace** | **bool**| Generate diffs that ignore whitespace | [optional] 

### Return type

[**PaginatedDiffstats**](PaginatedDiffstats.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The diff stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_issues_export_by_repo_nameissuesby_task_id_zip**
> IssueJobStatus get_repositories_by_username_by_repo_slug_issues_export_by_repo_nameissuesby_task_id_zip(username, repo_slug, repo_name, task_id)



This endpoint is used to poll for the progress of an issue export job and return the zip file after the job is complete. As long as the job is running, this will return a 200 response with in the response body a description of the current status.  After the job has been scheduled, but before it starts executing, this endpoint's response is:  {  \"type\": \"issue_job_status\",  \"status\": \"ACCEPTED\",  \"phase\": \"Initializing\",  \"total\": 0,  \"count\": 0,  \"pct\": 0 }   Then once it starts running, it becomes:  {  \"type\": \"issue_job_status\",  \"status\": \"STARTED\",  \"phase\": \"Attachments\",  \"total\": 15,  \"count\": 11,  \"pct\": 73 }  Once the job has successfully completed, it returns a stream of the zip file.

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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
repo_name = 'repo_name_example' # str | The name of the repo
task_id = 'task_id_example' # str | The ID of the export task

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_export_by_repo_nameissuesby_task_id_zip(username, repo_slug, repo_name, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_repositories_by_username_by_repo_slug_issues_export_by_repo_nameissuesby_task_id_zip: %s\n" % e)
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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
repo_name = 'repo_name_example' # str | The name of the repo
task_id = 'task_id_example' # str | The ID of the export task

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_export_by_repo_nameissuesby_task_id_zip(username, repo_slug, repo_name, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_repositories_by_username_by_repo_slug_issues_export_by_repo_nameissuesby_task_id_zip: %s\n" % e)
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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
repo_name = 'repo_name_example' # str | The name of the repo
task_id = 'task_id_example' # str | The ID of the export task

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_export_by_repo_nameissuesby_task_id_zip(username, repo_slug, repo_name, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_repositories_by_username_by_repo_slug_issues_export_by_repo_nameissuesby_task_id_zip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **repo_name** | **str**| The name of the repo | 
 **task_id** | **str**| The ID of the export task | 

### Return type

[**IssueJobStatus**](IssueJobStatus.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Export job accepted |  -  |
**401** | The request wasn&#39;t authenticated properly |  -  |
**403** | When the authenticated user does not have admin permission on the repo |  -  |
**404** | No export job has begun |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_username_by_repo_slug_issues_import**
> IssueJobStatus get_repositories_by_username_by_repo_slug_issues_import(username, repo_slug)



When using GET, this endpoint reports the status of the current import task. Request example:  ``` $ curl -u <username> -X GET https://api.bitbucket.org/2.0/repositories/<owner_username>/<repo_slug>/issues/import ```  After the job has been scheduled, but before it starts executing, this endpoint's response is:  ``` < HTTP/1.1 202 Accepted {     \"type\": \"issue_job_status\",     \"status\": \"PENDING\",     \"phase\": \"Attachments\",     \"total\": 15,     \"count\": 0,     \"percent\": 0 } ```  Once it starts running, it is a 202 response with status STARTED and progress filled.  After it is finished, it becomes a 200 response with status SUCCESS or FAILURE.

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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_import(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_repositories_by_username_by_repo_slug_issues_import: %s\n" % e)
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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_import(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_repositories_by_username_by_repo_slug_issues_import: %s\n" % e)
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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 

try:
    api_response = api_instance.get_repositories_by_username_by_repo_slug_issues_import(username, repo_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_repositories_by_username_by_repo_slug_issues_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 

### Return type

[**IssueJobStatus**](IssueJobStatus.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Import job complete with either FAILURE or SUCCESS status |  -  |
**202** | Import job started |  -  |
**401** | The request wasn&#39;t authenticated properly |  -  |
**403** | When the authenticated user does not have admin permission on the repo |  -  |
**404** | No export job has begun |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_logs_by_log_uuid**
> get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_logs_by_log_uuid()



### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.DefaultApi()

try:
    api_instance.get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_logs_by_log_uuid()
except ApiException as e:
    print("Exception when calling DefaultApi->get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_logs_by_log_uuid: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_test_reports**
> get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_test_reports()



### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.DefaultApi()

try:
    api_instance.get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_test_reports()
except ApiException as e:
    print("Exception when calling DefaultApi->get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_test_reports: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_test_reports_test_cases**
> get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_test_reports_test_cases()



### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.DefaultApi()

try:
    api_instance.get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_test_reports_test_cases()
except ApiException as e:
    print("Exception when calling DefaultApi->get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_test_reports_test_cases: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_test_reports_test_cases_by_test_case_uuid_test_case_reasons**
> get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_test_reports_test_cases_by_test_case_uuid_test_case_reasons()



### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.DefaultApi()

try:
    api_instance.get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_test_reports_test_cases_by_test_case_uuid_test_case_reasons()
except ApiException as e:
    print("Exception when calling DefaultApi->get_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_steps_by_step_uuid_test_reports_test_cases_by_test_case_uuid_test_case_reasons: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams_by_username_permissions**
> PaginatedTeamPermissions get_teams_by_username_permissions(username, q=q, sort=sort)



Returns an object for each team permission a user on the team has.  Permissions returned are effective permissions — if a user is a member of multiple groups with distinct roles, only the highest level is returned.  Permissions can be:  * `admin` * `collaborator`  Only users with admin permission for the team may access this resource.  Example:  ``` $ curl https://api.bitbucket.org/2.0/teams/atlassian_tutorial/permissions  {   \"pagelen\": 10,   \"values\": [     {       \"permission\": \"admin\",       \"type\": \"team_permission\",       \"user\": {         \"type\": \"user\",         \"username\": \"evzijst\",         \"nickname\": \"evzijst\",         \"display_name\": \"Erik van Zijst\",         \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\"       },       \"team\": {         \"username\": \"bitbucket\",         \"display_name\": \"Atlassian Bitbucket\",         \"uuid\": \"{4cc6108a-a241-4db0-96a5-64347ac04f87}\"       }     },     {       \"permission\": \"collaborator\",       \"type\": \"team_permission\",       \"user\": {         \"type\": \"user\",         \"username\": \"seanaty\",         \"nickname\": \"seanaty\",         \"display_name\": \"Sean Conaty\",         \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\"       },       \"team\": {         \"username\": \"bitbucket\",         \"display_name\": \"Atlassian Bitbucket\",         \"uuid\": \"{4cc6108a-a241-4db0-96a5-64347ac04f87}\"       }     }   ],   \"page\": 1,   \"size\": 2 } ```  Results may be further [filtered or sorted](../../../meta/filtering) by team, user, or permission by adding the following query string parameters:  * `q=user.username=\"evzijst\"` or `q=permission=\"admin\"` * `sort=team.display_name`  Note that the query parameter values need to be URL escaped so that `=` would become `%3D`.

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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Name of a response property sort the result by as per [filtering and sorting](../../../meta/filtering#query-sort).  (optional)

try:
    api_response = api_instance.get_teams_by_username_permissions(username, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_teams_by_username_permissions: %s\n" % e)
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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Name of a response property sort the result by as per [filtering and sorting](../../../meta/filtering#query-sort).  (optional)

try:
    api_response = api_instance.get_teams_by_username_permissions(username, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_teams_by_username_permissions: %s\n" % e)
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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Name of a response property sort the result by as per [filtering and sorting](../../../meta/filtering#query-sort).  (optional)

try:
    api_response = api_instance.get_teams_by_username_permissions(username, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_teams_by_username_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **q** | **str**|  Query string to narrow down the response as per [filtering and sorting](../../../meta/filtering). | [optional] 
 **sort** | **str**|  Name of a response property sort the result by as per [filtering and sorting](../../../meta/filtering#query-sort).  | [optional] 

### Return type

[**PaginatedTeamPermissions**](PaginatedTeamPermissions.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Repositories owned by a team. |  -  |
**403** | The requesting user isn&#39;t an admin of the team. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams_by_username_permissions_repositories**
> PaginatedRepositoryPermissions get_teams_by_username_permissions_repositories(username, q=q, sort=sort)



Returns an object for each repository permission for all of a team’s repositories.  If the username URL parameter refers to a user account instead of a team account, an object containing the repository permissions of all the username's repositories will be returned.  Permissions returned are effective permissions — the highest level of permission the user has. This does not include public repositories that users are not granted any specific permission in, and does not distinguish between direct and indirect privileges.  Only users with admin permission for the team may access this resource.  Permissions can be:  * `admin` * `write` * `read`  Example:  ``` $ curl https://api.bitbucket.org/2.0/teams/atlassian_tutorial/permissions/repositories  {   \"pagelen\": 10,   \"values\": [     {       \"type\": \"repository_permission\",       \"user\": {         \"type\": \"user\",         \"username\": \"evzijst\",         \"display_name\": \"Erik van Zijst\",         \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\"       },       \"repository\": {         \"type\": \"repository\",         \"name\": \"geordi\",         \"full_name\": \"bitbucket/geordi\",         \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"       },       \"permission\": \"admin\"     },     {       \"type\": \"repository_permission\",       \"user\": {         \"type\": \"user\",         \"username\": \"seanaty\",         \"display_name\": \"Sean Conaty\",         \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\"       },       \"repository\": {         \"type\": \"repository\",         \"name\": \"geordi\",         \"full_name\": \"bitbucket/geordi\",         \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"       },       \"permission\": \"write\"     }   ],   \"page\": 1,   \"size\": 2 } ```  Results may be further [filtered or sorted](../../../../meta/filtering) by repository, user, or permission by adding the following query string parameters:  * `q=repository.name=\"geordi\"` or `q=permission>\"read\"` * `sort=user.display_name`  Note that the query parameter values need to be URL escaped so that `=` would become `%3D`.

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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Name of a response property sort the result by as per [filtering and sorting](../../../../meta/filtering#query-sort).  (optional)

try:
    api_response = api_instance.get_teams_by_username_permissions_repositories(username, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_teams_by_username_permissions_repositories: %s\n" % e)
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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Name of a response property sort the result by as per [filtering and sorting](../../../../meta/filtering#query-sort).  (optional)

try:
    api_response = api_instance.get_teams_by_username_permissions_repositories(username, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_teams_by_username_permissions_repositories: %s\n" % e)
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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Name of a response property sort the result by as per [filtering and sorting](../../../../meta/filtering#query-sort).  (optional)

try:
    api_response = api_instance.get_teams_by_username_permissions_repositories(username, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_teams_by_username_permissions_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **q** | **str**|  Query string to narrow down the response as per [filtering and sorting](../../../../meta/filtering). | [optional] 
 **sort** | **str**|  Name of a response property sort the result by as per [filtering and sorting](../../../../meta/filtering#query-sort).  | [optional] 

### Return type

[**PaginatedRepositoryPermissions**](PaginatedRepositoryPermissions.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of team&#39;s repository permissions. |  -  |
**403** | The requesting user isn&#39;t an admin of the team. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams_by_username_permissions_repositories_by_repo_slug**
> PaginatedRepositoryPermissions get_teams_by_username_permissions_repositories_by_repo_slug(username, repo_slug, q=q, sort=sort)



Returns an object for each repository permission of a given repository.  If the username URL parameter refers to a user account instead of a team account, an object containing the repository permissions of the username's repository will be returned.  Permissions returned are effective permissions — the highest level of permission the user has. This does not include public repositories that users are not granted any specific permission in, and does not distinguish between direct and indirect privileges.  Only users with admin permission for the repository may access this resource.  Permissions can be:  * `admin` * `write` * `read`  Example:  ``` $ curl https://api.bitbucket.org/2.0/teams/atlassian_tutorial/permissions/repositories/geordi  {   \"pagelen\": 10,   \"values\": [     {       \"type\": \"repository_permission\",       \"user\": {         \"type\": \"user\",         \"username\": \"evzijst\",         \"display_name\": \"Erik van Zijst\",         \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\"       },       \"repository\": {         \"type\": \"repository\",         \"name\": \"geordi\",         \"full_name\": \"bitbucket/geordi\",         \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"       },       \"permission\": \"admin\"     },     {       \"type\": \"repository_permission\",       \"user\": {         \"type\": \"user\",         \"username\": \"seanaty\",         \"display_name\": \"Sean Conaty\",         \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\"       },       \"repository\": {         \"type\": \"repository\",         \"name\": \"geordi\",         \"full_name\": \"bitbucket/geordi\",         \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"       },       \"permission\": \"write\"     }   ],   \"page\": 1,   \"size\": 2 } ```  Results may be further [filtered or sorted](../../../../meta/filtering) by user, or permission by adding the following query string parameters:  * `q=permission>\"read\"` * `sort=user.display_name`  Note that the query parameter values need to be URL escaped so that `=` would become `%3D`.

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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Name of a response property sort the result by as per [filtering and sorting](../../../../meta/filtering#query-sort).  (optional)

try:
    api_response = api_instance.get_teams_by_username_permissions_repositories_by_repo_slug(username, repo_slug, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_teams_by_username_permissions_repositories_by_repo_slug: %s\n" % e)
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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Name of a response property sort the result by as per [filtering and sorting](../../../../meta/filtering#query-sort).  (optional)

try:
    api_response = api_instance.get_teams_by_username_permissions_repositories_by_repo_slug(username, repo_slug, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_teams_by_username_permissions_repositories_by_repo_slug: %s\n" % e)
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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
username = 'username_example' # str | This can either be the username or the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`. An account is either a team or user. 
repo_slug = 'repo_slug_example' # str | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Name of a response property sort the result by as per [filtering and sorting](../../../../meta/filtering#query-sort).  (optional)

try:
    api_response = api_instance.get_teams_by_username_permissions_repositories_by_repo_slug(username, repo_slug, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_teams_by_username_permissions_repositories_by_repo_slug: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| This can either be the username or the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;. An account is either a team or user.  | 
 **repo_slug** | **str**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **q** | **str**|  Query string to narrow down the response as per [filtering and sorting](../../../../meta/filtering). | [optional] 
 **sort** | **str**|  Name of a response property sort the result by as per [filtering and sorting](../../../../meta/filtering#query-sort).  | [optional] 

### Return type

[**PaginatedRepositoryPermissions**](PaginatedRepositoryPermissions.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of repository&#39;s repository permissions. |  -  |
**403** | The requesting user isn&#39;t an admin of the repository. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_permissions_teams**
> PaginatedTeamPermissions get_user_permissions_teams(q=q, sort=sort)



Returns an object for each team the caller is a member of, and their effective role — the highest level of privilege the caller has. If a user is a member of multiple groups with distinct roles, only the highest level is returned.  Permissions can be:  * `admin` * `collaborator`  Example:  ``` $ curl https://api.bitbucket.org/2.0/user/permissions/teams  {   \"pagelen\": 10,   \"values\": [     {       \"permission\": \"admin\",       \"type\": \"team_permission\",       \"user\": {         \"type\": \"user\",         \"username\": \"evzijst\",         \"nickname\": \"evzijst\",         \"display_name\": \"Erik van Zijst\",         \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\"       },       \"team\": {         \"username\": \"bitbucket\",         \"display_name\": \"Atlassian Bitbucket\",         \"uuid\": \"{4cc6108a-a241-4db0-96a5-64347ac04f87}\"       }     }   ],   \"page\": 1,   \"size\": 1 } ```  Results may be further [filtered or sorted](../../../meta/filtering) by team or permission by adding the following query string parameters:  * `q=team.username=\"bitbucket\"` or `q=permission=\"admin\"` * `sort=team.display_name`  Note that the query parameter values need to be URL escaped so that `=` would become `%3D`.

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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Name of a response property sort the result by as per [filtering and sorting](../../../meta/filtering#query-sort).  (optional)

try:
    api_response = api_instance.get_user_permissions_teams(q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_permissions_teams: %s\n" % e)
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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Name of a response property sort the result by as per [filtering and sorting](../../../meta/filtering#query-sort).  (optional)

try:
    api_response = api_instance.get_user_permissions_teams(q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_permissions_teams: %s\n" % e)
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
api_instance = bitbucketopenapi.DefaultApi(bitbucketopenapi.ApiClient(configuration))
q = 'q_example' # str |  Query string to narrow down the response as per [filtering and sorting](../../../meta/filtering). (optional)
sort = 'sort_example' # str |  Name of a response property sort the result by as per [filtering and sorting](../../../meta/filtering#query-sort).  (optional)

try:
    api_response = api_instance.get_user_permissions_teams(q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_permissions_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  Query string to narrow down the response as per [filtering and sorting](../../../meta/filtering). | [optional] 
 **sort** | **str**|  Name of a response property sort the result by as per [filtering and sorting](../../../meta/filtering#query-sort).  | [optional] 

### Return type

[**PaginatedTeamPermissions**](PaginatedTeamPermissions.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team permissions for the teams a caller is a member of. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_remotetriggers_by_trigger_key**
> update_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_remotetriggers_by_trigger_key()



### Example

```python
from __future__ import print_function
import time
import bitbucketopenapi
from bitbucketopenapi.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bitbucketopenapi.DefaultApi()

try:
    api_instance.update_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_remotetriggers_by_trigger_key()
except ApiException as e:
    print("Exception when calling DefaultApi->update_repositories_by_workspace_by_repo_slug_pipelines_by_pipeline_uuid_remotetriggers_by_trigger_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


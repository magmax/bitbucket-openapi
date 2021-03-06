# coding: utf-8

"""
    Bitbucket API

    Code against the Bitbucket API to automate simple tasks, embed Bitbucket data into your own site, build mobile or desktop apps, or even add custom UI add-ons into Bitbucket itself using the Connect framework.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@bitbucket.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from bitbucketopenapi.api_client import ApiClient
from bitbucketopenapi.exceptions import (
    ApiTypeError,
    ApiValueError
)


class SnippetApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_snippets_by_username_by_encoded_id_files_by_path(self, username, path, encoded_id, **kwargs):  # noqa: E501
        """get_snippets_by_username_by_encoded_id_files_by_path  # noqa: E501

        Convenience resource for getting to a snippet's raw files without the need for first having to retrieve the snippet itself and having to pull out the versioned file links.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_snippets_by_username_by_encoded_id_files_by_path(username, path, encoded_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str username: (required)
        :param str path: (required)
        :param str encoded_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_snippets_by_username_by_encoded_id_files_by_path_with_http_info(username, path, encoded_id, **kwargs)  # noqa: E501

    def get_snippets_by_username_by_encoded_id_files_by_path_with_http_info(self, username, path, encoded_id, **kwargs):  # noqa: E501
        """get_snippets_by_username_by_encoded_id_files_by_path  # noqa: E501

        Convenience resource for getting to a snippet's raw files without the need for first having to retrieve the snippet itself and having to pull out the versioned file links.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_snippets_by_username_by_encoded_id_files_by_path_with_http_info(username, path, encoded_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str username: (required)
        :param str path: (required)
        :param str encoded_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['username', 'path', 'encoded_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_snippets_by_username_by_encoded_id_files_by_path" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in local_var_params or
                local_var_params['username'] is None):
            raise ApiValueError("Missing the required parameter `username` when calling `get_snippets_by_username_by_encoded_id_files_by_path`")  # noqa: E501
        # verify the required parameter 'path' is set
        if ('path' not in local_var_params or
                local_var_params['path'] is None):
            raise ApiValueError("Missing the required parameter `path` when calling `get_snippets_by_username_by_encoded_id_files_by_path`")  # noqa: E501
        # verify the required parameter 'encoded_id' is set
        if ('encoded_id' not in local_var_params or
                local_var_params['encoded_id'] is None):
            raise ApiValueError("Missing the required parameter `encoded_id` when calling `get_snippets_by_username_by_encoded_id_files_by_path`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']  # noqa: E501
        if 'path' in local_var_params:
            path_params['path'] = local_var_params['path']  # noqa: E501
        if 'encoded_id' in local_var_params:
            path_params['encoded_id'] = local_var_params['encoded_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key', 'basic', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/snippets/{username}/{encoded_id}/files/{path}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

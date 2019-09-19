# coding: utf-8

"""
    Bitbucket API

    Code against the Bitbucket API to automate simple tasks, embed Bitbucket data into your own site, build mobile or desktop apps, or even add custom UI add-ons into Bitbucket itself using the Connect framework.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@bitbucket.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import bitbucketopenapi
from bitbucketopenapi.api.repositories_api import RepositoriesApi  # noqa: E501
from bitbucketopenapi.rest import ApiException


class TestRepositoriesApi(unittest.TestCase):
    """RepositoriesApi unit test stubs"""

    def setUp(self):
        self.api = bitbucketopenapi.api.repositories_api.RepositoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_repositories_by_username_by_repo_slug(self):
        """Test case for create_repositories_by_username_by_repo_slug

        """
        pass

    def test_create_repositories_by_username_by_repo_slug_commit_by_node_statuses_build(self):
        """Test case for create_repositories_by_username_by_repo_slug_commit_by_node_statuses_build

        """
        pass

    def test_create_repositories_by_username_by_repo_slug_forks(self):
        """Test case for create_repositories_by_username_by_repo_slug_forks

        """
        pass

    def test_create_repositories_by_username_by_repo_slug_hooks(self):
        """Test case for create_repositories_by_username_by_repo_slug_hooks

        """
        pass

    def test_create_repositories_by_username_by_repo_slug_src(self):
        """Test case for create_repositories_by_username_by_repo_slug_src

        """
        pass

    def test_delete_repositories_by_username_by_repo_slug(self):
        """Test case for delete_repositories_by_username_by_repo_slug

        """
        pass

    def test_delete_repositories_by_username_by_repo_slug_hooks_by_uid(self):
        """Test case for delete_repositories_by_username_by_repo_slug_hooks_by_uid

        """
        pass

    def test_get_repositories(self):
        """Test case for get_repositories

        """
        pass

    def test_get_repositories_by_username(self):
        """Test case for get_repositories_by_username

        """
        pass

    def test_get_repositories_by_username_by_repo_slug(self):
        """Test case for get_repositories_by_username_by_repo_slug

        """
        pass

    def test_get_repositories_by_username_by_repo_slug_commit_by_node_statuses(self):
        """Test case for get_repositories_by_username_by_repo_slug_commit_by_node_statuses

        """
        pass

    def test_get_repositories_by_username_by_repo_slug_commit_by_node_statuses_build_by_key(self):
        """Test case for get_repositories_by_username_by_repo_slug_commit_by_node_statuses_build_by_key

        """
        pass

    def test_get_repositories_by_username_by_repo_slug_filehistory_by_node_by_path(self):
        """Test case for get_repositories_by_username_by_repo_slug_filehistory_by_node_by_path

        """
        pass

    def test_get_repositories_by_username_by_repo_slug_forks(self):
        """Test case for get_repositories_by_username_by_repo_slug_forks

        """
        pass

    def test_get_repositories_by_username_by_repo_slug_hooks(self):
        """Test case for get_repositories_by_username_by_repo_slug_hooks

        """
        pass

    def test_get_repositories_by_username_by_repo_slug_hooks_by_uid(self):
        """Test case for get_repositories_by_username_by_repo_slug_hooks_by_uid

        """
        pass

    def test_get_repositories_by_username_by_repo_slug_pullrequests_by_pull_request_id_statuses(self):
        """Test case for get_repositories_by_username_by_repo_slug_pullrequests_by_pull_request_id_statuses

        """
        pass

    def test_get_repositories_by_username_by_repo_slug_src(self):
        """Test case for get_repositories_by_username_by_repo_slug_src

        """
        pass

    def test_get_repositories_by_username_by_repo_slug_src_by_node_by_path(self):
        """Test case for get_repositories_by_username_by_repo_slug_src_by_node_by_path

        """
        pass

    def test_get_repositories_by_username_by_repo_slug_watchers(self):
        """Test case for get_repositories_by_username_by_repo_slug_watchers

        """
        pass

    def test_get_user_permissions_repositories(self):
        """Test case for get_user_permissions_repositories

        """
        pass

    def test_update_repositories_by_username_by_repo_slug(self):
        """Test case for update_repositories_by_username_by_repo_slug

        """
        pass

    def test_update_repositories_by_username_by_repo_slug_commit_by_node_statuses_build_by_key(self):
        """Test case for update_repositories_by_username_by_repo_slug_commit_by_node_statuses_build_by_key

        """
        pass

    def test_update_repositories_by_username_by_repo_slug_hooks_by_uid(self):
        """Test case for update_repositories_by_username_by_repo_slug_hooks_by_uid

        """
        pass


if __name__ == '__main__':
    unittest.main()

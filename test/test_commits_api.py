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
from bitbucketopenapi.api.commits_api import CommitsApi  # noqa: E501
from bitbucketopenapi.rest import ApiException


class TestCommitsApi(unittest.TestCase):
    """CommitsApi unit test stubs"""

    def setUp(self):
        self.api = bitbucketopenapi.api.commits_api.CommitsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_repositories_by_username_by_repo_slug_commit_by_node_approve(self):
        """Test case for create_repositories_by_username_by_repo_slug_commit_by_node_approve

        """
        pass

    def test_create_repositories_by_username_by_repo_slug_commit_by_node_comments(self):
        """Test case for create_repositories_by_username_by_repo_slug_commit_by_node_comments

        """
        pass

    def test_create_repositories_by_username_by_repo_slug_commits(self):
        """Test case for create_repositories_by_username_by_repo_slug_commits

        """
        pass

    def test_create_repositories_by_username_by_repo_slug_commits_by_revision(self):
        """Test case for create_repositories_by_username_by_repo_slug_commits_by_revision

        """
        pass

    def test_delete_repositories_by_username_by_repo_slug_commit_by_node_approve(self):
        """Test case for delete_repositories_by_username_by_repo_slug_commit_by_node_approve

        """
        pass

    def test_get_repositories_by_username_by_repo_slug_commit_by_node(self):
        """Test case for get_repositories_by_username_by_repo_slug_commit_by_node

        """
        pass

    def test_get_repositories_by_username_by_repo_slug_commit_by_node_comments(self):
        """Test case for get_repositories_by_username_by_repo_slug_commit_by_node_comments

        """
        pass

    def test_get_repositories_by_username_by_repo_slug_commit_by_node_comments_by_comment_id(self):
        """Test case for get_repositories_by_username_by_repo_slug_commit_by_node_comments_by_comment_id

        """
        pass

    def test_get_repositories_by_username_by_repo_slug_commits(self):
        """Test case for get_repositories_by_username_by_repo_slug_commits

        """
        pass

    def test_get_repositories_by_username_by_repo_slug_commits_by_revision(self):
        """Test case for get_repositories_by_username_by_repo_slug_commits_by_revision

        """
        pass

    def test_get_repositories_by_username_by_repo_slug_diff_by_spec(self):
        """Test case for get_repositories_by_username_by_repo_slug_diff_by_spec

        """
        pass

    def test_get_repositories_by_username_by_repo_slug_patch_by_spec(self):
        """Test case for get_repositories_by_username_by_repo_slug_patch_by_spec

        """
        pass


if __name__ == '__main__':
    unittest.main()
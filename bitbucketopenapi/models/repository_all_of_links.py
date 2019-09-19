# coding: utf-8

"""
    Bitbucket API

    Code against the Bitbucket API to automate simple tasks, embed Bitbucket data into your own site, build mobile or desktop apps, or even add custom UI add-ons into Bitbucket itself using the Connect framework.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@bitbucket.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class RepositoryAllOfLinks(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'avatar': 'AccountAllOfLinksAvatar',
        'clone': 'list[AccountAllOfLinksAvatar]',
        'commits': 'AccountAllOfLinksAvatar',
        'downloads': 'AccountAllOfLinksAvatar',
        'forks': 'AccountAllOfLinksAvatar',
        'hooks': 'AccountAllOfLinksAvatar',
        'html': 'AccountAllOfLinksAvatar',
        'pullrequests': 'AccountAllOfLinksAvatar',
        '_self': 'AccountAllOfLinksAvatar',
        'watchers': 'AccountAllOfLinksAvatar'
    }

    attribute_map = {
        'avatar': 'avatar',
        'clone': 'clone',
        'commits': 'commits',
        'downloads': 'downloads',
        'forks': 'forks',
        'hooks': 'hooks',
        'html': 'html',
        'pullrequests': 'pullrequests',
        '_self': 'self',
        'watchers': 'watchers'
    }

    def __init__(self, avatar=None, clone=None, commits=None, downloads=None, forks=None, hooks=None, html=None, pullrequests=None, _self=None, watchers=None):  # noqa: E501
        """RepositoryAllOfLinks - a model defined in OpenAPI"""  # noqa: E501

        self._avatar = None
        self._clone = None
        self._commits = None
        self._downloads = None
        self._forks = None
        self._hooks = None
        self._html = None
        self._pullrequests = None
        self.__self = None
        self._watchers = None
        self.discriminator = None

        if avatar is not None:
            self.avatar = avatar
        if clone is not None:
            self.clone = clone
        if commits is not None:
            self.commits = commits
        if downloads is not None:
            self.downloads = downloads
        if forks is not None:
            self.forks = forks
        if hooks is not None:
            self.hooks = hooks
        if html is not None:
            self.html = html
        if pullrequests is not None:
            self.pullrequests = pullrequests
        if _self is not None:
            self._self = _self
        if watchers is not None:
            self.watchers = watchers

    @property
    def avatar(self):
        """Gets the avatar of this RepositoryAllOfLinks.  # noqa: E501


        :return: The avatar of this RepositoryAllOfLinks.  # noqa: E501
        :rtype: AccountAllOfLinksAvatar
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this RepositoryAllOfLinks.


        :param avatar: The avatar of this RepositoryAllOfLinks.  # noqa: E501
        :type: AccountAllOfLinksAvatar
        """

        self._avatar = avatar

    @property
    def clone(self):
        """Gets the clone of this RepositoryAllOfLinks.  # noqa: E501


        :return: The clone of this RepositoryAllOfLinks.  # noqa: E501
        :rtype: list[AccountAllOfLinksAvatar]
        """
        return self._clone

    @clone.setter
    def clone(self, clone):
        """Sets the clone of this RepositoryAllOfLinks.


        :param clone: The clone of this RepositoryAllOfLinks.  # noqa: E501
        :type: list[AccountAllOfLinksAvatar]
        """

        self._clone = clone

    @property
    def commits(self):
        """Gets the commits of this RepositoryAllOfLinks.  # noqa: E501


        :return: The commits of this RepositoryAllOfLinks.  # noqa: E501
        :rtype: AccountAllOfLinksAvatar
        """
        return self._commits

    @commits.setter
    def commits(self, commits):
        """Sets the commits of this RepositoryAllOfLinks.


        :param commits: The commits of this RepositoryAllOfLinks.  # noqa: E501
        :type: AccountAllOfLinksAvatar
        """

        self._commits = commits

    @property
    def downloads(self):
        """Gets the downloads of this RepositoryAllOfLinks.  # noqa: E501


        :return: The downloads of this RepositoryAllOfLinks.  # noqa: E501
        :rtype: AccountAllOfLinksAvatar
        """
        return self._downloads

    @downloads.setter
    def downloads(self, downloads):
        """Sets the downloads of this RepositoryAllOfLinks.


        :param downloads: The downloads of this RepositoryAllOfLinks.  # noqa: E501
        :type: AccountAllOfLinksAvatar
        """

        self._downloads = downloads

    @property
    def forks(self):
        """Gets the forks of this RepositoryAllOfLinks.  # noqa: E501


        :return: The forks of this RepositoryAllOfLinks.  # noqa: E501
        :rtype: AccountAllOfLinksAvatar
        """
        return self._forks

    @forks.setter
    def forks(self, forks):
        """Sets the forks of this RepositoryAllOfLinks.


        :param forks: The forks of this RepositoryAllOfLinks.  # noqa: E501
        :type: AccountAllOfLinksAvatar
        """

        self._forks = forks

    @property
    def hooks(self):
        """Gets the hooks of this RepositoryAllOfLinks.  # noqa: E501


        :return: The hooks of this RepositoryAllOfLinks.  # noqa: E501
        :rtype: AccountAllOfLinksAvatar
        """
        return self._hooks

    @hooks.setter
    def hooks(self, hooks):
        """Sets the hooks of this RepositoryAllOfLinks.


        :param hooks: The hooks of this RepositoryAllOfLinks.  # noqa: E501
        :type: AccountAllOfLinksAvatar
        """

        self._hooks = hooks

    @property
    def html(self):
        """Gets the html of this RepositoryAllOfLinks.  # noqa: E501


        :return: The html of this RepositoryAllOfLinks.  # noqa: E501
        :rtype: AccountAllOfLinksAvatar
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this RepositoryAllOfLinks.


        :param html: The html of this RepositoryAllOfLinks.  # noqa: E501
        :type: AccountAllOfLinksAvatar
        """

        self._html = html

    @property
    def pullrequests(self):
        """Gets the pullrequests of this RepositoryAllOfLinks.  # noqa: E501


        :return: The pullrequests of this RepositoryAllOfLinks.  # noqa: E501
        :rtype: AccountAllOfLinksAvatar
        """
        return self._pullrequests

    @pullrequests.setter
    def pullrequests(self, pullrequests):
        """Sets the pullrequests of this RepositoryAllOfLinks.


        :param pullrequests: The pullrequests of this RepositoryAllOfLinks.  # noqa: E501
        :type: AccountAllOfLinksAvatar
        """

        self._pullrequests = pullrequests

    @property
    def _self(self):
        """Gets the _self of this RepositoryAllOfLinks.  # noqa: E501


        :return: The _self of this RepositoryAllOfLinks.  # noqa: E501
        :rtype: AccountAllOfLinksAvatar
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this RepositoryAllOfLinks.


        :param _self: The _self of this RepositoryAllOfLinks.  # noqa: E501
        :type: AccountAllOfLinksAvatar
        """

        self.__self = _self

    @property
    def watchers(self):
        """Gets the watchers of this RepositoryAllOfLinks.  # noqa: E501


        :return: The watchers of this RepositoryAllOfLinks.  # noqa: E501
        :rtype: AccountAllOfLinksAvatar
        """
        return self._watchers

    @watchers.setter
    def watchers(self, watchers):
        """Sets the watchers of this RepositoryAllOfLinks.


        :param watchers: The watchers of this RepositoryAllOfLinks.  # noqa: E501
        :type: AccountAllOfLinksAvatar
        """

        self._watchers = watchers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RepositoryAllOfLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

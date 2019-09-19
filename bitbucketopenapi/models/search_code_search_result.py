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


class SearchCodeSearchResult(object):
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
        'content_match_count': 'int',
        'content_matches': 'list[SearchContentMatch]',
        'file': 'CommitFile',
        'path_matches': 'list[SearchSegment]',
        'type': 'str'
    }

    attribute_map = {
        'content_match_count': 'content_match_count',
        'content_matches': 'content_matches',
        'file': 'file',
        'path_matches': 'path_matches',
        'type': 'type'
    }

    def __init__(self, content_match_count=None, content_matches=None, file=None, path_matches=None, type=None):  # noqa: E501
        """SearchCodeSearchResult - a model defined in OpenAPI"""  # noqa: E501

        self._content_match_count = None
        self._content_matches = None
        self._file = None
        self._path_matches = None
        self._type = None
        self.discriminator = None

        if content_match_count is not None:
            self.content_match_count = content_match_count
        if content_matches is not None:
            self.content_matches = content_matches
        if file is not None:
            self.file = file
        if path_matches is not None:
            self.path_matches = path_matches
        if type is not None:
            self.type = type

    @property
    def content_match_count(self):
        """Gets the content_match_count of this SearchCodeSearchResult.  # noqa: E501


        :return: The content_match_count of this SearchCodeSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._content_match_count

    @content_match_count.setter
    def content_match_count(self, content_match_count):
        """Sets the content_match_count of this SearchCodeSearchResult.


        :param content_match_count: The content_match_count of this SearchCodeSearchResult.  # noqa: E501
        :type: int
        """

        self._content_match_count = content_match_count

    @property
    def content_matches(self):
        """Gets the content_matches of this SearchCodeSearchResult.  # noqa: E501


        :return: The content_matches of this SearchCodeSearchResult.  # noqa: E501
        :rtype: list[SearchContentMatch]
        """
        return self._content_matches

    @content_matches.setter
    def content_matches(self, content_matches):
        """Sets the content_matches of this SearchCodeSearchResult.


        :param content_matches: The content_matches of this SearchCodeSearchResult.  # noqa: E501
        :type: list[SearchContentMatch]
        """

        self._content_matches = content_matches

    @property
    def file(self):
        """Gets the file of this SearchCodeSearchResult.  # noqa: E501


        :return: The file of this SearchCodeSearchResult.  # noqa: E501
        :rtype: CommitFile
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this SearchCodeSearchResult.


        :param file: The file of this SearchCodeSearchResult.  # noqa: E501
        :type: CommitFile
        """

        self._file = file

    @property
    def path_matches(self):
        """Gets the path_matches of this SearchCodeSearchResult.  # noqa: E501


        :return: The path_matches of this SearchCodeSearchResult.  # noqa: E501
        :rtype: list[SearchSegment]
        """
        return self._path_matches

    @path_matches.setter
    def path_matches(self, path_matches):
        """Sets the path_matches of this SearchCodeSearchResult.


        :param path_matches: The path_matches of this SearchCodeSearchResult.  # noqa: E501
        :type: list[SearchSegment]
        """

        self._path_matches = path_matches

    @property
    def type(self):
        """Gets the type of this SearchCodeSearchResult.  # noqa: E501


        :return: The type of this SearchCodeSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SearchCodeSearchResult.


        :param type: The type of this SearchCodeSearchResult.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, SearchCodeSearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

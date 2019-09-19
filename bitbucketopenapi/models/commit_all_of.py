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


class CommitAllOf(object):
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
        'participants': 'list[Participant]',
        'repository': 'Repository'
    }

    attribute_map = {
        'participants': 'participants',
        'repository': 'repository'
    }

    def __init__(self, participants=None, repository=None):  # noqa: E501
        """CommitAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._participants = None
        self._repository = None
        self.discriminator = None

        if participants is not None:
            self.participants = participants
        if repository is not None:
            self.repository = repository

    @property
    def participants(self):
        """Gets the participants of this CommitAllOf.  # noqa: E501


        :return: The participants of this CommitAllOf.  # noqa: E501
        :rtype: list[Participant]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """Sets the participants of this CommitAllOf.


        :param participants: The participants of this CommitAllOf.  # noqa: E501
        :type: list[Participant]
        """

        self._participants = participants

    @property
    def repository(self):
        """Gets the repository of this CommitAllOf.  # noqa: E501


        :return: The repository of this CommitAllOf.  # noqa: E501
        :rtype: Repository
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this CommitAllOf.


        :param repository: The repository of this CommitAllOf.  # noqa: E501
        :type: Repository
        """

        self._repository = repository

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
        if not isinstance(other, CommitAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

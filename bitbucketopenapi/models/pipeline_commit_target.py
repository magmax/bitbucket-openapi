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


class PipelineCommitTarget(object):
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
        'type': 'str',
        'commit': 'Commit',
        'selector': 'PipelineSelector'
    }

    attribute_map = {
        'type': 'type',
        'commit': 'commit',
        'selector': 'selector'
    }

    def __init__(self, type=None, commit=None, selector=None):  # noqa: E501
        """PipelineCommitTarget - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._commit = None
        self._selector = None
        self.discriminator = None

        self.type = type
        if commit is not None:
            self.commit = commit
        if selector is not None:
            self.selector = selector

    @property
    def type(self):
        """Gets the type of this PipelineCommitTarget.  # noqa: E501


        :return: The type of this PipelineCommitTarget.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PipelineCommitTarget.


        :param type: The type of this PipelineCommitTarget.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def commit(self):
        """Gets the commit of this PipelineCommitTarget.  # noqa: E501


        :return: The commit of this PipelineCommitTarget.  # noqa: E501
        :rtype: Commit
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this PipelineCommitTarget.


        :param commit: The commit of this PipelineCommitTarget.  # noqa: E501
        :type: Commit
        """

        self._commit = commit

    @property
    def selector(self):
        """Gets the selector of this PipelineCommitTarget.  # noqa: E501


        :return: The selector of this PipelineCommitTarget.  # noqa: E501
        :rtype: PipelineSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this PipelineCommitTarget.


        :param selector: The selector of this PipelineCommitTarget.  # noqa: E501
        :type: PipelineSelector
        """

        self._selector = selector

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
        if not isinstance(other, PipelineCommitTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
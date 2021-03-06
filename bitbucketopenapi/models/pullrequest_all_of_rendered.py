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


class PullrequestAllOfRendered(object):
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
        'description': 'BaseCommitAllOfSummary',
        'reason': 'BaseCommitAllOfSummary',
        'title': 'BaseCommitAllOfSummary'
    }

    attribute_map = {
        'description': 'description',
        'reason': 'reason',
        'title': 'title'
    }

    def __init__(self, description=None, reason=None, title=None):  # noqa: E501
        """PullrequestAllOfRendered - a model defined in OpenAPI"""  # noqa: E501

        self._description = None
        self._reason = None
        self._title = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if reason is not None:
            self.reason = reason
        if title is not None:
            self.title = title

    @property
    def description(self):
        """Gets the description of this PullrequestAllOfRendered.  # noqa: E501


        :return: The description of this PullrequestAllOfRendered.  # noqa: E501
        :rtype: BaseCommitAllOfSummary
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PullrequestAllOfRendered.


        :param description: The description of this PullrequestAllOfRendered.  # noqa: E501
        :type: BaseCommitAllOfSummary
        """

        self._description = description

    @property
    def reason(self):
        """Gets the reason of this PullrequestAllOfRendered.  # noqa: E501


        :return: The reason of this PullrequestAllOfRendered.  # noqa: E501
        :rtype: BaseCommitAllOfSummary
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this PullrequestAllOfRendered.


        :param reason: The reason of this PullrequestAllOfRendered.  # noqa: E501
        :type: BaseCommitAllOfSummary
        """

        self._reason = reason

    @property
    def title(self):
        """Gets the title of this PullrequestAllOfRendered.  # noqa: E501


        :return: The title of this PullrequestAllOfRendered.  # noqa: E501
        :rtype: BaseCommitAllOfSummary
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PullrequestAllOfRendered.


        :param title: The title of this PullrequestAllOfRendered.  # noqa: E501
        :type: BaseCommitAllOfSummary
        """

        self._title = title

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
        if not isinstance(other, PullrequestAllOfRendered):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

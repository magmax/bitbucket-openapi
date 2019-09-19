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


class PullrequestAllOfMergeCommit(object):
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
        'hash': 'str'
    }

    attribute_map = {
        'hash': 'hash'
    }

    def __init__(self, hash=None):  # noqa: E501
        """PullrequestAllOfMergeCommit - a model defined in OpenAPI"""  # noqa: E501

        self._hash = None
        self.discriminator = None

        if hash is not None:
            self.hash = hash

    @property
    def hash(self):
        """Gets the hash of this PullrequestAllOfMergeCommit.  # noqa: E501


        :return: The hash of this PullrequestAllOfMergeCommit.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this PullrequestAllOfMergeCommit.


        :param hash: The hash of this PullrequestAllOfMergeCommit.  # noqa: E501
        :type: str
        """
        if hash is not None and not re.search(r'[0-9a-f]{7,}?', hash):  # noqa: E501
            raise ValueError(r"Invalid value for `hash`, must be a follow pattern or equal to `/[0-9a-f]{7,}?/`")  # noqa: E501

        self._hash = hash

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
        if not isinstance(other, PullrequestAllOfMergeCommit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
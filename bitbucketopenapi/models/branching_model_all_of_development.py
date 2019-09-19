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


class BranchingModelAllOfDevelopment(object):
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
        'branch': 'Branch',
        'name': 'str',
        'use_mainbranch': 'bool'
    }

    attribute_map = {
        'branch': 'branch',
        'name': 'name',
        'use_mainbranch': 'use_mainbranch'
    }

    def __init__(self, branch=None, name=None, use_mainbranch=None):  # noqa: E501
        """BranchingModelAllOfDevelopment - a model defined in OpenAPI"""  # noqa: E501

        self._branch = None
        self._name = None
        self._use_mainbranch = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
        self.name = name
        self.use_mainbranch = use_mainbranch

    @property
    def branch(self):
        """Gets the branch of this BranchingModelAllOfDevelopment.  # noqa: E501


        :return: The branch of this BranchingModelAllOfDevelopment.  # noqa: E501
        :rtype: Branch
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this BranchingModelAllOfDevelopment.


        :param branch: The branch of this BranchingModelAllOfDevelopment.  # noqa: E501
        :type: Branch
        """

        self._branch = branch

    @property
    def name(self):
        """Gets the name of this BranchingModelAllOfDevelopment.  # noqa: E501

        Name of the target branch. Will be listed here even when the target branch does not exist. Will be `null` if targeting the main branch and the repository is empty.  # noqa: E501

        :return: The name of this BranchingModelAllOfDevelopment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BranchingModelAllOfDevelopment.

        Name of the target branch. Will be listed here even when the target branch does not exist. Will be `null` if targeting the main branch and the repository is empty.  # noqa: E501

        :param name: The name of this BranchingModelAllOfDevelopment.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def use_mainbranch(self):
        """Gets the use_mainbranch of this BranchingModelAllOfDevelopment.  # noqa: E501

        Indicates if the setting points at an explicit branch (`false`) or tracks the main branch (`true`).  # noqa: E501

        :return: The use_mainbranch of this BranchingModelAllOfDevelopment.  # noqa: E501
        :rtype: bool
        """
        return self._use_mainbranch

    @use_mainbranch.setter
    def use_mainbranch(self, use_mainbranch):
        """Sets the use_mainbranch of this BranchingModelAllOfDevelopment.

        Indicates if the setting points at an explicit branch (`false`) or tracks the main branch (`true`).  # noqa: E501

        :param use_mainbranch: The use_mainbranch of this BranchingModelAllOfDevelopment.  # noqa: E501
        :type: bool
        """
        if use_mainbranch is None:
            raise ValueError("Invalid value for `use_mainbranch`, must not be `None`")  # noqa: E501

        self._use_mainbranch = use_mainbranch

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
        if not isinstance(other, BranchingModelAllOfDevelopment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class BranchingModelSettingsAllOfDevelopment(object):
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
        'is_valid': 'bool',
        'name': 'str',
        'use_mainbranch': 'bool'
    }

    attribute_map = {
        'is_valid': 'is_valid',
        'name': 'name',
        'use_mainbranch': 'use_mainbranch'
    }

    def __init__(self, is_valid=None, name=None, use_mainbranch=None):  # noqa: E501
        """BranchingModelSettingsAllOfDevelopment - a model defined in OpenAPI"""  # noqa: E501

        self._is_valid = None
        self._name = None
        self._use_mainbranch = None
        self.discriminator = None

        if is_valid is not None:
            self.is_valid = is_valid
        if name is not None:
            self.name = name
        if use_mainbranch is not None:
            self.use_mainbranch = use_mainbranch

    @property
    def is_valid(self):
        """Gets the is_valid of this BranchingModelSettingsAllOfDevelopment.  # noqa: E501

        Indicates if the configured branch is valid, that is, if the configured branch actually exists currently. Is always `true` when `use_mainbranch` is `true` (even if the main branch does not exist). This field is read-only. This field is ignored when updating/creating settings.  # noqa: E501

        :return: The is_valid of this BranchingModelSettingsAllOfDevelopment.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this BranchingModelSettingsAllOfDevelopment.

        Indicates if the configured branch is valid, that is, if the configured branch actually exists currently. Is always `true` when `use_mainbranch` is `true` (even if the main branch does not exist). This field is read-only. This field is ignored when updating/creating settings.  # noqa: E501

        :param is_valid: The is_valid of this BranchingModelSettingsAllOfDevelopment.  # noqa: E501
        :type: bool
        """

        self._is_valid = is_valid

    @property
    def name(self):
        """Gets the name of this BranchingModelSettingsAllOfDevelopment.  # noqa: E501

        The configured branch. It must be `null` when `use_mainbranch` is `true`. Otherwise it must be a non-empty value. It is possible for the configured branch to not exist (e.g. it was deleted after the settings are set). In this case `is_valid` will be `false`. The branch must exist when updating/setting the `name` or an error will occur.  # noqa: E501

        :return: The name of this BranchingModelSettingsAllOfDevelopment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BranchingModelSettingsAllOfDevelopment.

        The configured branch. It must be `null` when `use_mainbranch` is `true`. Otherwise it must be a non-empty value. It is possible for the configured branch to not exist (e.g. it was deleted after the settings are set). In this case `is_valid` will be `false`. The branch must exist when updating/setting the `name` or an error will occur.  # noqa: E501

        :param name: The name of this BranchingModelSettingsAllOfDevelopment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def use_mainbranch(self):
        """Gets the use_mainbranch of this BranchingModelSettingsAllOfDevelopment.  # noqa: E501

        Indicates if the setting points at an explicit branch (`false`) or tracks the main branch (`true`). When `true` the `name` must be `null` or not provided. When `false` the `name` must contain a non-empty branch name.  # noqa: E501

        :return: The use_mainbranch of this BranchingModelSettingsAllOfDevelopment.  # noqa: E501
        :rtype: bool
        """
        return self._use_mainbranch

    @use_mainbranch.setter
    def use_mainbranch(self, use_mainbranch):
        """Sets the use_mainbranch of this BranchingModelSettingsAllOfDevelopment.

        Indicates if the setting points at an explicit branch (`false`) or tracks the main branch (`true`). When `true` the `name` must be `null` or not provided. When `false` the `name` must contain a non-empty branch name.  # noqa: E501

        :param use_mainbranch: The use_mainbranch of this BranchingModelSettingsAllOfDevelopment.  # noqa: E501
        :type: bool
        """

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
        if not isinstance(other, BranchingModelSettingsAllOfDevelopment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

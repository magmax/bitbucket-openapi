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


class BranchrestrictionAllOf(object):
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
        'branch_match_kind': 'str',
        'branch_type': 'str',
        'groups': 'list[Group]',
        'id': 'int',
        'kind': 'str',
        'links': 'BranchingModelSettingsAllOfLinks',
        'pattern': 'str',
        'users': 'list[Account]',
        'value': 'int'
    }

    attribute_map = {
        'branch_match_kind': 'branch_match_kind',
        'branch_type': 'branch_type',
        'groups': 'groups',
        'id': 'id',
        'kind': 'kind',
        'links': 'links',
        'pattern': 'pattern',
        'users': 'users',
        'value': 'value'
    }

    def __init__(self, branch_match_kind=None, branch_type=None, groups=None, id=None, kind=None, links=None, pattern=None, users=None, value=None):  # noqa: E501
        """BranchrestrictionAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._branch_match_kind = None
        self._branch_type = None
        self._groups = None
        self._id = None
        self._kind = None
        self._links = None
        self._pattern = None
        self._users = None
        self._value = None
        self.discriminator = None

        self.branch_match_kind = branch_match_kind
        if branch_type is not None:
            self.branch_type = branch_type
        if groups is not None:
            self.groups = groups
        if id is not None:
            self.id = id
        self.kind = kind
        if links is not None:
            self.links = links
        self.pattern = pattern
        if users is not None:
            self.users = users
        if value is not None:
            self.value = value

    @property
    def branch_match_kind(self):
        """Gets the branch_match_kind of this BranchrestrictionAllOf.  # noqa: E501

        Indicates how the restriction is matched against a branch. The default is `glob`.  # noqa: E501

        :return: The branch_match_kind of this BranchrestrictionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._branch_match_kind

    @branch_match_kind.setter
    def branch_match_kind(self, branch_match_kind):
        """Sets the branch_match_kind of this BranchrestrictionAllOf.

        Indicates how the restriction is matched against a branch. The default is `glob`.  # noqa: E501

        :param branch_match_kind: The branch_match_kind of this BranchrestrictionAllOf.  # noqa: E501
        :type: str
        """
        if branch_match_kind is None:
            raise ValueError("Invalid value for `branch_match_kind`, must not be `None`")  # noqa: E501
        allowed_values = ["branching_model", "glob"]  # noqa: E501
        if branch_match_kind not in allowed_values:
            raise ValueError(
                "Invalid value for `branch_match_kind` ({0}), must be one of {1}"  # noqa: E501
                .format(branch_match_kind, allowed_values)
            )

        self._branch_match_kind = branch_match_kind

    @property
    def branch_type(self):
        """Gets the branch_type of this BranchrestrictionAllOf.  # noqa: E501

        Apply the restriction to branches of this type. Active when `branch_match_kind` is `branching_model`. The branch type will be calculated using the branching model configured for the repository.  # noqa: E501

        :return: The branch_type of this BranchrestrictionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._branch_type

    @branch_type.setter
    def branch_type(self, branch_type):
        """Sets the branch_type of this BranchrestrictionAllOf.

        Apply the restriction to branches of this type. Active when `branch_match_kind` is `branching_model`. The branch type will be calculated using the branching model configured for the repository.  # noqa: E501

        :param branch_type: The branch_type of this BranchrestrictionAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["feature", "bugfix", "release", "hotfix", "development", "production"]  # noqa: E501
        if branch_type not in allowed_values:
            raise ValueError(
                "Invalid value for `branch_type` ({0}), must be one of {1}"  # noqa: E501
                .format(branch_type, allowed_values)
            )

        self._branch_type = branch_type

    @property
    def groups(self):
        """Gets the groups of this BranchrestrictionAllOf.  # noqa: E501


        :return: The groups of this BranchrestrictionAllOf.  # noqa: E501
        :rtype: list[Group]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this BranchrestrictionAllOf.


        :param groups: The groups of this BranchrestrictionAllOf.  # noqa: E501
        :type: list[Group]
        """

        self._groups = groups

    @property
    def id(self):
        """Gets the id of this BranchrestrictionAllOf.  # noqa: E501

        The branch restriction status' id.  # noqa: E501

        :return: The id of this BranchrestrictionAllOf.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BranchrestrictionAllOf.

        The branch restriction status' id.  # noqa: E501

        :param id: The id of this BranchrestrictionAllOf.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def kind(self):
        """Gets the kind of this BranchrestrictionAllOf.  # noqa: E501

        The type of restriction that is being applied.  # noqa: E501

        :return: The kind of this BranchrestrictionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this BranchrestrictionAllOf.

        The type of restriction that is being applied.  # noqa: E501

        :param kind: The kind of this BranchrestrictionAllOf.  # noqa: E501
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501
        allowed_values = ["require_tasks_to_be_completed", "require_passing_builds_to_merge", "force", "require_all_dependencies_merged", "push", "require_approvals_to_merge", "enforce_merge_checks", "restrict_merges", "reset_pullrequest_approvals_on_change", "delete"]  # noqa: E501
        if kind not in allowed_values:
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def links(self):
        """Gets the links of this BranchrestrictionAllOf.  # noqa: E501


        :return: The links of this BranchrestrictionAllOf.  # noqa: E501
        :rtype: BranchingModelSettingsAllOfLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this BranchrestrictionAllOf.


        :param links: The links of this BranchrestrictionAllOf.  # noqa: E501
        :type: BranchingModelSettingsAllOfLinks
        """

        self._links = links

    @property
    def pattern(self):
        """Gets the pattern of this BranchrestrictionAllOf.  # noqa: E501

        Apply the restriction to branches that match this pattern. Active when `branch_match_kind` is `glob`. Will be empty when `branch_match_kind` is `branching_model`.  # noqa: E501

        :return: The pattern of this BranchrestrictionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this BranchrestrictionAllOf.

        Apply the restriction to branches that match this pattern. Active when `branch_match_kind` is `glob`. Will be empty when `branch_match_kind` is `branching_model`.  # noqa: E501

        :param pattern: The pattern of this BranchrestrictionAllOf.  # noqa: E501
        :type: str
        """
        if pattern is None:
            raise ValueError("Invalid value for `pattern`, must not be `None`")  # noqa: E501

        self._pattern = pattern

    @property
    def users(self):
        """Gets the users of this BranchrestrictionAllOf.  # noqa: E501


        :return: The users of this BranchrestrictionAllOf.  # noqa: E501
        :rtype: list[Account]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this BranchrestrictionAllOf.


        :param users: The users of this BranchrestrictionAllOf.  # noqa: E501
        :type: list[Account]
        """

        self._users = users

    @property
    def value(self):
        """Gets the value of this BranchrestrictionAllOf.  # noqa: E501

        Value with kind-specific semantics: \"require_approvals_to_merge\" uses it to require a minimum number of approvals on a PR; \"require_passing_builds_to_merge\" uses it to require a minimum number of passing builds.  # noqa: E501

        :return: The value of this BranchrestrictionAllOf.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BranchrestrictionAllOf.

        Value with kind-specific semantics: \"require_approvals_to_merge\" uses it to require a minimum number of approvals on a PR; \"require_passing_builds_to_merge\" uses it to require a minimum number of passing builds.  # noqa: E501

        :param value: The value of this BranchrestrictionAllOf.  # noqa: E501
        :type: int
        """

        self._value = value

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
        if not isinstance(other, BranchrestrictionAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

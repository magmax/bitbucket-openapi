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


class RepositoryAllOf(object):
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
        'created_on': 'datetime',
        'description': 'str',
        'fork_policy': 'str',
        'full_name': 'str',
        'has_issues': 'bool',
        'has_wiki': 'bool',
        'is_private': 'bool',
        'language': 'str',
        'links': 'RepositoryAllOfLinks',
        'mainbranch': 'Branch',
        'name': 'str',
        'owner': 'Account',
        'parent': 'Repository',
        'project': 'Project',
        'scm': 'str',
        'size': 'int',
        'updated_on': 'datetime',
        'uuid': 'str'
    }

    attribute_map = {
        'created_on': 'created_on',
        'description': 'description',
        'fork_policy': 'fork_policy',
        'full_name': 'full_name',
        'has_issues': 'has_issues',
        'has_wiki': 'has_wiki',
        'is_private': 'is_private',
        'language': 'language',
        'links': 'links',
        'mainbranch': 'mainbranch',
        'name': 'name',
        'owner': 'owner',
        'parent': 'parent',
        'project': 'project',
        'scm': 'scm',
        'size': 'size',
        'updated_on': 'updated_on',
        'uuid': 'uuid'
    }

    def __init__(self, created_on=None, description=None, fork_policy=None, full_name=None, has_issues=None, has_wiki=None, is_private=None, language=None, links=None, mainbranch=None, name=None, owner=None, parent=None, project=None, scm=None, size=None, updated_on=None, uuid=None):  # noqa: E501
        """RepositoryAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._created_on = None
        self._description = None
        self._fork_policy = None
        self._full_name = None
        self._has_issues = None
        self._has_wiki = None
        self._is_private = None
        self._language = None
        self._links = None
        self._mainbranch = None
        self._name = None
        self._owner = None
        self._parent = None
        self._project = None
        self._scm = None
        self._size = None
        self._updated_on = None
        self._uuid = None
        self.discriminator = None

        if created_on is not None:
            self.created_on = created_on
        if description is not None:
            self.description = description
        if fork_policy is not None:
            self.fork_policy = fork_policy
        if full_name is not None:
            self.full_name = full_name
        if has_issues is not None:
            self.has_issues = has_issues
        if has_wiki is not None:
            self.has_wiki = has_wiki
        if is_private is not None:
            self.is_private = is_private
        if language is not None:
            self.language = language
        if links is not None:
            self.links = links
        if mainbranch is not None:
            self.mainbranch = mainbranch
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if parent is not None:
            self.parent = parent
        if project is not None:
            self.project = project
        if scm is not None:
            self.scm = scm
        if size is not None:
            self.size = size
        if updated_on is not None:
            self.updated_on = updated_on
        if uuid is not None:
            self.uuid = uuid

    @property
    def created_on(self):
        """Gets the created_on of this RepositoryAllOf.  # noqa: E501


        :return: The created_on of this RepositoryAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this RepositoryAllOf.


        :param created_on: The created_on of this RepositoryAllOf.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def description(self):
        """Gets the description of this RepositoryAllOf.  # noqa: E501


        :return: The description of this RepositoryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RepositoryAllOf.


        :param description: The description of this RepositoryAllOf.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def fork_policy(self):
        """Gets the fork_policy of this RepositoryAllOf.  # noqa: E501

         Controls the rules for forking this repository.  * **allow_forks**: unrestricted forking * **no_public_forks**: restrict forking to private forks (forks cannot   be made public later) * **no_forks**: deny all forking   # noqa: E501

        :return: The fork_policy of this RepositoryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._fork_policy

    @fork_policy.setter
    def fork_policy(self, fork_policy):
        """Sets the fork_policy of this RepositoryAllOf.

         Controls the rules for forking this repository.  * **allow_forks**: unrestricted forking * **no_public_forks**: restrict forking to private forks (forks cannot   be made public later) * **no_forks**: deny all forking   # noqa: E501

        :param fork_policy: The fork_policy of this RepositoryAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["allow_forks", "no_public_forks", "no_forks"]  # noqa: E501
        if fork_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `fork_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(fork_policy, allowed_values)
            )

        self._fork_policy = fork_policy

    @property
    def full_name(self):
        """Gets the full_name of this RepositoryAllOf.  # noqa: E501

        The concatenation of the repository owner's username and the slugified name, e.g. \"evzijst/interruptingcow\". This is the same string used in Bitbucket URLs.  # noqa: E501

        :return: The full_name of this RepositoryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this RepositoryAllOf.

        The concatenation of the repository owner's username and the slugified name, e.g. \"evzijst/interruptingcow\". This is the same string used in Bitbucket URLs.  # noqa: E501

        :param full_name: The full_name of this RepositoryAllOf.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def has_issues(self):
        """Gets the has_issues of this RepositoryAllOf.  # noqa: E501


        :return: The has_issues of this RepositoryAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._has_issues

    @has_issues.setter
    def has_issues(self, has_issues):
        """Sets the has_issues of this RepositoryAllOf.


        :param has_issues: The has_issues of this RepositoryAllOf.  # noqa: E501
        :type: bool
        """

        self._has_issues = has_issues

    @property
    def has_wiki(self):
        """Gets the has_wiki of this RepositoryAllOf.  # noqa: E501


        :return: The has_wiki of this RepositoryAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._has_wiki

    @has_wiki.setter
    def has_wiki(self, has_wiki):
        """Sets the has_wiki of this RepositoryAllOf.


        :param has_wiki: The has_wiki of this RepositoryAllOf.  # noqa: E501
        :type: bool
        """

        self._has_wiki = has_wiki

    @property
    def is_private(self):
        """Gets the is_private of this RepositoryAllOf.  # noqa: E501


        :return: The is_private of this RepositoryAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """Sets the is_private of this RepositoryAllOf.


        :param is_private: The is_private of this RepositoryAllOf.  # noqa: E501
        :type: bool
        """

        self._is_private = is_private

    @property
    def language(self):
        """Gets the language of this RepositoryAllOf.  # noqa: E501


        :return: The language of this RepositoryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this RepositoryAllOf.


        :param language: The language of this RepositoryAllOf.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def links(self):
        """Gets the links of this RepositoryAllOf.  # noqa: E501


        :return: The links of this RepositoryAllOf.  # noqa: E501
        :rtype: RepositoryAllOfLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this RepositoryAllOf.


        :param links: The links of this RepositoryAllOf.  # noqa: E501
        :type: RepositoryAllOfLinks
        """

        self._links = links

    @property
    def mainbranch(self):
        """Gets the mainbranch of this RepositoryAllOf.  # noqa: E501


        :return: The mainbranch of this RepositoryAllOf.  # noqa: E501
        :rtype: Branch
        """
        return self._mainbranch

    @mainbranch.setter
    def mainbranch(self, mainbranch):
        """Sets the mainbranch of this RepositoryAllOf.


        :param mainbranch: The mainbranch of this RepositoryAllOf.  # noqa: E501
        :type: Branch
        """

        self._mainbranch = mainbranch

    @property
    def name(self):
        """Gets the name of this RepositoryAllOf.  # noqa: E501


        :return: The name of this RepositoryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RepositoryAllOf.


        :param name: The name of this RepositoryAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this RepositoryAllOf.  # noqa: E501


        :return: The owner of this RepositoryAllOf.  # noqa: E501
        :rtype: Account
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this RepositoryAllOf.


        :param owner: The owner of this RepositoryAllOf.  # noqa: E501
        :type: Account
        """

        self._owner = owner

    @property
    def parent(self):
        """Gets the parent of this RepositoryAllOf.  # noqa: E501


        :return: The parent of this RepositoryAllOf.  # noqa: E501
        :rtype: Repository
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this RepositoryAllOf.


        :param parent: The parent of this RepositoryAllOf.  # noqa: E501
        :type: Repository
        """

        self._parent = parent

    @property
    def project(self):
        """Gets the project of this RepositoryAllOf.  # noqa: E501


        :return: The project of this RepositoryAllOf.  # noqa: E501
        :rtype: Project
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this RepositoryAllOf.


        :param project: The project of this RepositoryAllOf.  # noqa: E501
        :type: Project
        """

        self._project = project

    @property
    def scm(self):
        """Gets the scm of this RepositoryAllOf.  # noqa: E501


        :return: The scm of this RepositoryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._scm

    @scm.setter
    def scm(self, scm):
        """Sets the scm of this RepositoryAllOf.


        :param scm: The scm of this RepositoryAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["hg", "git"]  # noqa: E501
        if scm not in allowed_values:
            raise ValueError(
                "Invalid value for `scm` ({0}), must be one of {1}"  # noqa: E501
                .format(scm, allowed_values)
            )

        self._scm = scm

    @property
    def size(self):
        """Gets the size of this RepositoryAllOf.  # noqa: E501


        :return: The size of this RepositoryAllOf.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this RepositoryAllOf.


        :param size: The size of this RepositoryAllOf.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def updated_on(self):
        """Gets the updated_on of this RepositoryAllOf.  # noqa: E501


        :return: The updated_on of this RepositoryAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this RepositoryAllOf.


        :param updated_on: The updated_on of this RepositoryAllOf.  # noqa: E501
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def uuid(self):
        """Gets the uuid of this RepositoryAllOf.  # noqa: E501

        The repository's immutable id. This can be used as a substitute for the slug segment in URLs. Doing this guarantees your URLs will survive renaming of the repository by its owner, or even transfer of the repository to a different user.  # noqa: E501

        :return: The uuid of this RepositoryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this RepositoryAllOf.

        The repository's immutable id. This can be used as a substitute for the slug segment in URLs. Doing this guarantees your URLs will survive renaming of the repository by its owner, or even transfer of the repository to a different user.  # noqa: E501

        :param uuid: The uuid of this RepositoryAllOf.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if not isinstance(other, RepositoryAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

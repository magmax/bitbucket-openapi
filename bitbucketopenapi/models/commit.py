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


class Commit(object):
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
        'author': 'Author',
        'date': 'datetime',
        'hash': 'str',
        'message': 'str',
        'parents': 'list[BaseCommit]',
        'summary': 'BaseCommitAllOfSummary',
        'participants': 'list[Participant]',
        'repository': 'Repository'
    }

    attribute_map = {
        'type': 'type',
        'author': 'author',
        'date': 'date',
        'hash': 'hash',
        'message': 'message',
        'parents': 'parents',
        'summary': 'summary',
        'participants': 'participants',
        'repository': 'repository'
    }

    def __init__(self, type=None, author=None, date=None, hash=None, message=None, parents=None, summary=None, participants=None, repository=None):  # noqa: E501
        """Commit - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._author = None
        self._date = None
        self._hash = None
        self._message = None
        self._parents = None
        self._summary = None
        self._participants = None
        self._repository = None
        self.discriminator = None

        self.type = type
        if author is not None:
            self.author = author
        if date is not None:
            self.date = date
        if hash is not None:
            self.hash = hash
        if message is not None:
            self.message = message
        if parents is not None:
            self.parents = parents
        if summary is not None:
            self.summary = summary
        if participants is not None:
            self.participants = participants
        if repository is not None:
            self.repository = repository

    @property
    def type(self):
        """Gets the type of this Commit.  # noqa: E501


        :return: The type of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Commit.


        :param type: The type of this Commit.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def author(self):
        """Gets the author of this Commit.  # noqa: E501


        :return: The author of this Commit.  # noqa: E501
        :rtype: Author
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Commit.


        :param author: The author of this Commit.  # noqa: E501
        :type: Author
        """

        self._author = author

    @property
    def date(self):
        """Gets the date of this Commit.  # noqa: E501


        :return: The date of this Commit.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Commit.


        :param date: The date of this Commit.  # noqa: E501
        :type: datetime
        """

        self._date = date

    @property
    def hash(self):
        """Gets the hash of this Commit.  # noqa: E501


        :return: The hash of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this Commit.


        :param hash: The hash of this Commit.  # noqa: E501
        :type: str
        """
        if hash is not None and not re.search(r'[0-9a-f]{7,}?', hash):  # noqa: E501
            raise ValueError(r"Invalid value for `hash`, must be a follow pattern or equal to `/[0-9a-f]{7,}?/`")  # noqa: E501

        self._hash = hash

    @property
    def message(self):
        """Gets the message of this Commit.  # noqa: E501


        :return: The message of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Commit.


        :param message: The message of this Commit.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def parents(self):
        """Gets the parents of this Commit.  # noqa: E501


        :return: The parents of this Commit.  # noqa: E501
        :rtype: list[BaseCommit]
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this Commit.


        :param parents: The parents of this Commit.  # noqa: E501
        :type: list[BaseCommit]
        """

        self._parents = parents

    @property
    def summary(self):
        """Gets the summary of this Commit.  # noqa: E501


        :return: The summary of this Commit.  # noqa: E501
        :rtype: BaseCommitAllOfSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this Commit.


        :param summary: The summary of this Commit.  # noqa: E501
        :type: BaseCommitAllOfSummary
        """

        self._summary = summary

    @property
    def participants(self):
        """Gets the participants of this Commit.  # noqa: E501


        :return: The participants of this Commit.  # noqa: E501
        :rtype: list[Participant]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """Sets the participants of this Commit.


        :param participants: The participants of this Commit.  # noqa: E501
        :type: list[Participant]
        """

        self._participants = participants

    @property
    def repository(self):
        """Gets the repository of this Commit.  # noqa: E501


        :return: The repository of this Commit.  # noqa: E501
        :rtype: Repository
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this Commit.


        :param repository: The repository of this Commit.  # noqa: E501
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
        if not isinstance(other, Commit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

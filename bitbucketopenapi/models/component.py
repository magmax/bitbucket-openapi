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


class Component(object):
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
        'id': 'int',
        'links': 'BranchingModelSettingsAllOfLinks',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'name': 'name'
    }

    def __init__(self, id=None, links=None, name=None):  # noqa: E501
        """Component - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._links = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this Component.  # noqa: E501


        :return: The id of this Component.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Component.


        :param id: The id of this Component.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this Component.  # noqa: E501


        :return: The links of this Component.  # noqa: E501
        :rtype: BranchingModelSettingsAllOfLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Component.


        :param links: The links of this Component.  # noqa: E501
        :type: BranchingModelSettingsAllOfLinks
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this Component.  # noqa: E501


        :return: The name of this Component.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Component.


        :param name: The name of this Component.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, Component):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

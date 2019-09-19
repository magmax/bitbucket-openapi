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


class PipelineVariable(object):
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
        'key': 'str',
        'secured': 'bool',
        'uuid': 'str',
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'secured': 'secured',
        'uuid': 'uuid',
        'value': 'value'
    }

    def __init__(self, key=None, secured=None, uuid=None, value=None):  # noqa: E501
        """PipelineVariable - a model defined in OpenAPI"""  # noqa: E501

        self._key = None
        self._secured = None
        self._uuid = None
        self._value = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if secured is not None:
            self.secured = secured
        if uuid is not None:
            self.uuid = uuid
        if value is not None:
            self.value = value

    @property
    def key(self):
        """Gets the key of this PipelineVariable.  # noqa: E501

        The unique name of the variable.  # noqa: E501

        :return: The key of this PipelineVariable.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this PipelineVariable.

        The unique name of the variable.  # noqa: E501

        :param key: The key of this PipelineVariable.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def secured(self):
        """Gets the secured of this PipelineVariable.  # noqa: E501

        If true, this variable will be treated as secured. The value will never be exposed in the logs or the REST API.  # noqa: E501

        :return: The secured of this PipelineVariable.  # noqa: E501
        :rtype: bool
        """
        return self._secured

    @secured.setter
    def secured(self, secured):
        """Sets the secured of this PipelineVariable.

        If true, this variable will be treated as secured. The value will never be exposed in the logs or the REST API.  # noqa: E501

        :param secured: The secured of this PipelineVariable.  # noqa: E501
        :type: bool
        """

        self._secured = secured

    @property
    def uuid(self):
        """Gets the uuid of this PipelineVariable.  # noqa: E501

        The UUID identifying the variable.  # noqa: E501

        :return: The uuid of this PipelineVariable.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PipelineVariable.

        The UUID identifying the variable.  # noqa: E501

        :param uuid: The uuid of this PipelineVariable.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def value(self):
        """Gets the value of this PipelineVariable.  # noqa: E501

        The value of the variable. If the variable is secured, this will be empty.  # noqa: E501

        :return: The value of this PipelineVariable.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PipelineVariable.

        The value of the variable. If the variable is secured, this will be empty.  # noqa: E501

        :param value: The value of this PipelineVariable.  # noqa: E501
        :type: str
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
        if not isinstance(other, PipelineVariable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

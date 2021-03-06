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


class IssueJobStatus(object):
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
        'count': 'int',
        'pct': 'float',
        'phase': 'str',
        'status': 'str',
        'total': 'int',
        'type': 'str'
    }

    attribute_map = {
        'count': 'count',
        'pct': 'pct',
        'phase': 'phase',
        'status': 'status',
        'total': 'total',
        'type': 'type'
    }

    def __init__(self, count=None, pct=None, phase=None, status=None, total=None, type=None):  # noqa: E501
        """IssueJobStatus - a model defined in OpenAPI"""  # noqa: E501

        self._count = None
        self._pct = None
        self._phase = None
        self._status = None
        self._total = None
        self._type = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if pct is not None:
            self.pct = pct
        if phase is not None:
            self.phase = phase
        if status is not None:
            self.status = status
        if total is not None:
            self.total = total
        if type is not None:
            self.type = type

    @property
    def count(self):
        """Gets the count of this IssueJobStatus.  # noqa: E501

        The total number of issues already imported/exported  # noqa: E501

        :return: The count of this IssueJobStatus.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this IssueJobStatus.

        The total number of issues already imported/exported  # noqa: E501

        :param count: The count of this IssueJobStatus.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def pct(self):
        """Gets the pct of this IssueJobStatus.  # noqa: E501

        The percentage of issues already imported/exported  # noqa: E501

        :return: The pct of this IssueJobStatus.  # noqa: E501
        :rtype: float
        """
        return self._pct

    @pct.setter
    def pct(self, pct):
        """Sets the pct of this IssueJobStatus.

        The percentage of issues already imported/exported  # noqa: E501

        :param pct: The pct of this IssueJobStatus.  # noqa: E501
        :type: float
        """
        if pct is not None and pct > 1E+2:  # noqa: E501
            raise ValueError("Invalid value for `pct`, must be a value less than or equal to `1E+2`")  # noqa: E501
        if pct is not None and pct < 0:  # noqa: E501
            raise ValueError("Invalid value for `pct`, must be a value greater than or equal to `0`")  # noqa: E501

        self._pct = pct

    @property
    def phase(self):
        """Gets the phase of this IssueJobStatus.  # noqa: E501

        The phase of the import/export job  # noqa: E501

        :return: The phase of this IssueJobStatus.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this IssueJobStatus.

        The phase of the import/export job  # noqa: E501

        :param phase: The phase of this IssueJobStatus.  # noqa: E501
        :type: str
        """

        self._phase = phase

    @property
    def status(self):
        """Gets the status of this IssueJobStatus.  # noqa: E501

        The status of the import/export job  # noqa: E501

        :return: The status of this IssueJobStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IssueJobStatus.

        The status of the import/export job  # noqa: E501

        :param status: The status of this IssueJobStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACCEPTED", "STARTED", "RUNNING", "FAILURE"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def total(self):
        """Gets the total of this IssueJobStatus.  # noqa: E501

        The total number of issues being imported/exported  # noqa: E501

        :return: The total of this IssueJobStatus.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this IssueJobStatus.

        The total number of issues being imported/exported  # noqa: E501

        :param total: The total of this IssueJobStatus.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def type(self):
        """Gets the type of this IssueJobStatus.  # noqa: E501


        :return: The type of this IssueJobStatus.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IssueJobStatus.


        :param type: The type of this IssueJobStatus.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, IssueJobStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

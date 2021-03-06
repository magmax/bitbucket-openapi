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


class DeploymentStateCompletedAllOf(object):
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
        'completion_date': 'datetime',
        'deployer': 'Account',
        'name': 'str',
        'start_date': 'datetime',
        'status': 'DeploymentStateCompletedStatus',
        'url': 'str'
    }

    attribute_map = {
        'completion_date': 'completion_date',
        'deployer': 'deployer',
        'name': 'name',
        'start_date': 'start_date',
        'status': 'status',
        'url': 'url'
    }

    def __init__(self, completion_date=None, deployer=None, name=None, start_date=None, status=None, url=None):  # noqa: E501
        """DeploymentStateCompletedAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._completion_date = None
        self._deployer = None
        self._name = None
        self._start_date = None
        self._status = None
        self._url = None
        self.discriminator = None

        if completion_date is not None:
            self.completion_date = completion_date
        if deployer is not None:
            self.deployer = deployer
        if name is not None:
            self.name = name
        if start_date is not None:
            self.start_date = start_date
        if status is not None:
            self.status = status
        if url is not None:
            self.url = url

    @property
    def completion_date(self):
        """Gets the completion_date of this DeploymentStateCompletedAllOf.  # noqa: E501

        The timestamp when the deployment completed.  # noqa: E501

        :return: The completion_date of this DeploymentStateCompletedAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._completion_date

    @completion_date.setter
    def completion_date(self, completion_date):
        """Sets the completion_date of this DeploymentStateCompletedAllOf.

        The timestamp when the deployment completed.  # noqa: E501

        :param completion_date: The completion_date of this DeploymentStateCompletedAllOf.  # noqa: E501
        :type: datetime
        """

        self._completion_date = completion_date

    @property
    def deployer(self):
        """Gets the deployer of this DeploymentStateCompletedAllOf.  # noqa: E501


        :return: The deployer of this DeploymentStateCompletedAllOf.  # noqa: E501
        :rtype: Account
        """
        return self._deployer

    @deployer.setter
    def deployer(self, deployer):
        """Sets the deployer of this DeploymentStateCompletedAllOf.


        :param deployer: The deployer of this DeploymentStateCompletedAllOf.  # noqa: E501
        :type: Account
        """

        self._deployer = deployer

    @property
    def name(self):
        """Gets the name of this DeploymentStateCompletedAllOf.  # noqa: E501

        The name of deployment state (COMPLETED).  # noqa: E501

        :return: The name of this DeploymentStateCompletedAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeploymentStateCompletedAllOf.

        The name of deployment state (COMPLETED).  # noqa: E501

        :param name: The name of this DeploymentStateCompletedAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["COMPLETED"]  # noqa: E501
        if name not in allowed_values:
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"  # noqa: E501
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def start_date(self):
        """Gets the start_date of this DeploymentStateCompletedAllOf.  # noqa: E501

        The timestamp when the deployment was started.  # noqa: E501

        :return: The start_date of this DeploymentStateCompletedAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this DeploymentStateCompletedAllOf.

        The timestamp when the deployment was started.  # noqa: E501

        :param start_date: The start_date of this DeploymentStateCompletedAllOf.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def status(self):
        """Gets the status of this DeploymentStateCompletedAllOf.  # noqa: E501


        :return: The status of this DeploymentStateCompletedAllOf.  # noqa: E501
        :rtype: DeploymentStateCompletedStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeploymentStateCompletedAllOf.


        :param status: The status of this DeploymentStateCompletedAllOf.  # noqa: E501
        :type: DeploymentStateCompletedStatus
        """

        self._status = status

    @property
    def url(self):
        """Gets the url of this DeploymentStateCompletedAllOf.  # noqa: E501

        Link to the deployment result.  # noqa: E501

        :return: The url of this DeploymentStateCompletedAllOf.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DeploymentStateCompletedAllOf.

        Link to the deployment result.  # noqa: E501

        :param url: The url of this DeploymentStateCompletedAllOf.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, DeploymentStateCompletedAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class CommitstatusAllOf(object):
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
        'key': 'str',
        'links': 'CommitstatusAllOfLinks',
        'name': 'str',
        'refname': 'str',
        'state': 'str',
        'updated_on': 'datetime',
        'url': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'created_on': 'created_on',
        'description': 'description',
        'key': 'key',
        'links': 'links',
        'name': 'name',
        'refname': 'refname',
        'state': 'state',
        'updated_on': 'updated_on',
        'url': 'url',
        'uuid': 'uuid'
    }

    def __init__(self, created_on=None, description=None, key=None, links=None, name=None, refname=None, state=None, updated_on=None, url=None, uuid=None):  # noqa: E501
        """CommitstatusAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._created_on = None
        self._description = None
        self._key = None
        self._links = None
        self._name = None
        self._refname = None
        self._state = None
        self._updated_on = None
        self._url = None
        self._uuid = None
        self.discriminator = None

        if created_on is not None:
            self.created_on = created_on
        if description is not None:
            self.description = description
        if key is not None:
            self.key = key
        if links is not None:
            self.links = links
        if name is not None:
            self.name = name
        if refname is not None:
            self.refname = refname
        if state is not None:
            self.state = state
        if updated_on is not None:
            self.updated_on = updated_on
        if url is not None:
            self.url = url
        if uuid is not None:
            self.uuid = uuid

    @property
    def created_on(self):
        """Gets the created_on of this CommitstatusAllOf.  # noqa: E501


        :return: The created_on of this CommitstatusAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this CommitstatusAllOf.


        :param created_on: The created_on of this CommitstatusAllOf.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def description(self):
        """Gets the description of this CommitstatusAllOf.  # noqa: E501

        A description of the build (e.g. \"Unit tests in Bamboo\")  # noqa: E501

        :return: The description of this CommitstatusAllOf.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CommitstatusAllOf.

        A description of the build (e.g. \"Unit tests in Bamboo\")  # noqa: E501

        :param description: The description of this CommitstatusAllOf.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def key(self):
        """Gets the key of this CommitstatusAllOf.  # noqa: E501

        An identifier for the status that's unique to         its type (current \"build\" is the only supported type) and the vendor,         e.g. BB-DEPLOY  # noqa: E501

        :return: The key of this CommitstatusAllOf.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CommitstatusAllOf.

        An identifier for the status that's unique to         its type (current \"build\" is the only supported type) and the vendor,         e.g. BB-DEPLOY  # noqa: E501

        :param key: The key of this CommitstatusAllOf.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def links(self):
        """Gets the links of this CommitstatusAllOf.  # noqa: E501


        :return: The links of this CommitstatusAllOf.  # noqa: E501
        :rtype: CommitstatusAllOfLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CommitstatusAllOf.


        :param links: The links of this CommitstatusAllOf.  # noqa: E501
        :type: CommitstatusAllOfLinks
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this CommitstatusAllOf.  # noqa: E501

        An identifier for the build itself, e.g. BB-DEPLOY-1  # noqa: E501

        :return: The name of this CommitstatusAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CommitstatusAllOf.

        An identifier for the build itself, e.g. BB-DEPLOY-1  # noqa: E501

        :param name: The name of this CommitstatusAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def refname(self):
        """Gets the refname of this CommitstatusAllOf.  # noqa: E501

         The name of the ref that pointed to this commit at the time the status object was created. Note that this the ref may since have moved off of the commit. This optional field can be useful for build systems whose build triggers and configuration are branch-dependent (e.g. a Pipeline build). It is legitimate for this field to not be set, or even apply (e.g. a static linting job).  # noqa: E501

        :return: The refname of this CommitstatusAllOf.  # noqa: E501
        :rtype: str
        """
        return self._refname

    @refname.setter
    def refname(self, refname):
        """Sets the refname of this CommitstatusAllOf.

         The name of the ref that pointed to this commit at the time the status object was created. Note that this the ref may since have moved off of the commit. This optional field can be useful for build systems whose build triggers and configuration are branch-dependent (e.g. a Pipeline build). It is legitimate for this field to not be set, or even apply (e.g. a static linting job).  # noqa: E501

        :param refname: The refname of this CommitstatusAllOf.  # noqa: E501
        :type: str
        """

        self._refname = refname

    @property
    def state(self):
        """Gets the state of this CommitstatusAllOf.  # noqa: E501

        Provides some indication of the status of this commit  # noqa: E501

        :return: The state of this CommitstatusAllOf.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CommitstatusAllOf.

        Provides some indication of the status of this commit  # noqa: E501

        :param state: The state of this CommitstatusAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCESSFUL", "FAILED", "INPROGRESS", "STOPPED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def updated_on(self):
        """Gets the updated_on of this CommitstatusAllOf.  # noqa: E501


        :return: The updated_on of this CommitstatusAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this CommitstatusAllOf.


        :param updated_on: The updated_on of this CommitstatusAllOf.  # noqa: E501
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def url(self):
        """Gets the url of this CommitstatusAllOf.  # noqa: E501

        A URL linking back to the vendor or build system, for providing more information about whatever process produced this status. Accepts context variables `repository` and `commit` that Bitbucket will evaluate at runtime whenever at runtime. For example, one could use https://foo.com/builds/{repository.full_name} which Bitbucket will turn into https://foo.com/builds/foo/bar at render time.  # noqa: E501

        :return: The url of this CommitstatusAllOf.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CommitstatusAllOf.

        A URL linking back to the vendor or build system, for providing more information about whatever process produced this status. Accepts context variables `repository` and `commit` that Bitbucket will evaluate at runtime whenever at runtime. For example, one could use https://foo.com/builds/{repository.full_name} which Bitbucket will turn into https://foo.com/builds/foo/bar at render time.  # noqa: E501

        :param url: The url of this CommitstatusAllOf.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def uuid(self):
        """Gets the uuid of this CommitstatusAllOf.  # noqa: E501

        The commit status' id.  # noqa: E501

        :return: The uuid of this CommitstatusAllOf.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this CommitstatusAllOf.

        The commit status' id.  # noqa: E501

        :param uuid: The uuid of this CommitstatusAllOf.  # noqa: E501
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
        if not isinstance(other, CommitstatusAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
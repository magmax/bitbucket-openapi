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


class PaginatedFiles(object):
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
        'next': 'str',
        'page': 'int',
        'pagelen': 'int',
        'previous': 'str',
        'size': 'int',
        'values': 'list[CommitFile]'
    }

    attribute_map = {
        'next': 'next',
        'page': 'page',
        'pagelen': 'pagelen',
        'previous': 'previous',
        'size': 'size',
        'values': 'values'
    }

    def __init__(self, next=None, page=None, pagelen=None, previous=None, size=None, values=None):  # noqa: E501
        """PaginatedFiles - a model defined in OpenAPI"""  # noqa: E501

        self._next = None
        self._page = None
        self._pagelen = None
        self._previous = None
        self._size = None
        self._values = None
        self.discriminator = None

        if next is not None:
            self.next = next
        if page is not None:
            self.page = page
        if pagelen is not None:
            self.pagelen = pagelen
        if previous is not None:
            self.previous = previous
        if size is not None:
            self.size = size
        if values is not None:
            self.values = values

    @property
    def next(self):
        """Gets the next of this PaginatedFiles.  # noqa: E501

        Link to the next page if it exists. The last page of a collection does not have this value. Use this link to navigate the result set and refrain from constructing your own URLs.  # noqa: E501

        :return: The next of this PaginatedFiles.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this PaginatedFiles.

        Link to the next page if it exists. The last page of a collection does not have this value. Use this link to navigate the result set and refrain from constructing your own URLs.  # noqa: E501

        :param next: The next of this PaginatedFiles.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def page(self):
        """Gets the page of this PaginatedFiles.  # noqa: E501

        Page number of the current results. This is an optional element that is not provided in all responses.  # noqa: E501

        :return: The page of this PaginatedFiles.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this PaginatedFiles.

        Page number of the current results. This is an optional element that is not provided in all responses.  # noqa: E501

        :param page: The page of this PaginatedFiles.  # noqa: E501
        :type: int
        """
        if page is not None and page < 1:  # noqa: E501
            raise ValueError("Invalid value for `page`, must be a value greater than or equal to `1`")  # noqa: E501

        self._page = page

    @property
    def pagelen(self):
        """Gets the pagelen of this PaginatedFiles.  # noqa: E501

        Current number of objects on the existing page. The default value is 10 with 100 being the maximum allowed value. Individual APIs may enforce different values.  # noqa: E501

        :return: The pagelen of this PaginatedFiles.  # noqa: E501
        :rtype: int
        """
        return self._pagelen

    @pagelen.setter
    def pagelen(self, pagelen):
        """Sets the pagelen of this PaginatedFiles.

        Current number of objects on the existing page. The default value is 10 with 100 being the maximum allowed value. Individual APIs may enforce different values.  # noqa: E501

        :param pagelen: The pagelen of this PaginatedFiles.  # noqa: E501
        :type: int
        """
        if pagelen is not None and pagelen < 1:  # noqa: E501
            raise ValueError("Invalid value for `pagelen`, must be a value greater than or equal to `1`")  # noqa: E501

        self._pagelen = pagelen

    @property
    def previous(self):
        """Gets the previous of this PaginatedFiles.  # noqa: E501

        Link to previous page if it exists. A collections first page does not have this value. This is an optional element that is not provided in all responses. Some result sets strictly support forward navigation and never provide previous links. Clients must anticipate that backwards navigation is not always available. Use this link to navigate the result set and refrain from constructing your own URLs.  # noqa: E501

        :return: The previous of this PaginatedFiles.  # noqa: E501
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this PaginatedFiles.

        Link to previous page if it exists. A collections first page does not have this value. This is an optional element that is not provided in all responses. Some result sets strictly support forward navigation and never provide previous links. Clients must anticipate that backwards navigation is not always available. Use this link to navigate the result set and refrain from constructing your own URLs.  # noqa: E501

        :param previous: The previous of this PaginatedFiles.  # noqa: E501
        :type: str
        """

        self._previous = previous

    @property
    def size(self):
        """Gets the size of this PaginatedFiles.  # noqa: E501

        Total number of objects in the response. This is an optional element that is not provided in all responses, as it can be expensive to compute.  # noqa: E501

        :return: The size of this PaginatedFiles.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PaginatedFiles.

        Total number of objects in the response. This is an optional element that is not provided in all responses, as it can be expensive to compute.  # noqa: E501

        :param size: The size of this PaginatedFiles.  # noqa: E501
        :type: int
        """
        if size is not None and size < 0:  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._size = size

    @property
    def values(self):
        """Gets the values of this PaginatedFiles.  # noqa: E501


        :return: The values of this PaginatedFiles.  # noqa: E501
        :rtype: list[CommitFile]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this PaginatedFiles.


        :param values: The values of this PaginatedFiles.  # noqa: E501
        :type: list[CommitFile]
        """

        self._values = values

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
        if not isinstance(other, PaginatedFiles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

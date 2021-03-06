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


class PullrequestAllOf(object):
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
        'author': 'Account',
        'close_source_branch': 'bool',
        'closed_by': 'Account',
        'comment_count': 'int',
        'created_on': 'datetime',
        'destination': 'PullrequestEndpoint',
        'id': 'int',
        'links': 'PullrequestAllOfLinks',
        'merge_commit': 'PullrequestAllOfMergeCommit',
        'participants': 'list[Participant]',
        'reason': 'str',
        'rendered': 'PullrequestAllOfRendered',
        'reviewers': 'list[Account]',
        'source': 'PullrequestEndpoint',
        'state': 'str',
        'summary': 'BaseCommitAllOfSummary',
        'task_count': 'int',
        'title': 'str',
        'updated_on': 'datetime'
    }

    attribute_map = {
        'author': 'author',
        'close_source_branch': 'close_source_branch',
        'closed_by': 'closed_by',
        'comment_count': 'comment_count',
        'created_on': 'created_on',
        'destination': 'destination',
        'id': 'id',
        'links': 'links',
        'merge_commit': 'merge_commit',
        'participants': 'participants',
        'reason': 'reason',
        'rendered': 'rendered',
        'reviewers': 'reviewers',
        'source': 'source',
        'state': 'state',
        'summary': 'summary',
        'task_count': 'task_count',
        'title': 'title',
        'updated_on': 'updated_on'
    }

    def __init__(self, author=None, close_source_branch=None, closed_by=None, comment_count=None, created_on=None, destination=None, id=None, links=None, merge_commit=None, participants=None, reason=None, rendered=None, reviewers=None, source=None, state=None, summary=None, task_count=None, title=None, updated_on=None):  # noqa: E501
        """PullrequestAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._author = None
        self._close_source_branch = None
        self._closed_by = None
        self._comment_count = None
        self._created_on = None
        self._destination = None
        self._id = None
        self._links = None
        self._merge_commit = None
        self._participants = None
        self._reason = None
        self._rendered = None
        self._reviewers = None
        self._source = None
        self._state = None
        self._summary = None
        self._task_count = None
        self._title = None
        self._updated_on = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if close_source_branch is not None:
            self.close_source_branch = close_source_branch
        if closed_by is not None:
            self.closed_by = closed_by
        if comment_count is not None:
            self.comment_count = comment_count
        if created_on is not None:
            self.created_on = created_on
        if destination is not None:
            self.destination = destination
        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if merge_commit is not None:
            self.merge_commit = merge_commit
        if participants is not None:
            self.participants = participants
        if reason is not None:
            self.reason = reason
        if rendered is not None:
            self.rendered = rendered
        if reviewers is not None:
            self.reviewers = reviewers
        if source is not None:
            self.source = source
        if state is not None:
            self.state = state
        if summary is not None:
            self.summary = summary
        if task_count is not None:
            self.task_count = task_count
        if title is not None:
            self.title = title
        if updated_on is not None:
            self.updated_on = updated_on

    @property
    def author(self):
        """Gets the author of this PullrequestAllOf.  # noqa: E501


        :return: The author of this PullrequestAllOf.  # noqa: E501
        :rtype: Account
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this PullrequestAllOf.


        :param author: The author of this PullrequestAllOf.  # noqa: E501
        :type: Account
        """

        self._author = author

    @property
    def close_source_branch(self):
        """Gets the close_source_branch of this PullrequestAllOf.  # noqa: E501

        A boolean flag indicating if merging the pull request closes the source branch.  # noqa: E501

        :return: The close_source_branch of this PullrequestAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._close_source_branch

    @close_source_branch.setter
    def close_source_branch(self, close_source_branch):
        """Sets the close_source_branch of this PullrequestAllOf.

        A boolean flag indicating if merging the pull request closes the source branch.  # noqa: E501

        :param close_source_branch: The close_source_branch of this PullrequestAllOf.  # noqa: E501
        :type: bool
        """

        self._close_source_branch = close_source_branch

    @property
    def closed_by(self):
        """Gets the closed_by of this PullrequestAllOf.  # noqa: E501


        :return: The closed_by of this PullrequestAllOf.  # noqa: E501
        :rtype: Account
        """
        return self._closed_by

    @closed_by.setter
    def closed_by(self, closed_by):
        """Sets the closed_by of this PullrequestAllOf.


        :param closed_by: The closed_by of this PullrequestAllOf.  # noqa: E501
        :type: Account
        """

        self._closed_by = closed_by

    @property
    def comment_count(self):
        """Gets the comment_count of this PullrequestAllOf.  # noqa: E501

        The number of comments for a specific pull request.  # noqa: E501

        :return: The comment_count of this PullrequestAllOf.  # noqa: E501
        :rtype: int
        """
        return self._comment_count

    @comment_count.setter
    def comment_count(self, comment_count):
        """Sets the comment_count of this PullrequestAllOf.

        The number of comments for a specific pull request.  # noqa: E501

        :param comment_count: The comment_count of this PullrequestAllOf.  # noqa: E501
        :type: int
        """
        if comment_count is not None and comment_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `comment_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._comment_count = comment_count

    @property
    def created_on(self):
        """Gets the created_on of this PullrequestAllOf.  # noqa: E501

        The ISO8601 timestamp the request was created.  # noqa: E501

        :return: The created_on of this PullrequestAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this PullrequestAllOf.

        The ISO8601 timestamp the request was created.  # noqa: E501

        :param created_on: The created_on of this PullrequestAllOf.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def destination(self):
        """Gets the destination of this PullrequestAllOf.  # noqa: E501


        :return: The destination of this PullrequestAllOf.  # noqa: E501
        :rtype: PullrequestEndpoint
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this PullrequestAllOf.


        :param destination: The destination of this PullrequestAllOf.  # noqa: E501
        :type: PullrequestEndpoint
        """

        self._destination = destination

    @property
    def id(self):
        """Gets the id of this PullrequestAllOf.  # noqa: E501

        The pull request's unique ID. Note that pull request IDs are only unique within their associated repository.  # noqa: E501

        :return: The id of this PullrequestAllOf.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PullrequestAllOf.

        The pull request's unique ID. Note that pull request IDs are only unique within their associated repository.  # noqa: E501

        :param id: The id of this PullrequestAllOf.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this PullrequestAllOf.  # noqa: E501


        :return: The links of this PullrequestAllOf.  # noqa: E501
        :rtype: PullrequestAllOfLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PullrequestAllOf.


        :param links: The links of this PullrequestAllOf.  # noqa: E501
        :type: PullrequestAllOfLinks
        """

        self._links = links

    @property
    def merge_commit(self):
        """Gets the merge_commit of this PullrequestAllOf.  # noqa: E501


        :return: The merge_commit of this PullrequestAllOf.  # noqa: E501
        :rtype: PullrequestAllOfMergeCommit
        """
        return self._merge_commit

    @merge_commit.setter
    def merge_commit(self, merge_commit):
        """Sets the merge_commit of this PullrequestAllOf.


        :param merge_commit: The merge_commit of this PullrequestAllOf.  # noqa: E501
        :type: PullrequestAllOfMergeCommit
        """

        self._merge_commit = merge_commit

    @property
    def participants(self):
        """Gets the participants of this PullrequestAllOf.  # noqa: E501

                The list of users that are collaborating on this pull request.         Collaborators are user that:          * are added to the pull request as a reviewer (part of the reviewers           list)         * are not explicit reviewers, but have commented on the pull request         * are not explicit reviewers, but have approved the pull request          Each user is wrapped in an object that indicates the user's role and         whether they have approved the pull request. For performance reasons,         the API only returns this list when an API requests a pull request by         id.           # noqa: E501

        :return: The participants of this PullrequestAllOf.  # noqa: E501
        :rtype: list[Participant]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """Sets the participants of this PullrequestAllOf.

                The list of users that are collaborating on this pull request.         Collaborators are user that:          * are added to the pull request as a reviewer (part of the reviewers           list)         * are not explicit reviewers, but have commented on the pull request         * are not explicit reviewers, but have approved the pull request          Each user is wrapped in an object that indicates the user's role and         whether they have approved the pull request. For performance reasons,         the API only returns this list when an API requests a pull request by         id.           # noqa: E501

        :param participants: The participants of this PullrequestAllOf.  # noqa: E501
        :type: list[Participant]
        """

        self._participants = participants

    @property
    def reason(self):
        """Gets the reason of this PullrequestAllOf.  # noqa: E501

        Explains why a pull request was declined. This field is only applicable to pull requests in rejected state.  # noqa: E501

        :return: The reason of this PullrequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this PullrequestAllOf.

        Explains why a pull request was declined. This field is only applicable to pull requests in rejected state.  # noqa: E501

        :param reason: The reason of this PullrequestAllOf.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def rendered(self):
        """Gets the rendered of this PullrequestAllOf.  # noqa: E501


        :return: The rendered of this PullrequestAllOf.  # noqa: E501
        :rtype: PullrequestAllOfRendered
        """
        return self._rendered

    @rendered.setter
    def rendered(self, rendered):
        """Sets the rendered of this PullrequestAllOf.


        :param rendered: The rendered of this PullrequestAllOf.  # noqa: E501
        :type: PullrequestAllOfRendered
        """

        self._rendered = rendered

    @property
    def reviewers(self):
        """Gets the reviewers of this PullrequestAllOf.  # noqa: E501

        The list of users that were added as reviewers on this pull request when it was created. For performance reasons, the API only includes this list on a pull request's `self` URL.  # noqa: E501

        :return: The reviewers of this PullrequestAllOf.  # noqa: E501
        :rtype: list[Account]
        """
        return self._reviewers

    @reviewers.setter
    def reviewers(self, reviewers):
        """Sets the reviewers of this PullrequestAllOf.

        The list of users that were added as reviewers on this pull request when it was created. For performance reasons, the API only includes this list on a pull request's `self` URL.  # noqa: E501

        :param reviewers: The reviewers of this PullrequestAllOf.  # noqa: E501
        :type: list[Account]
        """

        self._reviewers = reviewers

    @property
    def source(self):
        """Gets the source of this PullrequestAllOf.  # noqa: E501


        :return: The source of this PullrequestAllOf.  # noqa: E501
        :rtype: PullrequestEndpoint
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this PullrequestAllOf.


        :param source: The source of this PullrequestAllOf.  # noqa: E501
        :type: PullrequestEndpoint
        """

        self._source = source

    @property
    def state(self):
        """Gets the state of this PullrequestAllOf.  # noqa: E501

        The pull request's current status.  # noqa: E501

        :return: The state of this PullrequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PullrequestAllOf.

        The pull request's current status.  # noqa: E501

        :param state: The state of this PullrequestAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["MERGED", "SUPERSEDED", "OPEN", "DECLINED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def summary(self):
        """Gets the summary of this PullrequestAllOf.  # noqa: E501


        :return: The summary of this PullrequestAllOf.  # noqa: E501
        :rtype: BaseCommitAllOfSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this PullrequestAllOf.


        :param summary: The summary of this PullrequestAllOf.  # noqa: E501
        :type: BaseCommitAllOfSummary
        """

        self._summary = summary

    @property
    def task_count(self):
        """Gets the task_count of this PullrequestAllOf.  # noqa: E501

        The number of open tasks for a specific pull request.  # noqa: E501

        :return: The task_count of this PullrequestAllOf.  # noqa: E501
        :rtype: int
        """
        return self._task_count

    @task_count.setter
    def task_count(self, task_count):
        """Sets the task_count of this PullrequestAllOf.

        The number of open tasks for a specific pull request.  # noqa: E501

        :param task_count: The task_count of this PullrequestAllOf.  # noqa: E501
        :type: int
        """
        if task_count is not None and task_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `task_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._task_count = task_count

    @property
    def title(self):
        """Gets the title of this PullrequestAllOf.  # noqa: E501

        Title of the pull request.  # noqa: E501

        :return: The title of this PullrequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PullrequestAllOf.

        Title of the pull request.  # noqa: E501

        :param title: The title of this PullrequestAllOf.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def updated_on(self):
        """Gets the updated_on of this PullrequestAllOf.  # noqa: E501

        The ISO8601 timestamp the request was last updated.  # noqa: E501

        :return: The updated_on of this PullrequestAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this PullrequestAllOf.

        The ISO8601 timestamp the request was last updated.  # noqa: E501

        :param updated_on: The updated_on of this PullrequestAllOf.  # noqa: E501
        :type: datetime
        """

        self._updated_on = updated_on

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
        if not isinstance(other, PullrequestAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

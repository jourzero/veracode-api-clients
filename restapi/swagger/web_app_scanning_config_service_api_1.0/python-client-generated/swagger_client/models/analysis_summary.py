# coding: utf-8

"""
    Veracode Web Application Scanning Configuration Service API

    Web Application Scanning Configuration API Documentation  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: veracode@veracode.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AnalysisSummary(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'org': 'str',
        'analysis_id': 'str',
        'name': 'str',
        'number_of_scans': 'int',
        'schedule_summary': 'ScanSchedule',
        'latest_occurrence_id': 'str',
        'latest_occurrence_date_time': 'str',
        'latest_occurrence_status': 'AnalysisOccurrenceStatus',
        'latest_verification_occurrence_id': 'str',
        'latest_verification_occurrence_status': 'AnalysisOccurrenceStatus',
        'next_occurrence_date_time': 'str',
        'has_verification_failures': 'bool',
        'has_result_import_in_progress': 'bool',
        'throttled': 'bool',
        'actions': 'list[str]',
        'created_on': 'str',
        'last_modified_on': 'str',
        'links': 'list[Link]',
        'capabilities': 'list[str]'
    }

    attribute_map = {
        'org': 'org',
        'analysis_id': 'analysis_id',
        'name': 'name',
        'number_of_scans': 'number_of_scans',
        'schedule_summary': 'schedule_summary',
        'latest_occurrence_id': 'latest_occurrence_id',
        'latest_occurrence_date_time': 'latest_occurrence_date_time',
        'latest_occurrence_status': 'latest_occurrence_status',
        'latest_verification_occurrence_id': 'latest_verification_occurrence_id',
        'latest_verification_occurrence_status': 'latest_verification_occurrence_status',
        'next_occurrence_date_time': 'next_occurrence_date_time',
        'has_verification_failures': 'has_verification_failures',
        'has_result_import_in_progress': 'has_result_import_in_progress',
        'throttled': 'throttled',
        'actions': 'actions',
        'created_on': 'created_on',
        'last_modified_on': 'last_modified_on',
        'links': '_links',
        'capabilities': 'capabilities'
    }

    def __init__(self, org=None, analysis_id=None, name=None, number_of_scans=None, schedule_summary=None, latest_occurrence_id=None, latest_occurrence_date_time=None, latest_occurrence_status=None, latest_verification_occurrence_id=None, latest_verification_occurrence_status=None, next_occurrence_date_time=None, has_verification_failures=None, has_result_import_in_progress=None, throttled=None, actions=None, created_on=None, last_modified_on=None, links=None, capabilities=None):  # noqa: E501
        """AnalysisSummary - a model defined in Swagger"""  # noqa: E501

        self._org = None
        self._analysis_id = None
        self._name = None
        self._number_of_scans = None
        self._schedule_summary = None
        self._latest_occurrence_id = None
        self._latest_occurrence_date_time = None
        self._latest_occurrence_status = None
        self._latest_verification_occurrence_id = None
        self._latest_verification_occurrence_status = None
        self._next_occurrence_date_time = None
        self._has_verification_failures = None
        self._has_result_import_in_progress = None
        self._throttled = None
        self._actions = None
        self._created_on = None
        self._last_modified_on = None
        self._links = None
        self._capabilities = None
        self.discriminator = None

        if org is not None:
            self.org = org
        if analysis_id is not None:
            self.analysis_id = analysis_id
        if name is not None:
            self.name = name
        if number_of_scans is not None:
            self.number_of_scans = number_of_scans
        if schedule_summary is not None:
            self.schedule_summary = schedule_summary
        if latest_occurrence_id is not None:
            self.latest_occurrence_id = latest_occurrence_id
        if latest_occurrence_date_time is not None:
            self.latest_occurrence_date_time = latest_occurrence_date_time
        if latest_occurrence_status is not None:
            self.latest_occurrence_status = latest_occurrence_status
        if latest_verification_occurrence_id is not None:
            self.latest_verification_occurrence_id = latest_verification_occurrence_id
        if latest_verification_occurrence_status is not None:
            self.latest_verification_occurrence_status = latest_verification_occurrence_status
        if next_occurrence_date_time is not None:
            self.next_occurrence_date_time = next_occurrence_date_time
        if has_verification_failures is not None:
            self.has_verification_failures = has_verification_failures
        if has_result_import_in_progress is not None:
            self.has_result_import_in_progress = has_result_import_in_progress
        if throttled is not None:
            self.throttled = throttled
        if actions is not None:
            self.actions = actions
        if created_on is not None:
            self.created_on = created_on
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if links is not None:
            self.links = links
        if capabilities is not None:
            self.capabilities = capabilities

    @property
    def org(self):
        """Gets the org of this AnalysisSummary.  # noqa: E501

        Organization identifier.  # noqa: E501

        :return: The org of this AnalysisSummary.  # noqa: E501
        :rtype: str
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this AnalysisSummary.

        Organization identifier.  # noqa: E501

        :param org: The org of this AnalysisSummary.  # noqa: E501
        :type: str
        """

        self._org = org

    @property
    def analysis_id(self):
        """Gets the analysis_id of this AnalysisSummary.  # noqa: E501

        Unique identifier of the Dynamic Analysis.  # noqa: E501

        :return: The analysis_id of this AnalysisSummary.  # noqa: E501
        :rtype: str
        """
        return self._analysis_id

    @analysis_id.setter
    def analysis_id(self, analysis_id):
        """Sets the analysis_id of this AnalysisSummary.

        Unique identifier of the Dynamic Analysis.  # noqa: E501

        :param analysis_id: The analysis_id of this AnalysisSummary.  # noqa: E501
        :type: str
        """

        self._analysis_id = analysis_id

    @property
    def name(self):
        """Gets the name of this AnalysisSummary.  # noqa: E501

        Name of the Dynamic Analysis.  # noqa: E501

        :return: The name of this AnalysisSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnalysisSummary.

        Name of the Dynamic Analysis.  # noqa: E501

        :param name: The name of this AnalysisSummary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number_of_scans(self):
        """Gets the number_of_scans of this AnalysisSummary.  # noqa: E501

        Number of URL scans in the Dynamic Analysis.  # noqa: E501

        :return: The number_of_scans of this AnalysisSummary.  # noqa: E501
        :rtype: int
        """
        return self._number_of_scans

    @number_of_scans.setter
    def number_of_scans(self, number_of_scans):
        """Sets the number_of_scans of this AnalysisSummary.

        Number of URL scans in the Dynamic Analysis.  # noqa: E501

        :param number_of_scans: The number_of_scans of this AnalysisSummary.  # noqa: E501
        :type: int
        """

        self._number_of_scans = number_of_scans

    @property
    def schedule_summary(self):
        """Gets the schedule_summary of this AnalysisSummary.  # noqa: E501

        Summary of the schedule for this Dynamic Analysis.  # noqa: E501

        :return: The schedule_summary of this AnalysisSummary.  # noqa: E501
        :rtype: ScanSchedule
        """
        return self._schedule_summary

    @schedule_summary.setter
    def schedule_summary(self, schedule_summary):
        """Sets the schedule_summary of this AnalysisSummary.

        Summary of the schedule for this Dynamic Analysis.  # noqa: E501

        :param schedule_summary: The schedule_summary of this AnalysisSummary.  # noqa: E501
        :type: ScanSchedule
        """

        self._schedule_summary = schedule_summary

    @property
    def latest_occurrence_id(self):
        """Gets the latest_occurrence_id of this AnalysisSummary.  # noqa: E501

        Identifier of the latest occurrence of this Dynamic Analysis.  # noqa: E501

        :return: The latest_occurrence_id of this AnalysisSummary.  # noqa: E501
        :rtype: str
        """
        return self._latest_occurrence_id

    @latest_occurrence_id.setter
    def latest_occurrence_id(self, latest_occurrence_id):
        """Sets the latest_occurrence_id of this AnalysisSummary.

        Identifier of the latest occurrence of this Dynamic Analysis.  # noqa: E501

        :param latest_occurrence_id: The latest_occurrence_id of this AnalysisSummary.  # noqa: E501
        :type: str
        """

        self._latest_occurrence_id = latest_occurrence_id

    @property
    def latest_occurrence_date_time(self):
        """Gets the latest_occurrence_date_time of this AnalysisSummary.  # noqa: E501

        Start date and time in ISO-8601 format for the latest occurrence of this Dynamic Analysis.  # noqa: E501

        :return: The latest_occurrence_date_time of this AnalysisSummary.  # noqa: E501
        :rtype: str
        """
        return self._latest_occurrence_date_time

    @latest_occurrence_date_time.setter
    def latest_occurrence_date_time(self, latest_occurrence_date_time):
        """Sets the latest_occurrence_date_time of this AnalysisSummary.

        Start date and time in ISO-8601 format for the latest occurrence of this Dynamic Analysis.  # noqa: E501

        :param latest_occurrence_date_time: The latest_occurrence_date_time of this AnalysisSummary.  # noqa: E501
        :type: str
        """

        self._latest_occurrence_date_time = latest_occurrence_date_time

    @property
    def latest_occurrence_status(self):
        """Gets the latest_occurrence_status of this AnalysisSummary.  # noqa: E501

        Status of the latest occurrence of this Dynamic Analysis.  # noqa: E501

        :return: The latest_occurrence_status of this AnalysisSummary.  # noqa: E501
        :rtype: AnalysisOccurrenceStatus
        """
        return self._latest_occurrence_status

    @latest_occurrence_status.setter
    def latest_occurrence_status(self, latest_occurrence_status):
        """Sets the latest_occurrence_status of this AnalysisSummary.

        Status of the latest occurrence of this Dynamic Analysis.  # noqa: E501

        :param latest_occurrence_status: The latest_occurrence_status of this AnalysisSummary.  # noqa: E501
        :type: AnalysisOccurrenceStatus
        """

        self._latest_occurrence_status = latest_occurrence_status

    @property
    def latest_verification_occurrence_id(self):
        """Gets the latest_verification_occurrence_id of this AnalysisSummary.  # noqa: E501

        Identifier of the latest verification-only occurrence of this Dynamic Analysis.  # noqa: E501

        :return: The latest_verification_occurrence_id of this AnalysisSummary.  # noqa: E501
        :rtype: str
        """
        return self._latest_verification_occurrence_id

    @latest_verification_occurrence_id.setter
    def latest_verification_occurrence_id(self, latest_verification_occurrence_id):
        """Sets the latest_verification_occurrence_id of this AnalysisSummary.

        Identifier of the latest verification-only occurrence of this Dynamic Analysis.  # noqa: E501

        :param latest_verification_occurrence_id: The latest_verification_occurrence_id of this AnalysisSummary.  # noqa: E501
        :type: str
        """

        self._latest_verification_occurrence_id = latest_verification_occurrence_id

    @property
    def latest_verification_occurrence_status(self):
        """Gets the latest_verification_occurrence_status of this AnalysisSummary.  # noqa: E501

        Status of the latest verification-only occurrence of this Dynamic Analysis.  # noqa: E501

        :return: The latest_verification_occurrence_status of this AnalysisSummary.  # noqa: E501
        :rtype: AnalysisOccurrenceStatus
        """
        return self._latest_verification_occurrence_status

    @latest_verification_occurrence_status.setter
    def latest_verification_occurrence_status(self, latest_verification_occurrence_status):
        """Sets the latest_verification_occurrence_status of this AnalysisSummary.

        Status of the latest verification-only occurrence of this Dynamic Analysis.  # noqa: E501

        :param latest_verification_occurrence_status: The latest_verification_occurrence_status of this AnalysisSummary.  # noqa: E501
        :type: AnalysisOccurrenceStatus
        """

        self._latest_verification_occurrence_status = latest_verification_occurrence_status

    @property
    def next_occurrence_date_time(self):
        """Gets the next_occurrence_date_time of this AnalysisSummary.  # noqa: E501

        Date and time in ISO-8601 format for the next scheduled occurrence of this Dynamic Analysis.  # noqa: E501

        :return: The next_occurrence_date_time of this AnalysisSummary.  # noqa: E501
        :rtype: str
        """
        return self._next_occurrence_date_time

    @next_occurrence_date_time.setter
    def next_occurrence_date_time(self, next_occurrence_date_time):
        """Sets the next_occurrence_date_time of this AnalysisSummary.

        Date and time in ISO-8601 format for the next scheduled occurrence of this Dynamic Analysis.  # noqa: E501

        :param next_occurrence_date_time: The next_occurrence_date_time of this AnalysisSummary.  # noqa: E501
        :type: str
        """

        self._next_occurrence_date_time = next_occurrence_date_time

    @property
    def has_verification_failures(self):
        """Gets the has_verification_failures of this AnalysisSummary.  # noqa: E501

        If this value is true, one or more URL scans in the analysis has failed verification.  # noqa: E501

        :return: The has_verification_failures of this AnalysisSummary.  # noqa: E501
        :rtype: bool
        """
        return self._has_verification_failures

    @has_verification_failures.setter
    def has_verification_failures(self, has_verification_failures):
        """Sets the has_verification_failures of this AnalysisSummary.

        If this value is true, one or more URL scans in the analysis has failed verification.  # noqa: E501

        :param has_verification_failures: The has_verification_failures of this AnalysisSummary.  # noqa: E501
        :type: bool
        """

        self._has_verification_failures = has_verification_failures

    @property
    def has_result_import_in_progress(self):
        """Gets the has_result_import_in_progress of this AnalysisSummary.  # noqa: E501

        If true, indicates one or more URL scans are having their results imported into corresponding linked application profiles.  # noqa: E501

        :return: The has_result_import_in_progress of this AnalysisSummary.  # noqa: E501
        :rtype: bool
        """
        return self._has_result_import_in_progress

    @has_result_import_in_progress.setter
    def has_result_import_in_progress(self, has_result_import_in_progress):
        """Sets the has_result_import_in_progress of this AnalysisSummary.

        If true, indicates one or more URL scans are having their results imported into corresponding linked application profiles.  # noqa: E501

        :param has_result_import_in_progress: The has_result_import_in_progress of this AnalysisSummary.  # noqa: E501
        :type: bool
        """

        self._has_result_import_in_progress = has_result_import_in_progress

    @property
    def throttled(self):
        """Gets the throttled of this AnalysisSummary.  # noqa: E501

        This value indicates that one or more URL scans of the latest occurrence of the Dynamic Analysis were throttled  because the maximum number of URL scans was reached.   # noqa: E501

        :return: The throttled of this AnalysisSummary.  # noqa: E501
        :rtype: bool
        """
        return self._throttled

    @throttled.setter
    def throttled(self, throttled):
        """Sets the throttled of this AnalysisSummary.

        This value indicates that one or more URL scans of the latest occurrence of the Dynamic Analysis were throttled  because the maximum number of URL scans was reached.   # noqa: E501

        :param throttled: The throttled of this AnalysisSummary.  # noqa: E501
        :type: bool
        """

        self._throttled = throttled

    @property
    def actions(self):
        """Gets the actions of this AnalysisSummary.  # noqa: E501

        The list of actions that can be performed to this Dynamic Analysis based on the status of its latest occurrence.  # noqa: E501

        :return: The actions of this AnalysisSummary.  # noqa: E501
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this AnalysisSummary.

        The list of actions that can be performed to this Dynamic Analysis based on the status of its latest occurrence.  # noqa: E501

        :param actions: The actions of this AnalysisSummary.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["STOP_SAVE", "STOP_DELETE", "PAUSE", "RESUME"]  # noqa: E501
        if not set(actions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `actions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(actions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._actions = actions

    @property
    def created_on(self):
        """Gets the created_on of this AnalysisSummary.  # noqa: E501

        The UTC-format date and time of when the Dynamic Analysis occurrence was created.  # noqa: E501

        :return: The created_on of this AnalysisSummary.  # noqa: E501
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this AnalysisSummary.

        The UTC-format date and time of when the Dynamic Analysis occurrence was created.  # noqa: E501

        :param created_on: The created_on of this AnalysisSummary.  # noqa: E501
        :type: str
        """

        self._created_on = created_on

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this AnalysisSummary.  # noqa: E501

        The UTC-format date and time when the Dynamic Analysis occurrence was last modified.  # noqa: E501

        :return: The last_modified_on of this AnalysisSummary.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this AnalysisSummary.

        The UTC-format date and time when the Dynamic Analysis occurrence was last modified.  # noqa: E501

        :param last_modified_on: The last_modified_on of this AnalysisSummary.  # noqa: E501
        :type: str
        """

        self._last_modified_on = last_modified_on

    @property
    def links(self):
        """Gets the links of this AnalysisSummary.  # noqa: E501


        :return: The links of this AnalysisSummary.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AnalysisSummary.


        :param links: The links of this AnalysisSummary.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def capabilities(self):
        """Gets the capabilities of this AnalysisSummary.  # noqa: E501


        :return: The capabilities of this AnalysisSummary.  # noqa: E501
        :rtype: list[str]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this AnalysisSummary.


        :param capabilities: The capabilities of this AnalysisSummary.  # noqa: E501
        :type: list[str]
        """

        self._capabilities = capabilities

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(AnalysisSummary, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AnalysisSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

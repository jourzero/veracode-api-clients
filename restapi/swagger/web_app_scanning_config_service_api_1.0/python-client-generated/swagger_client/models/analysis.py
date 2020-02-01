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


class Analysis(object):
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
        'analysis_id': 'str',
        'name': 'str',
        'org': 'str',
        'org_info': 'OrgInformation',
        'scan_setting': 'ScanSetting',
        'schedule': 'ScanSchedule',
        'special_instructions': 'str',
        'throttled': 'bool',
        'visibility': 'VisibilitySetup',
        'created_on': 'str',
        'last_modified_on': 'str',
        'latest_occurrence_status': 'AnalysisOccurrenceStatus',
        'links': 'list[Link]'
    }

    attribute_map = {
        'analysis_id': 'analysis_id',
        'name': 'name',
        'org': 'org',
        'org_info': 'org_info',
        'scan_setting': 'scan_setting',
        'schedule': 'schedule',
        'special_instructions': 'special_instructions',
        'throttled': 'throttled',
        'visibility': 'visibility',
        'created_on': 'created_on',
        'last_modified_on': 'last_modified_on',
        'latest_occurrence_status': 'latest_occurrence_status',
        'links': '_links'
    }

    def __init__(self, analysis_id=None, name=None, org=None, org_info=None, scan_setting=None, schedule=None, special_instructions=None, throttled=None, visibility=None, created_on=None, last_modified_on=None, latest_occurrence_status=None, links=None):  # noqa: E501
        """Analysis - a model defined in Swagger"""  # noqa: E501

        self._analysis_id = None
        self._name = None
        self._org = None
        self._org_info = None
        self._scan_setting = None
        self._schedule = None
        self._special_instructions = None
        self._throttled = None
        self._visibility = None
        self._created_on = None
        self._last_modified_on = None
        self._latest_occurrence_status = None
        self._links = None
        self.discriminator = None

        if analysis_id is not None:
            self.analysis_id = analysis_id
        if name is not None:
            self.name = name
        if org is not None:
            self.org = org
        if org_info is not None:
            self.org_info = org_info
        if scan_setting is not None:
            self.scan_setting = scan_setting
        if schedule is not None:
            self.schedule = schedule
        if special_instructions is not None:
            self.special_instructions = special_instructions
        if throttled is not None:
            self.throttled = throttled
        if visibility is not None:
            self.visibility = visibility
        if created_on is not None:
            self.created_on = created_on
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if latest_occurrence_status is not None:
            self.latest_occurrence_status = latest_occurrence_status
        if links is not None:
            self.links = links

    @property
    def analysis_id(self):
        """Gets the analysis_id of this Analysis.  # noqa: E501

        Identifier of the Dynamic Analysis.  # noqa: E501

        :return: The analysis_id of this Analysis.  # noqa: E501
        :rtype: str
        """
        return self._analysis_id

    @analysis_id.setter
    def analysis_id(self, analysis_id):
        """Sets the analysis_id of this Analysis.

        Identifier of the Dynamic Analysis.  # noqa: E501

        :param analysis_id: The analysis_id of this Analysis.  # noqa: E501
        :type: str
        """

        self._analysis_id = analysis_id

    @property
    def name(self):
        """Gets the name of this Analysis.  # noqa: E501

        Name of the Dynamic Analysis.  # noqa: E501

        :return: The name of this Analysis.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Analysis.

        Name of the Dynamic Analysis.  # noqa: E501

        :param name: The name of this Analysis.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def org(self):
        """Gets the org of this Analysis.  # noqa: E501

        Identifier of the organization.  # noqa: E501

        :return: The org of this Analysis.  # noqa: E501
        :rtype: str
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this Analysis.

        Identifier of the organization.  # noqa: E501

        :param org: The org of this Analysis.  # noqa: E501
        :type: str
        """

        self._org = org

    @property
    def org_info(self):
        """Gets the org_info of this Analysis.  # noqa: E501

        Organization details.  # noqa: E501

        :return: The org_info of this Analysis.  # noqa: E501
        :rtype: OrgInformation
        """
        return self._org_info

    @org_info.setter
    def org_info(self, org_info):
        """Sets the org_info of this Analysis.

        Organization details.  # noqa: E501

        :param org_info: The org_info of this Analysis.  # noqa: E501
        :type: OrgInformation
        """

        self._org_info = org_info

    @property
    def scan_setting(self):
        """Gets the scan_setting of this Analysis.  # noqa: E501

        Scan setting for the Dynamic Analysis that applies to all URL scans in analysis, unless overridden at the URL scan level.  # noqa: E501

        :return: The scan_setting of this Analysis.  # noqa: E501
        :rtype: ScanSetting
        """
        return self._scan_setting

    @scan_setting.setter
    def scan_setting(self, scan_setting):
        """Sets the scan_setting of this Analysis.

        Scan setting for the Dynamic Analysis that applies to all URL scans in analysis, unless overridden at the URL scan level.  # noqa: E501

        :param scan_setting: The scan_setting of this Analysis.  # noqa: E501
        :type: ScanSetting
        """

        self._scan_setting = scan_setting

    @property
    def schedule(self):
        """Gets the schedule of this Analysis.  # noqa: E501

        The schedule for the Dynamic Analysis.  # noqa: E501

        :return: The schedule of this Analysis.  # noqa: E501
        :rtype: ScanSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this Analysis.

        The schedule for the Dynamic Analysis.  # noqa: E501

        :param schedule: The schedule of this Analysis.  # noqa: E501
        :type: ScanSchedule
        """

        self._schedule = schedule

    @property
    def special_instructions(self):
        """Gets the special_instructions of this Analysis.  # noqa: E501

        Special instructions related to the Dynamic Analysis. Can be null. Instructions can delay the analysis.  # noqa: E501

        :return: The special_instructions of this Analysis.  # noqa: E501
        :rtype: str
        """
        return self._special_instructions

    @special_instructions.setter
    def special_instructions(self, special_instructions):
        """Sets the special_instructions of this Analysis.

        Special instructions related to the Dynamic Analysis. Can be null. Instructions can delay the analysis.  # noqa: E501

        :param special_instructions: The special_instructions of this Analysis.  # noqa: E501
        :type: str
        """

        self._special_instructions = special_instructions

    @property
    def throttled(self):
        """Gets the throttled of this Analysis.  # noqa: E501


        :return: The throttled of this Analysis.  # noqa: E501
        :rtype: bool
        """
        return self._throttled

    @throttled.setter
    def throttled(self, throttled):
        """Sets the throttled of this Analysis.


        :param throttled: The throttled of this Analysis.  # noqa: E501
        :type: bool
        """

        self._throttled = throttled

    @property
    def visibility(self):
        """Gets the visibility of this Analysis.  # noqa: E501

        The setting that determines who can access the analysis.  # noqa: E501

        :return: The visibility of this Analysis.  # noqa: E501
        :rtype: VisibilitySetup
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this Analysis.

        The setting that determines who can access the analysis.  # noqa: E501

        :param visibility: The visibility of this Analysis.  # noqa: E501
        :type: VisibilitySetup
        """

        self._visibility = visibility

    @property
    def created_on(self):
        """Gets the created_on of this Analysis.  # noqa: E501

        The UTC-format date and time when the Dynamic Analysis was created.  # noqa: E501

        :return: The created_on of this Analysis.  # noqa: E501
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Analysis.

        The UTC-format date and time when the Dynamic Analysis was created.  # noqa: E501

        :param created_on: The created_on of this Analysis.  # noqa: E501
        :type: str
        """

        self._created_on = created_on

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this Analysis.  # noqa: E501

        UTC-format date and time when the Dynamic Analysis was last modified.  # noqa: E501

        :return: The last_modified_on of this Analysis.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this Analysis.

        UTC-format date and time when the Dynamic Analysis was last modified.  # noqa: E501

        :param last_modified_on: The last_modified_on of this Analysis.  # noqa: E501
        :type: str
        """

        self._last_modified_on = last_modified_on

    @property
    def latest_occurrence_status(self):
        """Gets the latest_occurrence_status of this Analysis.  # noqa: E501

        Status of the latest occurrence of this Dynamic Analysis.  # noqa: E501

        :return: The latest_occurrence_status of this Analysis.  # noqa: E501
        :rtype: AnalysisOccurrenceStatus
        """
        return self._latest_occurrence_status

    @latest_occurrence_status.setter
    def latest_occurrence_status(self, latest_occurrence_status):
        """Sets the latest_occurrence_status of this Analysis.

        Status of the latest occurrence of this Dynamic Analysis.  # noqa: E501

        :param latest_occurrence_status: The latest_occurrence_status of this Analysis.  # noqa: E501
        :type: AnalysisOccurrenceStatus
        """

        self._latest_occurrence_status = latest_occurrence_status

    @property
    def links(self):
        """Gets the links of this Analysis.  # noqa: E501


        :return: The links of this Analysis.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Analysis.


        :param links: The links of this Analysis.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

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
        if issubclass(Analysis, dict):
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
        if not isinstance(other, Analysis):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

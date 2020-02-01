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


class ScanSchedule(object):
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
        'duration': 'ScanDuration',
        'effective_end_date': 'str',
        'effective_start_date': 'str',
        'end_date': 'str',
        'now': 'bool',
        'scan_blackout_schedule': 'ScanBlackoutSchedule',
        'scan_recurrence_schedule': 'ScanRecurrenceSchedule',
        'schedule_status': 'str',
        'start_date': 'str'
    }

    attribute_map = {
        'duration': 'duration',
        'effective_end_date': 'effective_end_date',
        'effective_start_date': 'effective_start_date',
        'end_date': 'end_date',
        'now': 'now',
        'scan_blackout_schedule': 'scan_blackout_schedule',
        'scan_recurrence_schedule': 'scan_recurrence_schedule',
        'schedule_status': 'schedule_status',
        'start_date': 'start_date'
    }

    def __init__(self, duration=None, effective_end_date=None, effective_start_date=None, end_date=None, now=None, scan_blackout_schedule=None, scan_recurrence_schedule=None, schedule_status=None, start_date=None):  # noqa: E501
        """ScanSchedule - a model defined in Swagger"""  # noqa: E501

        self._duration = None
        self._effective_end_date = None
        self._effective_start_date = None
        self._end_date = None
        self._now = None
        self._scan_blackout_schedule = None
        self._scan_recurrence_schedule = None
        self._schedule_status = None
        self._start_date = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if effective_end_date is not None:
            self.effective_end_date = effective_end_date
        if effective_start_date is not None:
            self.effective_start_date = effective_start_date
        if end_date is not None:
            self.end_date = end_date
        if now is not None:
            self.now = now
        if scan_blackout_schedule is not None:
            self.scan_blackout_schedule = scan_blackout_schedule
        if scan_recurrence_schedule is not None:
            self.scan_recurrence_schedule = scan_recurrence_schedule
        if schedule_status is not None:
            self.schedule_status = schedule_status
        if start_date is not None:
            self.start_date = start_date

    @property
    def duration(self):
        """Gets the duration of this ScanSchedule.  # noqa: E501

        Duration of the URL scan.  # noqa: E501

        :return: The duration of this ScanSchedule.  # noqa: E501
        :rtype: ScanDuration
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ScanSchedule.

        Duration of the URL scan.  # noqa: E501

        :param duration: The duration of this ScanSchedule.  # noqa: E501
        :type: ScanDuration
        """

        self._duration = duration

    @property
    def effective_end_date(self):
        """Gets the effective_end_date of this ScanSchedule.  # noqa: E501

        Present only in responses. The effective end date in ISO-8601 format of the URL scan as calculated from the specified schedule.  # noqa: E501

        :return: The effective_end_date of this ScanSchedule.  # noqa: E501
        :rtype: str
        """
        return self._effective_end_date

    @effective_end_date.setter
    def effective_end_date(self, effective_end_date):
        """Sets the effective_end_date of this ScanSchedule.

        Present only in responses. The effective end date in ISO-8601 format of the URL scan as calculated from the specified schedule.  # noqa: E501

        :param effective_end_date: The effective_end_date of this ScanSchedule.  # noqa: E501
        :type: str
        """

        self._effective_end_date = effective_end_date

    @property
    def effective_start_date(self):
        """Gets the effective_start_date of this ScanSchedule.  # noqa: E501

        Present only in responses. The effective start date in ISO-8601 format of the URL scan as calculated from the specified schedule.  # noqa: E501

        :return: The effective_start_date of this ScanSchedule.  # noqa: E501
        :rtype: str
        """
        return self._effective_start_date

    @effective_start_date.setter
    def effective_start_date(self, effective_start_date):
        """Sets the effective_start_date of this ScanSchedule.

        Present only in responses. The effective start date in ISO-8601 format of the URL scan as calculated from the specified schedule.  # noqa: E501

        :param effective_start_date: The effective_start_date of this ScanSchedule.  # noqa: E501
        :type: str
        """

        self._effective_start_date = effective_start_date

    @property
    def end_date(self):
        """Gets the end_date of this ScanSchedule.  # noqa: E501

        If the URL scan duration is zero or less, you must specify the end date as a date and time in future,  and it must be later than the startDate. Must be in ISO-8601 format, for example: 2016-12-03T10:15+01:00.  You can include seconds and milliseconds but are ignored.   # noqa: E501

        :return: The end_date of this ScanSchedule.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ScanSchedule.

        If the URL scan duration is zero or less, you must specify the end date as a date and time in future,  and it must be later than the startDate. Must be in ISO-8601 format, for example: 2016-12-03T10:15+01:00.  You can include seconds and milliseconds but are ignored.   # noqa: E501

        :param end_date: The end_date of this ScanSchedule.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def now(self):
        """Gets the now of this ScanSchedule.  # noqa: E501

        Indicates that the URL scan should start as soon as possible.  # noqa: E501

        :return: The now of this ScanSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._now

    @now.setter
    def now(self, now):
        """Sets the now of this ScanSchedule.

        Indicates that the URL scan should start as soon as possible.  # noqa: E501

        :param now: The now of this ScanSchedule.  # noqa: E501
        :type: bool
        """

        self._now = now

    @property
    def scan_blackout_schedule(self):
        """Gets the scan_blackout_schedule of this ScanSchedule.  # noqa: E501

        URL scan blackout configuration to schedule auto-pause and resume.  # noqa: E501

        :return: The scan_blackout_schedule of this ScanSchedule.  # noqa: E501
        :rtype: ScanBlackoutSchedule
        """
        return self._scan_blackout_schedule

    @scan_blackout_schedule.setter
    def scan_blackout_schedule(self, scan_blackout_schedule):
        """Sets the scan_blackout_schedule of this ScanSchedule.

        URL scan blackout configuration to schedule auto-pause and resume.  # noqa: E501

        :param scan_blackout_schedule: The scan_blackout_schedule of this ScanSchedule.  # noqa: E501
        :type: ScanBlackoutSchedule
        """

        self._scan_blackout_schedule = scan_blackout_schedule

    @property
    def scan_recurrence_schedule(self):
        """Gets the scan_recurrence_schedule of this ScanSchedule.  # noqa: E501

        URL scan recurrence configuration to schedule batch scans on a recurring basis.  # noqa: E501

        :return: The scan_recurrence_schedule of this ScanSchedule.  # noqa: E501
        :rtype: ScanRecurrenceSchedule
        """
        return self._scan_recurrence_schedule

    @scan_recurrence_schedule.setter
    def scan_recurrence_schedule(self, scan_recurrence_schedule):
        """Sets the scan_recurrence_schedule of this ScanSchedule.

        URL scan recurrence configuration to schedule batch scans on a recurring basis.  # noqa: E501

        :param scan_recurrence_schedule: The scan_recurrence_schedule of this ScanSchedule.  # noqa: E501
        :type: ScanRecurrenceSchedule
        """

        self._scan_recurrence_schedule = scan_recurrence_schedule

    @property
    def schedule_status(self):
        """Gets the schedule_status of this ScanSchedule.  # noqa: E501

        The status of the current schedule, whether active, completed, or canceled.  # noqa: E501

        :return: The schedule_status of this ScanSchedule.  # noqa: E501
        :rtype: str
        """
        return self._schedule_status

    @schedule_status.setter
    def schedule_status(self, schedule_status):
        """Sets the schedule_status of this ScanSchedule.

        The status of the current schedule, whether active, completed, or canceled.  # noqa: E501

        :param schedule_status: The schedule_status of this ScanSchedule.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "CANCELED", "COMPLETED"]  # noqa: E501
        if schedule_status not in allowed_values:
            raise ValueError(
                "Invalid value for `schedule_status` ({0}), must be one of {1}"  # noqa: E501
                .format(schedule_status, allowed_values)
            )

        self._schedule_status = schedule_status

    @property
    def start_date(self):
        """Gets the start_date of this ScanSchedule.  # noqa: E501

        The date and time the URL scan should start. Must be in ISO-8601 format, for example:  2016-12-03T10:15+01:00. You can include seconds and milliseconds but they are ignored. If now is set to true, this value is calcuated  as the current time, unless already specified.   # noqa: E501

        :return: The start_date of this ScanSchedule.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ScanSchedule.

        The date and time the URL scan should start. Must be in ISO-8601 format, for example:  2016-12-03T10:15+01:00. You can include seconds and milliseconds but they are ignored. If now is set to true, this value is calcuated  as the current time, unless already specified.   # noqa: E501

        :param start_date: The start_date of this ScanSchedule.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

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
        if issubclass(ScanSchedule, dict):
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
        if not isinstance(other, ScanSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

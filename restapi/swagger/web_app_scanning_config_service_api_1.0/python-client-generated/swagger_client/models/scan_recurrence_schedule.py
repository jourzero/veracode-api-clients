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


class ScanRecurrenceSchedule(object):
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
        'day_of_week': 'str',
        'recurrence_interval': 'int',
        'recurrence_type': 'str',
        'schedule_end_after': 'int',
        'week_of_month': 'str'
    }

    attribute_map = {
        'day_of_week': 'day_of_week',
        'recurrence_interval': 'recurrence_interval',
        'recurrence_type': 'recurrence_type',
        'schedule_end_after': 'schedule_end_after',
        'week_of_month': 'week_of_month'
    }

    def __init__(self, day_of_week=None, recurrence_interval=None, recurrence_type=None, schedule_end_after=None, week_of_month=None):  # noqa: E501
        """ScanRecurrenceSchedule - a model defined in Swagger"""  # noqa: E501

        self._day_of_week = None
        self._recurrence_interval = None
        self._recurrence_type = None
        self._schedule_end_after = None
        self._week_of_month = None
        self.discriminator = None

        if day_of_week is not None:
            self.day_of_week = day_of_week
        if recurrence_interval is not None:
            self.recurrence_interval = recurrence_interval
        if recurrence_type is not None:
            self.recurrence_type = recurrence_type
        if schedule_end_after is not None:
            self.schedule_end_after = schedule_end_after
        if week_of_month is not None:
            self.week_of_month = week_of_month

    @property
    def day_of_week(self):
        """Gets the day_of_week of this ScanRecurrenceSchedule.  # noqa: E501

        The day of the week.  # noqa: E501

        :return: The day_of_week of this ScanRecurrenceSchedule.  # noqa: E501
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """Sets the day_of_week of this ScanRecurrenceSchedule.

        The day of the week.  # noqa: E501

        :param day_of_week: The day_of_week of this ScanRecurrenceSchedule.  # noqa: E501
        :type: str
        """
        allowed_values = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]  # noqa: E501
        if day_of_week not in allowed_values:
            raise ValueError(
                "Invalid value for `day_of_week` ({0}), must be one of {1}"  # noqa: E501
                .format(day_of_week, allowed_values)
            )

        self._day_of_week = day_of_week

    @property
    def recurrence_interval(self):
        """Gets the recurrence_interval of this ScanRecurrenceSchedule.  # noqa: E501

        The time between two recurrences of a URL scan.  # noqa: E501

        :return: The recurrence_interval of this ScanRecurrenceSchedule.  # noqa: E501
        :rtype: int
        """
        return self._recurrence_interval

    @recurrence_interval.setter
    def recurrence_interval(self, recurrence_interval):
        """Sets the recurrence_interval of this ScanRecurrenceSchedule.

        The time between two recurrences of a URL scan.  # noqa: E501

        :param recurrence_interval: The recurrence_interval of this ScanRecurrenceSchedule.  # noqa: E501
        :type: int
        """

        self._recurrence_interval = recurrence_interval

    @property
    def recurrence_type(self):
        """Gets the recurrence_type of this ScanRecurrenceSchedule.  # noqa: E501

        The URL scan recurrence schedule type.  # noqa: E501

        :return: The recurrence_type of this ScanRecurrenceSchedule.  # noqa: E501
        :rtype: str
        """
        return self._recurrence_type

    @recurrence_type.setter
    def recurrence_type(self, recurrence_type):
        """Sets the recurrence_type of this ScanRecurrenceSchedule.

        The URL scan recurrence schedule type.  # noqa: E501

        :param recurrence_type: The recurrence_type of this ScanRecurrenceSchedule.  # noqa: E501
        :type: str
        """
        allowed_values = ["MONTHLY", "WEEKLY"]  # noqa: E501
        if recurrence_type not in allowed_values:
            raise ValueError(
                "Invalid value for `recurrence_type` ({0}), must be one of {1}"  # noqa: E501
                .format(recurrence_type, allowed_values)
            )

        self._recurrence_type = recurrence_type

    @property
    def schedule_end_after(self):
        """Gets the schedule_end_after of this ScanRecurrenceSchedule.  # noqa: E501

        The end of the recurrence schedule.  # noqa: E501

        :return: The schedule_end_after of this ScanRecurrenceSchedule.  # noqa: E501
        :rtype: int
        """
        return self._schedule_end_after

    @schedule_end_after.setter
    def schedule_end_after(self, schedule_end_after):
        """Sets the schedule_end_after of this ScanRecurrenceSchedule.

        The end of the recurrence schedule.  # noqa: E501

        :param schedule_end_after: The schedule_end_after of this ScanRecurrenceSchedule.  # noqa: E501
        :type: int
        """

        self._schedule_end_after = schedule_end_after

    @property
    def week_of_month(self):
        """Gets the week_of_month of this ScanRecurrenceSchedule.  # noqa: E501

        The week of the month.  # noqa: E501

        :return: The week_of_month of this ScanRecurrenceSchedule.  # noqa: E501
        :rtype: str
        """
        return self._week_of_month

    @week_of_month.setter
    def week_of_month(self, week_of_month):
        """Sets the week_of_month of this ScanRecurrenceSchedule.

        The week of the month.  # noqa: E501

        :param week_of_month: The week_of_month of this ScanRecurrenceSchedule.  # noqa: E501
        :type: str
        """
        allowed_values = ["FIRST", "SECOND", "THIRD", "FOURTH", "LAST"]  # noqa: E501
        if week_of_month not in allowed_values:
            raise ValueError(
                "Invalid value for `week_of_month` ({0}), must be one of {1}"  # noqa: E501
                .format(week_of_month, allowed_values)
            )

        self._week_of_month = week_of_month

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
        if issubclass(ScanRecurrenceSchedule, dict):
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
        if not isinstance(other, ScanRecurrenceSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

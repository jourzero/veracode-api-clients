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


class ScanOccurrenceStatus(object):
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
        'status_type': 'str'
    }

    attribute_map = {
        'status_type': 'status_type'
    }

    def __init__(self, status_type=None):  # noqa: E501
        """ScanOccurrenceStatus - a model defined in Swagger"""  # noqa: E501

        self._status_type = None
        self.discriminator = None

        if status_type is not None:
            self.status_type = status_type

    @property
    def status_type(self):
        """Gets the status_type of this ScanOccurrenceStatus.  # noqa: E501

        The URL scan occurrence status type code.  # noqa: E501

        :return: The status_type of this ScanOccurrenceStatus.  # noqa: E501
        :rtype: str
        """
        return self._status_type

    @status_type.setter
    def status_type(self, status_type):
        """Sets the status_type of this ScanOccurrenceStatus.

        The URL scan occurrence status type code.  # noqa: E501

        :param status_type: The status_type of this ScanOccurrenceStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["SCHEDULED", "SUBMITTED", "SUBMIT_FAILED", "VERIFICATION_FAILED", "QUEUED", "QUEUED_WITH_WARNING", "IN_PROGRESS", "IN_PROGRESS_WITH_WARNING", "PAUSING", "PAUSED", "RESUMING", "STOPPING_SAVING_RESULT", "STOPPING_DELETING_RESULT", "STOPPED", "STOPPED_TIME", "STOPPED_TIME_VERIFYING_RESULTS", "STOPPED_TECHNICAL_ISSUE", "STOPPED_VERIFYING_RESULTS_BY_USER", "STOPPED_VERIFYING_RESULTS", "FINISHED_VERIFYING_RESULTS", "FINISHED_RESULTS_AVAILABLE"]  # noqa: E501
        if status_type not in allowed_values:
            raise ValueError(
                "Invalid value for `status_type` ({0}), must be one of {1}"  # noqa: E501
                .format(status_type, allowed_values)
            )

        self._status_type = status_type

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
        if issubclass(ScanOccurrenceStatus, dict):
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
        if not isinstance(other, ScanOccurrenceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

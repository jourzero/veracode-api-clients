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


class ServiceError(object):
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
        'code': 'str',
        'id': 'str',
        'meta': 'object',
        'source': 'Source',
        'status': 'str'
    }

    attribute_map = {
        'code': 'code',
        'id': 'id',
        'meta': 'meta',
        'source': 'source',
        'status': 'status'
    }

    def __init__(self, code=None, id=None, meta=None, source=None, status=None):  # noqa: E501
        """ServiceError - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._id = None
        self._meta = None
        self._source = None
        self._status = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if id is not None:
            self.id = id
        if meta is not None:
            self.meta = meta
        if source is not None:
            self.source = source
        if status is not None:
            self.status = status

    @property
    def code(self):
        """Gets the code of this ServiceError.  # noqa: E501

        The coded enum of the error.  # noqa: E501

        :return: The code of this ServiceError.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ServiceError.

        The coded enum of the error.  # noqa: E501

        :param code: The code of this ServiceError.  # noqa: E501
        :type: str
        """
        allowed_values = ["INVALID_ANALYSIS_IDENTIFIER", "INVALID_ANALYSIS_STATE", "NAME_ERROR", "INVALID_NUMBER_OF_SCANS", "INVALID_SCHEDULE", "INVALID_BATCH_SETTING", "SCAN_VALIDATION_ERROR", "INVALID_ACTION_TYPE", "SCAN_IDENTIFIER_NOT_SPECIFIED", "INVALID_SCAN_IDENTIFIER", "SCAN_IN_USE", "INVALID_APPLICATION_REQUEST", "INVALID_SCAN_CONFIGURATION_REQUEST", "SCAN_LOCKED", "GATEWAY_IDENTIFIER_NOT_SPECIFIED", "ENDPOINT_IDENTIFIER_NOT_SPECIFIED", "INVALID_GATEWAY_OR_ENDPOINT_IDENTIFIER", "FAILED_TO_VALIDATE_INTERNAL_SCAN_CONFIGURATION", "APP_LINK_ERROR", "INVALID_APPLICATION_IDENTIFIER", "NAME_NOT_SPECIFIED", "NAME_NOT_UNIQUE", "NAME_INVALID_LENGTH", "APPLICATION_ID_NOT_SPECIFIED", "INVALID_APPLICATION_ID", "SCAN_NOT_LINKED_TO_AN_APP", "RESULT_IMPORT_INPROGRESS_FOR_SCAN", "APPLICATION_NOT_FOUND", "ACCESS_DENIED_FOR_APPLICATION", "UNEXPECTED_RESPONSE_ON_RETRIEVE_APP", "UNEXPECTED_RESPONSE_ON_RETRIEVE_APPS", "DUPLICATE_LINK_APP_ID_IN_SAME_ANALYSIS", "MISSING_SCAN_CONFIGURATION", "INVALID_SCAN_CONFIGURATION_IDENTIFIER", "INVALID_TARGET_URL", "DUPLICATE_SCAN_CONFIGURATION", "INVALID_AUTH_SETTING", "INVALID_CRAWL_SETTING", "INVALID_SCAN_SETTING", "INVALID_INCLUSION_LIST", "START_DATE_NOT_SPECIFIED", "MISSING_DURATION", "WRONG_DURATION", "ENDS_IN_PAST", "END_DATE_BEFORE_START_DATE", "TOO_FAR_IN_FUTURE", "INVALID_START_DATE", "INVALID_NUMBER_OF_INTERVALS_FOR_RECURRING_SCANS", "INVALID_NUMBER_OF_EVENTS_FOR_RECURRING_SCANS", "RECURRING_SCAN_STARTS_DURING_INITIAL_SCAN", "INVALID_DURATION_FOR_SCAN_RECURRENCE", "INVALID_SCHEDULE_END_FOR_RECURRING_SCHEDULE", "INVALID_CONFIGURATION_FOR_WEEKLY_RECURRING_SCHEDULE", "INVALID_RECURRENCE_TYPE", "INVALID_BLACKOUT_TYPE", "BLACKOUT_DAYS_NOT_SPECIFIED", "INVALID_START_TIME_FOR_BLACKOUT_SCHEDULE", "INVALID_END_TIME_FOR_BLACKOUT_SCHEDULE", "TOO_SHORT_BLACKOUT_THESE_HOURS_DURATION", "TOO_LONG_BLACKOUT_THESE_HOURS_DURATION", "INVALID_BLACKOUT_DAYS_FOR_THESE_DAYS_SCHEDULE", "SCAN_CANNOT_START_INSIDE_BLACKOUT_PERIOD", "ONE_OF_THE_RECURRING_SCANS_IS_INSIDE_BLACKOUT_PERIOD", "TOO_SHORT_SCAN_DURATION_FOR_AUTO_PAUSE_RESUME", "NOT_ENOUGH_DURATION_TO_CREATE_OCCURRENCE", "ANALYSIS_OCCURRENCE_IS_ACTIVE_FOR_ANALYSIS", "ANOTHER_VERIFICATION_OCCURRENCE_IS_ACTIVE_FOR_ANALYSIS", "INVALID_MAX_LINKS", "INVALID_RESPONSE_TIMEOUT", "INVALID_EXCLUSION_LIST", "INVALIDATED_SAVED_SCANS", "MISSING_TARGET_URL", "MALFORMED_URL", "IPV6_NOT_SUPPORTED", "INAPPROPRIATE_PROTOCOL", "USERINFO_DETECTED_IN_URL", "OUT_OF_SCOPE_TARGET_URL", "EXCLUDED_TARGET_URL", "LOCALHOST_URL", "PRIVATE_IP_URL", "TOO_SHORT_SCAN_WINDOW", "TOO_SHORT_VERIFICATION_WINDOW", "INVALID_SCAN_STATUS", "INVALID_ANALYSIS_STATUS", "OCCURRENCE_NOT_READY", "LICENSE_NOT_FOUND_FOR_ORGID", "ACCESS_DENIED_FOR_ORG", "UNEXPECTED_RESPONSE_ON_RETRIEVE_LICENSE", "EXCLUDED_INCLUSION_URL", "INVALID_AUTH_IDENTIFIER", "MISSING_USERNAME", "INVALID_USERNAME_LENGTH", "MISSING_PASSWORD", "INVALID_PASSWORD_LENGTH", "INVALID_DOMAIN_LENGTH", "MISSING_SELENIUM_SCRIPT", "INVALID_SELENIUM_SCRIPT_LENGTH", "INVALID_SELENIUM_SCRIPT_CONTENT", "UNSUPPORTED_SCRIPT_TYPE", "MORE_THAN_ONE_SCRIPT", "UNSUPPORTED_SCRIPT_FEATURES", "NO_SCRIPT", "MISSING_SCRIPT_FEATURES", "MISSING_SELENIUM_VERIFICATION_URL_OR_PATTERN", "INVALID_VERIFICATION_URL", "MISSING_VERIFICATION_AND_LOGOUTDETECTION", "INVALID_LOGOUT_DETECTION_PATTERN_LENGTH", "INVALID_VERIFICATION_URL_LENGTH", "INVALID_VERIFICATION_PATTERN_LENGTH", "ANALYSIS_OCCURRENCE_REQUEST_ERROR", "SERVICE_ACCESS_ERROR", "EMPTY_FILE_CONTENT", "RESOURCE_DELETED", "INVALID_ID", "INVALID_CONTACT_INFO", "INVALID_BUSINESS_OWNER", "INVALID_INPUT", "INVALID_USERNAME", "INVALID_CUSTOM_USER_AGENT", "INVALID_DOMAIN", "INVALID_VERIFICATION_TEXT"]  # noqa: E501
        if code not in allowed_values:
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"  # noqa: E501
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def id(self):
        """Gets the id of this ServiceError.  # noqa: E501

        The unique identifier of the error. This value indicates that the error was logged on the service and you can use it to troubleshoot.  # noqa: E501

        :return: The id of this ServiceError.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServiceError.

        The unique identifier of the error. This value indicates that the error was logged on the service and you can use it to troubleshoot.  # noqa: E501

        :param id: The id of this ServiceError.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def meta(self):
        """Gets the meta of this ServiceError.  # noqa: E501

        Additional information regarding the error.  # noqa: E501

        :return: The meta of this ServiceError.  # noqa: E501
        :rtype: object
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ServiceError.

        Additional information regarding the error.  # noqa: E501

        :param meta: The meta of this ServiceError.  # noqa: E501
        :type: object
        """

        self._meta = meta

    @property
    def source(self):
        """Gets the source of this ServiceError.  # noqa: E501

        The location where the error originates if this error is related to an API parameter.  # noqa: E501

        :return: The source of this ServiceError.  # noqa: E501
        :rtype: Source
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ServiceError.

        The location where the error originates if this error is related to an API parameter.  # noqa: E501

        :param source: The source of this ServiceError.  # noqa: E501
        :type: Source
        """

        self._source = source

    @property
    def status(self):
        """Gets the status of this ServiceError.  # noqa: E501

        'String value of the HTTP status that best represents the error, for example: 404.'   # noqa: E501

        :return: The status of this ServiceError.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ServiceError.

        'String value of the HTTP status that best represents the error, for example: 404.'   # noqa: E501

        :param status: The status of this ServiceError.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(ServiceError, dict):
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
        if not isinstance(other, ServiceError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

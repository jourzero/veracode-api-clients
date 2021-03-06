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


class ScanSetting(object):
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
        'blacklist_configuration': 'BlacklistConfiguration',
        'advanced_mode': 'bool',
        'user_agent': 'UserAgent'
    }

    attribute_map = {
        'blacklist_configuration': 'blacklist_configuration',
        'advanced_mode': 'advanced_mode',
        'user_agent': 'user_agent'
    }

    def __init__(self, blacklist_configuration=None, advanced_mode=None, user_agent=None):  # noqa: E501
        """ScanSetting - a model defined in Swagger"""  # noqa: E501

        self._blacklist_configuration = None
        self._advanced_mode = None
        self._user_agent = None
        self.discriminator = None

        if blacklist_configuration is not None:
            self.blacklist_configuration = blacklist_configuration
        if advanced_mode is not None:
            self.advanced_mode = advanced_mode
        if user_agent is not None:
            self.user_agent = user_agent

    @property
    def blacklist_configuration(self):
        """Gets the blacklist_configuration of this ScanSetting.  # noqa: E501

        The blacklist configuration for the URL scan, including rules to exclude specific URLs during the URL scan.  # noqa: E501

        :return: The blacklist_configuration of this ScanSetting.  # noqa: E501
        :rtype: BlacklistConfiguration
        """
        return self._blacklist_configuration

    @blacklist_configuration.setter
    def blacklist_configuration(self, blacklist_configuration):
        """Sets the blacklist_configuration of this ScanSetting.

        The blacklist configuration for the URL scan, including rules to exclude specific URLs during the URL scan.  # noqa: E501

        :param blacklist_configuration: The blacklist_configuration of this ScanSetting.  # noqa: E501
        :type: BlacklistConfiguration
        """

        self._blacklist_configuration = blacklist_configuration

    @property
    def advanced_mode(self):
        """Gets the advanced_mode of this ScanSetting.  # noqa: E501

        True, if advanced mode is enabled.  # noqa: E501

        :return: The advanced_mode of this ScanSetting.  # noqa: E501
        :rtype: bool
        """
        return self._advanced_mode

    @advanced_mode.setter
    def advanced_mode(self, advanced_mode):
        """Sets the advanced_mode of this ScanSetting.

        True, if advanced mode is enabled.  # noqa: E501

        :param advanced_mode: The advanced_mode of this ScanSetting.  # noqa: E501
        :type: bool
        """

        self._advanced_mode = advanced_mode

    @property
    def user_agent(self):
        """Gets the user_agent of this ScanSetting.  # noqa: E501

        The user agent header to use for scanning. This is the header string that is attached to all requests made to the target site.  # noqa: E501

        :return: The user_agent of this ScanSetting.  # noqa: E501
        :rtype: UserAgent
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this ScanSetting.

        The user agent header to use for scanning. This is the header string that is attached to all requests made to the target site.  # noqa: E501

        :param user_agent: The user_agent of this ScanSetting.  # noqa: E501
        :type: UserAgent
        """

        self._user_agent = user_agent

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
        if issubclass(ScanSetting, dict):
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
        if not isinstance(other, ScanSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

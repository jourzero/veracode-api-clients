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


class LoginVerification(object):
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
        'verification_pattern': 'str',
        'verification_url': 'str'
    }

    attribute_map = {
        'verification_pattern': 'verification_pattern',
        'verification_url': 'verification_url'
    }

    def __init__(self, verification_pattern=None, verification_url=None):  # noqa: E501
        """LoginVerification - a model defined in Swagger"""  # noqa: E501

        self._verification_pattern = None
        self._verification_url = None
        self.discriminator = None

        if verification_pattern is not None:
            self.verification_pattern = verification_pattern
        if verification_url is not None:
            self.verification_url = verification_url

    @property
    def verification_pattern(self):
        """Gets the verification_pattern of this LoginVerification.  # noqa: E501

        Verification pattern. Can be a regular expression.  # noqa: E501

        :return: The verification_pattern of this LoginVerification.  # noqa: E501
        :rtype: str
        """
        return self._verification_pattern

    @verification_pattern.setter
    def verification_pattern(self, verification_pattern):
        """Sets the verification_pattern of this LoginVerification.

        Verification pattern. Can be a regular expression.  # noqa: E501

        :param verification_pattern: The verification_pattern of this LoginVerification.  # noqa: E501
        :type: str
        """

        self._verification_pattern = verification_pattern

    @property
    def verification_url(self):
        """Gets the verification_url of this LoginVerification.  # noqa: E501

        Verification URL  # noqa: E501

        :return: The verification_url of this LoginVerification.  # noqa: E501
        :rtype: str
        """
        return self._verification_url

    @verification_url.setter
    def verification_url(self, verification_url):
        """Sets the verification_url of this LoginVerification.

        Verification URL  # noqa: E501

        :param verification_url: The verification_url of this LoginVerification.  # noqa: E501
        :type: str
        """

        self._verification_url = verification_url

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
        if issubclass(LoginVerification, dict):
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
        if not isinstance(other, LoginVerification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

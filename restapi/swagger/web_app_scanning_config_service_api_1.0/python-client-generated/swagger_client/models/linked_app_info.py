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


class LinkedAppInfo(object):
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
        'analysis_unit_id': 'str',
        'app_ver_id': 'str',
        'result_import_request_status': 'str'
    }

    attribute_map = {
        'analysis_unit_id': 'analysis_unit_id',
        'app_ver_id': 'app_ver_id',
        'result_import_request_status': 'result_import_request_status'
    }

    def __init__(self, analysis_unit_id=None, app_ver_id=None, result_import_request_status=None):  # noqa: E501
        """LinkedAppInfo - a model defined in Swagger"""  # noqa: E501

        self._analysis_unit_id = None
        self._app_ver_id = None
        self._result_import_request_status = None
        self.discriminator = None

        if analysis_unit_id is not None:
            self.analysis_unit_id = analysis_unit_id
        if app_ver_id is not None:
            self.app_ver_id = app_ver_id
        if result_import_request_status is not None:
            self.result_import_request_status = result_import_request_status

    @property
    def analysis_unit_id(self):
        """Gets the analysis_unit_id of this LinkedAppInfo.  # noqa: E501

        Identifier for the Dynamic Analysis.  # noqa: E501

        :return: The analysis_unit_id of this LinkedAppInfo.  # noqa: E501
        :rtype: str
        """
        return self._analysis_unit_id

    @analysis_unit_id.setter
    def analysis_unit_id(self, analysis_unit_id):
        """Sets the analysis_unit_id of this LinkedAppInfo.

        Identifier for the Dynamic Analysis.  # noqa: E501

        :param analysis_unit_id: The analysis_unit_id of this LinkedAppInfo.  # noqa: E501
        :type: str
        """

        self._analysis_unit_id = analysis_unit_id

    @property
    def app_ver_id(self):
        """Gets the app_ver_id of this LinkedAppInfo.  # noqa: E501

        Identifier for version of linked application.  # noqa: E501

        :return: The app_ver_id of this LinkedAppInfo.  # noqa: E501
        :rtype: str
        """
        return self._app_ver_id

    @app_ver_id.setter
    def app_ver_id(self, app_ver_id):
        """Sets the app_ver_id of this LinkedAppInfo.

        Identifier for version of linked application.  # noqa: E501

        :param app_ver_id: The app_ver_id of this LinkedAppInfo.  # noqa: E501
        :type: str
        """

        self._app_ver_id = app_ver_id

    @property
    def result_import_request_status(self):
        """Gets the result_import_request_status of this LinkedAppInfo.  # noqa: E501

        Status of the results import request.  # noqa: E501

        :return: The result_import_request_status of this LinkedAppInfo.  # noqa: E501
        :rtype: str
        """
        return self._result_import_request_status

    @result_import_request_status.setter
    def result_import_request_status(self, result_import_request_status):
        """Sets the result_import_request_status of this LinkedAppInfo.

        Status of the results import request.  # noqa: E501

        :param result_import_request_status: The result_import_request_status of this LinkedAppInfo.  # noqa: E501
        :type: str
        """

        self._result_import_request_status = result_import_request_status

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
        if issubclass(LinkedAppInfo, dict):
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
        if not isinstance(other, LinkedAppInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

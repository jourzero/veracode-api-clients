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


class PagedDetailedScan(object):
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
        'embedded': 'EmbeddedDetailedScan',
        'capabilities': 'list[str]',
        'links': 'list[Link]',
        'page': 'PageMeta'
    }

    attribute_map = {
        'embedded': '_embedded',
        'capabilities': 'capabilities',
        'links': '_links',
        'page': 'page'
    }

    def __init__(self, embedded=None, capabilities=None, links=None, page=None):  # noqa: E501
        """PagedDetailedScan - a model defined in Swagger"""  # noqa: E501

        self._embedded = None
        self._capabilities = None
        self._links = None
        self._page = None
        self.discriminator = None

        if embedded is not None:
            self.embedded = embedded
        if capabilities is not None:
            self.capabilities = capabilities
        if links is not None:
            self.links = links
        if page is not None:
            self.page = page

    @property
    def embedded(self):
        """Gets the embedded of this PagedDetailedScan.  # noqa: E501


        :return: The embedded of this PagedDetailedScan.  # noqa: E501
        :rtype: EmbeddedDetailedScan
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this PagedDetailedScan.


        :param embedded: The embedded of this PagedDetailedScan.  # noqa: E501
        :type: EmbeddedDetailedScan
        """

        self._embedded = embedded

    @property
    def capabilities(self):
        """Gets the capabilities of this PagedDetailedScan.  # noqa: E501


        :return: The capabilities of this PagedDetailedScan.  # noqa: E501
        :rtype: list[str]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this PagedDetailedScan.


        :param capabilities: The capabilities of this PagedDetailedScan.  # noqa: E501
        :type: list[str]
        """

        self._capabilities = capabilities

    @property
    def links(self):
        """Gets the links of this PagedDetailedScan.  # noqa: E501


        :return: The links of this PagedDetailedScan.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PagedDetailedScan.


        :param links: The links of this PagedDetailedScan.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def page(self):
        """Gets the page of this PagedDetailedScan.  # noqa: E501


        :return: The page of this PagedDetailedScan.  # noqa: E501
        :rtype: PageMeta
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this PagedDetailedScan.


        :param page: The page of this PagedDetailedScan.  # noqa: E501
        :type: PageMeta
        """

        self._page = page

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
        if issubclass(PagedDetailedScan, dict):
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
        if not isinstance(other, PagedDetailedScan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

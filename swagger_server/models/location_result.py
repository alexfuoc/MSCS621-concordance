# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.location_result_location import LocationResultLocation  # noqa: F401,E501
from swagger_server import util


class LocationResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, location: List[LocationResultLocation]=None, input: str=None):  # noqa: E501
        """LocationResult - a model defined in Swagger

        :param location: The location of this LocationResult.  # noqa: E501
        :type location: List[LocationResultLocation]
        :param input: The input of this LocationResult.  # noqa: E501
        :type input: str
        """
        self.swagger_types = {
            'location': List[LocationResultLocation],
            'input': str
        }

        self.attribute_map = {
            'location': 'location',
            'input': 'input'
        }
        self._location = location
        self._input = input

    @classmethod
    def from_dict(cls, dikt) -> 'LocationResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The locationResult of this LocationResult.  # noqa: E501
        :rtype: LocationResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def location(self) -> List[LocationResultLocation]:
        """Gets the location of this LocationResult.


        :return: The location of this LocationResult.
        :rtype: List[LocationResultLocation]
        """
        return self._location

    @location.setter
    def location(self, location: List[LocationResultLocation]):
        """Sets the location of this LocationResult.


        :param location: The location of this LocationResult.
        :type location: List[LocationResultLocation]
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def input(self) -> str:
        """Gets the input of this LocationResult.


        :return: The input of this LocationResult.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input: str):
        """Sets the input of this LocationResult.


        :param input: The input of this LocationResult.
        :type input: str
        """
        if input is None:
            raise ValueError("Invalid value for `input`, must not be `None`")  # noqa: E501

        self._input = input

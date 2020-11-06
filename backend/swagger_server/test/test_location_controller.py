# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.location_result import LocationResult  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLocationController(BaseTestCase):
    """LocationController integration test stubs"""

    def test_get_location(self):
        """Test case for get_location

        Calculate
        """
        body = '\"The brown fox jumped over the brown log.\"'
        response = self.client.open(
            '/mscs721/concordance/1.0.0/locate',
            method='POST',
            data=json.dumps(body),
            content_type='text/plain')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO
from swagger_server.models.analysis_result import AnalysisResult  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNltkController(BaseTestCase):
    """NltkController integration test stubs"""

    def test_get_nltk_concordance(self):
        """Test case for get_nltk_concordance

        Calculate
        """
        body = '\"The brown fox jumped over the brown log.\"'
        response = self.client.open(
            '/mscs721/concordance/1.0.0/nltk',
            method='POST',
            data=json.dumps(body),
            content_type='text/plain')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

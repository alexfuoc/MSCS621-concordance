import connexion
import six

from swagger_server.models.location_result import LocationResult  # noqa: E501
from swagger_server import util


def get_location(body=None):  # noqa: E501
    """Calculate

    Post text to generate location of tokens # noqa: E501

    :param body: Text to be analyzed
    :type body: dict | bytes

    :rtype: LocationResult
    """
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

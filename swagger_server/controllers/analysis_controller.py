import connexion
import six

from swagger_server.models.result import Result  # noqa: E501
from swagger_server import util


def get_concordance(body=None):  # noqa: E501
    """Calculate

    Post text to generate concordance # noqa: E501

    :param body: Text to be analyzed
    :type body: dict | bytes

    :rtype: Result
    """
    print("-----------------")
    print("Inside the get_concordance method")
    print(body)
    print("-----------------")
    print("")

    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'I am doing the homework!'

import connexion
import string
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
    print(type(body))
    print("-----------------")

    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    if type(body) == bytes:
        words = str(body, "utf-8")

    print(words)
    words = words.lower().split()
    print("-----------------")
    print(words)
    #remove punctuation from each word
    punct_table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(punct_table) for w in words]
    print(stripped)

    return 'I am doing the homework!'

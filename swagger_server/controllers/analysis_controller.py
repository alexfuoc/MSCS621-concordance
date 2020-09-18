import connexion
import string
import six

from swagger_server.models.result import Result  # noqa: E501
from swagger_server import util


def format_concordance(incoming_concordance={}):
    concordance = {
        'concordance': [
        ]
    }

    for token, count in incoming_concordance.items():
        concordance['concordance'].append({
            'token': token,
            'count': count
        })

    return concordance


def sort_concordance(body=None):
    concordance = {}

    for word in body:
        if word in concordance:
            concordance[word] += 1
        else:
            concordance[word] = 1

    return concordance


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

    # handle invalid inputs
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    if type(body) == bytes:
        words = str(body, "utf-8")

    input = words
    print(input)

    words = words.lower().split()
    print("----------------- SPLIT")
    print(words)

    # remove punctuation from each word
    punct_table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(punct_table) for w in words]
    print("----------------- FORMATTED")
    print(stripped)

    stripped.sort()
    print("----------------- SORTED")
    print(stripped)

    concordance = sort_concordance(stripped)
    print("----------------- CONCORDANCE")
    print(concordance)

    concordance = format_concordance(concordance)
    concordance['input'] = input
    print("----------------- Final Formatted CONCORDANCE")
    print(concordance)

    return concordance

""" The controller for the analyze endpoint. 
Will return the concordanance based on the input."""
import json
import string

import connexion
# import swagger_server.controllers.aws_controller as aws


def format_concordance(incoming_concordance=None):
    """ Format Concordance

    :param incoming_concordance: The dictionary of the concordance
    :type incoming_concordance: dict

    return the formatted concordance

    """
    if incoming_concordance is None:
        return {}
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
    """Sort Concordance

    Takes in the posted text array and gets concordance

    :param body: Text array to be analyzed
    :type body: string array

    :rtype: Result
    """
    if body is None:
        return None
    concordance = {}

    for word in body:
        if word in concordance:
            concordance[word] += 1
        else:
            if not word == "":
                concordance[word] = 1
    return concordance


def get_concordance(body=None):  # noqa: E501
    """Calculate

    Post text to generate concordance # noqa: E501

    :param body: Text to be analyzed
    :type body: dict | bytes

    :rtype: AnalysisResult
    """

    # handle invalid inputs
    if connexion.request.is_json:
        body = json.loads(connexion.request.get_json())  # noqa: E501
    words = body
    if isinstance(body, bytes):
        words = str(body, "utf-8")
    body_input = words

    # Query DB for input
    # db_result = aws.get_concordance(words)
    # if db_result is not None:
    #     print("already uploaded, returning from db")
    #     return db_result

    # split, removed punctuation and numeric chars from each word and sorted
    words = ''.join(ch for ch in words if not ch.isdigit())
    words = words.lower().split()
    punct_table = str.maketrans('', '', string.punctuation)
    words = [w.translate(punct_table) for w in words]
    words.sort()

    if not words:
        return {}

    # sort the concordance dict and format it
    concordance = sort_concordance(words)
    concordance = format_concordance(concordance)
    concordance['input'] = body_input

    # add concordance to the DB, hashing if input is too big, 2048 bytes is max for key
    # aws.put_concordance(concordance)
    # CHANHE TO TEST TRAVIS.CI

    return concordance

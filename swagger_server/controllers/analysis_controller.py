import connexion
import string

from swagger_server.models.result import Result  # noqa: E501


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

    :rtype: Result
    """
    # print("-----------------")
    # print("Inside the get_concordance method")
    # print(body)

    # handle invalid inputs
    if connexion.request.is_json:
        body = str(connexion.request.get_json())  # noqa: E501
        words = body
    if type(body) == bytes:
        words = str(body, "utf-8")

    body_input = words
    # print(body_input)

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

    # print('----------------- Final Formatted CONCORDANCE')
    # print(concordance)

    return concordance

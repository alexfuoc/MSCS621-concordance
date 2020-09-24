import connexion
import six
import string
from operator import itemgetter

from swagger_server.models.location_result import LocationResult  # noqa: E501
from swagger_server import util
'''
Location shape
location = {
      "input": "The brown cow...."
      "location": [
        {
            "token": "brown",
            "location": [
                1,
                6
            ]
        },
    ]
}
'''  

def find_location(body=None):
    """Sort Location

    Takes in the posted text array and gets concordance

    :param body: Text array to be analyzed
    :type body: string array

    :rtype: Result
    """
    if body is None:
        return None

    location = []
    inputted_words = []

    for word in body:
        if word not in inputted_words:
            location.append({
                'token': word,
                'location': [i for i, x in enumerate(body) if x == word]
            })
            inputted_words.append(word)
                
    return location

def get_location(body=None):  # noqa: E501
    """Calculate

    Post text to generate location of tokens # noqa: E501

    :param body: Text to be analyzed
    :type body: dict | bytes

    :rtype: LocationResult
    """
    # print("-----------------")
    # print("Inside the get_location method")
    # print(body)

    # handle invalid inputs
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
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

    if not words:
        return {}

    # sort the words array and format for locations
    location = find_location(words)
    print(location)
    print('---------------------------')
    print()
    location = {'location': sorted(location, key=itemgetter('token'))}
    location['input'] = body_input
    print(location)

    return location

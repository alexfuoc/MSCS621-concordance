""" The controller for the analyze endpoint. 
Will return the concordanance based on the input.

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
"""
import json
import string
from operator import itemgetter

import connexion
# import swagger_server.controllers.aws_controller as aws


def find_location(body=None):
    """Sort Location

    Takes in the posted text array and gets locations

    :param body: Text array to be analyzed
    :type body: string array

    :rtype: Result
    """
    if body is None:
        return None

    location = []
    inputted_words = []

    for word in body:
        if word not in inputted_words and word != "":
            location.append(
                {
                    "token": word,
                    "location": [i for i, x in enumerate(body) if x == word],
                }
            )
            inputted_words.append(word)

    return location


def get_location(body=None):  # noqa: E501
    """Calculate

    Post text to generate location of tokens # noqa: E501

    :param body: Text to be analyzed
    :type body: dict | bytes

    :rtype: LocationResult
    """

    # handle invalid inputs
    if connexion.request.is_json:
        body = json.loads(connexion.request.get_json())  # noqa: E501
    words = body
    if isinstance(body, bytes):
        words = str(body, "utf-8")
    body_input = words

    # Query DB for input
    # db_result = aws.get_location(words)
    # if db_result is not None:
    #     print("already uploaded, returning from db")
    #     return db_result

    # split, removed punctuation and numeric chars from each word and sorted
    words = "".join(ch for ch in words if not ch.isdigit())
    words = words.lower().split()
    punct_table = str.maketrans("", "", string.punctuation)
    words = [w.translate(punct_table) for w in words]

    if not words:
        return {}

    # sort the words array and format for locations
    location = find_location(words)
    location = {
        "location": sorted(location, key=itemgetter("token")),
        "input": body_input,
    }

    # add location to the DB, hashing input 2048 bytes is max for key
    # aws.put_location(location)

    return location

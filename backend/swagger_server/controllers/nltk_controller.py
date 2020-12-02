import string

import connexion
import nltk
import six
from swagger_server import util
from swagger_server.models.analysis_result import AnalysisResult  # noqa: E501


def get_nltk_concordance(body=None):  # noqa: E501
    """Calculate

    Post text to generate concordance # noqa: E501

    :param body: Text to be analyzed
    :type body: dict | bytes

    :rtype: AnalysisResult
    """
    nltk.download('punkt')
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    words = body
    if isinstance(body, bytes):
        words = str(body, "utf-8")
    body_input = words
    print(body_input)

    tokens = nltk.tokenize.word_tokenize(words)
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    # remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]
    words.sort()

    freq1 = nltk.FreqDist(words)

    concordance = []
    for word, frequency in freq1.most_common(len(words)):
        concordance.append({
            'token': word,
            'count': frequency
        })

    return {
        'concordance': concordance,
        'input': body_input
    }

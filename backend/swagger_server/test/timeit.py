# importing the required modules
import json
import string
import timeit
from time import perf_counter

import nltk

# small, medium and large input
small_input = "I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn’t really happy."

f = open('large.txt', 'r')
large_input = f.read()
f.close()


def nltk_analysis(words):
    body_input = words

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


def analysis(words):
    body_input = words
    words = ''.join(ch for ch in words if not ch.isdigit())
    words = words.lower().split()
    punct_table = str.maketrans('', '', string.punctuation)
    words = [w.translate(punct_table) for w in words]
    words.sort()

    if not words:
        return {}

    # sort the concordance dict and format it
    concordance = {}

    for word in words:
        if word in concordance:
            concordance[word] += 1
        else:
            if not word == "":
                concordance[word] = 1

    concordanceArray = []
    for token, count in concordance.items():
        concordanceArray.append({
            'token': token,
            'count': count
        })

    return {
        "concordance": concordanceArray,
        "input": body_input
    }


# # compute binary search time
# def binary_time():
#     SETUP_CODE = '''
# from __main__ import analysis
# from random import randint'''

#     TEST_CODE = '''
# small_input = "I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn’t really happy."
# analysis(small_input)'''

#     # timeit.repeat statement
#     print(timeit(setup=SETUP_CODE,
#                  stmt=TEST_CODE,
#                  number=1000))


# compute linear search time
def analysis_time(input):

    t1_start = perf_counter()
    for i in range(15):
        returned = analysis(input)

    # Stop the stopwatch / counter
    t1_stop = perf_counter()

    print("------------Analysis-----------------")
    print("Elapsed time:", t1_stop, t1_start)

    print("Elapsed time during the whole program in seconds:",
          t1_stop-t1_start)

    print("Time per execution: ",  (t1_stop-t1_start)/15)

    # compute linear search time


def nltk_time(input):

    t1_start = perf_counter()
    for i in range(15):
        returned = nltk_analysis(input)

    # Stop the stopwatch / counter
    t1_stop = perf_counter()

    print("------------NLTK-----------------")
    print("Elapsed time:", t1_stop, t1_start)

    print("Elapsed time during the whole program in seconds:",
          t1_stop-t1_start)

    print("Time per execution: ",  (t1_stop-t1_start)/15)


if __name__ == "__main__":
    print("######################## NO INPUT ###############")
    analysis_time(small_input)
    nltk_time(small_input)
    print()
    print("######################## SMALL ###############")
    analysis_time(small_input)
    nltk_time(small_input)
    print()
    print("######################## LARGE ###############")
    analysis_time(large_input)
    nltk_time(large_input)

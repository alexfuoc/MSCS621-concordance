from hashlib import blake2b
from swagger_server.controllers.aws_controller import *

# concordance_resp = put_concordance({
#         "concordance": [
#             {
#                 "count": 1,
#                 "token": "fun"
#             },
#             {
#                 "count": 1,
#                 "token": "i"
#             },
#             {
#                 "count": 1,
#                 "token": "is"
#             },
#             {
#                 "count": 1,
#                 "token": "it"
#             },
#             {
#                 "count": 2,
#                 "token": "love"
#             },
#             {
#                 "count": 1,
#                 "token": "so"
#             },
#             {
#                 "count": 2,
#                 "token": "youtube"
#             }
#         ],
#         "input": "I love youtube. Youtube is so fun. Love it"
#     })

brown_fox = 'The brown fox jumped over the brown log.'
youtube = 'I love youtube. Youtube is so fun. Love it'
youtubeLocation = {
  "input": "I love youtube. Youtube is so fun. Love it",
  "location": [
    {
      "location": [
        6
      ],
      "token": "fun"
    },
    {
      "location": [
        0
      ],
      "token": "i"
    },
    {
      "location": [
        4
      ],
      "token": "is"
    },
    {
      "location": [
        8
      ],
      "token": "it"
    },
    {
      "location": [
        1,
        7
      ],
      "token": "love"
    },
    {
      "location": [
        5
      ],
      "token": "so"
    },
    {
      "location": [
        2,
        3
      ],
      "token": "youtube"
    }
  ]
}

if __name__ == '__main__':
    string1 = 'I love youtube. Youtube is so fun. Love it'

    print(get_location(string1))
    print(put_location(youtubeLocation))
    print(get_location(string1))

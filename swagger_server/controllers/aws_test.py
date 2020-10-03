import boto3
import json
from botocore.exceptions import ClientError


# dynamodb = boto3.resource('dynamodb')

# concordance_table = dynamodb.Table('Concordance')

# def put_location(location):
#     dynamodb = boto3.resource('dynamodb')

#     location_table = dynamodb.Table('Location')

#     response = location_table.put_item(
#         Item={
#             'input': location['input'],
#             'location': location['location']
#         }
#     )

#     return response


# def put_concordance(concordance):

#    response = concordance_table.put_item(
#        Item={
#            'input': concordance['input'],
#            'concordance': concordance['concordance']
#        }
#    )

#    print(response)

#    return response

# if __name__ == '__main__':

#     concordance_resp = put_concordance({
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

# location_resp = put_location({
#     "input": "I love youtube. Youtube is so fun. Love it",
#     "location": [
#         {
#             "location": [
#                 6
#             ],
#             "token": "fun"
#         },
#         {
#             "location": [
#                 0
#             ],
#             "token": "i"
#         },
#         {
#             "location": [
#                 4
#             ],
#             "token": "is"
#         },
#         {
#             "location": [
#                 8
#             ],
#             "token": "it"
#         },
#         {
#             "location": [
#                 1,
#                 7
#             ],
#             "token": "love"
#         },
#         {
#             "location": [
#                 5
#             ],
#             "token": "so"
#         },
#         {
#             "location": [
#                 2,
#                 3
#             ],
#             "token": "youtube"
#         }
#     ]
# })
# print("Concordance put worked:")
# print(concordance_resp)


def get_location(input):
    dynamodb = boto3.resource('dynamodb')

    location_table = dynamodb.Table('Location')

    try:
        response = location_table.get_item(Key={'input': input})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response


if __name__ == '__main__':
    location = get_location(
        'The girl loved her calzones. Almost as much a Ben Wyatt, the ice mayor, loved calzones. But not as much as the girl loved pudding.')
    if location:
        print("Get location succeeded:")
        print(location)

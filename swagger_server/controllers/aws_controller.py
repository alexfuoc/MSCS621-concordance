import boto3
from botocore.exceptions import ClientError

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
concordance_Table = dynamodb.Table('Concordance')
location_Table = dynamodb.Table('Location')


def put_concordance(concordance):
    dynamodb = boto3.resource('dynamodb')

    concordance_table = dynamodb.Table('Concordance')

    response = concordance_table.put_item(
        Item={
            'input': concordance['input'],
            'concordance': concordance['concordance']
        }
    )

    print(response)

    return response


def put_location(location):
    dynamodb = boto3.resource('dynamodb')

    location_table = dynamodb.Table('Location')

    response = location_table.put_item(
        Item={
            'input': location['input'],
            'location': location['location']
        }
    )
    print(response)
    return response


def get_location(input):
    location_table = dynamodb.Table('Location')

    try:
        response = location_table.get_item(Key={'input': input})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


def get_concordance(input):
    dynamodb = boto3.resource('dynamodb')

    concordance_table = dynamodb.Table('Concordance')

    try:
        response = concordance_table.get_item(Key={'input': input})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']

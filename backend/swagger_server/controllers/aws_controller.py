""" The controller for the aws database. 
Queries and updates the db."""

from hashlib import blake2b

import boto3
from botocore.exceptions import ClientError

# Get the service resource.
DYNMAO_DB = boto3.resource("dynamodb")

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
CONCORDANCE_TABLE = DYNMAO_DB.Table("Concordance")
LOCATION_TABLE = DYNMAO_DB.Table("Location")


def put_concordance(concordance):
    """
    Puts concordance in the concordance table, gets HashKey first

    Parameters:
    concordance (obj): concordance with attributes of input(string) and concordance(obj)

    """
    try:
        response = CONCORDANCE_TABLE.put_item(
            Item={
                "HashKey": get_hash_key(concordance["input"]),
                "input": concordance["input"],
                "concordance": concordance["concordance"],
            }
        )
        print("Concordance put in DB", response)
    except:
        print("Not successful input to DB")


def put_location(location):
    """
    Puts location in the location table, gets HashKey first

    Parameters:
    location (obj): concordance with attributes of input(string) and location(obj)
    """
    try:
        response = LOCATION_TABLE.put_item(
            Item={
                "HashKey": get_hash_key(location["input"]),
                "input": location["input"],
                "location": location["location"],
            }
        )
        print("Loction put in DB:", response)
    except:
        print("Not successful input to DB")


def get_location(body_input):
    """
    Queries the Location table in DB for the input

    Parameters:
    input (String): Input string of location to find in DB

    Returns:
    obj: location obj if found, None if not found
    """

    try:
        response = LOCATION_TABLE.get_item(
            Key={"HashKey": get_hash_key(body_input)})
    except ClientError as err:
        print(err.response["Error"]["Message"])
    else:
        try:
            location = response["Item"]
            print("Location in DB:")
            return location
        except KeyError as err:
            print("Not found in DB")

    return None


def get_concordance(body_input):
    """
    Queries the Concordance table in DB for the input

    Parameters:
    body_input (Bytes): Input bytes of concordance to find in DB

    Returns:
    obj: concordance obj if found, None if not found
    """

    try:
        response = CONCORDANCE_TABLE.get_item(
            Key={"HashKey": get_hash_key(body_input)})
    except ClientError as err:
        print(err.response["Error"]["Message"])
    else:
        try:
            concordance = response["Item"]
            print("Concordance in DB:", concordance)
            return concordance
        except KeyError as err:
            print("Not found in DB")

    return None


def get_hash_key(hash_input):
    """
    Gets the hash key for the input

    Parameters:
    hash_input (Bytes or str): Input bytes or string to hash

    Returns:
    str: hashed result
    """
    h = blake2b(digest_size=64)

    # change type to bytes
    if isinstance(hash_input, str):
        hash_input = str.encode(hash_input)

    h.update(hash_input)
    return h.hexdigest()

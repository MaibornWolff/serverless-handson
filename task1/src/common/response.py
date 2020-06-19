import json


def create(message, value):
    body = {
        "message": message
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

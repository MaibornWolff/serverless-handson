import json

def create(message):
    body = {
        "message": message
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

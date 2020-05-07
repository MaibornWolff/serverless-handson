import json

def create(message, statusCode):
    body = {
        "message": message
    }

    response = {
        "statusCode": statusCode,
        "body": json.dumps(body)
    }

    return response
import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    logger.info("Hello from somewhere in the cloud")


    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

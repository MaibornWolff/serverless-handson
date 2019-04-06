import json
import logging
from common.generate_log import debug
logger = logging.getLogger()
logger.setLevel(logging.INFO)


"""
    This serverless function returns the current brightness
"""
def brightness(event, context):
    debug("There will be sunshine", 1)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    logger.info("Hello from somewhere in the cloud! This is the API /brightness")

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


import json
import logging
from common.generate_log import debug
logger = logging.getLogger()
logger.setLevel(logging.INFO)

"""
    This serverless function returns the current storm warning
"""
def stormwarning(event, context):
    debug("There is a storm warning - Take shelter", 3)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    logger.info("Hello from somewhere in the cloud! This is the API /stormwarning")

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


import json
import logging
import random
from common.generate_log import debug
logger = logging.getLogger()
logger.setLevel(logging.INFO)

"""
    This serverless function returns the current storm warning
"""
def stormwarning(event, context):
    stormwarning = random.randint(0,1)

    debug("There is a storm warning - Take shelter",stormwarning)

    body = {
        "message": "Stormwarning retrieved successfully",
        "input": event,
        "value": stormwarning
    }

    logger.info("Hello from somewhere in the cloud! This is the API /stormwarning")

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


import json
import logging
import random
from common.generate_log import debug
logger = logging.getLogger()
logger.setLevel(logging.INFO)


"""
    This serverless function returns the current brightness
"""
def brightness(event, context):
    brightness = random.randint(0,100)

    debug("There will be sunshine", brightness)

    body = {
        "message": "Brightness retrieved successfully",
        "input": event,
        "value": brightness
    }

    logger.info("Hello from somewhere in the cloud! This is the API /brightness")

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


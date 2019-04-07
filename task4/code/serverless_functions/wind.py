import json
import logging
import random
from common.generate_log import debug
logger = logging.getLogger()
logger.setLevel(logging.INFO)

"""
    This serverless function returns the current wind
"""
def wind(event, context):
    wind = random.randint(0,100)

    debug("There is maybe a little bit wind - Be cautious with your hat", wind)

    body = {
        "message": "Wind retrieved successfully",
        "input": event,
        "value": wind
    }

    logger.info("Hello from somewhere in the cloud! This is the API /wind")

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


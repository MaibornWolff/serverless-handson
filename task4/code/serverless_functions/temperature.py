import json
import logging
import random
from common.generate_log import debug
logger = logging.getLogger()
logger.setLevel(logging.INFO)


"""
    This serverless function returns the current temperature
"""
def temperature(event, context):
    temperature = random.randint(30,42)

    debug("There are high temperatures - Margarita time", temperature)

    body = {
        "message": "Temperature retrieved successfully",
        "input": event,
        "value": temperature
    }

    logger.info("Hello from somewhere in the cloud! This is the API /temperature")

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


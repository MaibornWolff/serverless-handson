import json
import logging
import random
from common.generate_log import debug
logger = logging.getLogger()
logger.setLevel(logging.INFO)


"""
    This serverless function returns the current humidity
"""
def humidity(event, context):
    humidity = random.randint(0,120)

    debug("There is will be rain - Take an umbrella with you", humidity, 5, 0)

    body = {
        "message": "Humidity retrieved successfully",
        "input": event,
        "value": humidity
    }

    logger.info("Hello from somewhere in the cloud! This is the API /humidity")

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


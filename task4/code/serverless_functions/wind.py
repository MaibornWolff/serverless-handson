import json
import logging
from common.generate_log import debug
logger = logging.getLogger()
logger.setLevel(logging.INFO)

"""
    This serverless function returns the current wind
"""
def wind(event, context):
    debug("There is maybe a little bit wind - Be cautious with your hat", 2)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    logger.info("Hello from somewhere in the cloud! This is the API /wind")

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


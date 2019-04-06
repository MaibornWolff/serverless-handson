import json
import logging
from common.generate_log import debug
logger = logging.getLogger()
logger.setLevel(logging.INFO)


"""
    This serverless function returns the current humidity
"""
def humidity(event, context):
    debug("There is will be rain - Take an umbrella with you", 5)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    logger.info("Hello from somewhere in the cloud! This is the API /humidity")

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


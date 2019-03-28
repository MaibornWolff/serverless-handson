import json
import logging
from common.generate_log import debug

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def hello(event, context):
    debug("HELLO", 1)

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


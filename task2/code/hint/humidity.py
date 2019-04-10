from common import logger
from common import response

"""
    This serverless function returns the current humidity
"""
def humidity(event, context):
    logger.info("Hello from somewhere in the cloud! This is the API /humidity")

    return response.create(
        message="Your serverless function executed successfully!",
        value=120
    )

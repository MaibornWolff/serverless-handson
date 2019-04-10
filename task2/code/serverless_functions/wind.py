from common import logger
from common import response

"""
    This serverless function returns the current wind
"""
def wind(event, context):
    logger.info("Hello from somewhere in the cloud! This is the API /wind")

    return response.create(
        message="Your serverless function executed successfully!",
        value=3
    )


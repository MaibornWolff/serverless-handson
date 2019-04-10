from common import logger
from common import response

"""
    This serverless function returns the current brightness
"""
def wind(event, context):

    logger.info("Hello I am a monolith! This is my API /wind")

    return response.create(
        message="Monoliths never break! Not even in a storm",
        value=3
    )


from common import logger
from common import response

"""
    This serverless function returns the current brightness
"""
def brightness(event, context):

    logger.info("Hello I am a monolith! This is my API /brightness")

    return response.create(
        message="Monoliths are so solid! Sunshine every day",
        value=60
    )


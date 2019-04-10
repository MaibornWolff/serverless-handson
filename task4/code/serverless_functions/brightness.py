import random
from common import monitor
from common import logger
from common import response



"""
    This serverless function returns the current brightness
"""
def brightness(event, context):
    brightness = random.randint(0,100)

    logger.info("Hello from somewhere in the cloud! This is the API /brightness")

    monitor.send_to_dashboard("There will be sunshine", brightness)

    return response.create(
        message="Brightness retrieved successfully",
        value=brightness
    )


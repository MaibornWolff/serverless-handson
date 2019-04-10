import random
from common import monitor
from common import logger
from common import response


"""
    This serverless function returns the current storm warning
"""
def stormwarning(event, context):
    stormwarning = random.randint(0, 1)

    logger.info("Hello from somewhere in the cloud! This is the API /stormwarning")

    monitor.send_to_dashboard("There is a storm warning - Take shelter", stormwarning)

    return response.create(
        message="Stormwarning retrieved successfully",
        value=stormwarning
    )
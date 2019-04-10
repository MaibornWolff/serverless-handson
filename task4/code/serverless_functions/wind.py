import random
from common import monitor
from common import logger
from common import response


"""
    This serverless function returns the current wind
"""
def wind(event, context):
    wind = random.randint(0, 100)

    logger.info("Hello from somewhere in the cloud! This is the API /wind")

    monitor.send_to_dashboard("There is maybe a little bit wind - Be cautious with your hat", wind)

    return response.create(
        message="Wind retrieved successfully",
        value=wind
    )
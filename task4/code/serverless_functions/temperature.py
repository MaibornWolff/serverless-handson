import random
import sys
from common import monitor
from common import logger
from common import response


"""
    This serverless function returns the current temperature
"""
def temperature(event, context):
    temperature = random.randint(30, 42)

    logger.info("Hello from somewhere in the cloud! This is the API /temperature")

    monitor.send_to_dashboard("There are high temperatures - Margarita time", temperature)

    return response.create(
        message="Temperature retrieved successfully",
        value=temperature
    )
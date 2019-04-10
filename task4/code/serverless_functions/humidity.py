import random
from common import monitor
from common import logger
from common import response


"""
    This serverless function returns the current humidity
"""
def humidity(event, context):
    humidity = random.randint(0, 120)

    logger.info("Hello from somewhere in the cloud! This is the API /humidity")

    monitor.send_to_dashboard("There is will be rain - Take an umbrella with you", humidity)

    return response.create(
        message="humidity retrieved successfully",
        value=humidity
    )


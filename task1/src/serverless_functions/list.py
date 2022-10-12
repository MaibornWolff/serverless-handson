from common import logger
from common import response

"""
    This serverless function lists the uploaded images
"""


def list(event, context):
    logger.info("Get /list")
    return response.create("Here are your images!")

from common import logger
from common import response

"""
    This serverless function uploads an image
"""


def upload(event, context):
    logger.info("Post /upload")
    return response.create("Image uploaded successfully!")

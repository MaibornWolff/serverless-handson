import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def info(message):
    logger.info(message)

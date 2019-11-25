from typing import Dict
from common import logger
from common import response


class MyApp:
    #TODO: migrate all logic below to multiple serverless_functions
    def get(self, event) -> Dict[str, str]:
        logger.info("Hello I am a monolith! This is my API")
        context = event.get('data',{}).get('context')
        
        if context == 'brightness':
            logger.info("Get /brightness")
            message="Monoliths are so solid! Sunshine every day",
            value=70

        elif context == 'wind':
            logger.info("Get /wind")
            message="Monoliths never break! Not even in a storm",
            value=43

        else:
            logger.info("Get /")
            message="",
            value=0

        return response.create(
            message,
            value
        )
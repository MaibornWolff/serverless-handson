from typing import Dict
from common import logger
from common import response


class MyApp:
    def get(self, event) -> Dict[str, str]:
        logger.info("Hello I am a monolith! This is my API")
        context = event.get('data', {}).get('context')

        if context == 'upload':
            logger.info("Get /upload")
            message = "Image uploaded successfully!"

        elif context == 'list':
            logger.info("Get /list")
            message = "Here are your images!"

        else:
            logger.info("Get /")
            message = ""

        return response.create(
            message
        )

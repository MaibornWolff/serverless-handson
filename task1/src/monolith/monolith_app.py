from typing import Dict

from common import logger
from common import response


class MyApp:

    def upload(self, event) -> Dict[str, str]:
        logger.info("Hello, I am a monolith! This is my API /upload")

        return response.create(
            message="Image uploaded successfully!"
        )

    def list(self, event) -> Dict[str, str]:
        logger.info("Hello, I am a monolith! This is my API /list")

        return response.create(
            message="Here are your images!"
        )

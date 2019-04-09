from typing import Dict
from common import logger
from common import response


class MyApp:

    def brightness(self, event) -> Dict[str, str]:
        logger.info("Hello I am a monolith! This is my API /brightness")

        return response.create(
            message="Monoliths are so solid! Sunshine every day",
            value=60
        )

    def wind(self, event) -> Dict[str, str]:
        logger.info("Hello I am a monolith! This is my API /wind")

        return response.create(
            message="Monoliths never break! Not even in a storm",
            value=3
        )
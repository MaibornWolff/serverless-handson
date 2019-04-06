import json
from typing import Dict


class MyApp:

    def brightness(self, event) -> Dict[str, str]:
        body = {
            "message": "Monoliths are so solid!",
            "input": event
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        return response

    def wind(self, event) -> Dict[str, str]:
        body = {
            "message": "Monoliths are so super solid!",
            "input": event
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        return response

    def temperature(self, event) -> Dict[str, str]:
        body = {
            "message": "Monoliths never break",
            "input": event
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        return response

    def stormwarning(self, event) -> Dict[str, str]:
        body = {
            "message": "Monoliths can scale like nothing else",
            "input": event
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        return response

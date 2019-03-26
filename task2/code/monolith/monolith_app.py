import json
from typing import Dict


class MyApp:

    def hello1(self, event) -> Dict[str, str]:
        body = {
            "message": "Monoliths are so solid!",
            "input": event
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        return response

    def hello2(self, event) -> Dict[str, str]:
        body = {
            "message": "Monoliths are so super solid!",
            "input": event
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        return response

    def hello3(self, event) -> Dict[str, str]:
        body = {
            "message": "Monoliths never break",
            "input": event
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        return response

    def hello4(self, event) -> Dict[str, str]:
        body = {
            "message": "Monoliths can scale like nothing else",
            "input": event
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        return response

    def hello5(self, event) -> Dict[str, str]:
        body = {
            "message": "Monoliths works for me(?)",
            "input": event
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        return response

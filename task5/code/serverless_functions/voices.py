import json
import boto3
from common.general import Response



"""
    This serverless function returns available polly voices
"""
def voices(event: dict, context: dict) -> dict:

    # calling AWS Polly API - get all voices as list
    voices = get_voices_from_polly_api()


    return Response(json.dumps(voices)).create()



def get_voices_from_polly_api() -> list:
    polly_client = boto3.client('polly')

    params = {}
    return_value = []

    while True:
        response = polly_client.describe_voices(**params)
        return_value.extend(response.get("Voices", []))

        if "NextToken" in response:
            params = {"NextToken": response["NextToken"]}
        else:
            break

    return return_value
import json
import boto3
from botocore.exceptions import BotoCoreError, ClientError

# defined data types for easier handling
from config.general import Response, logger


polly = boto3.client('polly')


def voices(event: dict, context: dict) -> dict:
    try:
        voices = get_voices_from_polly_api(polly)
    except NameError:
        return Response(501, "Polly not found").as_dict()

    except (BotoCoreError, ClientError) as err:
        # The service returned an error
        logger.error("error fetching polly response" + str(err))
        return Response(500, str(err)).as_dict()

    return Response(200, json.dumps(voices)).as_dict()


def get_voices_from_polly_api(polly_client) -> list:
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

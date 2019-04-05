import json
import boto3
import logging
from collections import namedtuple
from botocore.exceptions import BotoCoreError, ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# defined data types for easier handling
defaultHeader = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
}
fields = ("statusCode", "body", "headers", "isBase64Encoded")
Response = namedtuple("HTTPResponse", fields, defaults=(None, None, defaultHeader, False))


#
# COMMENT IN HERE!!!
# polly = boto3.client('polly')
#

# Mapping the output format used in the client to the content type for the response
AUDIO_FORMATS = {"ogg_vorbis": "audio/ogg", "mp3": "audio/mpeg", "pcm": "audio/wave; codecs=1"}


# see also https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html

def handler(event: dict, context: dict) -> dict:
    """Handles routing for listing available voices"""
    params = {}
    voices = []

    while True:
        try:
            # Request list of available voices, if a continuation token
            # was returned by the previous call then use it to continue
            # listing
            response = polly.describe_voices(**params)
        except NameError:
            return dict(Response(statusCode=501, body="Polly not found")._asdict())
        except (BotoCoreError, ClientError) as err:
            # The service returned an error
            return dict(Response(statusCode=500, body=str(err))._asdict())

        # Collect all the voices
        voices.extend(response.get("Voices", []))

        # If a continuation token was returned continue, stop iterating
        # otherwise
        if "NextToken" in response:
            params = {"NextToken": response["NextToken"]}
        else:
            break

    return dict(Response(statusCode=200, body=json.dumps(voices))._asdict())

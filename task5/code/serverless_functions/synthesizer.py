import base64
import json
import logging
import boto3
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

polly = boto3.client('polly')

# Mapping the output format used in the client to the content type for the response
AUDIO_FORMATS = {"ogg_vorbis": "audio/ogg", "mp3": "audio/mpeg", "pcm": "audio/wave; codecs=1"}


# see also https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html

def handler(event: dict, context: dict) -> dict:
    """Handles routing for reading text (speech synthesis)"""

    logger.info(event)

    if 'queryStringParameters' not in event:
        logger.error("No query parameters passed")
        return {}

    text = event.get('queryStringParameters').get('text', None)
    voice_id = event.get('queryStringParameters').get('voiceId', None)
    output_format = event.get('queryStringParameters').get('outputFormat', None)

    if len(text) == 0 or len(voice_id) == 0 or output_format not in AUDIO_FORMATS:
        logger.error("Bad request: wrong parameters")
    else:
        try:
            # Request speech synthesis
            synthesized_text = polly.synthesize_speech(Text=text,
                                                       VoiceId=voice_id,
                                                       OutputFormat=output_format).get("AudioStream").read()

            response = json.dumps({'speech': base64.b64encode(synthesized_text).decode("utf-8")})

            return dict(Response(statusCode=200, body=response)._asdict())

        except (BotoCoreError, ClientError) as err:
            # The service returned an error
            logger.error("error fetching polly response" + str(err))

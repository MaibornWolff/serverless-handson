import base64
import json
import boto3
import sys
from botocore.exceptions import BotoCoreError, ClientError

from config.general import AUDIO_FORMATS, logger, Response

polly = boto3.client('polly')


def synthesizer(event: dict, context: dict) -> dict:

    text, voice_id, output_format = get_validated_parameters_from_request(event)

    try:
        # Request speech synthesis
        synthesized_text = polly\
            .synthesize_speech(Text=text, VoiceId=voice_id, OutputFormat=output_format)\
            .get("AudioStream")\
            .read()

        response = encode_for_response(synthesized_text)

        return Response(200, response).as_dict()

    except (BotoCoreError, ClientError) as err:
        # The service returned an error
        logger.error("error fetching polly response" + str(err))
        return Response(200, str(err)).as_dict()


def get_validated_parameters_from_request(event: dict)-> (str, str, str):

    logger.info(event)

    if 'queryStringParameters' not in event:
        logger.error("No query parameters passed")
        return {}

    text = event.get('queryStringParameters').get('text', None)
    voice_id = event.get('queryStringParameters').get('voiceId', None)
    output_format = event.get('queryStringParameters').get('outputFormat', None)

    if len(text) == 0 or len(voice_id) == 0 or output_format not in AUDIO_FORMATS:
        logger.error("Bad request: wrong parameters")
        sys.exit(1)

    return text, voice_id, output_format


def encode_for_response(data: str) -> str:
    return json.dumps({'speech': base64.b64encode(data).decode("utf-8")})

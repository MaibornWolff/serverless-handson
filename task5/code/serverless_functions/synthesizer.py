import base64
import json
import boto3
import sys
from botocore.exceptions import BotoCoreError, ClientError
from common.general import AUDIO_FORMATS, logger, Response


"""
    This serverless function converts text to speech with a given voice
"""
def synthesizer(event: dict, context: dict) -> dict:

    # extracting parameters
    text, voice_id, output_format = extract_parameters_from_request(event)


    # calling AWS Polly API - synthezise text to speech
    speech = synthesize_speech(text, voice_id, output_format)


    return Response(speech).create()



def synthesize_speech(text, voice_id, output_format):
    polly = boto3.client('polly')

    synthesized_text = polly.synthesize_speech(Text=text, VoiceId=voice_id, OutputFormat=output_format) \
        .get("AudioStream") \
        .read()

    response = encode_for_response(synthesized_text)

    return response


def encode_for_response(data: str) -> str:
    return json.dumps({'speech': base64.b64encode(data).decode("utf-8")})


def extract_parameters_from_request(event: dict)-> (str, str, str):

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




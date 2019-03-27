import json
# import logging
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)
# from collections import namedtuple
# import boto3
# from botocore.exceptions import BotoCoreError, ClientError

# defined data types for easies handling
# fields = ("statusCode", "body", "header")
# defaultHeader = {
#     'Content-Type': 'application/json',
#     'Access-Control-Allow-Origin': '*'
# }
# Response = namedtuple("HTTPStatus", fields, defaults=(None, None, defaultHeader))
#
# polly = boto3.client('polly')


def voices(event, context):
    """Handles routing for listing available voices"""
    params = {}
    voices = []

    # while True:
    #     try:
    #         # Request list of available voices, if a continuation token
    #         # was returned by the previous call then use it to continue
    #         # listing
    #         response = polly.describe_voices(**params)
    #     except (BotoCoreError, ClientError) as err:
    #         # The service returned an error
    #         return Response(statusCode=500, message=str(err))
    #
    #     # Collect all the voices
    #     voices.extend(response.get("Voices", []))
    #
    #     # If a continuation token was returned continue, stop iterating
    #     # otherwise
    #     if "NextToken" in response:
    #         params = {"NextToken": response["NextToken"]}
    #     else:
    #         break

    # return dict(Response(statusCode=200, body=json.dumps(voices))._asdict())
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


# def speechSynthesize(event, context):
#     return ""
#     # """Handles routing for reading text (speech synthesis)"""
#     # # Get the parameters from the query string
#     # text = self.query_get(query, "text")
#     # voiceId = self.query_get(query, "voiceId")
#     # outputFormat = self.query_get(query, "outputFormat")
#     #
#     # # Validate the parameters, set error flag in case of unexpected
#     # # values
#     # if len(text) == 0 or len(voiceId) == 0 or \
#     #         outputFormat not in AUDIO_FORMATS:
#     #     raise HTTPStatusError(HTTP_STATUS["BAD_REQUEST"],
#     #                           "Wrong parameters")
#     # else:
#     #     try:
#     #         # Request speech synthesis
#     #         response = polly.synthesize_speech(Text=text,
#     #                                            VoiceId=voiceId,
#     #                                            OutputFormat=outputFormat)
#     #     except (BotoCoreError, ClientError) as err:
#     #         # The service returned an error
#     #         raise HTTPStatusError(HTTP_STATUS["INTERNAL_SERVER_ERROR"],
#     #                               str(err))



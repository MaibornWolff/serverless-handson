import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
DEFAULT_HEADER = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
}

AUDIO_FORMATS = {"ogg_vorbis": "audio/ogg", "mp3": "audio/mpeg", "pcm": "audio/wave; codecs=1"}
fields = ("statusCode", "body", "headers", "isBase64Encoded")


class Response:

    def __init__(self, status_code, body: str, headers=None, is_base64encoded=False):
        if headers is None:
            headers = DEFAULT_HEADER

        if status_code is None:
            status_code = 200

        self.status_code = status_code
        self.body = body
        self.headers = headers
        self.isBase64Encoded = is_base64encoded

    def as_dict(self):
        return {
            "statusCode": self.status_code,
            "body": self.body,
            "headers": self.headers,
            "isBase64Encoded": self.isBase64Encoded
        }

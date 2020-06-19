import base64
import os.path
import re

from requests.structures import CaseInsensitiveDict
from requests_toolbelt.multipart import decoder

from common import response

allowed_content_types = ['image/jpeg', 'image/jpg', 'image/png']


def extract_uploaded_files(event):
    case_insensitive_event = CaseInsensitiveDict(event)
    case_insensitive_headers = CaseInsensitiveDict(case_insensitive_event['headers'])
    content_type_header = case_insensitive_headers['content-type']

    if not content_type_header.startswith('multipart/form-data'):
        raise Exception('Requires multipart/form-data')

    multipart_string = base64.b64decode(case_insensitive_event['body'])
    multipart_data = decoder.MultipartDecoder(multipart_string, content_type_header)

    files = []

    for part in multipart_data.parts:
        content_type = part.headers[b'Content-Type'].decode()
        if not content_type in allowed_content_types:
            raise Exception('Content-Type not supported')

        match = re.search('filename="(.+)"', part.headers[b'Content-Disposition'].decode())

        if match:
            filename = match.group(1)
            files.append((filename, part.content))
        else:
            raise Exception('Filename not provided')

    return files


def encode_image(filename, data):
    extension = os.path.splitext(filename)[1][1:]
    content_type = 'image/' + extension
    contents = data['Body'].read()
    encoded_str = base64.b64encode(contents).decode()
    return response.create_base64(content_type, encoded_str)

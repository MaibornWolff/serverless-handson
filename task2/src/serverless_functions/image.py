from common import logger
from common import response
import boto3
import base64
import re
import os.path
from botocore.exceptions import ClientError
from requests.structures import CaseInsensitiveDict
from requests_toolbelt.multipart import decoder

s3_client = boto3.client('s3')
s3_bucket = boto3.resource('s3')
BUCKET_NAME = "mw-serverless-cloud-school"
bucket = s3_bucket.Bucket(BUCKET_NAME)

allowed_content_types = ['image/jpeg', 'image/jpg', 'image/png']

# npm init
# npm install --save serverless-python-requirements

# need to change python version to 3.6 or we change init scripts


def upload(event, context):
    case_insensitive_event = CaseInsensitiveDict(event)
    case_insensitive_headers = CaseInsensitiveDict(
        case_insensitive_event['headers'])
    content_type_header = case_insensitive_headers['content-type']

    if not content_type_header.startswith("multipart/form-data"):
        return response.create('Requires multipart/form-data', 400)

    multipart_string = base64.b64decode(case_insensitive_event['body'])
    multipart_data = decoder.MultipartDecoder(multipart_string,
                                              content_type_header)

    for part in multipart_data.parts:
        logger.info(part.headers)

        content_type = part.headers[b'Content-Type'].decode()
        if not content_type in allowed_content_types:
            return response.create('Content-Type not supported', 400)

        match = re.search('filename="(.+)"',
                          part.headers[b'Content-Disposition'].decode())
        if match:
            filename = match.group(1)
        else:
            return response.create('Filename not provided', 400)

        try:
            s3_response = s3_client.put_object(Bucket=BUCKET_NAME,
                                               Key=filename,
                                               Body=part.content)
        except Exception as e:
            return response.create(str(e), 500)

    return response.redirect('list')


def upload_html(event, context):
    form = """<form action="upload" method="post" enctype="multipart/form-data">
        <label for="img">Select image:</label>
        <input type="file" name="img" accept="image/*" />
        <input type="submit" />
        </form>"""
    return response.html(form)


def get(event, context):
    filename = event["queryStringParameters"]["filename"]
    try:
        data = s3_client.get_object(Bucket=BUCKET_NAME, Key=filename)
        extension = os.path.splitext(filename)[1][1:]
        contents = data['Body'].read()
        encoded_str = base64.b64encode(contents).decode()
        return {
            "isBase64Encoded": True,
            "statusCode": 200,
            "headers": {
                "content-type": "image/" + extension
            },
            "body": encoded_str
        }
    except Exception as e:
        return response.create(str(e), 500)


def list_files(event, context):
    try:
        files = bucket.objects.all()
        file_list = [str(s3_file.key) for s3_file in files]
        html_files = [
            f'<li><img alt="{f_string}" src="get?filename={f_string}" /></li>'
            for f_string in file_list
        ]
        return response.html(f"<ul>{''.join(html_files)}</ul>")
    except Exception as e:
        return response.create(str(e), 500)

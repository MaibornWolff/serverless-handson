import boto3
from common import image_helper
from common import logger
from common import response

s3_client = boto3.client('s3')


def get_upload_form(event, context):
    # Task 1.1
    return response.html_upload_form()


def upload_image(event, context):
    # Task 1.3 - TODO
    # First step: Extract the uploaded files out of the event
    # Second step: Use s3_client.put_object(Bucket=..., Key=..., Body=...) to finally upload each file
    # A "for" loop may be useful
    return


def get_image(event, context):
    return


def list_images(event, context):
    return

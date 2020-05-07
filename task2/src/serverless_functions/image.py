from common import logger
from common import response
import boto3
import base64
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')

"""
    This serverless function returns the current brightness
"""

def upload(event, context):
    BUCKET_NAME = "mw-serverless-cloud-school"
    file_content = "test-text" # base64.b64decode(event['content'])
    file_path = 'test.txt'   
    try:
        s3_response = s3_client.put_object(Bucket=BUCKET_NAME, Key=file_path, Body=file_content) 
        return response.create(s3_response, 200)
    except ClientError as e:
        logger.info(e)
        return response.create(e, 500)   
    except Exception as e:
        raise IOError(e)    


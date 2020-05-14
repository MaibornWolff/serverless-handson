from common import logger
from common import response
import boto3
import base64
from botocore.exceptions import ClientError

from requests_toolbelt.multipart import decoder

s3_client = boto3.client('s3')
s3_bucket = boto3.resource('s3')
BUCKET_NAME = "mw-serverless-cloud-school"
bucket = s3_bucket.Bucket(BUCKET_NAME)

"""
    This serverless function returns the current brightness
"""

# to make this work, apolicy nedes to be attached to the rule
# IAM --> Roles --> <task-policy> --> attach Role --> "S3 Full Acccess"
# Boto3 Docu https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.put_object

# npm init
# npm install --save serverless-python-requirements
# pip install requests-toolbelt

# need to change python version to 3.6 or we change init scripts

# binary media type */* ??

# notes: https://stackoverflow.com/questions/44860486/how-to-return-binary-data-from-lambda-function-in-aws-in-python

def upload(event, context):
    # return response.create(str(event), 200)

    multipart_string_b64 = event['body']
    multipart_string = base64.b64decode(multipart_string_b64)
    print(event)
    # return response.create(event['headers'], 200)
    content_type_header = event['headers']['content-type']
    
    assert content_type_header.startswith("multipart/form-data")
    multipart_data = decoder.MultipartDecoder(multipart_string, content_type_header)
    
    # Currently only processes the first image
    for part in multipart_data.parts:
        # assert part.headers[b'Content-Type'] == b'image/jpeg'
        print(part)
        filename = "teams.jpg" # part.headers['filename']
        # print(part.content)
        content = part.content # base64.b64decode(part.content) 
        print(part.headers)
        # decoded_content = base64.b64decode(content.decode("utf-8"))

        try:
            s3_response = s3_client.put_object(Bucket=BUCKET_NAME, Key=filename, Body=content) 
            return response.create(s3_response, 200)
        except Exception as e:
            return response.create(str(e), 500)
    
        
def upload_html(event, context):
    form = """<form action="image/upload" method="post" enctype="multipart/form-data">
        <label for="img">Select image:</label>
        <input type="file" id="img" name="img" accept="image/*">
        <input type="submit">
        </form>"""
    return response.html(form)
        
def get(event, context):
    filename = event["queryStringParameters"]["filename"]
    try: 
        # bytes_buffer = io.BytesIO()
        # bucket.download_fileobj(Bucket=BUCKET_NAME, Key=filename, Fileobj=bytes_buffer)
        # byte_value = bytes_buffer.getvalue()
        # str_value = byte_value.decode() #python3, default decoding is utf-8
        
        data = s3_client.get_object(Bucket=BUCKET_NAME, Key=filename)
        print(data)
        contents = data['Body'].read()
        encoded_str = base64.b64encode(contents).decode("utf-8")
        # print(encoded_str)
        return {
          "isBase64Encoded": True,
          "statusCode": 200,
          "headers": { "content-type": "image/jpeg"},
          "body":  encoded_str
        }
    except Exception as e:
        return response.create(str(e), 500)  
            

def list_files(event, context):
    try:
        files = bucket.objects.all()
        file_list = [str(s3_file.key) for s3_file in files]
        # todo encode html link
        html_files = [f'<li><img alt="{f_string}" src="get?filename={f_string}"></img></li>' for f_string in file_list]
        
        return response.html(f"<ul>{''.join(html_files)}</ul>")

    except Exception as e:
        return response.create(str(e), 500)   

def html(event, context): 
    html_content = "<h1>HTML from API Gateway/Lambda</h1>";
    return response.html(html_content)

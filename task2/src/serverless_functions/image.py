import boto3
from common import image_helper
from common import logger
from common import response

s3_client = boto3.client('s3')
s3_bucket = boto3.resource('s3')

BUCKET_NAME = "mw-serverless-cloud-school"


def get_upload_form(event, context):
    form = """<form action="upload" method="post" enctype="multipart/form-data">
        <label for="img">Select image:</label>
        <input type="file" name="img" accept="image/*" />
        <input type="submit" />
        </form>"""
    return response.html('Upload image', form)


def upload_image(event, context):
    try:
        uploaded_images = image_helper.extract_uploaded_files(event)

        for uploaded_image in uploaded_images:
            s3_response = s3_client.put_object(Bucket=BUCKET_NAME, Key=uploaded_image[0], Body=uploaded_image[1])
            logger.info(f'Uploaded image {uploaded_image[0]} successfully: {s3_response}')

        return response.redirect('list')
    except Exception as e:
        logger.info(f'Failed to upload image {uploaded_image[0]}: {str(e)}')
        return response.create(str(e), 500)


def get_image(event, context):
    try:
        image_name = event["queryStringParameters"]["image"]
        image_data = s3_client.get_object(Bucket=BUCKET_NAME, Key=image_name)

        return image_helper.encode_image(image_name, image_data)
    except Exception as e:
        return response.create(str(e), 500)


def list_images(event, context):
    try:
        images = s3_bucket.Bucket(BUCKET_NAME).objects.all()

        images_markup = [
            f'<li><img alt="{image.key}" src="get?image={image.key}" /></li>'
            for image in images
        ]

        return response.html('Images', f"<ul>{''.join(images_markup)}</ul>")
    except Exception as e:
        return response.create(str(e), 500)

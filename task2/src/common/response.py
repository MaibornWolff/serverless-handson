import json


def create(message, statusCode):
    body = {"message": message}

    return {
        "statusCode": statusCode,
        "body": json.dumps(body)}


def create_base64(content_type, encoded_str):
    return {
        "isBase64Encoded": True,
        "statusCode": 200,
        "headers": {
            "content-type": content_type
        },
        "body": encoded_str
    }


def redirect(location):
    return {"statusCode": 301, "headers": {"Location": location}}


def html(html_title, html_content):
    body = f'<html><head><style type="text/css">img {{ max-width: 100vw; }}</style><title>{html_title}</title></head><body>{html_content}</body></html>'
    return {
        "statusCode": 200,
        "body": body,
        "headers": {
            'Content-Type': 'text/html',
        }
    }

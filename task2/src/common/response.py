import json

def create(message, statusCode):
    body = {
        "message": message
    }

    response = {
        "statusCode": statusCode,
        "body": json.dumps(body)
    }

    return response
    
    
def html(html_content):
    body = f"<html><head><title>HTML from API Gateway/Lambda</title></head><body>{html_content}</body></html>"
    return {
        "statusCode": 200,
        "body": body,
        "headers": {
            'Content-Type': 'text/html',
        }
    }
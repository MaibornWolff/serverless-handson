from common import response

def hello_world(event, context):
    return response.create("Hello World")

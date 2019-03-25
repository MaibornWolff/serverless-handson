import json
from random import randint
from ..common import generate_log

def hello(event, context):

    generate_log.debug("SLS MESSAGE "+str(randint(0, 999999999)))

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    print("hello")

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response




import requests
import json
from datetime import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def activate_request_logging():
    import http.client as http_client
    http_client.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

def generate_payload(message):
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z"
    payload = {
        '@timestamp': timestamp,  # 2019-01-14T10:15:43.000Z -> UTC timestamp
        'log': message
    }
    return payload


def debug(message):
    logger.info("log message in Elastic - "+message)


    #activate_request_logging()

    url = "http://18.184.29.31:9200/myindex/mydoc"
    headers = {'Content-type': 'application/json'}
    r = requests.post(url=url, data=json.dumps(generate_payload(message)), headers=headers)



    if(r.status_code == 201 and r.reason == "Created"):
        return True
    else:
        raise Exception('Elastic API didnt response as expected', {'statusCode': r.status_code, 'reason': r.reason, 'content': r.content})

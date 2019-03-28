
from datetime import datetime
import logging
import random
import urllib3.request
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def generate_payload(message, function_id):
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z"
    payload = {
        '@timestamp': timestamp,  # 2019-01-14T10:15:43.000Z -> UTC timestamp
        'log': message ,
        'function_id': function_id,
        'serverless_request_id': random.randint(0,65535),
        'success': True
    }
    return payload


def debug(message, function_id=None):
    logger.info("log message in Elastic - "+message)
    if(function_id == None):
        function_id = random.randint(0, 5)

    url = "http://35.156.188.64:9200/myindex/mydoc"
    headers = {'Content-type': 'application/json'}
    http = urllib3.PoolManager()
    r = http.request("POST", url, body=json.dumps(generate_payload(message, function_id)), headers=headers)
    http.clear()

    if(r.status == 201 and r.reason == "Created"):
        return True
    else:
        raise Exception('Elastic API didnt response as expected', {'statusCode': r.status_code, 'reason': r.reason, 'content': r.content})
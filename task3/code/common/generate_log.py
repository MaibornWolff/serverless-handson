
from datetime import datetime
import logging
import random
import urllib3.request
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def generate_payload(message, function_id, group_id, temperature):
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z"
    payload = {
        '@timestamp': timestamp,  # 2019-01-14T10:15:43.000Z -> UTC timestamp
        'log': message ,
        'function_id': function_id,
        'group_id': group_id,
        'temperature': temperature,
        'serverless_request_id': random.randint(0,65535),
        'success': True
    }

    return payload


def monitor(message, group_id, temperature):
    logger.info("Log message in Elastic - "+message)

    # this is only used with function3
    function_id = 3

    elastic_url = "http://3.120.207.235:9200/myindex/mydoc"
    elastic_headers = {'Content-type': 'application/json'}
    http = urllib3.PoolManager()
    r = http.request("POST", elastic_url, body=json.dumps(generate_payload(message, function_id, group_id, temperature)), headers=elastic_headers)
    http.clear()

    if(r.status == 201 and r.reason == "Created"):
        return True
    else:
        raise Exception('Elastic API didnt response as expected', {'statusCode': r.status_code, 'reason': r.reason, 'content': r.content})
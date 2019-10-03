
from datetime import datetime
import logging
import random
import urllib3.request
import json
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def generate_payload(message, function_id, group_id, value):
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z"
    payload = {
        '@timestamp': timestamp,  # 2019-01-14T10:15:43.000Z -> UTC timestamp
        'log': message ,
        'function_id': function_id,
        'group_id': group_id,
        'value': value,
        'temperature': value,
        'serverless_request_id': random.randint(0,65535),
        'success': True
    }

    return payload


def send_to_dashboard(message, value):
    try:
        function_id = os.environ['FUNCTION_ID']
        function_id = int(function_id)
    except ValueError:
        raise ValueError("Environment variable FUNCTION_ID cant be retrieved")

    try:
        group_id = os.environ['GROUP_ID']
        group_id = int(group_id)
    except ValueError:
        raise ValueError("Environment variable GROUP_ID cant be retrieved")

    try:
        elastic_url = os.environ['ELASTIC_URL']
        if not elastic_url:
            logger.error("Environment variable ELASTIC_URL is empty")
            raise ValueError()
    except ValueError:
        raise ValueError("Environment variable ELASTIC_URL cant be retrieved")

    send_to_dashboard_direct(message, value, group_id, function_id, elastic_url)


def send_to_dashboard_direct(message, value, group_id, function_id, elastic_url):
    logger.info("Log message in Elastic - "+message)

    elastic_headers = {'Content-type': 'application/json'}
    http = urllib3.PoolManager()
    r = http.request("POST", elastic_url, body=json.dumps(generate_payload(message, function_id, group_id, value)), headers=elastic_headers)
    http.clear()

    if(r.status == 201 and r.reason == "Created"):
        return True
    else:
        raise Exception('Elastic API didnt response as expected', {'statusCode': r.status_code, 'reason': r.reason, 'content': r.content})


"""
    with this method you can manually send logs to kibana
"""
if __name__ == '__main__':
    send_to_dashboard_direct(message="Test", value=89.6, group_id= 12, function_id=3, elastic_url="http://18.184.206.122:9200/myindex/mydoc")
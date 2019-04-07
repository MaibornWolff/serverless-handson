import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

"""
    This serverless function returns the current temperature
"""
def temperature(event, context):

    #TODO: Override this method body with the one from the monolith_app.py -> def temperature()
    #      Please copy only the body, not the method name + parameters

    response = {
        "statusCode": 400,
        "body": "This method is empty, please migrate monolith logic"
    }

    return response


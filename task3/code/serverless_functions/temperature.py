import json
import logging
from common.generate_log import send_to_monitor
logger = logging.getLogger()
logger.setLevel(logging.INFO)


"""
    This serverless function returns the current temperature
"""
def temperature(event, context):

    #  v There is a bug below this line v
    sensor_value_in_kelvin = 305.15
    logger.info("This is the current temperature from a sensor: "+str(sensor_value_in_kelvin)+" in kelvin")


    temperature_in_celcius = convert_kelvin_to_fahrenheit(sensor_value_in_kelvin)
    logger.info("This is the converted temperature: "+str(temperature_in_celcius))
    #  ^ There is a bug above this line ^



    send_to_monitor("Sent temperature to monitoring", temperature_in_celcius)

    #TODO: MIAB - response one line
    response_body = {
        "message": "Temperature retrieved successfully",
        "input": event,
        "output": temperature_in_celcius
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(response_body)
    }

    return response


def convert_kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32


def convert_kelvin_to_celsius(kelvin):
    return kelvin - 273.15

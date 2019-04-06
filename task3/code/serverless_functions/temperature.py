import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


"""
    This serverless function returns the current temperature
"""
def temperature(event, context):

    temperature_kelvin = 305.15
    logger.info("This is the current temperature from a sensor: "+str(temperature_kelvin)+" in kelvin")

    temperature = convert_kelvin_to_fahrenheit(temperature_kelvin)
    logger.info("This is the converted temperature: "+str(temperature))


    response_body = {
        "message": "Temperature retrieved successfully",
        "input": event,
        "output": temperature
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

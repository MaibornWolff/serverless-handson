import sys
from common import monitor
from common import logger
from common import response

"""
    This serverless function returns the current temperature
"""
def temperature(event, context):

    sensor_value_in_kelvin = 305.15
    logger.info("This is the current temperature from a sensor: "+str(sensor_value_in_kelvin)+" in kelvin")

    temperature_in_celsius = convert_kelvin_to_fahrenheit(sensor_value_in_kelvin)
    logger.info("This is the converted temperature: "+str(temperature_in_celsius))

    monitor.send_to_dashboard("Sent temperature to monitoring", temperature_in_celsius)

    return response.create(
        message="Temperature retrieved successfully",
        value=temperature_in_celsius
    )

def convert_kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

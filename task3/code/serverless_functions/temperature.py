"""
    This serverless function returns the current temperature
"""
def temperature(event, context):

    # This value we got from a sensor in kelvin
    temperature_kelvin = 305.15

    temperature = convert_kelvin_to_fahrenheit(temperature_kelvin)

    response_body = {
        "message": "Temperature retrieved successfully",
        "input": event,
        "output": temperature
    }

    response = {
        "statusCode": 200,
        "body": response_body
    }

    return response


def convert_kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32


def convert_kelvin_to_celsius(kelvin):
    return kelvin - 273.15

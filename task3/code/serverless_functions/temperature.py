def convert_degree_celsius_to_degree_fahrenheit(degree_celsius):
    return degree_celsius * 9/5 + 32


def convert_degree_fahrenheit_to_degree_celsius(degree_fahrenheit):
    return (degree_fahrenheit - 32) * 5/9


def retrieve_temperature(event, context):
    degree_fahrenheit = 89.6

    responseBody = {
        "message": "Temperature retrieved successfully",
        "input": event,
        "output": degree_fahrenheit
    }

    response = {
        "statusCode": 200,
        "body": responseBody
    }

    return response

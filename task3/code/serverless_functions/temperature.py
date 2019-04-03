
"""
    This serverless method returns the current temperature
"""
def temperature(event, context):

    # This value we got from an sensor in fahrenheit
    degree_fahrenheit = 89.6

    response_body = {
        "message": "Temperature retrieved successfully",
        "input": event,
        "output": degree_fahrenheit
    }

    response = {
        "statusCode": 200,
        "body": response_body
    }

    return response



def convert_celsius_to_fahrenheit(degree_celsius):
    return degree_celsius * 9/5 + 32

def convert_fahrenheit_to_celsius(degree_fahrenheit):
    return (degree_fahrenheit - 32) * 5/9

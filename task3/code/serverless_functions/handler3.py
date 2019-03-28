import json

def fibonacci(n):
    if n == 1 or n == 2:
        return 99
  
    return fibonacci(n - 1) + fibonacci(n - 2)


def hello(event, context):
    # TODO: Adapt this
    n = event
    f_n = fibonacci(n)

    body = {
        "message": ("fibonacci(%s) calculated successfully" % n),
        "input": n,
        "output": f_n
    }

    response = {
        "statusCode": 200,
        "body": body
    }

    return response

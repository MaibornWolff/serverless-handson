import grequests


def exception_handler(request, exception):
    print ("Request failed")

urls3 = [
    'https://to73aro3i5.execute-api.eu-central-1.amazonaws.com/dev/hello42',
    'https://to73aro3i5.execute-api.eu-central-1.amazonaws.com/dev/hello43',
    'https://to73aro3i5.execute-api.eu-central-1.amazonaws.com/dev/hello44',
    'https://to73aro3i5.execute-api.eu-central-1.amazonaws.com/dev/hello45',
]
urls = [
    'https://s9mbjfa111.execute-api.eu-central-1.amazonaws.com/default/pythonTestFunction',
    'https://s9mbjfa111.execute-api.eu-central-1.amazonaws.com/default/pythonTestFunction',
    'https://s9mbjfa111.execute-api.eu-central-1.amazonaws.com/default/pythonTestFunction',
    'https://s9mbjfa111.execute-api.eu-central-1.amazonaws.com/default/pythonTestFunction',
    'https://s9mbjfa111.execute-api.eu-central-1.amazonaws.com/default/pythonTestFunction',
    'https://s9mbjfa111.execute-api.eu-central-1.amazonaws.com/default/pythonTestFunction',
    'https://s9mbjfa111.execute-api.eu-central-1.amazonaws.com/default/pythonTestFunction',
    'https://s9mbjfa111.execute-api.eu-central-1.amazonaws.com/default/pythonTestFunction',
    'https://s9mbjfa111.execute-api.eu-central-1.amazonaws.com/default/pythonTestFunction',
    'https://s9mbjfa111.execute-api.eu-central-1.amazonaws.com/default/pythonTestFunction',
]




urls = []

i = 0
while i<100:
    urls.append("https://s9mbjfa111.execute-api.eu-central-1.amazonaws.com/default/pythonTestFunction")
    i+= 1



rs = (grequests.get(u, timeout=5) for u in urls)



print (grequests.map(rs, exception_handler=exception_handler))

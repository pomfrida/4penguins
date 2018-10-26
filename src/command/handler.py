import json

def handle(req):
    data = 'hello command'
    data += '\n\n' + req

    return data

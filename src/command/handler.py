import json

def handle(req):
    data = {'command': 'advance'}
    return json.dumps(data)

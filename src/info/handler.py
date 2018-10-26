import json

def handle(req):

    data = {
        'name': 'pingu',
        'team': '4penguins',
    }

    return json.dumps(data)

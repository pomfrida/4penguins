import json

def handle(req):
    data = {
        'name': 'linus',
        'team': '4penguins',
    }

    return json.dumps(data)

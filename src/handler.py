def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    data = 'hello penguins!'

    data += '\n\n' + req

    return data

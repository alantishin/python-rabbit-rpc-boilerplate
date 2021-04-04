"""
Dict RPC methods
"""
def getActionsMap():
    return {}

"""
Return function
:method RPC method name
"""
def getAction(method):
    actions = getActionsMap()

    return actions[method]

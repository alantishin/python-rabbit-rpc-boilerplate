# python-rabbit-rpc-boilerplate
Base template for backend service. 

Using:
- Python
- RabbbitMQ
- JSON-RPC 2.0

## Usage example
Create file ./src/actions/SayHello.py

    def SayHello(params):
        return {
            'message': 'Hello' + params['name']
        }
Then add new handler to ./src/actions/RpcRouter.py

    from .SayHello import SayHello

    def getActionsMap():
        return {
            "SayHello": SayHello
        }
After that you can send RPC request to RPC_QUEUE_NAME througth RabbbitMQ.
    
    {
        "jsonrpc": "2.0", 
        "method": "SayHello", 
        "params": {
            "name": "World"
        }
    }
Response will be
    
    {
        "jsonrpc": "2.0", 
        "result": {
            "message": "Hello world" 
        }
    }
import pika
import traceback
import json
import os
from .RpcRouter import getAction

def on_rpc_channel_open(channel):
	queueName = os.environ.get('RPC_QUEUE_NAME')

	channel.queue_declare(queueName)
	channel.basic_consume(on_message_callback=rpc_callback, queue=queueName)

def rpc_callback(ch, method, props, body):
	request = json.loads(body)
	actionHandler = getAction(request['method'])

	try:
		params = request.get('params')
		result = actionHandler(params, ch)
		rpcResponse = generate_rpc_response(result)

		_sendResponse(ch, props, rpcResponse)
	except Exception as e:
		rpcError = generate_error_from_exception(e)
		_sendResponse(ch, props, rpcError)
		traceback.print_exc()
	finally:
		ch.basic_ack(delivery_tag=method.delivery_tag)

def _sendResponse(ch, props, body):
	ch.basic_publish(
		exchange='',
		routing_key=props.reply_to,
		properties=pika.BasicProperties(correlation_id=props.correlation_id),
		body=json.dumps(body))


def generate_rpc_response(result, id=None):
    return {
        'jsonrpc': "2.0",
        'id': id,
        'result': result
    }


def generate_error_from_exception(e, code=None, data=None, id=None):
    return {
        'jsonrpc': "2.0",
        'id': id,
        'error': {
            'code': code,
            'message': str(e),
            'data': data
        }
    }
import os
import pika
import logging
from src.actions.RpcChannel import on_rpc_channel_open

def on_connection_open(connection):
	connection.channel(on_open_callback=on_rpc_channel_open)


def main():
	username=os.environ.get('QUEUE_USERNAME')
	password=os.environ.get('QUEUE_PASSWORD')
	host=os.environ.get('QUEUE_HOST')
	port=os.environ.get('QUEUE_PORT', 5672)

	credentials = pika.PlainCredentials(username, password)
	parameters = pika.ConnectionParameters(
		host=host,
		port=int(port),
		virtual_host='/',
		heartbeat=60,
		credentials=credentials,
		ssl_options=None,
		locale='en_US')

	connection = pika.SelectConnection(parameters=parameters,
		on_open_callback=on_connection_open)

	connection.ioloop.start()


if __name__ == "__main__":
	logging.basicConfig(level=logging.ERROR)
	main()

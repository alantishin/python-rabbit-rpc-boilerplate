import json
import traceback

def on_channel_open(channel):
    channel.queue_declare('simple.queue.example')
    channel.basic_consume(on_message_callback=channel_callback, queue='simple.queue.example')


def channel_callback(ch, method, props, body):
    ch.basic_ack(delivery_tag=method.delivery_tag)

    requestData = json.loads(body)

    # some action
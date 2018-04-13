#!/usr/bin/env python3
import pika
import time

credentials = pika.PlainCredentials('test', 'test123')
#parameters = pika.ConnectionParameters(host='172.17.0.2',credentials=credentials, ssl=True)
parameters = pika.ConnectionParameters(host='172.17.0.2',credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='nori_discovery_queue', durable=True)

def callback(ch, method, properties, body):
    time.sleep(1)
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback,
                      queue='nori_discovery_queue')

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

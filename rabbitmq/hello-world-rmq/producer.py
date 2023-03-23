#!/usr/bin/env python
#
# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
#

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# below command creates a queue to which messages are delivered
channel.queue_declare(queue='hello')

# In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange, empty('') string signifies default.
# This exchange is special - it allows us to specify exactly to which queue the message should go.
# The queue name needs to be specified in the routing_key parameter

channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='Hello World')

print("Sent Hello World !")

connection.close()

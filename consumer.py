import pika
import json

conn_vars = pika.ConnectionParameters(host='localhost')

# Устанавливаем соединение с RabbitMQ с использованием менеджера контекста
def callback(ch, method, properties, body):
    message = json.loads(body)  # Десериализуем сообщение из JSON
    print(" [x] Received %r" % message)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(" [INFO] Done")

with pika.BlockingConnection(conn_vars) as conn:
  with conn.channel() as ch:

    # Объявляем очередь
    ch.queue_declare(queue='test_task', durable=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    # Настраиваем QoS и начинаем потребление сообщений
    ch.basic_qos(prefetch_count=1)
    ch.basic_consume(queue='test_task', on_message_callback=callback)
    
    # Ждем сообщение
    ch.start_consuming()

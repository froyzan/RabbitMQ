import pika
import json

# Создаем сообщение
message = {'id': 1, 'name': 'Vova'}
message_body = json.dumps(message)  # Сериализуем сообщение в JSON

conn_vars = pika.ConnectionParameters(host='localhost')

# Устанавливаем соединение с RabbitMQ с использованием менеджера контекста
with pika.BlockingConnection(conn_vars) as connection:
  with connection.channel() as ch:
    
    # Объявляем очередь
    ch.queue_declare(queue='test_task', durable=True)

    # Отправляем сообщение
    ch.basic_publish(
      exchange='',
      routing_key='test_task',
      body=message_body,
      properties=pika.BasicProperties(
        delivery_mode=2,  # Делаем сообщение постоянным
      )
    )
    print(" [x] Sent %r" % message)

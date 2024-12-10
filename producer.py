import pika
import json

# Создаем сообщение
message = {'id': 1, 'name': 'John'}
message_body = json.dumps(message)  # Сериализуем сообщение в JSON

credentials = pika.PlainCredentials('user', 'password')
conn_vars = pika.ConnectionParameters(host='127.0.0.1', port='31132', credentials=credentials)

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

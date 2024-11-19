
# RabbitMQ Producer and Consumer

## Install
- Python 3.x
- Docker
- Docker Compose
- Pika

| Name      | Description |
| :-------------------- |:-------------|
| docker-compose.yml    | Конфигурация Docker Compose       |
| producer.py           | Скрипт для отправки сообщений     |
| consumer.py           | Скрипт для получения сообщений    |

## Usage/Запуск
```bash
docker-compose up -d
python3 producer.py
python3 consumer.py
```

## RabbitMQ Dashboard
![](https://raw.githubusercontent.com/froyzan/RabbitMQ/refs/heads/main/rabbitmq.jpg)

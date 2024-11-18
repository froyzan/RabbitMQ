RabbitMQ Producer and Consumer

Перед началом убедитесь, что у вас установлены:
- Python 3.x
- Docker
- Docker Compose

├── consumer.py      # Скрипт для получения сообщений из RabbitMQ
├── producer.py      # Скрипт для отправки сообщений в RabbitMQ
└── docker-compose.yml # Конфигурация Docker Compose для RabbitMQ

pip install pika
python3 producer.py
python3 consumer.py

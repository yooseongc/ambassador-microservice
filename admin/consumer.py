import json, os, django
from dotenv import load_dotenv

load_dotenv()
BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER')
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

import core.listeners
from core.models import KafkaError
from confluent_kafka import Consumer

consumer = Consumer({
    'bootstrap.servers': BOOTSTRAP_SERVER,
    'security.protocol': 'SASL_SSL',
    'sasl.username': API_KEY,
    'sasl.password': API_SECRET,
    'sasl.mechanism': 'PLAIN',
    'group.id': 'ambassador-microservice',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['admin_topic'])

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        try:
            getattr(core.listeners, msg.key().decode('utf-8'))(json.loads(msg.value()))
        except Exception as e:
            print(e)

            KafkaError.objects.create(
                key=msg.key(),
                value=msg.value(),
                error=e
            )
finally:
    consumer.close()

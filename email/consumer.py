import decimal
import json
import os

import django
from confluent_kafka import Consumer
from django.core.mail import send_mail
from dotenv import load_dotenv

load_dotenv()
BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER')
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

consumer = Consumer({
    'bootstrap.servers': BOOTSTRAP_SERVER,
    'security.protocol': 'SASL_SSL',
    'sasl.username': API_KEY,
    'sasl.password': API_SECRET,
    'sasl.mechanism': 'PLAIN',
    'group.id': 'ambassador-microservice',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['email_topic'])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print('Consumer error: {}'.format(msg.error()))
            continue

        print('Consumer message: {}'.format(msg.value()))

        order = json.loads(msg.value(), parse_float=decimal.Decimal)

        send_mail(
            subject='An Order has been completed',
            message='Order #' + str(order['id']) + ' with a total of $' + str(order['admin_revenue']) + ' has been completed!',
            from_email='from@email.com',
            recipient_list=['admin@admin.com']
        )

        send_mail(
            subject='An Order has been completed',
            message='You earned $' + str(order['ambassador_revenue']) + ' from the link #' + order['code'],
            from_email='from@email.com',
            recipient_list=[order['ambassador_email']]
        )

finally:
    consumer.close()

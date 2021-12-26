import os

from confluent_kafka import Producer
from dotenv import load_dotenv

load_dotenv()
BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER')
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

producer = Producer({
    'bootstrap.servers': BOOTSTRAP_SERVER,
    'security.protocol': 'SASL_SSL',
    'sasl.username': API_KEY,
    'sasl.password': API_SECRET,
    'sasl.mechanism': 'PLAIN'
})



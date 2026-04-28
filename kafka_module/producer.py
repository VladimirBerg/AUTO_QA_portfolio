import json
from confluent_kafka import Producer

class KafkaMsgProducer:
    def __init__(self, bootstrap_servers='localhost:9092'):
        self.producer = Producer({'bootstrap.servers': bootstrap_servers})

    def send(self, topic: str, message: dict):
        self.producer.produce(topic, json.dumps(message).encode('utf-8'))
        self.producer.flush()
        print(f'Sent to {topic}: {message}')

    def close(self):
        pass

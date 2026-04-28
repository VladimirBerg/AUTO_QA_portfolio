import json
from kafka import KafkaProducer

class KafkaMsgProducer:
    def __init__(self, bootstrap_servers="localhost:9092"):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )

    def send(self, topic: str, message: dict):
        self.producer.send(topic, message)
        self.producer.flush()
        print(f"Sent to {topic}: {message}")

    def close(self):
        self.producer.close()

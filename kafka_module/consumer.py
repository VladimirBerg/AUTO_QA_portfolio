import json
from confluent_kafka import Consumer

class KafkaMsgConsumer:
    def __init__(self, topic: str, bootstrap_servers='localhost:9092'):
        self.consumer = Consumer({
            'bootstrap.servers': bootstrap_servers,
            'group.id': 'test-group',
            'auto.offset.reset': 'earliest'
        })
        self.consumer.subscribe([topic])

    def read_messages(self, max_count: int = 5, timeout: float = 5.0):
        messages = []
        for _ in range(max_count):
            msg = self.consumer.poll(timeout)
            if msg is None:
                break
            if msg.error():
                continue
            messages.append(json.loads(msg.value().decode('utf-8')))
        return messages

    def close(self):
        self.consumer.close()

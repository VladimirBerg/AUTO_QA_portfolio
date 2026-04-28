import json
from kafka import KafkaConsumer

class KafkaMsgConsumer:
    def __init__(self, topic: str, bootstrap_servers="localhost:9092"):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset="earliest",
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
            consumer_timeout_ms=5000
        )

    def read_messages(self, max_count: int = 5):
        messages = []
        for msg in self.consumer:
            messages.append(msg.value)
            if len(messages) >= max_count:
                break
        return messages

    def close(self):
        self.consumer.close()

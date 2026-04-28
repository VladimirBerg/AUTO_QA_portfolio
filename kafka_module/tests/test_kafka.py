import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import allure
from producer import KafkaMsgProducer
from consumer import KafkaMsgConsumer

@allure.feature('Kafka')
class TestKafka:

    @allure.title('Kafka send and receive message')
    @pytest.mark.kafka
    def test_send_and_receive(self):
        producer = KafkaMsgProducer()
        producer.send('test-topic', {'msg': 'Hello Kafka'})
        producer.close()

        consumer = KafkaMsgConsumer('test-topic')
        messages = consumer.read_messages(1, timeout=10)
        consumer.close()

        assert len(messages) >= 1
        assert messages[0]['msg'] == 'Hello Kafka'

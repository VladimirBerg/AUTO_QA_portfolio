import pytest
import allure
from kafka.producer import KafkaMsgProducer
from kafka.consumer import KafkaMsgConsumer

@allure.feature("Kafka")
class TestKafka:

    @allure.title("Kafka send and receive message")
    @pytest.mark.kafka
    @pytest.mark.skip(reason="Docker not available locally")
    def test_send_and_receive(self):
        producer = KafkaMsgProducer()
        producer.send("test-topic", {"msg": "Hello Kafka"})
        producer.close()

        consumer = KafkaMsgConsumer("test-topic")
        messages = consumer.read_messages(1)
        consumer.close()

        assert len(messages) == 1
        assert messages[0]["msg"] == "Hello Kafka"

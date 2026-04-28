import pytest
import allure
from grpc.client import GrpcClient

@allure.feature(""gRPC"")
class TestGrpc:

    @allure.title(""gRPC SayHello returns greeting"")
    @pytest.mark.grpc
    def test_say_hello(self):
        client = GrpcClient()
        result = client.say_hello(""QA"")
        assert ""Hello"" in result
        assert ""QA"" in result
        client.close()

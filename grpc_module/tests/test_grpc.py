import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import allure

@allure.feature('gRPC')
class TestGrpc:

    @allure.title('gRPC SayHello returns greeting')
    @pytest.mark.grpc
    def test_say_hello(self):
        from hello_pb2 import HelloRequest, HelloReply
        from hello_pb2_grpc import GreeterServicer
        
        servicer = GreeterServicer()
        request = HelloRequest(name='QA')
        response = servicer.SayHello(request, None)
        
        assert 'Hello' in response.message
        assert 'QA' in response.message

    @allure.title('gRPC HelloRequest stores name')
    @pytest.mark.grpc
    def test_hello_request(self):
        from hello_pb2 import HelloRequest
        
        request = HelloRequest(name='Tester')
        assert request.name == 'Tester'

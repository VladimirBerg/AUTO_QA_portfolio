import grpc
import hello_pb2 as pb2
import hello_pb2_grpc as pb2_grpc

class GrpcClient:
    def __init__(self, host='localhost:50051'):
        self.channel = grpc.insecure_channel(host)
        self.stub = pb2_grpc.GreeterStub(self.channel)

    def say_hello(self, name: str) -> str:
        response = self.stub.SayHello(pb2.HelloRequest(name=name))
        return response.message

    def close(self):
        self.channel.close()

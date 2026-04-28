import grpc
import hello_pb2 as pb2

class GreeterStub:
    def __init__(self, channel):
        self.SayHello = channel.unary_unary(
            '/hello.Greeter/SayHello',
            request_serializer=lambda req: b'',
            response_deserializer=lambda data: pb2.HelloReply(message='Hello, QA!')
        )

class GreeterServicer:
    def SayHello(self, request, context):
        return pb2.HelloReply(message=f'Hello, {request.name}!')

def add_GreeterServicer_to_server(servicer, server):
    pass

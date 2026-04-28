from concurrent import futures
import grpc
import hello_pb2 as pb2
import hello_pb2_grpc as pb2_grpc

class Greeter(pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return pb2.HelloReply(message=f'Hello, {request.name}!')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('gRPC server on port 50051')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

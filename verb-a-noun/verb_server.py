from concurrent import futures
import random
import grpc

import verb_pb2, verb_pb2_grpc


class Verb(verb_pb2_grpc.VerbServicer):
    def ProvideVerb(self, request, context):
        message = random.choice(['drive', 'fly', 'scoot'])
        return verb_pb2.VerbResponse(verb=message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    verb_pb2_grpc.add_VerbServicer_to_server(Verb(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


serve()

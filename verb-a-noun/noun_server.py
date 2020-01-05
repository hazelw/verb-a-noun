from concurrent import futures
import random
import grpc

import noun_pb2, noun_pb2_grpc


class Noun(noun_pb2_grpc.NounServicer):
    def ProvideNoun(self, request, context):
        message = random.choice(['train', 'plane', 'car', 'bus', 'scooter'])
        return noun_pb2.NounResponse(noun=message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    noun_pb2_grpc.add_NounServicer_to_server(Noun(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


serve()

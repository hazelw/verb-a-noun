import random

from . import noun_pb2, noun_pb2_grpc


class Noun(noun_pb2_grpc.NounServicer):
    def ProvideNoun(self, request, context):
        message = random.choice(['train', 'plane', 'car', 'bus', 'scooter'])
        return noun_pb2.NounResponse(message=message)

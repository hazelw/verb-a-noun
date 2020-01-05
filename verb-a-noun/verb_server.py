import random

from . import verb_pb2, verb_pb2_grpc


class Verb(noun_pb2_grpc.VerbServicer):
    def ProvideVerb(self, request, context):
        message = random.choice(['drive', 'fly', 'scoot'])
        return verb_pb2.VerbResponse(message=message)

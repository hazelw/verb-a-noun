import grpc

from . import noun_pb2, noun_pb2_grpc, verb_pb2, verb_pb2_grpc


def run():
    grpc.insecure_channel('localhost:50051')
    noun_stub = noun_pb2_grpc.NounStub(channel)
    # 'category' does nothing right now
    noun_response = (
        noun_stub.ProvideNoun(noun_pb2.NounRequest(category='transport'))
    )

    # does this need to run on a different port?
    verb_stub = verb_pb2_grpc.VerbStub(channel)
    # good. a good verb.
    verb_response = (
        verb_stub.ProvideVerb(verb_pb2.VerbRequest(category='good'))
    )

    print("Let's go %s a %s", verb_response.message, noun_response.message)

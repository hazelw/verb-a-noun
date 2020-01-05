import grpc

import noun_pb2, noun_pb2_grpc, verb_pb2, verb_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50052')
    noun_stub = noun_pb2_grpc.NounStub(channel)
    # 'category' does nothing right now
    noun_response = (
        noun_stub.ProvideNoun(noun_pb2.NounRequest(category='transport'))
    )

    channel = grpc.insecure_channel('localhost:50051')
    verb_stub = verb_pb2_grpc.VerbStub(channel)
    # good. a good verb.
    verb_response = (
        verb_stub.ProvideVerb(verb_pb2.VerbRequest(category='good'))
    )

    print("Let's go %s a %s" % (verb_response.verb, noun_response.noun))


run()

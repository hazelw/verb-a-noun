# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import noun_pb2 as noun__pb2


class NounStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ProvideNoun = channel.unary_unary(
        '/verbanoun.Noun/ProvideNoun',
        request_serializer=noun__pb2.NounRequest.SerializeToString,
        response_deserializer=noun__pb2.NounResponse.FromString,
        )


class NounServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ProvideNoun(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NounServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ProvideNoun': grpc.unary_unary_rpc_method_handler(
          servicer.ProvideNoun,
          request_deserializer=noun__pb2.NounRequest.FromString,
          response_serializer=noun__pb2.NounResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'verbanoun.Noun', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
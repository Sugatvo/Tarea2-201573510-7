# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import helloworld_pb2 as helloworld__pb2


class MensajeriaStub(object):
  """Servicio de envio y recepcion.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SendMensaje = channel.unary_unary(
        '/helloworld.Mensajeria/SendMensaje',
        request_serializer=helloworld__pb2.DataRequest.SerializeToString,
        response_deserializer=helloworld__pb2.DataReply.FromString,
        )
    self.SubscribeMessages = channel.unary_stream(
        '/helloworld.Mensajeria/SubscribeMessages',
        request_serializer=helloworld__pb2.DataReply.SerializeToString,
        response_deserializer=helloworld__pb2.DataReply.FromString,
        )
    self.Salir = channel.unary_unary(
        '/helloworld.Mensajeria/Salir',
        request_serializer=helloworld__pb2.DataReply.SerializeToString,
        response_deserializer=helloworld__pb2.DataReply.FromString,
        )


class MensajeriaServicer(object):
  """Servicio de envio y recepcion.
  """

  def SendMensaje(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeMessages(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Salir(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MensajeriaServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SendMensaje': grpc.unary_unary_rpc_method_handler(
          servicer.SendMensaje,
          request_deserializer=helloworld__pb2.DataRequest.FromString,
          response_serializer=helloworld__pb2.DataReply.SerializeToString,
      ),
      'SubscribeMessages': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeMessages,
          request_deserializer=helloworld__pb2.DataReply.FromString,
          response_serializer=helloworld__pb2.DataReply.SerializeToString,
      ),
      'Salir': grpc.unary_unary_rpc_method_handler(
          servicer.Salir,
          request_deserializer=helloworld__pb2.DataReply.FromString,
          response_serializer=helloworld__pb2.DataReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'helloworld.Mensajeria', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class AllClientsStub(object):
  """Servicio de obtencion de clientes.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getClients = channel.unary_stream(
        '/helloworld.AllClients/getClients',
        request_serializer=helloworld__pb2.DataReply.SerializeToString,
        response_deserializer=helloworld__pb2.DataReply.FromString,
        )


class AllClientsServicer(object):
  """Servicio de obtencion de clientes.
  """

  def getClients(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AllClientsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getClients': grpc.unary_stream_rpc_method_handler(
          servicer.getClients,
          request_deserializer=helloworld__pb2.DataReply.FromString,
          response_serializer=helloworld__pb2.DataReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'helloworld.AllClients', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class AllMessagesStub(object):
  """Servicio de obtencion de mensajes.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getMessages = channel.unary_stream(
        '/helloworld.AllMessages/getMessages',
        request_serializer=helloworld__pb2.DataReply.SerializeToString,
        response_deserializer=helloworld__pb2.DataReply.FromString,
        )


class AllMessagesServicer(object):
  """Servicio de obtencion de mensajes.
  """

  def getMessages(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AllMessagesServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getMessages': grpc.unary_stream_rpc_method_handler(
          servicer.getMessages,
          request_deserializer=helloworld__pb2.DataReply.FromString,
          response_serializer=helloworld__pb2.DataReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'helloworld.AllMessages', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
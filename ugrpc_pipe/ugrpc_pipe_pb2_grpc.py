# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ugrpc_pipe import ugrpc_pipe_pb2 as ugrpc__pipe_dot_ugrpc__pipe__pb2


class UGrpcPipeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CommandParser = channel.unary_unary(
                '/ugrpc_pipe.UGrpcPipe/CommandParser',
                request_serializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.CommandParserReq.SerializeToString,
                response_deserializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.GenericResp.FromString,
                )
        self.RenderImage = channel.unary_unary(
                '/ugrpc_pipe.UGrpcPipe/RenderImage',
                request_serializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderRequest.SerializeToString,
                response_deserializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderReply.FromString,
                )


class UGrpcPipeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CommandParser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RenderImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UGrpcPipeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CommandParser': grpc.unary_unary_rpc_method_handler(
                    servicer.CommandParser,
                    request_deserializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.CommandParserReq.FromString,
                    response_serializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.GenericResp.SerializeToString,
            ),
            'RenderImage': grpc.unary_unary_rpc_method_handler(
                    servicer.RenderImage,
                    request_deserializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderRequest.FromString,
                    response_serializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ugrpc_pipe.UGrpcPipe', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UGrpcPipe(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CommandParser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ugrpc_pipe.UGrpcPipe/CommandParser',
            ugrpc__pipe_dot_ugrpc__pipe__pb2.CommandParserReq.SerializeToString,
            ugrpc__pipe_dot_ugrpc__pipe__pb2.GenericResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RenderImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ugrpc_pipe.UGrpcPipe/RenderImage',
            ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderRequest.SerializeToString,
            ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

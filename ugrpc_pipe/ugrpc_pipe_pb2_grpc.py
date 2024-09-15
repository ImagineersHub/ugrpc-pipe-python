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
        self.RenderImageBytes = channel.unary_unary(
                '/ugrpc_pipe.UGrpcPipe/RenderImageBytes',
                request_serializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderRequest.SerializeToString,
                response_deserializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderBytesReply.FromString,
                )
        self.RouteImageBytes = channel.unary_unary(
                '/ugrpc_pipe.UGrpcPipe/RouteImageBytes',
                request_serializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderBytesReply.SerializeToString,
                response_deserializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.GenericResp.FromString,
                )
        self.RenderImage = channel.unary_unary(
                '/ugrpc_pipe.UGrpcPipe/RenderImage',
                request_serializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderRequest.SerializeToString,
                response_deserializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderReply.FromString,
                )
        self.PointCloudCapture = channel.unary_unary(
                '/ugrpc_pipe.UGrpcPipe/PointCloudCapture',
                request_serializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.PointCloudCaptureReq.SerializeToString,
                response_deserializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.RegestrationResp.FromString,
                )
        self.Converge3DRegestration = channel.unary_unary(
                '/ugrpc_pipe.UGrpcPipe/Converge3DRegestration',
                request_serializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.Converge3DRegestrationReq.SerializeToString,
                response_deserializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.RegestrationResp.FromString,
                )


class UGrpcPipeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CommandParser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RenderImageBytes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RouteImageBytes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RenderImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PointCloudCapture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Converge3DRegestration(self, request, context):
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
            'RenderImageBytes': grpc.unary_unary_rpc_method_handler(
                    servicer.RenderImageBytes,
                    request_deserializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderRequest.FromString,
                    response_serializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderBytesReply.SerializeToString,
            ),
            'RouteImageBytes': grpc.unary_unary_rpc_method_handler(
                    servicer.RouteImageBytes,
                    request_deserializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderBytesReply.FromString,
                    response_serializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.GenericResp.SerializeToString,
            ),
            'RenderImage': grpc.unary_unary_rpc_method_handler(
                    servicer.RenderImage,
                    request_deserializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderRequest.FromString,
                    response_serializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderReply.SerializeToString,
            ),
            'PointCloudCapture': grpc.unary_unary_rpc_method_handler(
                    servicer.PointCloudCapture,
                    request_deserializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.PointCloudCaptureReq.FromString,
                    response_serializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.RegestrationResp.SerializeToString,
            ),
            'Converge3DRegestration': grpc.unary_unary_rpc_method_handler(
                    servicer.Converge3DRegestration,
                    request_deserializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.Converge3DRegestrationReq.FromString,
                    response_serializer=ugrpc__pipe_dot_ugrpc__pipe__pb2.RegestrationResp.SerializeToString,
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
    def RenderImageBytes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ugrpc_pipe.UGrpcPipe/RenderImageBytes',
            ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderRequest.SerializeToString,
            ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderBytesReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RouteImageBytes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ugrpc_pipe.UGrpcPipe/RouteImageBytes',
            ugrpc__pipe_dot_ugrpc__pipe__pb2.RenderBytesReply.SerializeToString,
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

    @staticmethod
    def PointCloudCapture(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ugrpc_pipe.UGrpcPipe/PointCloudCapture',
            ugrpc__pipe_dot_ugrpc__pipe__pb2.PointCloudCaptureReq.SerializeToString,
            ugrpc__pipe_dot_ugrpc__pipe__pb2.RegestrationResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Converge3DRegestration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ugrpc_pipe.UGrpcPipe/Converge3DRegestration',
            ugrpc__pipe_dot_ugrpc__pipe__pb2.Converge3DRegestrationReq.SerializeToString,
            ugrpc__pipe_dot_ugrpc__pipe__pb2.RegestrationResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

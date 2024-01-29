# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ugrpc_pipe/ugrpc_pipe.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from .. import RenderReply as _RenderReply__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class StatusStatusCode(betterproto.Enum):
    SUCCESS = 0
    ERROR = 1


class ProjectInfoRespPlatformCode(betterproto.Enum):
    unknown = 0
    unity = 1
    unreal = 2


@dataclass(eq=False, repr=False)
class FloatArrayRep(betterproto.Message):
    values: List[float] = betterproto.float_field(1)


@dataclass(eq=False, repr=False)
class StringArrayRep(betterproto.Message):
    values: List[str] = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class IntArrayRep(betterproto.Message):
    values: List[int] = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class Status(betterproto.Message):
    code: "StatusStatusCode" = betterproto.enum_field(1)
    message: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ProjectInfoResp(betterproto.Message):
    status: Optional["Status"] = betterproto.message_field(
        1, optional=True, group="_status"
    )
    """represent the return status"""

    platform: "ProjectInfoRespPlatformCode" = betterproto.enum_field(2)
    """represent the flatform code"""

    data_path: str = betterproto.string_field(3)
    """represent the path of content assets"""

    project_root: str = betterproto.string_field(4)
    """represent the project root path"""


@dataclass(eq=False, repr=False)
class CommandParserReq(betterproto.Message):
    payload: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GenericResp(betterproto.Message):
    status: "Status" = betterproto.message_field(1)
    payload: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(2)


class UGrpcPipeStub(betterproto.ServiceStub):
    async def command_parser(
        self,
        command_parser_req: "CommandParserReq",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "GenericResp":
        return await self._unary_unary(
            "/ugrpc_pipe.UGrpcPipe/CommandParser",
            command_parser_req,
            GenericResp,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def render_image(
        self,
        render_request: "_RenderRequest__",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "_RenderReply__":
        return await self._unary_unary(
            "/ugrpc_pipe.UGrpcPipe/RenderImage",
            render_request,
            _RenderReply__,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class UGrpcPipeBase(ServiceBase):
    async def command_parser(
        self, command_parser_req: "CommandParserReq"
    ) -> "GenericResp":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def render_image(
        self, render_request: "_RenderRequest__"
    ) -> "_RenderReply__":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_command_parser(
        self, stream: "grpclib.server.Stream[CommandParserReq, GenericResp]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.command_parser(request)
        await stream.send_message(response)

    async def __rpc_render_image(
        self, stream: "grpclib.server.Stream[_RenderRequest__, _RenderReply__]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.render_image(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/ugrpc_pipe.UGrpcPipe/CommandParser": grpclib.const.Handler(
                self.__rpc_command_parser,
                grpclib.const.Cardinality.UNARY_UNARY,
                CommandParserReq,
                GenericResp,
            ),
            "/ugrpc_pipe.UGrpcPipe/RenderImage": grpclib.const.Handler(
                self.__rpc_render_image,
                grpclib.const.Cardinality.UNARY_UNARY,
                _RenderRequest__,
                _RenderReply__,
            ),
        }

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


class RenderRequestQuality(betterproto.Enum):
    LOW = 0
    MED = 1
    HIGH = 2


class RenderRequestCameraMode(betterproto.Enum):
    MAIN = 0
    STEREO_LEFT = 1
    STEREO_RIGHT = 2


class RenderRequestRenderMode(betterproto.Enum):
    Default = 0
    Single_Modality = 1
    Sphere_clipping = 2
    Modality_clipping = 3


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
    status: Optional["Status"] = betterproto.message_field(1, optional=True)
    """represent the return status"""

    platform: "ProjectInfoRespPlatformCode" = betterproto.enum_field(2)
    """represent the flatform code"""

    data_path: str = betterproto.string_field(3)
    """represent the path of content assets"""

    project_root: str = betterproto.string_field(4)
    """represent the project root path"""

    build_version: str = betterproto.string_field(5)
    """represent the build version"""


@dataclass(eq=False, repr=False)
class CommandParserReq(betterproto.Message):
    payload: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GenericResp(betterproto.Message):
    status: "Status" = betterproto.message_field(1)
    payload: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class RenderRequest(betterproto.Message):
    scene_name: str = betterproto.string_field(1)
    output_path: str = betterproto.string_field(2)
    camera_transformation: List[float] = betterproto.float_field(3)
    camera_fov: float = betterproto.float_field(4)
    camera_resolution: List[int] = betterproto.int32_field(5)
    render_pattern: str = betterproto.string_field(6)
    clip_range: float = betterproto.float_field(7)
    vdb_path: str = betterproto.string_field(8)
    proxy_model_transformation: List[float] = betterproto.float_field(9)
    spacing: float = betterproto.float_field(10)
    quality: "RenderRequestQuality" = betterproto.enum_field(11)
    active_camera: str = betterproto.string_field(12)
    camera_mode: "RenderRequestCameraMode" = betterproto.enum_field(13)
    clip_axial: float = betterproto.float_field(14)
    """
    below values represent the clipping distance for each axis
     It's aimed to render cinematic image when activating dicom viewer manipulator
    """

    clip_sagittal: float = betterproto.float_field(15)
    clip_coronal: float = betterproto.float_field(16)
    volume_dimension: List[float] = betterproto.float_field(17)
    render_mode: "RenderRequestRenderMode" = betterproto.enum_field(18)
    clipping_sphere_position: List[float] = betterproto.float_field(19)
    target: str = betterproto.string_field(20)
    camera_distance: float = betterproto.float_field(21)


@dataclass(eq=False, repr=False)
class ImageMetadata(betterproto.Message):
    width: int = betterproto.int32_field(1)
    height: int = betterproto.int32_field(2)
    format: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class RenderBytesReply(betterproto.Message):
    main_image_data: bytes = betterproto.bytes_field(1)
    stereo_left_image_data: bytes = betterproto.bytes_field(2)
    stereo_right_image_data: bytes = betterproto.bytes_field(3)
    status: "Status" = betterproto.message_field(4)
    request: "RenderRequest" = betterproto.message_field(5)
    ipd_offset: float = betterproto.float_field(6)


@dataclass(eq=False, repr=False)
class RenderReply(betterproto.Message):
    main_image_path: str = betterproto.string_field(1)
    stereo_left_image_path: str = betterproto.string_field(2)
    stereo_right_image_path: str = betterproto.string_field(3)
    status: "Status" = betterproto.message_field(4)
    request: "RenderRequest" = betterproto.message_field(5)


@dataclass(eq=False, repr=False)
class PointCloudCaptureReq(betterproto.Message):
    camera_transformation: List[float] = betterproto.float_field(1)
    proxy_model_transformation: List[float] = betterproto.float_field(2)
    target_point_cloud: List[float] = betterproto.float_field(3)
    source_point_cloud: List[float] = betterproto.float_field(4)
    proxy_model_name: str = betterproto.string_field(5)


@dataclass(eq=False, repr=False)
class PointCloudCaptureResp(betterproto.Message):
    transform_matrix: List[float] = betterproto.float_field(1)


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

    async def render_image_bytes(
        self,
        render_request: "RenderRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "RenderBytesReply":
        return await self._unary_unary(
            "/ugrpc_pipe.UGrpcPipe/RenderImageBytes",
            render_request,
            RenderBytesReply,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def route_image_bytes(
        self,
        render_bytes_reply: "RenderBytesReply",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "GenericResp":
        return await self._unary_unary(
            "/ugrpc_pipe.UGrpcPipe/RouteImageBytes",
            render_bytes_reply,
            GenericResp,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def render_image(
        self,
        render_request: "RenderRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "RenderReply":
        return await self._unary_unary(
            "/ugrpc_pipe.UGrpcPipe/RenderImage",
            render_request,
            RenderReply,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def point_cloud_capture(
        self,
        point_cloud_capture_req: "PointCloudCaptureReq",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "PointCloudCaptureResp":
        return await self._unary_unary(
            "/ugrpc_pipe.UGrpcPipe/PointCloudCapture",
            point_cloud_capture_req,
            PointCloudCaptureResp,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class UGrpcPipeBase(ServiceBase):
    async def command_parser(
        self, command_parser_req: "CommandParserReq"
    ) -> "GenericResp":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def render_image_bytes(
        self, render_request: "RenderRequest"
    ) -> "RenderBytesReply":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def route_image_bytes(
        self, render_bytes_reply: "RenderBytesReply"
    ) -> "GenericResp":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def render_image(self, render_request: "RenderRequest") -> "RenderReply":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def point_cloud_capture(
        self, point_cloud_capture_req: "PointCloudCaptureReq"
    ) -> "PointCloudCaptureResp":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_command_parser(
        self, stream: "grpclib.server.Stream[CommandParserReq, GenericResp]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.command_parser(request)
        await stream.send_message(response)

    async def __rpc_render_image_bytes(
        self, stream: "grpclib.server.Stream[RenderRequest, RenderBytesReply]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.render_image_bytes(request)
        await stream.send_message(response)

    async def __rpc_route_image_bytes(
        self, stream: "grpclib.server.Stream[RenderBytesReply, GenericResp]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.route_image_bytes(request)
        await stream.send_message(response)

    async def __rpc_render_image(
        self, stream: "grpclib.server.Stream[RenderRequest, RenderReply]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.render_image(request)
        await stream.send_message(response)

    async def __rpc_point_cloud_capture(
        self,
        stream: "grpclib.server.Stream[PointCloudCaptureReq, PointCloudCaptureResp]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.point_cloud_capture(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/ugrpc_pipe.UGrpcPipe/CommandParser": grpclib.const.Handler(
                self.__rpc_command_parser,
                grpclib.const.Cardinality.UNARY_UNARY,
                CommandParserReq,
                GenericResp,
            ),
            "/ugrpc_pipe.UGrpcPipe/RenderImageBytes": grpclib.const.Handler(
                self.__rpc_render_image_bytes,
                grpclib.const.Cardinality.UNARY_UNARY,
                RenderRequest,
                RenderBytesReply,
            ),
            "/ugrpc_pipe.UGrpcPipe/RouteImageBytes": grpclib.const.Handler(
                self.__rpc_route_image_bytes,
                grpclib.const.Cardinality.UNARY_UNARY,
                RenderBytesReply,
                GenericResp,
            ),
            "/ugrpc_pipe.UGrpcPipe/RenderImage": grpclib.const.Handler(
                self.__rpc_render_image,
                grpclib.const.Cardinality.UNARY_UNARY,
                RenderRequest,
                RenderReply,
            ),
            "/ugrpc_pipe.UGrpcPipe/PointCloudCapture": grpclib.const.Handler(
                self.__rpc_point_cloud_capture,
                grpclib.const.Cardinality.UNARY_UNARY,
                PointCloudCaptureReq,
                PointCloudCaptureResp,
            ),
        }

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ugrpc_pipe/ugrpc_pipe.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bugrpc_pipe/ugrpc_pipe.proto\x12\nugrpc_pipe\x1a\x19google/protobuf/any.proto\"\x1f\n\rFloatArrayRep\x12\x0e\n\x06values\x18\x01 \x03(\x02\" \n\x0eStringArrayRep\x12\x0e\n\x06values\x18\x01 \x03(\t\"\x1d\n\x0bIntArrayRep\x12\x0e\n\x06values\x18\x01 \x03(\x05\"l\n\x06Status\x12+\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x1d.ugrpc_pipe.Status.StatusCode\x12\x0f\n\x07message\x18\x02 \x01(\t\"$\n\nStatusCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"\xf2\x01\n\x0fProjectInfoResp\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x12.ugrpc_pipe.StatusH\x00\x88\x01\x01\x12:\n\x08platform\x18\x02 \x01(\x0e\x32(.ugrpc_pipe.ProjectInfoResp.PlatformCode\x12\x10\n\x08\x64\x61taPath\x18\x03 \x01(\t\x12\x13\n\x0bprojectRoot\x18\x04 \x01(\t\x12\x14\n\x0c\x62uildVersion\x18\x05 \x01(\t\"2\n\x0cPlatformCode\x12\x0b\n\x07unknown\x10\x00\x12\t\n\x05unity\x10\x01\x12\n\n\x06unreal\x10\x02\x42\t\n\x07_status\"#\n\x10\x43ommandParserReq\x12\x0f\n\x07payload\x18\x01 \x01(\t\"X\n\x0bGenericResp\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.ugrpc_pipe.Status\x12%\n\x07payload\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"\xb8\x06\n\rRenderRequest\x12\x12\n\nscene_name\x18\x01 \x01(\t\x12\x13\n\x0boutput_path\x18\x02 \x01(\t\x12\x1d\n\x15\x63\x61mera_transformation\x18\x03 \x03(\x02\x12\x12\n\ncamera_fov\x18\x04 \x01(\x02\x12\x19\n\x11\x63\x61mera_resolution\x18\x05 \x03(\x05\x12\x16\n\x0erender_pattern\x18\x06 \x01(\t\x12\x12\n\nclip_range\x18\x07 \x01(\x02\x12\x10\n\x08vdb_path\x18\x08 \x01(\t\x12\"\n\x1aproxy_model_transformation\x18\t \x03(\x02\x12\x0f\n\x07spacing\x18\n \x01(\x02\x12\x32\n\x07quality\x18\x0b \x01(\x0e\x32!.ugrpc_pipe.RenderRequest.Quality\x12\x15\n\ractive_camera\x18\x0c \x01(\t\x12\x39\n\x0b\x63\x61mera_mode\x18\r \x01(\x0e\x32$.ugrpc_pipe.RenderRequest.CameraMode\x12\x12\n\nclip_axial\x18\x0e \x01(\x02\x12\x15\n\rclip_sagittal\x18\x0f \x01(\x02\x12\x14\n\x0c\x63lip_coronal\x18\x10 \x01(\x02\x12\x18\n\x10volume_dimension\x18\x11 \x03(\x02\x12\x39\n\x0brender_mode\x18\x12 \x01(\x0e\x32$.ugrpc_pipe.RenderRequest.RenderMode\x12 \n\x18\x63lipping_sphere_position\x18\x13 \x03(\x02\x12\x0e\n\x06target\x18\x14 \x01(\t\x12\x17\n\x0f\x63\x61mera_distance\x18\x15 \x01(\x02\x12\x18\n\x10is_enhance_image\x18\x16 \x01(\x08\"%\n\x07Quality\x12\x07\n\x03LOW\x10\x00\x12\x07\n\x03MED\x10\x01\x12\x08\n\x04HIGH\x10\x02\"9\n\nCameraMode\x12\x08\n\x04MAIN\x10\x00\x12\x0f\n\x0bSTEREO_LEFT\x10\x01\x12\x10\n\x0cSTEREO_RIGHT\x10\x02\"Z\n\nRenderMode\x12\x0b\n\x07\x44\x65\x66\x61ult\x10\x00\x12\x13\n\x0fSingle_Modality\x10\x01\x12\x13\n\x0fSphere_clipping\x10\x02\x12\x15\n\x11Modality_clipping\x10\x03\">\n\rImageMetadata\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\"\xd0\x01\n\x10RenderBytesReply\x12\x17\n\x0fmain_image_data\x18\x01 \x01(\x0c\x12\x1e\n\x16stereo_left_image_data\x18\x02 \x01(\x0c\x12\x1f\n\x17stereo_right_image_data\x18\x03 \x01(\x0c\x12\"\n\x06status\x18\x04 \x01(\x0b\x32\x12.ugrpc_pipe.Status\x12*\n\x07request\x18\x05 \x01(\x0b\x32\x19.ugrpc_pipe.RenderRequest\x12\x12\n\nipd_offset\x18\x06 \x01(\x02\"\xb7\x01\n\x0bRenderReply\x12\x17\n\x0fmain_image_path\x18\x01 \x01(\t\x12\x1e\n\x16stereo_left_image_path\x18\x02 \x01(\t\x12\x1f\n\x17stereo_right_image_path\x18\x03 \x01(\t\x12\"\n\x06status\x18\x04 \x01(\x0b\x32\x12.ugrpc_pipe.Status\x12*\n\x07request\x18\x05 \x01(\x0b\x32\x19.ugrpc_pipe.RenderRequest\"\xab\x01\n\x14PointCloudCaptureReq\x12\x1d\n\x15\x63\x61mera_transformation\x18\x01 \x03(\x02\x12\"\n\x1aproxy_model_transformation\x18\x02 \x03(\x02\x12\x1a\n\x12target_point_cloud\x18\x03 \x03(\x02\x12\x1a\n\x12source_point_cloud\x18\x04 \x03(\x02\x12\x18\n\x10proxy_model_name\x18\x05 \x01(\t\"\x89\x01\n\x19\x43onverge3DRegestrationReq\x12\x0e\n\x06models\x18\x01 \x03(\t\x12\x11\n\tdirection\x18\x02 \x03(\x02\x12\x0e\n\x06radius\x18\x03 \x01(\x02\x12\x15\n\rtarget_points\x18\x04 \x03(\x02\x12\x0f\n\x07\x63\x61se_id\x18\x05 \x01(\x05\x12\x11\n\tcase_guid\x18\x06 \x01(\t\",\n\x10RegestrationResp\x12\x18\n\x10transform_matrix\x18\x01 \x03(\x02\x32\xeb\x03\n\tUGrpcPipe\x12\x46\n\rCommandParser\x12\x1c.ugrpc_pipe.CommandParserReq\x1a\x17.ugrpc_pipe.GenericResp\x12M\n\x10RenderImageBytes\x12\x19.ugrpc_pipe.RenderRequest\x1a\x1c.ugrpc_pipe.RenderBytesReply\"\x00\x12J\n\x0fRouteImageBytes\x12\x1c.ugrpc_pipe.RenderBytesReply\x1a\x17.ugrpc_pipe.GenericResp\"\x00\x12\x43\n\x0bRenderImage\x12\x19.ugrpc_pipe.RenderRequest\x1a\x17.ugrpc_pipe.RenderReply\"\x00\x12U\n\x11PointCloudCapture\x12 .ugrpc_pipe.PointCloudCaptureReq\x1a\x1c.ugrpc_pipe.RegestrationResp\"\x00\x12_\n\x16\x43onverge3DRegestration\x12%.ugrpc_pipe.Converge3DRegestrationReq\x1a\x1c.ugrpc_pipe.RegestrationResp\"\x00\x42\x1d\xaa\x02\x1aUGrpc.Pipeline.GrpcPipe.V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ugrpc_pipe.ugrpc_pipe_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\032UGrpc.Pipeline.GrpcPipe.V1'
  _FLOATARRAYREP._serialized_start=70
  _FLOATARRAYREP._serialized_end=101
  _STRINGARRAYREP._serialized_start=103
  _STRINGARRAYREP._serialized_end=135
  _INTARRAYREP._serialized_start=137
  _INTARRAYREP._serialized_end=166
  _STATUS._serialized_start=168
  _STATUS._serialized_end=276
  _STATUS_STATUSCODE._serialized_start=240
  _STATUS_STATUSCODE._serialized_end=276
  _PROJECTINFORESP._serialized_start=279
  _PROJECTINFORESP._serialized_end=521
  _PROJECTINFORESP_PLATFORMCODE._serialized_start=460
  _PROJECTINFORESP_PLATFORMCODE._serialized_end=510
  _COMMANDPARSERREQ._serialized_start=523
  _COMMANDPARSERREQ._serialized_end=558
  _GENERICRESP._serialized_start=560
  _GENERICRESP._serialized_end=648
  _RENDERREQUEST._serialized_start=651
  _RENDERREQUEST._serialized_end=1475
  _RENDERREQUEST_QUALITY._serialized_start=1287
  _RENDERREQUEST_QUALITY._serialized_end=1324
  _RENDERREQUEST_CAMERAMODE._serialized_start=1326
  _RENDERREQUEST_CAMERAMODE._serialized_end=1383
  _RENDERREQUEST_RENDERMODE._serialized_start=1385
  _RENDERREQUEST_RENDERMODE._serialized_end=1475
  _IMAGEMETADATA._serialized_start=1477
  _IMAGEMETADATA._serialized_end=1539
  _RENDERBYTESREPLY._serialized_start=1542
  _RENDERBYTESREPLY._serialized_end=1750
  _RENDERREPLY._serialized_start=1753
  _RENDERREPLY._serialized_end=1936
  _POINTCLOUDCAPTUREREQ._serialized_start=1939
  _POINTCLOUDCAPTUREREQ._serialized_end=2110
  _CONVERGE3DREGESTRATIONREQ._serialized_start=2113
  _CONVERGE3DREGESTRATIONREQ._serialized_end=2250
  _REGESTRATIONRESP._serialized_start=2252
  _REGESTRATIONRESP._serialized_end=2296
  _UGRPCPIPE._serialized_start=2299
  _UGRPCPIPE._serialized_end=2790
# @@protoc_insertion_point(module_scope)

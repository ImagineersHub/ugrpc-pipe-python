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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bugrpc_pipe/ugrpc_pipe.proto\x12\nugrpc_pipe\x1a\x19google/protobuf/any.proto\"\x1f\n\rFloatArrayRep\x12\x0e\n\x06values\x18\x01 \x03(\x02\" \n\x0eStringArrayRep\x12\x0e\n\x06values\x18\x01 \x03(\t\"\x1d\n\x0bIntArrayRep\x12\x0e\n\x06values\x18\x01 \x03(\x05\"l\n\x06Status\x12+\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x1d.ugrpc_pipe.Status.StatusCode\x12\x0f\n\x07message\x18\x02 \x01(\t\"$\n\nStatusCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"\xdc\x01\n\x0fProjectInfoResp\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x12.ugrpc_pipe.StatusH\x00\x88\x01\x01\x12:\n\x08platform\x18\x02 \x01(\x0e\x32(.ugrpc_pipe.ProjectInfoResp.PlatformCode\x12\x10\n\x08\x64\x61taPath\x18\x03 \x01(\t\x12\x13\n\x0bprojectRoot\x18\x04 \x01(\t\"2\n\x0cPlatformCode\x12\x0b\n\x07unknown\x10\x00\x12\t\n\x05unity\x10\x01\x12\n\n\x06unreal\x10\x02\x42\t\n\x07_status\"#\n\x10\x43ommandParserReq\x12\x0f\n\x07payload\x18\x01 \x01(\t\"X\n\x0bGenericResp\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.ugrpc_pipe.Status\x12%\n\x07payload\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"\x9b\x01\n\rRenderRequest\x12\x12\n\nscene_name\x18\x01 \x01(\t\x12\x1d\n\x15\x63\x61mera_transformation\x18\x02 \x03(\x02\x12\x0b\n\x03\x66ov\x18\x03 \x01(\x02\x12\x12\n\nresolution\x18\x04 \x03(\x05\x12\x10\n\x08vdb_path\x18\x05 \x01(\t\x12\x10\n\x08modality\x18\x06 \x01(\t\x12\x12\n\nclip_range\x18\x07 \x03(\x02\"!\n\x0bRenderReply\x12\x12\n\nimage_data\x18\x01 \x01(\x0c\x32\x98\x01\n\tUGrpcPipe\x12\x46\n\rCommandParser\x12\x1c.ugrpc_pipe.CommandParserReq\x1a\x17.ugrpc_pipe.GenericResp\x12\x43\n\x0bRenderImage\x12\x19.ugrpc_pipe.RenderRequest\x1a\x17.ugrpc_pipe.RenderReply\"\x00\x42\x1d\xaa\x02\x1aUGrpc.Pipeline.GrpcPipe.V1b\x06proto3')

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
  _PROJECTINFORESP._serialized_end=499
  _PROJECTINFORESP_PLATFORMCODE._serialized_start=438
  _PROJECTINFORESP_PLATFORMCODE._serialized_end=488
  _COMMANDPARSERREQ._serialized_start=501
  _COMMANDPARSERREQ._serialized_end=536
  _GENERICRESP._serialized_start=538
  _GENERICRESP._serialized_end=626
  _RENDERREQUEST._serialized_start=629
  _RENDERREQUEST._serialized_end=784
  _RENDERREPLY._serialized_start=786
  _RENDERREPLY._serialized_end=819
  _UGRPCPIPE._serialized_start=822
  _UGRPCPIPE._serialized_end=974
# @@protoc_insertion_point(module_scope)

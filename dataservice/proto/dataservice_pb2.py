# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dataservice/proto/dataservice.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#dataservice/proto/dataservice.proto\x12\x0b\x64\x61taservice\x1a\x1cgoogle/protobuf/struct.proto\"H\n\x11IngestDataRequest\x12\x11\n\tdatasetId\x18\x01 \x01(\t\x12\x0e\n\x06\x62ucket\x18\x02 \x01(\t\x12\x10\n\x08\x66ileName\x18\x03 \x01(\t\"%\n\x12IngestDataResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"2\n\x0eGetDataRequest\x12\x11\n\tdatasetId\x18\x01 \x01(\t\x12\r\n\x05query\x18\x02 \x01(\t\"\x1c\n\x0c\x44\x61taResponse\x12\x0c\n\x04\x62ody\x18\x01 \x01(\t2\xa5\x01\n\x0b\x44\x61taService\x12O\n\nIngestData\x12\x1e.dataservice.IngestDataRequest\x1a\x1f.dataservice.IngestDataResponse\"\x00\x12\x45\n\x07GetData\x12\x1b.dataservice.GetDataRequest\x1a\x19.dataservice.DataResponse\"\x00\x30\x01\x42\x12\xaa\x02\x0f\x44\x61taServiceGrpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dataservice.proto.dataservice_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\017DataServiceGrpc'
  _globals['_INGESTDATAREQUEST']._serialized_start=82
  _globals['_INGESTDATAREQUEST']._serialized_end=154
  _globals['_INGESTDATARESPONSE']._serialized_start=156
  _globals['_INGESTDATARESPONSE']._serialized_end=193
  _globals['_GETDATAREQUEST']._serialized_start=195
  _globals['_GETDATAREQUEST']._serialized_end=245
  _globals['_DATARESPONSE']._serialized_start=247
  _globals['_DATARESPONSE']._serialized_end=275
  _globals['_DATASERVICE']._serialized_start=278
  _globals['_DATASERVICE']._serialized_end=443
# @@protoc_insertion_point(module_scope)

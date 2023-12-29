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


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#dataservice/proto/dataservice.proto\x12\x0b\x64\x61taservice\x1a\x1fgoogle/protobuf/timestamp.proto\"H\n\x11IngestDataRequest\x12\x11\n\tdatasetId\x18\x01 \x01(\t\x12\x0e\n\x06\x62ucket\x18\x02 \x01(\t\x12\x10\n\x08\x66ileName\x18\x03 \x01(\t\"%\n\x12IngestDataResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"2\n\x0eGetDataRequest\x12\x11\n\tdatasetId\x18\x01 \x01(\t\x12\r\n\x05query\x18\x02 \x01(\t\"\x85\x01\n\nFlightData\x12\x38\n\x11\x66light_descriptor\x18\x01 \x01(\x0b\x32\x1d.dataservice.FlightDescriptor\x12\x13\n\x0b\x64\x61ta_header\x18\x02 \x01(\x0c\x12\x14\n\x0c\x61pp_metadata\x18\x03 \x01(\x0c\x12\x12\n\tdata_body\x18\xe8\x07 \x01(\x0c\"=\n\x10HandshakeRequest\x12\x18\n\x10protocol_version\x18\x01 \x01(\x04\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\">\n\x11HandshakeResponse\x12\x18\n\x10protocol_version\x18\x01 \x01(\x04\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\"/\n\tBasicAuth\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"\x07\n\x05\x45mpty\"/\n\nActionType\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\x1e\n\x08\x43riteria\x12\x12\n\nexpression\x18\x01 \x01(\x0c\"$\n\x06\x41\x63tion\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\x0c\"@\n\x17\x43\x61ncelFlightInfoRequest\x12%\n\x04info\x18\x01 \x01(\x0b\x32\x17.dataservice.FlightInfo\"K\n\x1aRenewFlightEndpointRequest\x12-\n\x08\x65ndpoint\x18\x01 \x01(\x0b\x32\x1b.dataservice.FlightEndpoint\"\x16\n\x06Result\x12\x0c\n\x04\x62ody\x18\x01 \x01(\x0c\"C\n\x16\x43\x61ncelFlightInfoResult\x12)\n\x06status\x18\x01 \x01(\x0e\x32\x19.dataservice.CancelStatus\"\x1e\n\x0cSchemaResult\x12\x0e\n\x06schema\x18\x01 \x01(\x0c\"\x9b\x01\n\x10\x46lightDescriptor\x12:\n\x04type\x18\x01 \x01(\x0e\x32,.dataservice.FlightDescriptor.DescriptorType\x12\x0b\n\x03\x63md\x18\x02 \x01(\x0c\x12\x0c\n\x04path\x18\x03 \x03(\t\"0\n\x0e\x44\x65scriptorType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04PATH\x10\x01\x12\x07\n\x03\x43MD\x10\x02\"\xd8\x01\n\nFlightInfo\x12\x0e\n\x06schema\x18\x01 \x01(\x0c\x12\x38\n\x11\x66light_descriptor\x18\x02 \x01(\x0b\x32\x1d.dataservice.FlightDescriptor\x12-\n\x08\x65ndpoint\x18\x03 \x03(\x0b\x32\x1b.dataservice.FlightEndpoint\x12\x15\n\rtotal_records\x18\x04 \x01(\x03\x12\x13\n\x0btotal_bytes\x18\x05 \x01(\x03\x12\x0f\n\x07ordered\x18\x06 \x01(\x08\x12\x14\n\x0c\x61pp_metadata\x18\x07 \x01(\x0c\"\xc4\x01\n\x08PollInfo\x12%\n\x04info\x18\x01 \x01(\x0b\x32\x17.dataservice.FlightInfo\x12\x38\n\x11\x66light_descriptor\x18\x02 \x01(\x0b\x32\x1d.dataservice.FlightDescriptor\x12\x15\n\x08progress\x18\x03 \x01(\x01H\x00\x88\x01\x01\x12\x33\n\x0f\x65xpiration_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0b\n\t_progress\"\xa9\x01\n\x0e\x46lightEndpoint\x12#\n\x06ticket\x18\x01 \x01(\x0b\x32\x13.dataservice.Ticket\x12\'\n\x08location\x18\x02 \x03(\x0b\x32\x15.dataservice.Location\x12\x33\n\x0f\x65xpiration_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0c\x61pp_metadata\x18\x04 \x01(\x0c\"\x17\n\x08Location\x12\x0b\n\x03uri\x18\x01 \x01(\t\"\x18\n\x06Ticket\x12\x0e\n\x06ticket\x18\x01 \x01(\x0c\"!\n\tPutResult\x12\x14\n\x0c\x61pp_metadata\x18\x01 \x01(\x0c*\x8b\x01\n\x0c\x43\x61ncelStatus\x12\x1d\n\x19\x43\x41NCEL_STATUS_UNSPECIFIED\x10\x00\x12\x1b\n\x17\x43\x41NCEL_STATUS_CANCELLED\x10\x01\x12\x1c\n\x18\x43\x41NCEL_STATUS_CANCELLING\x10\x02\x12!\n\x1d\x43\x41NCEL_STATUS_NOT_CANCELLABLE\x10\x03\x32\xa3\x01\n\x0b\x44\x61taService\x12O\n\nIngestData\x12\x1e.dataservice.IngestDataRequest\x1a\x1f.dataservice.IngestDataResponse\"\x00\x12\x43\n\x07GetData\x12\x1b.dataservice.GetDataRequest\x1a\x17.dataservice.FlightData\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dataservice.proto.dataservice_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CANCELSTATUS']._serialized_start=1793
  _globals['_CANCELSTATUS']._serialized_end=1932
  _globals['_INGESTDATAREQUEST']._serialized_start=85
  _globals['_INGESTDATAREQUEST']._serialized_end=157
  _globals['_INGESTDATARESPONSE']._serialized_start=159
  _globals['_INGESTDATARESPONSE']._serialized_end=196
  _globals['_GETDATAREQUEST']._serialized_start=198
  _globals['_GETDATAREQUEST']._serialized_end=248
  _globals['_FLIGHTDATA']._serialized_start=251
  _globals['_FLIGHTDATA']._serialized_end=384
  _globals['_HANDSHAKEREQUEST']._serialized_start=386
  _globals['_HANDSHAKEREQUEST']._serialized_end=447
  _globals['_HANDSHAKERESPONSE']._serialized_start=449
  _globals['_HANDSHAKERESPONSE']._serialized_end=511
  _globals['_BASICAUTH']._serialized_start=513
  _globals['_BASICAUTH']._serialized_end=560
  _globals['_EMPTY']._serialized_start=562
  _globals['_EMPTY']._serialized_end=569
  _globals['_ACTIONTYPE']._serialized_start=571
  _globals['_ACTIONTYPE']._serialized_end=618
  _globals['_CRITERIA']._serialized_start=620
  _globals['_CRITERIA']._serialized_end=650
  _globals['_ACTION']._serialized_start=652
  _globals['_ACTION']._serialized_end=688
  _globals['_CANCELFLIGHTINFOREQUEST']._serialized_start=690
  _globals['_CANCELFLIGHTINFOREQUEST']._serialized_end=754
  _globals['_RENEWFLIGHTENDPOINTREQUEST']._serialized_start=756
  _globals['_RENEWFLIGHTENDPOINTREQUEST']._serialized_end=831
  _globals['_RESULT']._serialized_start=833
  _globals['_RESULT']._serialized_end=855
  _globals['_CANCELFLIGHTINFORESULT']._serialized_start=857
  _globals['_CANCELFLIGHTINFORESULT']._serialized_end=924
  _globals['_SCHEMARESULT']._serialized_start=926
  _globals['_SCHEMARESULT']._serialized_end=956
  _globals['_FLIGHTDESCRIPTOR']._serialized_start=959
  _globals['_FLIGHTDESCRIPTOR']._serialized_end=1114
  _globals['_FLIGHTDESCRIPTOR_DESCRIPTORTYPE']._serialized_start=1066
  _globals['_FLIGHTDESCRIPTOR_DESCRIPTORTYPE']._serialized_end=1114
  _globals['_FLIGHTINFO']._serialized_start=1117
  _globals['_FLIGHTINFO']._serialized_end=1333
  _globals['_POLLINFO']._serialized_start=1336
  _globals['_POLLINFO']._serialized_end=1532
  _globals['_FLIGHTENDPOINT']._serialized_start=1535
  _globals['_FLIGHTENDPOINT']._serialized_end=1704
  _globals['_LOCATION']._serialized_start=1706
  _globals['_LOCATION']._serialized_end=1729
  _globals['_TICKET']._serialized_start=1731
  _globals['_TICKET']._serialized_end=1755
  _globals['_PUTRESULT']._serialized_start=1757
  _globals['_PUTRESULT']._serialized_end=1790
  _globals['_DATASERVICE']._serialized_start=1935
  _globals['_DATASERVICE']._serialized_end=2098
# @@protoc_insertion_point(module_scope)

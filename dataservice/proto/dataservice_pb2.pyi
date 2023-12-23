from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IngestDataCommand(_message.Message):
    __slots__ = ("datasetId", "fileName")
    DATASETID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    datasetId: str
    fileName: str
    def __init__(self, datasetId: _Optional[str] = ..., fileName: _Optional[str] = ...) -> None: ...

class IngestDataCommandResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

#!/bin/bash

python -m grpc_tools.protoc --proto_path=. dataservice/proto/dataservice.proto --grpc_python_out=. --python_out=. --pyi_out=.
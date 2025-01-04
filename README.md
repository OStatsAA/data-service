# DataService

Internal OStats service to manage datasets raw data.

## Generate code from proto

Activate env
```{bash}
poetry shell
```

Generate grpc service
```{bash}
python -m grpc_tools.protoc --proto_path=. dataservice/proto/dataservice.proto --grpc_python_out=. --python_out=. --pyi_out=.
```
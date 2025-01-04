# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from dataservice.proto import dataservice_pb2 as dataservice_dot_proto_dot_dataservice__pb2


class DataServiceStub(object):
    """DataService
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.IngestData = channel.unary_unary(
                '/dataservice.DataService/IngestData',
                request_serializer=dataservice_dot_proto_dot_dataservice__pb2.IngestDataRequest.SerializeToString,
                response_deserializer=dataservice_dot_proto_dot_dataservice__pb2.IngestDataResponse.FromString,
                )
        self.GetData = channel.unary_stream(
                '/dataservice.DataService/GetData',
                request_serializer=dataservice_dot_proto_dot_dataservice__pb2.GetDataRequest.SerializeToString,
                response_deserializer=dataservice_dot_proto_dot_dataservice__pb2.DataResponse.FromString,
                )
        self.DeleteDataset = channel.unary_unary(
                '/dataservice.DataService/DeleteDataset',
                request_serializer=dataservice_dot_proto_dot_dataservice__pb2.DeleteDatasetRequest.SerializeToString,
                response_deserializer=dataservice_dot_proto_dot_dataservice__pb2.DeleteDatasetResponse.FromString,
                )


class DataServiceServicer(object):
    """DataService
    """

    def IngestData(self, request, context):
        """Ingest raw data from raw-datasets-uploads bucket and transforms them to parquet in datasets bucket
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDataset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'IngestData': grpc.unary_unary_rpc_method_handler(
                    servicer.IngestData,
                    request_deserializer=dataservice_dot_proto_dot_dataservice__pb2.IngestDataRequest.FromString,
                    response_serializer=dataservice_dot_proto_dot_dataservice__pb2.IngestDataResponse.SerializeToString,
            ),
            'GetData': grpc.unary_stream_rpc_method_handler(
                    servicer.GetData,
                    request_deserializer=dataservice_dot_proto_dot_dataservice__pb2.GetDataRequest.FromString,
                    response_serializer=dataservice_dot_proto_dot_dataservice__pb2.DataResponse.SerializeToString,
            ),
            'DeleteDataset': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDataset,
                    request_deserializer=dataservice_dot_proto_dot_dataservice__pb2.DeleteDatasetRequest.FromString,
                    response_serializer=dataservice_dot_proto_dot_dataservice__pb2.DeleteDatasetResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dataservice.DataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataService(object):
    """DataService
    """

    @staticmethod
    def IngestData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataservice.DataService/IngestData',
            dataservice_dot_proto_dot_dataservice__pb2.IngestDataRequest.SerializeToString,
            dataservice_dot_proto_dot_dataservice__pb2.IngestDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dataservice.DataService/GetData',
            dataservice_dot_proto_dot_dataservice__pb2.GetDataRequest.SerializeToString,
            dataservice_dot_proto_dot_dataservice__pb2.DataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteDataset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataservice.DataService/DeleteDataset',
            dataservice_dot_proto_dot_dataservice__pb2.DeleteDatasetRequest.SerializeToString,
            dataservice_dot_proto_dot_dataservice__pb2.DeleteDatasetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

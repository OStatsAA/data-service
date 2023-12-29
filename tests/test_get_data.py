from concurrent import futures
import json
import grpc
import pytest
from dataservice.data_service import DataService
import dataservice.proto.dataservice_pb2 as pb2
import dataservice.proto.dataservice_pb2_grpc as pb2_grpc


@pytest.fixture(scope="function")
def stub():
    servicer = DataService()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    pb2_grpc.add_DataServiceServicer_to_server(servicer, server)
    port = server.add_insecure_port("[::]:0")
    server.start()

    try:
        with grpc.insecure_channel(f"localhost:{port}") as channel:
            yield pb2_grpc.DataServiceStub(channel)
    finally:
        server.stop(None)


""" def test_request(stub):
    request: pb2.GetDataRequest = pb2.GetDataRequest(
        datasetId="1ed87fda-7499-4f0a-aa94-680e73228d30", query=""
    )
    for response in stub.GetData(request):
        assert isinstance(json.loads(response.body), list)
 """
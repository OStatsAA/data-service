"""This module contains tests for the gRPC server."""

from concurrent import futures
import json
import os
import shutil
import grpc
import pytest
from dataservice.config import TESTING_CONFIG
from dataservice.data_service import DataService

# pylint: disable=no-name-in-module
from dataservice.proto.dataservice_pb2 import GetDataRequest

# pylint: enable=no-name-in-module
import dataservice.proto.dataservice_pb2_grpc as pb2_grpc


@pytest.fixture(scope="function")
def stub():
    """
    A helper function to set up a test environment for the DataService.

    Returns:
        pb2_grpc.DataServiceStub: The gRPC stub for the DataService.
    """
    config = TESTING_CONFIG
    if not os.path.exists(f"{config['DATASETS_DIR']}/"):
        os.makedirs(f"{config['DATASETS_DIR']}/")

    dataset_path = f"{config['DATASETS_DIR']}/server_testing_dataset.arrow"
    test_dataset_path = "tests/assets/test_dataset.arrow"
    shutil.copy(test_dataset_path, dataset_path)

    servicer = DataService(config)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    pb2_grpc.add_DataServiceServicer_to_server(servicer, server)
    port = server.add_insecure_port("[::]:0")
    server.start()

    try:
        with grpc.insecure_channel(f"localhost:{port}") as channel:
            yield pb2_grpc.DataServiceStub(channel)
    finally:
        server.stop(None)
        if os.path.exists(dataset_path):
            os.remove(dataset_path)


def test_request(stub):  # pylint: disable=redefined-outer-name
    """
    Test the request function.

    Args:
        stub: The stub object used for making requests.

    Returns:
        None
    """
    request: GetDataRequest = GetDataRequest(
        datasetId="server_testing_dataset", query=""
    )
    for response in stub.GetData(request):
        assert isinstance(json.loads(response.body), list)

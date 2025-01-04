"""
DataService module
"""

from datetime import datetime
import json
import logging
import os

import boto3
import duckdb
from grpc import ServicerContext
from pyarrow import csv, feather, dataset
from dataservice.config import Config

# pylint: disable=no-name-in-module
from dataservice.proto.dataservice_pb2 import (
    DataResponse,
    DeleteDatasetResponse,
    GetDataRequest,
    IngestDataRequest,
    IngestDataResponse,
)
# pylint: enable=no-name-in-module
from dataservice.proto.dataservice_pb2_grpc import DataServiceServicer


class DataService(DataServiceServicer):
    """
    A class that provides data services for ingesting and retrieving data.

    Args:
        config (Config): The configuration object for the data service.

    Attributes:
        _config (Config): The configuration object for the data service.

    """

    def __init__(self, config: Config):
        self._config = config
        self._s3 = boto3.client(**config["S3_CLIENT_KWARGS"])
        self._datasets_bucket = config["DATASETS_BUCKET"]
        self._datasets_dir = config["DATASETS_DIR"]

    def IngestData(
        self, request: IngestDataRequest, context: ServicerContext
    ) -> IngestDataResponse:
        """
        Ingests data into the data service.

        Args:
            request (IngestDataRequest): The request object containing the data to be ingested.
            context (ServicerContext): The context object for the gRPC service.

        Returns:
            IngestDataResponse: The response object indicating the success or failure of the ingestion.
        """
        self._log_ingest_data_command(request)
        response = IngestDataResponse()
        bucket = request.bucket
        destination_key = request.datasetId
        path = f"{self._datasets_dir}/{destination_key}.arrow"
        object_ = self._s3.get_object(Bucket=bucket, Key=request.fileName)
        data = csv.read_csv(object_["Body"])
        try:
            feather.write_feather(data, path, "uncompressed")
            self._s3.upload_file(path, self._datasets_bucket, destination_key)
        except Exception as e:  # pylint: disable=broad-exception-caught
            logging.log(logging.ERROR, e)
            response.success = False
        else:
            response.success = True
            self._s3.delete_object(Bucket=bucket, Key=request.fileName)

        return response

    def GetData(self, request: GetDataRequest, context):
        """
        Retrieves data from the data service.

        Args:
            request (GetDataRequest): The request object containing the query and dataset ID.
            context: The context object for the gRPC service.

        Yields:
            DataResponse: The response object containing the retrieved data.

        """
        self._log_get_data_command(request)
        query = request.query if request.query else "SELECT * FROM data"
        data = dataset.dataset( # pylint: disable=unused-variable
            f"{self._datasets_dir}/{request.datasetId}.arrow", format="arrow"
        )
        logging.log(logging.INFO, "Loaded dataset")
        con = duckdb.connect()
        table = con.execute(query).arrow()
        logging.log(logging.INFO, "Built table: %s", str(table.schema))
        for batch in table.to_batches(max_chunksize=1000):
            d = batch.to_pylist()
            yield DataResponse(body=json.dumps(d))

    def DeleteDataset(self, request, context):
        """
        Deletes a dataset from the data service.

        Args:
            request (DeleteDatasetRequest): The request object containing the dataset ID.
            context (ServicerContext): The context object for the gRPC service.

        Returns:
            DeleteDatasetResponse: The response object indicating the success or failure of the deletion.
        """
        response = DeleteDatasetResponse()
        dataset_id = request.datasetId
        path = f"{self._datasets_dir}/{dataset_id}.arrow"
        if not os.path.exists(path):
            response.success = True
            return response
        try:
            os.remove(path)
        except Exception as e:  # pylint: disable=broad-exception-caught
            logging.log(logging.ERROR, e)
            response.success = False
        else:
            response.success = True

        return response

    def _log_ingest_data_command(self, request: IngestDataRequest):
        """
        Logs the ingest data command.

        Args:
            request (IngestDataRequest): The request object containing the data to be ingested.

        """
        logging.basicConfig(level=logging.INFO)
        logging.log(
            logging.INFO,
            "%s: Received IngestDataRequest - datasetId: %s, bucket: %s, fileName: %s",
            str(datetime.now()),
            request.datasetId,
            request.bucket,
            request.fileName,
        )

    def _log_get_data_command(self, request: GetDataRequest):
        """
        Logs the get data command.

        Args:
            request (GetDataRequest): The request object containing the query and dataset ID.

        """
        logging.basicConfig(level=logging.INFO)
        logging.log(
            logging.INFO,
            "%s: Received GetDataRequest - datasetId: %s, bucket: %s",
            str(datetime.now()),
            request.datasetId,
            request.query,
        )

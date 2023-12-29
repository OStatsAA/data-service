"""
DataService module
"""

import logging
import os
from dotenv import load_dotenv

import boto3
import duckdb
from pyarrow import csv, feather, dataset, flight

from dataservice.proto.dataservice_pb2 import (
    FlightData,
    GetDataRequest,
    IngestDataRequest,
    IngestDataResponse,
)
from dataservice.proto.dataservice_pb2_grpc import DataServiceServicer

load_dotenv()

_s3 = boto3.client(
    service_name="s3",
    endpoint_url=f"https://{os.getenv('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
    aws_access_key_id=os.getenv("R2_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("R2_SECRET_ACCESS_KEY"),
    region_name="auto",
)

_DATASETS_BUCKET = "datasets"


class DataService(DataServiceServicer):
    def IngestData(self, request: IngestDataRequest, context) -> IngestDataResponse:
        self._log_ingest_data_command(request)
        response = IngestDataResponse()
        bucket = request.bucket
        destination_key = request.datasetId
        path = f".temp/{destination_key}.arrow"
        object_ = _s3.get_object(Bucket=bucket, Key=request.fileName)
        data = csv.read_csv(object_["Body"])
        try:
            feather.write_feather(data, path, "uncompressed")
            _s3.upload_file(path, _DATASETS_BUCKET, destination_key)
        except Exception as e:  # pylint: disable=broad-exception-caught
            logging.log(logging.ERROR, e)
            response.success = False
        else:
            response.success = True

        return response

    def GetData(self, request: GetDataRequest, context) -> FlightData:
        self._log_get_data_command(request)
        query = request.query if request.query else "SELECT * FROM data"
        data = dataset.dataset(f".temp/{request.datasetId}.arrow", format="arrow")
        con = duckdb.connect()
        table = con.execute(query).arrow()
        logging.log(logging.INFO, "Built table: %s", str(table.schema))
        return flight.RecordBatchStream(table)

    def _log_ingest_data_command(self, request: IngestDataRequest):
        logging.basicConfig(level=logging.INFO)
        logging.log(
            logging.INFO,
            "Received IngestDataRequest - datasetId: %s, bucket: %s, fileName: %s",
            request.datasetId,
            request.bucket,
            request.fileName,
        )

    def _log_get_data_command(self, request: GetDataRequest):
        logging.basicConfig(level=logging.INFO)
        logging.log(
            logging.INFO,
            "Received GetDataRequest - datasetId: %s, bucket: %s",
            request.datasetId,
            request.query,
        )


if __name__ == "__main__":
    test = DataService()
    test.GetData(
        GetDataRequest(datasetId="1ed87fda-7499-4f0a-aa94-680e73228d30", query=""),
        {},
    )

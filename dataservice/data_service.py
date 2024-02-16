"""
DataService module
"""

from datetime import datetime
import json
import logging
import os
from dotenv import load_dotenv

import boto3
import duckdb
from grpc import ServicerContext
from pyarrow import csv, feather, dataset

from dataservice.proto.dataservice_pb2 import (
    DataResponse,
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
_DATASETS_PATH = "/datasets"


class DataService(DataServiceServicer):
    def IngestData(self, request: IngestDataRequest, context: ServicerContext) -> IngestDataResponse:
        self._log_ingest_data_command(request)
        response = IngestDataResponse()
        bucket = request.bucket
        destination_key = request.datasetId
        path = f"{_DATASETS_PATH}/{destination_key}.arrow"
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

    def GetData(self, request: GetDataRequest, context):
        self._log_get_data_command(request)
        query = request.query if request.query else "SELECT * FROM data"
        data = dataset.dataset(f"{_DATASETS_PATH}/{request.datasetId}.arrow", format="arrow")
        logging.log(logging.INFO, "Loaded dataset")
        con = duckdb.connect()
        table = con.execute(query).arrow()
        logging.log(logging.INFO, "Built table: %s", str(table.schema))
        for batch in table.to_batches(max_chunksize=1000):
            d = batch.to_pylist()
            yield DataResponse(body=json.dumps(d))

    def _log_ingest_data_command(self, request: IngestDataRequest):
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
        logging.basicConfig(level=logging.INFO)
        logging.log(
            logging.INFO,
            "%s: Received GetDataRequest - datasetId: %s, bucket: %s",
            str(datetime.now()),
            request.datasetId,
            request.query,
        )

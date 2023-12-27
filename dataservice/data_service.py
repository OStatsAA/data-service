"""
DataService module
"""

import logging
import os
from dotenv import load_dotenv

import boto3
from pyarrow import csv
from pyarrow import feather

from dataservice.proto.dataservice_pb2 import (
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
        source_key = request.fileName
        bucket = request.bucket
        destination_key = request.datasetId
        temp_path = f".temp/{destination_key}.arrow"
        object_ = _s3.get_object(Bucket=bucket, Key=source_key)
        data = csv.read_csv(object_["Body"])
        try:
            feather.write_feather(data, temp_path, "uncompressed")
            _s3.upload_file(temp_path, _DATASETS_BUCKET, destination_key)
        except Exception as e:  # pylint: disable=broad-exception-caught
            logging.log(logging.ERROR, e)
            response.success = False
        else:
            response.success = True
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

        return response

    def _log_ingest_data_command(self, request):
        logging.basicConfig(level=logging.INFO)
        logging.log(
            logging.INFO,
            "Received IngestDataCommand - datasetId: %s, bucket: %s, fileName: %s",
            request.datasetId,
            request.bucket,
            request.fileName,
        )

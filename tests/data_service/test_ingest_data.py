"""Data service unit tests for the IngestData method of the DataService class."""

import os
import unittest
import uuid
from unittest.mock import MagicMock, patch

from dataservice.config import TESTING_CONFIG
from dataservice.data_service import DataService

# pylint: disable=no-name-in-module
from dataservice.proto.dataservice_pb2 import (
    IngestDataRequest,
)

# pylint: enable=no-name-in-module


class TestIngestingData(unittest.TestCase):
    """
    Unit tests for the DataService class.
    """

    @patch("dataservice.data_service.boto3.client")
    def setUp(self, mock_boto3_client): # pylint: disable=arguments-differ
        """
        Set up the test environment before each test case.

        Args:
            mock_boto3_client: Mock object for the boto3.client method.
        """
        self.config = TESTING_CONFIG
        self.data_service = DataService(self.config)
        self.mock_s3_client = mock_boto3_client.return_value
        self.dataset_id = str(uuid.uuid4())
        self.ingest_kwargs = {
            "bucket": "test-bucket",
            "fileName": "test-file.csv",
            "datasetId": self.dataset_id,
        }

        if not os.path.exists(f"{self.config['DATASETS_DIR']}/"):
            os.makedirs(f"{self.config['DATASETS_DIR']}/")

    def tearDown(self):
        """
        Clean up any resources used in the tests.
        """
        if os.path.exists(f"{self.config['DATASETS_DIR']}/{self.dataset_id}.arrow"):
            os.remove(f"{self.config['DATASETS_DIR']}/{self.dataset_id}.arrow")

    def test_ingest_data_success(self):
        """
        Test case to verify the behavior of the IngestData method when data ingestion is successful.
        """
        # Mock the S3 client's methods
        self.mock_s3_client.get_object.return_value = {
            "Body": open("tests/assets/test_dataset.csv", "rb")
        }
        self.mock_s3_client.upload_file.return_value = None
        self.mock_s3_client.delete_object.return_value = None

        # Create a sample IngestDataRequest
        request = IngestDataRequest(**self.ingest_kwargs)

        # Call the IngestData method
        response = self.data_service.IngestData(request, MagicMock())

        # Assert that the response success flag is True
        self.assertTrue(response.success)

        # Assert that the S3 client's methods were called with the correct arguments
        self.mock_s3_client.get_object.assert_called_once_with(
            Bucket=request.bucket, Key=request.fileName
        )
        self.mock_s3_client.upload_file.assert_called_once_with(
            f"{self.config['DATASETS_DIR']}/{request.datasetId}.arrow",
            self.config["DATASETS_BUCKET"],
            request.datasetId,
        )
        self.mock_s3_client.delete_object.assert_called_once_with(
            Bucket=request.bucket, Key=request.fileName
        )

    def test_ingest_data_failure(self):
        """
        Test case to verify the behavior of the IngestData method
        when an exception is raised by the S3 client's get_object method.
        """
        # Mock the S3 client's get_object method to raise an exception
        self.mock_s3_client.get_object.side_effect = Exception("Test exception")

        request = IngestDataRequest(**self.ingest_kwargs)

        with self.assertRaises(Exception):
            self.data_service.IngestData(request, MagicMock())

        self.mock_s3_client.get_object.assert_called_once_with(
            Bucket=request.bucket, Key=request.fileName
        )


if __name__ == "__main__":
    unittest.main()

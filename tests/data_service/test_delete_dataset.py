"""Data service unit tests for the DeleteDataset method of the DataService class."""

import os
import shutil
import unittest
import uuid
from dataservice.config import TESTING_CONFIG

from dataservice.data_service import DataService

# pylint: disable=no-name-in-module
from dataservice.proto.dataservice_pb2 import (
    DeleteDatasetRequest,
    DeleteDatasetResponse,
)

# pylint: enable=no-name-in-module


class TestDeleteDataset(unittest.TestCase):
    """
    Unit tests for the DeleteDataset method of the DataService class.
    """

    def setUp(self):
        """
        Set up the test environment before each test case.
        """
        self.config = TESTING_CONFIG
        self.data_service = DataService(self.config)
        self.dataset_id = str(uuid.uuid4())
        self.path = os.path.join(".temp_datasets", f"{self.dataset_id}.arrow")

        source_file = "tests/assets/test_dataset.arrow"
        destination_dir = ".temp_datasets"
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir, exist_ok=True)
        shutil.copy(source_file, self.path)

    def tearDown(self):
        """
        Clean up the test environment after each test case.

        This method is called automatically after each test case.
        It removes the test_dataset.arrow file from the .temp_datasets directory if it exists.
        """
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_delete_dataset(self):
        """
        Test that the DeleteDataset method deletes a dataset from the data service.
        """
        request = DeleteDatasetRequest(datasetId=self.dataset_id)
        response = self.data_service.DeleteDataset(request, None)
        self.assertIsInstance(response, DeleteDatasetResponse)
        self.assertTrue(response.success)
        self.assertFalse(os.path.exists(self.path))

    def test_delete_dataset_nonexistent(self):
        """
        Test that the DeleteDataset method returns a success response when the dataset does not exist.
        """
        request = DeleteDatasetRequest(datasetId=str(uuid.uuid4()))
        response = self.data_service.DeleteDataset(request, None)
        self.assertIsInstance(response, DeleteDatasetResponse)
        self.assertTrue(response.success)

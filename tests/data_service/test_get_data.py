"""Data service unit tests for the GetData method of the DataService class."""

import os
import shutil
import json
import unittest
from unittest.mock import MagicMock
from dataservice.config import TESTING_CONFIG

from dataservice.data_service import DataService

# pylint: disable=no-name-in-module
from dataservice.proto.dataservice_pb2 import (
    DataResponse,
)

# pylint: enable=no-name-in-module


class TestGetData(unittest.TestCase):
    """
    Unit tests for the GetData method of the DataService class.
    """

    def setUp(self):
        """
        Set up the test environment before each test case.

        This method is called automatically before each test case.
        It copies the test_dataset.arrow file to the .temp_datasets directory.
        """
        source_file = "tests/assets/test_dataset.arrow"
        destination_dir = ".temp_datasets"
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir, exist_ok=True)
        shutil.copy(source_file, destination_dir)

    def tearDown(self):
        """
        Clean up the test environment after each test case.

        This method is called automatically after each test case.
        It removes the test_dataset.arrow file from the .temp_datasets directory if it exists.
        """
        file_path = os.path.join(".temp_datasets", "test_dataset.arrow")
        if os.path.exists(file_path):
            os.remove(file_path)

    def test_get_data(self):
        """
        Test case for the GetData method of the DataService class.

        This test verifies that the GetData method returns a valid response
        with a non-empty body that is a valid JSON string.

        It creates a mock request object with a datasetId and query,
        creates a mock context object, and instantiates the DataService class.

        Then it calls the GetData method and iterates over the response.
        For each response, it asserts that the response is of type DataResponse,
        that the response body is not empty, and that the response body is a valid JSON string.
        """
        # Create a mock request object
        request = MagicMock()
        request.datasetId = "test_dataset"
        request.query = "SELECT * FROM data"

        # Create a mock context object
        context = MagicMock()

        # Create an instance of the DataService class
        data_service = DataService(TESTING_CONFIG)

        # Call the GetData method and iterate over the response
        response_iterator = data_service.GetData(request, context)
        for response in response_iterator:
            # Assert that the response is of type DataResponse
            self.assertIsInstance(response, DataResponse)

            # Assert that the response body is not empty
            self.assertIsNotNone(response.body)

            # Assert that the response body is a valid JSON string
            try:
                json.loads(response.body)
            except json.JSONDecodeError:
                self.fail("Response body is not a valid JSON string")

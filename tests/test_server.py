""""Test cases for the server module."""

import pytest
from dataservice.server import serve
from dataservice.config import TESTING_CONFIG, Config


@pytest.mark.asyncio
async def test_serve_without_exceptions():
    """
    Test case to ensure that the serve function runs without raising any exceptions.
    """
    config: Config = {**TESTING_CONFIG, "LISTEN_ADDR": "[::]:12345"}
    try:
        await serve(config)
    except Exception as e: # pylint: disable=broad-except
        assert False, f"Running server function raised an exception: {e}"

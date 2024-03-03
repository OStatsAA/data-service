"""Test the config module."""

from dataservice.config import get_config, DEFAULT_CONFIG


def test_config_defaults():
    """
    Test the get_config function returns DEFAULT config
    when an invalid environment is passed.

    Returns:
        None
    """
    config = get_config("SOME_CLEARLY_INVALID_ENVIRONMENT")
    assert config == DEFAULT_CONFIG

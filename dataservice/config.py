"""Dataservice configuration file"""

import os
from typing import TypedDict

from dotenv import load_dotenv

load_dotenv()


class Config(TypedDict):
    """Dataservice configuration"""

    # Storage configuration
    S3_CLIENT_KWARGS: dict
    DATASETS_BUCKET: str
    DATASETS_DIR: str

    # Server configuration
    LISTEN_ADDR: str


DEFAULT_CONFIG = Config(
    S3_CLIENT_KWARGS={
        "service_name": "s3",
        "endpoint_url": f"https://{os.getenv('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
        "aws_access_key_id": os.getenv("R2_ACCESS_KEY"),
        "aws_secret_access_key": os.getenv("R2_SECRET_ACCESS_KEY"),
        "region_name": "auto",
    },
    DATASETS_BUCKET="datasets",
    DATASETS_DIR="/datasets",
    LISTEN_ADDR="[::]:50051",
)

TESTING_CONFIG: Config = {**DEFAULT_CONFIG, "DATASETS_DIR": ".temp_datasets"}


def get_config(config_type: str = "DEFAULT") -> Config:
    """Get configuration by type"""
    config_selector = {
        "DEVELOPMENT": TESTING_CONFIG,
        "DEFAULT": DEFAULT_CONFIG,
    }
    return config_selector.get(config_type, DEFAULT_CONFIG)

#!/bin/bash

# Install dependencies using Poetry
poetry install

# Activate .venv
source .venv/bin/activate

# Install localstack awslocal cli
pip install awscli-local[ver1]

# Create datasets bucket in localstack s3
awslocal --endpoint-url=http://s3:4566 s3 mb s3://raw-datasets-uploads
awslocal --endpoint-url=http://s3:4566 s3 mb s3://datasets

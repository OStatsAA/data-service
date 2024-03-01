#!/bin/bash

# Activate .venv
source .venv/bin/activate

# Run test coverage report
coverage run

# Generate HTML report
coverage html

# Serve HTML report
python -m http.server 8000 --directory htmlcov

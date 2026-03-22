#!/bin/sh
set -e

echo ""

echo "Running migrations"
uv run flask db upgrade

echo  "Starting server"
uv run flask run --host=0.0.0.0 --port=5000
#!/bin/sh
set -e

echo "Running migrations..."
exec uv run flask db upgrade

echo "Starting server..."
exec uv run flask run --host=0.0.0.0
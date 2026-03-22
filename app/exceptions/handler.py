from flask import Flask, jsonify, request
from app.exceptions.base import ApiException
import logging

logger = logging.getLogger(__name__)

def register_error_handlers(app: Flask):

    @app.errorhandler(ApiException)
    def handle_app_exception(e: ApiException):
        logger.error(f"API Exception on {request.method} {request.path}: {e.message} (Status: {e.status_code})")
        return jsonify(e.to_dict()), e.status_code

    @app.errorhandler(Exception)
    def handle_unexpected_error(e: Exception):
        logger.error(f"Unexpected error on {request.method} {request.path}: {str(e)}", exc_info=True)
        return jsonify({
            "error": "InternalServerError",
            "message": "An unexpected error occurred",
            "status_code": 500
        }), 500
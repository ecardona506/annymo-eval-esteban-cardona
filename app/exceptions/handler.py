from flask import Flask, jsonify
from app.exceptions.base import ApiException

def register_error_handlers(app: Flask):

    @app.errorhandler(ApiException)
    def handle_app_exception(e: ApiException):
        return jsonify(e.to_dict()), e.status_code
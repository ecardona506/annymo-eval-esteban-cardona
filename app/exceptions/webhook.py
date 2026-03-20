from http import HTTPStatus
from app.exceptions.base import ApiException

class WebhookSignatureException(ApiException):
    status_code = HTTPStatus.UNAUTHORIZED
    message = "Invalid or missing webhook signature"
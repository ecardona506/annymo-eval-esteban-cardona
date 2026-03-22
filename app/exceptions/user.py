from http import HTTPStatus
from app.exceptions.base import ApiException

class UserAlreadyExistsException(ApiException):
    status_code = HTTPStatus.CONFLICT
    message = "User with the same email or phone number already exists"
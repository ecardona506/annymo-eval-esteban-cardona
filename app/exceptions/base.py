from http import HTTPStatus

class ApiException(Exception):
    """Base exception for all custom exceptions."""
    status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR
    message: str = "An unexpected error occurred"

    def __init__(self, message: str | None = None):
        self.message = message or self.__class__.message
        super().__init__(self.message)

    def to_dict(self):
        return {
            "error": self.__class__.__name__,
            "message": self.message,
            "status_code": self.status_code,
        }
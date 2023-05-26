from typing import Mapping

from vizme.config import settings


class ApiException(Exception):
    """
    Base class for API exceptions
    """

    status_code: int = 500
    message: str = "Упс! Что-то пошло не так ;("

    def __init__(
        self,
        message: str | None = None,
        payload: Mapping | None = None,
        exception_class: str | None = None,
    ):
        self.message = message or self.message
        self.payload = payload
        self.exception_class = exception_class

    def _type(self):
        return self.__class__.__name__

    def to_json(self) -> Mapping:
        return {"code": self.status_code, "message": self.message, "payload": self.payload}


class ServerError(ApiException):
    status_code = 500
    message = "Упс! Что-то пошло не так ;("


class NotFoundError(ApiException):
    status_code = 404
    message = "Not Found"


class ObjectNotFoundError(ApiException):
    status_code = 404
    message = "Object Not Found"


class BadRequestError(ApiException):
    status_code = 400


class ValidationError(ApiException):
    status_code = 400


class UserNotFoundError(ApiException):
    status_code = 400
    message = "User not found"


class UserAlreadyRegistered(ApiException):
    status_code = 400
    message = "User already registered"


class PasswordMatchError(ApiException):
    status_code = 400
    message = "Passwords did not match"


class ForbiddenError(ApiException):
    status_code = 403
    message = "Forbidden"


class UnauthorizedError(ApiException):
    status_code = 401
    message = "Unauthorized"


class JWTExpiredSignatureError(ApiException):
    status_code = 426
    message = "Token expired"


class JWTDecodeError(ApiException):
    status_code = 401
    message = "Token decode error"


class ProfileEditNonArgs(ApiException):
    status_code = 400
    message = "Not provides any args to edit profile"


class FileTooLargeError(ApiException):
    status_code = 400
    message = f"Provide only: {settings.ALLOWED_UPLOAD_TYPES}"


class UnsupportedFileTypeError(ApiException):
    status_code = 400
    message = f"Max file size: {settings.FILE_MAX_SIZE_MB}Mb"

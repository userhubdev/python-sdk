import sys
from http import HTTPStatus

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from ._str_enum import StrEnum


class Code(StrEnum):
    OK = "OK"
    CANCELED = "CANCELLED"
    UNKNOWN = "UNKNOWN"
    INVALID_ARGUMENT = "INVALID_ARGUMENT"
    DEADLINE_EXCEEDED = "DEADLINE_EXCEEDED"
    NOT_FOUND = "NOT_FOUND"
    ALREADY_EXISTS = "ALREADY_EXISTS"
    PERMISSION_DENIED = "PERMISSION_DENIED"
    UNAUTHENTICATED = "UNAUTHENTICATED"
    RESOURCE_EXHAUSTED = "RESOURCE_EXHAUSTED"
    FAILED_PRECONDITION = "FAILED_PRECONDITION"
    ABORTED = "ABORTED"
    OUT_OF_RANGE = "OUT_OF_RANGE"
    UNIMPLEMENTED = "UNIMPLEMENTED"
    INTERNAL = "INTERNAL"
    UNAVAILABLE = "UNAVAILABLE"
    DATA_LOSS = "DATA_LOSS"

    @property
    def webhook_status_code(self) -> int:
        if self is self.OK:
            return HTTPStatus.OK
        if self in (
            self.ALREADY_EXISTS,
            self.FAILED_PRECONDITION,
            self.INVALID_ARGUMENT,
        ):
            return HTTPStatus.BAD_REQUEST
        if self is self.NOT_FOUND:
            return HTTPStatus.NOT_FOUND
        if self is self.RESOURCE_EXHAUSTED:
            return HTTPStatus.TOO_MANY_REQUESTS
        if self is self.UNIMPLEMENTED:
            return HTTPStatus.NOT_IMPLEMENTED
        return HTTPStatus.INTERNAL_SERVER_ERROR

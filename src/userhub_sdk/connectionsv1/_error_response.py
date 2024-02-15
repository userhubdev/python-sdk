# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class ErrorResponse:
    """
    The connection error response.
    """

    #: The error code (e.g. `INVALID_ARGUMENT`).
    code: str = ""
    #: A user-facing error message.
    message: Optional[str] = None

    def __json_encode__(self):
        data = {}

        if self.code is not None:
            data["code"] = self.code

        if self.message is not None:
            data["message"] = self.message

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("code") is not None:
            kwargs["code"] = data["code"]

        if data.get("message") is not None:
            kwargs["message"] = data["message"]

        return ErrorResponse(**kwargs)

# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class OperationError:
    """
    The operation error.
    """

    #: The error code.
    code: Optional[str] = None
    #: The error message.
    message: Optional[str] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.code is not None:
            data["code"] = self.code

        if self.message is not None:
            data["message"] = self.message

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "OperationError":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("code") is not None:
            kwargs["code"] = data["code"]

        if data.get("message") is not None:
            kwargs["message"] = data["message"]

        return OperationError(**kwargs)

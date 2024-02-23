# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class Status:
    """
    The full API error.
    """

    #: The general error code (e.g. `INVALID_ARGUMENT`).
    code: str = ""
    #: A developer-facing error message.
    message: str = ""
    #: A reason code for the error (e.g. `USER_PENDING_DELETION`).
    reason: Optional[str] = None
    #: The parameter path related to the error (e.g. `member.userId`).
    param: Optional[str] = None
    #: Additional metadata related to the error.
    metadata: Optional[Dict[str, str]] = dataclasses.field(default_factory=dict)

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.code is not None:
            data["code"] = self.code

        if self.message is not None:
            data["message"] = self.message

        if self.reason is not None:
            data["reason"] = self.reason

        if self.param is not None:
            data["param"] = self.param

        if self.metadata is not None:
            data["metadata"] = self.metadata

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Status":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("code") is not None:
            kwargs["code"] = data["code"]

        if data.get("message") is not None:
            kwargs["message"] = data["message"]

        if data.get("reason") is not None:
            kwargs["reason"] = data["reason"]

        if data.get("param") is not None:
            kwargs["param"] = data["param"]

        if data.get("metadata") is not None:
            kwargs["metadata"] = data["metadata"]

        return Status(**kwargs)

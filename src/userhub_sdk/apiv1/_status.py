# Code generated. DO NOT EDIT.

import dataclasses
from typing import Dict
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class Status:
    """
    The full API error.
    """

    #: The general error code (e.g. `INVALID_ARGUMENT`).
    code: Optional[str] = None
    #: A developer-facing error message.
    message: Optional[str] = None
    #: A reason code for the error (e.g. `USER_PENDING_DELETION`).
    reason: Optional[str] = None
    #: The parameter path related to the error (e.g. `member.userId`).
    param: Optional[str] = None
    #: Additional metadata related to the error.
    metadata: Dict[str, str] = dataclasses.field(default_factory=dict)

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

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

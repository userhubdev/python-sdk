# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class StatusDetails:
    """
    The API error with the fields that already exist
    in Status removed.
    """

    #: A reason code for the error (e.g. `PENDING_DELETION`).
    reason: Optional[str] = None
    #: The parameter path related to the error (e.g. `member.userId`).
    param: Optional[str] = None
    #: Additional metadata related to the error.
    metadata: Optional[Dict[str, str]] = dataclasses.field(default_factory=dict)
    #: A user-facing error message.
    locale_message: Optional[str] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.reason is not None:
            data["reason"] = self.reason

        if self.param is not None:
            data["param"] = self.param

        if self.metadata is not None:
            data["metadata"] = self.metadata

        if self.locale_message is not None:
            data["localeMessage"] = self.locale_message

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "StatusDetails":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("reason") is not None:
            kwargs["reason"] = data["reason"]

        if data.get("param") is not None:
            kwargs["param"] = data["param"]

        if data.get("metadata") is not None:
            kwargs["metadata"] = data["metadata"]

        if data.get("localeMessage") is not None:
            kwargs["locale_message"] = data["localeMessage"]

        return StatusDetails(**kwargs)

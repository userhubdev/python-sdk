# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, List


@dataclasses.dataclass
class BuiltinEmailConnection:
    """
    The builtin email specific connection data.
    """

    #: The allowed email list.
    allowed_emails: List[str] = dataclasses.field(default_factory=list)

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.allowed_emails is not None:
            data["allowedEmails"] = self.allowed_emails

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "BuiltinEmailConnection":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("allowedEmails") is not None:
            kwargs["allowed_emails"] = data["allowedEmails"]

        return BuiltinEmailConnection(**kwargs)

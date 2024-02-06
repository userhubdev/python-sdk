# Code generated. DO NOT EDIT.

import dataclasses
from typing import List
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class BuiltinEmailConnection:
    """
    The builtin email specific connection data.
    """

    #: The allowed email list.
    allowed_emails: List[str] = dataclasses.field(default_factory=list)

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("allowedEmails") is not None:
            kwargs["allowed_emails"] = data["allowedEmails"]

        return BuiltinEmailConnection(**kwargs)

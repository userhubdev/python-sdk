# Code generated. DO NOT EDIT.

import dataclasses
from typing import Dict
from typing import Optional

from .._internal import util


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
    metadata: Dict[str, str] = dataclasses.field(default_factory=dict)

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("reason") is not None:
            kwargs["reason"] = data["reason"]

        if data.get("param") is not None:
            kwargs["param"] = data["param"]

        if data.get("metadata") is not None:
            kwargs["metadata"] = data["metadata"]

        return StatusDetails(**kwargs)

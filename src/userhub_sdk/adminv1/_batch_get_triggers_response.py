# Code generated. DO NOT EDIT.

import dataclasses
from typing import List
from typing import Optional

from .._internal import util
from ._trigger_result import TriggerResult


@dataclasses.dataclass
class BatchGetTriggersResponse:
    """
    Response message for BatchGetTriggers.
    """

    #: The triggers.
    triggers: Optional[List[TriggerResult]] = dataclasses.field(default_factory=list)

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("triggers") is not None:
            kwargs["triggers"] = [
                TriggerResult.__json_decode__(v) for v in data["triggers"]
            ]

        return BatchGetTriggersResponse(**kwargs)

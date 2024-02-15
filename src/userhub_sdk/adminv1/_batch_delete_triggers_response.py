# Code generated. DO NOT EDIT.

import dataclasses
from typing import List, Optional

from ._trigger_result import TriggerResult


@dataclasses.dataclass
class BatchDeleteTriggersResponse:
    """
    Response message for BatchDeleteTriggers.
    """

    #: The triggers.
    triggers: Optional[List[TriggerResult]] = dataclasses.field(default_factory=list)

    def __json_encode__(self):
        data = {}

        if self.triggers is not None:
            data["triggers"] = [TriggerResult.__json_encode__(v) for v in self.triggers]

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("triggers") is not None:
            kwargs["triggers"] = [
                TriggerResult.__json_decode__(v) for v in data["triggers"]
            ]

        return BatchDeleteTriggersResponse(**kwargs)

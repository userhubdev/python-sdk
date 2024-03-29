# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, List

from ._trigger_result import TriggerResult


@dataclasses.dataclass
class BatchDeleteTriggersResponse:
    """
    Response message for BatchDeleteTriggers.
    """

    #: The triggers.
    triggers: List[TriggerResult] = dataclasses.field(default_factory=list)

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.triggers is not None:
            data["triggers"] = [TriggerResult.__json_encode__(v) for v in self.triggers]

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "BatchDeleteTriggersResponse":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("triggers") is not None:
            kwargs["triggers"] = [
                TriggerResult.__json_decode__(v) for v in data["triggers"]
            ]

        return BatchDeleteTriggersResponse(**kwargs)

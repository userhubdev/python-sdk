# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


@dataclasses.dataclass
class PlanGroupChangePath:
    """
    The change path.
    """

    #: Whether the change is considered an upgrade or
    #: a downgrade.
    direction: str = ""

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.direction is not None:
            data["direction"] = self.direction

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "PlanGroupChangePath":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("direction") is not None:
            kwargs["direction"] = data["direction"]

        return PlanGroupChangePath(**kwargs)

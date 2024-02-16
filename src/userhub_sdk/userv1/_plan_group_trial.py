# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class PlanGroupTrial:
    """
    The trial settings.
    """

    #: The number of days in the trial.
    days: Optional[int] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.days is not None:
            data["days"] = self.days

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "PlanGroupTrial":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("days") is not None:
            kwargs["days"] = data["days"]

        return PlanGroupTrial(**kwargs)

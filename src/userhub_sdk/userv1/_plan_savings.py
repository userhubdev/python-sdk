# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class PlanSavings:
    """
    The savings for the plan.
    """

    #: The percentage savings (1-100).
    #:
    #: This percentage is rounded down.
    percentage: Optional[int] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.percentage is not None:
            data["percentage"] = self.percentage

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "PlanSavings":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("percentage") is not None:
            kwargs["percentage"] = data["percentage"]

        return PlanSavings(**kwargs)

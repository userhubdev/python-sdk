# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


@dataclasses.dataclass
class CheckoutPlanTrial:
    """
    The trial details.
    """

    #: The number of days in the trial.
    days: int = 0

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.days is not None:
            data["days"] = self.days

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "CheckoutPlanTrial":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("days") is not None:
            kwargs["days"] = data["days"]

        return CheckoutPlanTrial(**kwargs)
